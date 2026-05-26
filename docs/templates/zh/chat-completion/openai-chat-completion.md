# OpenAI

### 1. 概述

OpenAI 是全球领先的 AI 研究机构，提供强大的 GPT 系列大语言模型，包括 GPT-4、GPT-3.5 等，支持文本生成、对话、图像生成等多种 AI 能力。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-5` (chat 模式)
* `gpt-5.1` (chat 模式)
* `gpt-5.2` (chat 模式)
* `gpt-5.4` (chat 模式)
* `gpt-5.3-codex` (chat 模式)

### 2. 文件输入说明

{% hint style="info" %}
`/v1/chat/completions` 支持通过 `file_data` 传入 base64 文件内容，也兼容 OpenAI 的 `file_id` 字段；不支持 `file_url`。如需通过 URL 传入文件，请使用 Responses API。
{% endhint %}

| 字段 | 支持情况 | 建议 |
| --- | --- | --- |
| `file_data` | 支持 | 当前推荐，适合直接以内联 base64 传入文件内容 |
| `file_id` | OpenAI 兼容字段，适配中 | 来源于 Files API 上传后返回的文件 ID，实际可用性取决于文件托管和模型侧支持 |
| `file_url` | 不支持 | 请改用 `/v1/responses` 的 `input_file.file_url` |

### 3.接口详情

{% openapi-operation spec="openai-zh-{{ENV}}" path="/v1/chat/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/openai.bundled.yaml)
{% endopenapi-operation %}
