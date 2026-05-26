# OpenAI - Responses

### 1. 概述

OpenAI Responses API，用于统一文本、多模态与工具调用响应。

{% hint style="success" %}
本 API 与 OpenAI Responses 接口格式兼容。
{% endhint %}

### 2. 文件与图片输入说明

{% hint style="info" %}
`/v1/responses` 支持通过 URL 或 data URL 传入图片和文件，也兼容 OpenAI 的 `file_id`。当前建议优先使用 `image_url`、`file_url` 或 `file_data`；图片和文件的 `file_id` 均依赖 Files API 上传、文件托管和模型侧映射能力。
{% endhint %}

| 字段 | 适用类型 | 支持情况 | 建议 |
| --- | --- | --- |
| `image_url` | `input_image` | 支持 | 当前推荐，适合图片 URL 或图片 data URL |
| `file_url` | `input_file` | 支持 | 当前推荐，适合可公开访问的文件 URL |
| `file_data` | `input_file` | 支持 | 当前推荐，适合以内联 base64 传入文件内容 |
| `file_id` | `input_image` / `input_file` | OpenAI 兼容字段，适配中 | 来源于 Files API 上传后返回的文件 ID，实际可用性取决于文件托管和模型侧支持 |

### 3. 接口详情

{% openapi-operation spec="openai-zh-{{ENV}}" path="/v1/responses" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/openai.bundled.yaml)
{% endopenapi-operation %}
