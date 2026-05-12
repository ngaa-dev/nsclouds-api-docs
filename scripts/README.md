# 文档生成与厂家维护说明

本文档说明当前仓库的 API 文档生成方式，以及新增厂家、更新模型、验证接口时应遵循的维护流程。

## 当前生成链路

- 入口脚本：`build-docs.sh`
- Markdown 与导航生成：`scripts/generate_env_docs.py`
- OpenAPI YAML 生成：`scripts/render_env_openapi.rb`
- 数据源：
  - 国内：`scripts/data/cn_model_info.json`
  - 国际：`scripts/data/global_model_info.json`

构建时会生成两类产物：

- 页面文档：`docs/{cn,global}/{zh,en}/`
- GitBook 导入用 OpenAPI：`docs/{cn,global}/{zh,en}/openapi/`
- bundle 后的 OpenAPI：`docs/bundled/{cn,global}/{zh,en}/`

## 维护原则

- 不要手工维护 `docs/cn/`、`docs/global/`、`docs/bundled/` 下的生成结果，这些都应通过脚本重建。
- 左侧导航、厂家显隐、能力显隐，统一由 `scripts/data/global_model_info.json` / `scripts/data/cn_model_info.json` 决定。
- 公开能力必须按 `model_info.supported_endpoints` 判定，不按 `mode` 单独猜测。
- `Text Completions` 跟随 `/v1/chat/completions` 展示。
- `Messages`、`Responses`、`Gemini Native` 只在 `supported_endpoints` 命中时展示。
- 国内与国际环境分别只展示各自真实公开可用的厂家与能力。

## 更新模型或能力时怎么做

### 1. 更新数据源

先更新：

- `scripts/data/cn_model_info.json`
- `scripts/data/global_model_info.json`

重点字段：

- `model_name`
- `model_info.original_provider`
- `model_info.mode`
- `model_info.supported_endpoints`

其中：

- 厂家归属看 `original_provider`
- 页面和导航能力看 `supported_endpoints`

### 2. 判断是否需要改模板

以下情况通常不需要新增模板文件：

- 只是模型上下架
- 只是某个厂家新增或减少 `chat/messages/responses/images/audio` 能力
- 新厂家复用已有兼容协议

以下情况需要改模板或脚本：

- 新增全新的协议形态
- 现有协议需要新增 path
- 某个厂家需要单独的请求/响应示例
- GitBook 展示需要补充专门的 examples 或描述

OpenAPI 生成脚本会按能力选择合适的基础模板，并自动把 examples 里的 `model` / `modelVersion` 替换成当前环境真实可用的示例模型。

### 3. 重建文档

```bash
bash build-docs.sh
```

可按环境单独生成：

```bash
bash build-docs.sh cn
bash build-docs.sh global
```

### 4. 验证结果

至少检查以下内容：

- `docs/{env}/{lang}/SUMMARY.md` 是否符合预期导航
- `docs/{env}/{lang}/chat-completion/` 下厂家与能力是否正确
- `docs/{env}/{lang}/openapi/*.yaml` 是否包含正确 path、tags、examples
- `docs/bundled/{env}/{lang}/*.bundled.yaml` 是否生成成功

`build-docs.sh` 内部已执行 `swagger-cli validate`，用于校验 bundled YAML 合法性。

## 新增厂家时怎么做

### 1. 先补数据，再看生成结果

优先更新 `scripts/data/global_model_info.json` / `scripts/data/cn_model_info.json`，让生成脚本先跑出导航和页面。

如果新厂家只是兼容已有协议，通常不需要手工增加一整套 Markdown 页面，生成器会自动产出：

- 厂家目录
- README
- 能力页
- OpenAPI 文件

### 2. 什么时候需要改 `scripts/render_env_openapi.rb`

当出现以下情况时再修改：

- 新能力不属于现有 capability 集合
- 新能力需要新的 OpenAPI path
- 新协议不适合复用 `openai` / `anthropic` / `google` / 其他已有基础模板
- 需要为某个能力选择新的示例模型规则

### 3. 什么时候需要改 `scripts/generate_env_docs.py`

当出现以下情况时再修改：

- 左侧导航层级调整
- 新增能力分类
- 中英文文案需要统一变更
- 厂家 README 或能力页结构需要变化

## 接口验证建议

如果要对实际网关做验证，建议优先使用简单请求确认兼容性，再决定是否补文档示例。

常用检查项：

- `/v1/chat/completions`
- `/v1/messages`
- `/v1/responses`
- `/v1/images/generations`
- `/v1/images/edits`
- `/v1/audio/transcriptions`
- `Gemini Native` 相关路径

验证时建议记录：

- 请求命令
- 实际响应
- 是否支持流式
- 是否支持多模态
- 是否支持工具调用

这些记录如果只是临时测试，不要再放回仓库；除非它们会被明确纳入长期维护文档。

## 不再使用的旧流程

以下做法已经不适合当前仓库：

- 在 `test_openapi/` 下长期保存测试结果并作为维护入口
- 手工复制旧模板后逐个厂商维护 `docs/zh/...` 或 `docs/en/...` 页面
- 手工编辑生成后的 `docs/cn/`、`docs/global/`、`docs/bundled/` 内容

当前正确方式是：

1. 更新 `scripts/data/` 下的数据源
2. 必要时调整模板或生成脚本
3. 运行 `build-docs.sh`
4. 检查生成结果
