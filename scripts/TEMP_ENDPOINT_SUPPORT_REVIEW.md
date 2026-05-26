# 临时能力对照说明

内部临时说明文件，不接入 GitBook 导航。

## 目的

- 记录“网关已经支持的能力”和“当前本地模型元数据里明确对外说明的能力”之间的差异。
- 作为后续是否将能力纳入公开文档的内部判断依据。
- 后续计划通过 `codex cli` 和 `claude code cli` 做真实验证，再决定是否加入正式文档展示。

## 范围

- 对照文件：
  - `scripts/data/cn_model_info.json`
  - `scripts/data/global_model_info.json`
- 记录时间：
  - 2026-05-14

## 对话模型

| 模型 | 网关预期支持 | `cn_model_info.json` 当前明确说明 | `global_model_info.json` 当前明确说明 | 内部结论 |
| --- | --- | --- | --- | --- |
| `MiniMax-M2.5` | `chat` | `chat` | `chat` | 已对齐。 |
| `MiniMax-M2.7` | `chat` | `chat` | `chat` | 已对齐。 |
| `qwen3.6-plus` | `chat`、`responses`、`messages` | `chat`、`responses` | `chat`、`responses` | `messages` 目前视为网关已支持，但还不是当前明确对外说明能力，暂不公开。 |
| `qwen3.6-flash` | `chat`、`responses`、`messages` | `chat`、`responses` | `chat`、`responses` | 同上。 |
| `qwen3.6-max-preview` | `chat`、`messages` | `chat` | `chat` | `messages` 目前视为网关已支持，但还不是当前明确对外说明能力。 |
| `doubao-seed-2-0-lite-260215` | `chat`、`responses`、`messages` | `chat`、`responses` | `chat`、`responses` | `messages` 需验证后再决定是否公开。 |
| `doubao-seed-2-0-pro-260215` | `chat`、`responses`、`messages` | `chat`、`responses` | `chat`、`responses` | 同上。 |
| `zai/glm-4.7` | `chat`、`responses`、`messages` | `chat` | `chat` | `responses/messages` 暂按网关能力处理，不直接公开。 |
| `volcengine/glm-4-7-251222` | `chat`、`responses`、`messages` | `chat`、`responses` | `chat`、`responses` | `messages` 需验证后再决定是否公开。 |
| `zai/glm-5.1` | `chat`、`responses`、`messages` | `chat` | `chat` | `responses/messages` 暂按网关能力处理，不直接公开。 |
| `dashscope/glm-5.1` | `chat`、`responses`、`messages` | `chat` | `chat` | 同上。 |
| `zai/glm-4.6v` | `chat_vision` | `chat` | `chat` | 当前仍然通过 `chat/completions` 承载，多模态差异主要体现在模型能力，不急于调整端点说明。 |

## 文生图模型

| 模型 | 网关预期支持 | `cn_model_info.json` 当前明确说明 | `global_model_info.json` 当前明确说明 | 内部结论 |
| --- | --- | --- | --- | --- |
| `zai/cogview-4-250304` | `image_generation` | `image_generation` | `image_generation` | 已对齐。 |
| `qwen-image-2.0-pro` | `image_generation` | `image_generation`、`image_edits` | `image_generation`、`image_edits` | 当前配置是更大能力集合。如果公开文档要保守，仍可只先展示生成能力。 |
| `qwen-image-2.0` | `image_generation` | `image_generation`、`image_edits` | `image_generation`、`image_edits` | 同上。 |
| `volcengine/doubao-seedream-4-5-251128` | `image_generation` | `image_generation`、`image_edits` | `image_generation` | 国内外当前不一致，`edits` 建议先内部保留，待海外验证后再公开。 |
| `volcengine/doubao-seedream-5-0-260128` | `image_generation` | `image_generation`、`image_edits` | `image_generation` | 同上。 |

## 音频转文字模型

| 模型 | 网关预期支持 | `cn_model_info.json` 当前明确说明 | `global_model_info.json` 当前明确说明 | 内部结论 |
| --- | --- | --- | --- | --- |
| `glm-asr-2512` | `audio_transcription` | `audio_transcription` | `audio_transcription` | 已对齐。 |

## 后续建议

1. 先把上面这些“网关已支持但未明确公开”的能力，继续当作内部能力管理。
2. 用 `codex cli` 和 `claude code cli` 做真实调用验证。
3. 验证通过后，再更新公开文档使用的 `supported_endpoints`，并重新生成文档。
