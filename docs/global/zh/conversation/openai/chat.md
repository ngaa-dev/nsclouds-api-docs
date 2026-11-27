# OpenAI - Chat Completions

### 1. 概述

OpenAI 在当前环境中提供的对话生成能力。

{% hint style="success" %}
本接口提供与 OpenAI Chat Completions 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。
{% endhint %}

**模型列表：**

* `gpt-5`
* `gpt-5.1`
* `gpt-5.2`
* `gpt-5.3-codex`
* `gpt-5.4`
* `gpt-5.4-mini`
* `gpt-5.5`


### 2. 文件输入说明

{% hint style="info" %}
`/v1/chat/completions` 支持通过 `file_data` 传入 base64 文件内容，也兼容 OpenAI 的 `file_id` 字段；不支持 `file_url`。如需通过 URL 传入文件，请使用 Responses API。
{% endhint %}

| 字段 | 支持情况 | 建议 |
| --- | --- | --- |
| `file_data` | 支持 | 当前推荐，适合直接以内联 base64 传入文件内容 |
| `file_id` | OpenAI 兼容字段，适配中 | 来源于 Files API 上传后返回的文件 ID，实际可用性取决于文件托管和模型侧支持 |
| `file_url` | 不支持 | 请改用 `/v1/responses` 的 `input_file.file_url` |

### 3. 接口详情

{% openapi-operation spec="openai-zh-global" path="/v1/chat/completions" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/zh/openai.bundled.yaml)
{% endopenapi-operation %}
