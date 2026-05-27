# 仓库与 GitBook 过渡期协作说明

本文档用于说明 `nsclouds-api-docs` 从个人 GitHub/GitBook 过渡到公司 GitHub/GitBook 期间的协作方式。

## 当前状态

- 个人 GitHub 仓库：`git@github.com:liujia-hbu/nsclouds-api-docs.git`
- 公司 GitHub 仓库：`git@github.com:ngaa-dev/nsclouds-api-docs.git`
- 当前 GitBook：仍使用个人 GitBook 项目。
- 公司 GitBook：尚未准备好。
- 当前 GitBook OpenAPI raw URL：仍指向个人 GitHub 仓库。

因此，当前阶段不要把个人 GitHub/GitBook 直接当成正式生产环境；它承担的是“过渡期预览与调试环境”的角色。公司 GitHub 已存在，但公司 GitBook 未就绪前，公司链路还不能完整承接线上展示。

## 当前过渡期原则

- 个人 GitHub/GitBook 继续作为预览环境使用，保证现有 GitBook 同步链路不断。
- 公司 GitHub 作为未来正式源提前同步，避免迁移当天再一次性搬运大量提交。
- 公司 GitBook 未准备好之前，不修改默认 GitBook 同步脚本指向，避免影响当前可预览链路。
- 文档里的示例和 OpenAPI 展示必须按线上真实可用状态维护；未完成适配的能力可以保留 schema，但需要明确标注“建设中”或“适配中”，不要放入可执行示例。
- 所有接口验证使用环境变量传入密钥，禁止把密钥写入文档、提交记录、脚本默认值或命令输出。

## 目标状态

最终应形成两套清晰环境：

| 环境 | GitHub | GitBook | 用途 |
| --- | --- | --- | --- |
| 预览/调试 | `liujia-hbu/nsclouds-api-docs` | 个人 GitBook | 修改、构建、预览、验证 |
| 正式/线上 | `ngaa-dev/nsclouds-api-docs` | 公司 GitBook | 对外正式展示 |

正式迁移完成后，线上 GitBook 应只从公司 GitHub raw URL 拉取 OpenAPI：

```text
https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled
```

个人 GitBook 继续从个人 GitHub raw URL 拉取 OpenAPI：

```text
https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled
```

## 推荐 remote 配置

过渡期建议不要反复 `git remote set-url origin ...` 在个人和公司之间切换。更清晰的做法是同时保留两个 remote：

```bash
git remote rename origin preview
git remote add company git@github.com:ngaa-dev/nsclouds-api-docs.git
git remote -v
```

推荐含义：

- `preview`：个人 GitHub，用于预览环境。
- `company`：公司 GitHub，用于正式环境。

如果本地已经把 `origin` 改成公司仓库，也可以保留这个约定：

```bash
git remote add preview git@github.com:liujia-hbu/nsclouds-api-docs.git
git remote rename origin company
```

关键是团队内部统一命名，避免不知道当前 `origin` 指向哪里。

## 过渡期开发流程

### 1. 开始修改前同步公司仓库

公司 GitHub 是未来正式源，因此每次修改前应先合并公司最新提交：

```bash
git fetch company
git checkout main
git merge company/main
```

如果公司仓库当前只是落后个人仓库，可以先把个人当前最新推给公司一次：

```bash
git push company main
```

后续常规更新仍建议先 `fetch company` 再 `merge company/main`。

### 2. 本地修改并构建

```bash
bash build-docs.sh
```

构建后重点检查：

- `docs/{cn,global}/{zh,en}/`
- `docs/{cn,global}/{zh,en}/openapi/`
- `docs/bundled/{cn,global}/{zh,en}/`

不要手工维护这些生成目录，应修改 `docs/templates/`、`scripts/data/` 或生成脚本后重建。

### 3. 推送个人 GitHub 做预览

公司 GitBook 未就绪前，GitBook 展示仍依赖个人 GitHub raw URL。因此需要先推个人仓库：

```bash
git push preview main
```

然后同步个人 GitBook：

```bash
source ~/.bash_profile
python3 scripts/sync_gitbook_openapi.py --wait
```

当前脚本默认 raw base 是个人 GitHub：

```text
https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled
```

### 4. 验证通过后推送公司 GitHub

个人 GitBook 预览和接口验证通过后，再推公司仓库：

```bash
git push company main
```

在公司 GitBook 准备好之前，这一步只是让公司 GitHub 跟上最新正式候选版本，不会自动改变线上 GitBook 展示。

## 角色分工建议

- 日常修改者：先合并公司仓库最新代码，再在本地修改和构建。
- 预览发布者：负责推送个人 GitHub，并同步个人 GitBook 做展示验证。
- 正式发布者：负责把验证通过的提交推送公司 GitHub；公司 GitBook 就绪后，再同步公司 GitBook。
- 验收者：按 GitBook 展示的请求示例做真实 curl 验证，尤其关注多模态 `image_url`、文件上传、`file_id` 等容易和协议适配状态不一致的内容。

如果同一个人承担多个角色，也建议按这个顺序执行，避免跳过预览直接发布。

## 公司 GitBook 准备好后的切换流程

公司 GitBook 就绪后，需要完成以下动作。

### 1. 准备公司 GitBook token 和 org id

需要公司 GitBook 的：

- `GITBOOK_TOKEN`
- `GITBOOK_ORG_ID`

不要复用个人 GitBook token 作为正式发布凭据。

### 2. 使用公司 raw base 同步公司 GitBook

首次同步建议显式传入公司 raw base：

```bash
GITBOOK_RAW_BASE=https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled \
python3 scripts/sync_gitbook_openapi.py --wait
```

如果本机 shell 里同时保存了个人和公司 GitBook 凭据，建议使用更明确的变量名，再在命令中赋值：

```bash
GITBOOK_TOKEN="$COMPANY_GITBOOK_TOKEN" \
GITBOOK_ORG_ID="$COMPANY_GITBOOK_ORG_ID" \
GITBOOK_RAW_BASE=https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled \
python3 scripts/sync_gitbook_openapi.py --wait
```

### 3. 更新生成脚本中的 raw URL 策略

当前 `scripts/generate_env_docs.py` 和 `scripts/sync_gitbook_openapi.py` 默认使用个人 GitHub raw URL。公司 GitBook 上线后，建议把默认值调整为公司仓库，或新增明确的预览/正式发布脚本。

推荐方向：

- 预览发布使用个人 raw base。
- 正式发布使用公司 raw base。
- 不依赖人工临时记忆当前 raw base 指向哪里。

建议新增两个脚本：

```text
scripts/sync_preview_gitbook_openapi.sh
scripts/sync_company_gitbook_openapi.sh
```

分别固定：

- GitBook token/org 来源。
- raw base。
- 是否 `--wait`。

## 发布检查清单

每次准备正式发布前至少检查：

- 已执行 `git fetch company` 并合并 `company/main`。
- 已执行 `bash build-docs.sh`。
- `git diff --check` 通过。
- GitHub remote 指向清晰，不依赖临时记忆 `origin` 当前代表个人还是公司。
- GitBook 展示的请求示例已经真实 curl 验证。
- 密钥只通过环境变量使用，未写入文档、命令输出或提交。
- 个人 GitBook 预览通过。
- 公司 GitHub 已推送最新提交。
- 公司 GitBook 就绪后，公司 GitBook 同步使用公司 raw base。

## 注意事项

- GitBook OpenAPI 同步脚本不是上传本地文件，而是让 GitBook 从 raw GitHub URL 拉取 `docs/bundled` 下的 YAML。
- 因此，必须先把对应分支推到对应 GitHub 仓库，再同步对应 GitBook。
- 如果 raw base 仍指向个人仓库，公司 GitBook 即使同步成功，也会展示个人仓库内容。
- 如果公司 GitBook 还没准备好，不要把个人 GitBook 当作正式环境对外承诺。
- 过渡期可以继续用个人 GitBook 预览，但最终线上真实展示必须收敛到公司 GitHub + 公司 GitBook。
