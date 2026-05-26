#!/bin/bash
set -euo pipefail

# 构建脚本：根据目标环境生成不同域名的文档
# 使用方法：
#   bash build-docs.sh         # 同时生成国内外版本
#   bash build-docs.sh cn      # 只生成国内版本
#   bash build-docs.sh global  # 只生成国际版本

# 生成 bundled 文件的函数
run_swagger_cli() {
  if command -v swagger-cli >/dev/null 2>&1; then
    swagger-cli "$@"
  else
    npx --yes @apidevtools/swagger-cli "$@"
  fi
}

generate_bundled() {
  local env=$1
  local output_prefix=$2
  local temp_dir=$(mktemp -d)
  
  # 创建临时目录
  mkdir -p $temp_dir/zh/openapi $temp_dir/en/openapi
  
  ruby scripts/render_env_openapi.rb "$env" "$temp_dir"
  
  # 根据环境替换占位符
  if [ "$env" == "cn" ]; then
    sed -i '' 's/${SERVER_URL}/https:\/\/aillm.nsclouds.com/g' $temp_dir/zh/openapi/_common.yaml
    sed -i '' 's/${SERVER_DESCRIPTION}/国内服务器/g' $temp_dir/zh/openapi/_common.yaml
    sed -i '' 's/${SERVER_URL}/https:\/\/aillm.nsclouds.com/g' $temp_dir/en/openapi/_common.yaml
    sed -i '' 's/${SERVER_DESCRIPTION}/China Server/g' $temp_dir/en/openapi/_common.yaml
  else
    sed -i '' 's/${SERVER_URL}/https:\/\/aillm.nscloud.ai/g' $temp_dir/zh/openapi/_common.yaml
    sed -i '' 's/${SERVER_DESCRIPTION}/国际服务器/g' $temp_dir/zh/openapi/_common.yaml
    sed -i '' 's/${SERVER_URL}/https:\/\/aillm.nscloud.ai/g' $temp_dir/en/openapi/_common.yaml
    sed -i '' 's/${SERVER_DESCRIPTION}/Global Server/g' $temp_dir/en/openapi/_common.yaml
  fi
  
  # 创建输出目录
  rm -rf docs/bundled/${output_prefix}zh
  rm -rf docs/bundled/${output_prefix}en
  mkdir -p docs/bundled/${output_prefix}zh
  mkdir -p docs/bundled/${output_prefix}en
  
  echo "Generating bundled YAML files for ${output_prefix} environment..."
  
  for spec in "$temp_dir"/zh/openapi/*.yaml; do
    vendor=$(basename "$spec" .yaml)
    if [ "$vendor" != "_common" ]; then
      run_swagger_cli bundle "$spec" -o docs/bundled/${output_prefix}zh/${vendor}.bundled.yaml -t yaml
      run_swagger_cli validate docs/bundled/${output_prefix}zh/${vendor}.bundled.yaml
    fi
  done

  for spec in "$temp_dir"/en/openapi/*.yaml; do
    vendor=$(basename "$spec" .yaml)
    if [ "$vendor" != "_common" ]; then
      run_swagger_cli bundle "$spec" -o docs/bundled/${output_prefix}en/${vendor}.bundled.yaml -t yaml
      run_swagger_cli validate docs/bundled/${output_prefix}en/${vendor}.bundled.yaml
    fi
  done
  
  # 清理临时目录
  rm -rf $temp_dir
}

# 生成文档的函数
generate_docs() {
  local env=$1
  
  # 创建文档目录
  rm -rf docs/${env}/zh
  rm -rf docs/${env}/en
  mkdir -p docs/${env}/zh
  mkdir -p docs/${env}/en
  
  echo "Generating docs for ${env} environment..."
  
  # 复制模板并替换占位符
  if [ -d "docs/templates/zh" ]; then
    cp -r docs/templates/zh/* docs/${env}/zh/
  fi
  if [ -d "docs/templates/en" ]; then
    cp -r docs/templates/en/* docs/${env}/en/
  fi
  
  # 替换占位符
  find docs/${env} -name "*.md" -exec sed -i '' "s/{{ENV}}/${env}/g" {} \;

  python3 scripts/generate_env_docs.py render-env "${env}"
  ruby scripts/render_env_openapi.rb "${env}" "docs/${env}"
}

# 生成国内版本
build_cn() {
  echo "Building docs for cn environment..."
  
  # 生成 bundled 文件
  generate_bundled "cn" "cn/"
  
  # 生成文档
  generate_docs "cn"
  
  echo "Configured for China environment (aillm.nsclouds.com)"
}

# 生成国际版本
build_global() {
  echo "Building docs for global environment..."
  
  # 生成 bundled 文件
  generate_bundled "global" "global/"
  
  # 生成文档
  generate_docs "global"
  
  echo "Configured for Global environment (aillm.nscloud.ai)"
}

# 主逻辑
case "$1" in
  "cn")
    build_cn
    ;;
  "global")
    build_global
    ;;
  "")
    # 不写参数，同时生成国内外版本
    build_cn
    echo ""
    build_global
    ;;
  *)
    echo "Usage: bash build-docs.sh [cn|global]"
    echo "  Without argument: build both cn and global versions"
    echo "  cn: build only China version"
    echo "  global: build only Global version"
    exit 1
    ;;
esac

echo ""
echo "Build completed successfully!"
echo "Bundled files are available in:"
echo "  - docs/bundled/cn/ (China version)"
echo "  - docs/bundled/global/ (Global version)"
echo "Generated docs are available in:"
echo "  - docs/cn/ (China version)"
echo "  - docs/global/ (Global version)"
