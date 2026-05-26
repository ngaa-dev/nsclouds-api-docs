# OpenAI - Responses

### 1. Overview

OpenAI Responses API for unified text, multimodal, and tool-calling responses.

{% hint style="success" %}
This API is compatible with OpenAI Responses format.
{% endhint %}

### 2. File And Image Input Notes

{% hint style="info" %}
`/v1/responses` supports image and file inputs by URL or data URL, and keeps OpenAI-compatible `file_id`. Prefer `image_url`, `file_url`, or `file_data` today; image and file `file_id` both depend on Files API upload, file hosting, and model-side mapping support.
{% endhint %}

| Field | Applies to | Support | Recommendation |
| --- | --- | --- | --- |
| `image_url` | `input_image` | Supported | Recommended today for image URLs or image data URLs |
| `file_url` | `input_file` | Supported | Recommended today for publicly accessible file URLs |
| `file_data` | `input_file` | Supported | Recommended today for inline base64 file content |
| `file_id` | `input_image` / `input_file` | OpenAI-compatible field, in adaptation | Comes from a Files API upload; actual availability depends on file hosting and model-side support |

### 3. API Details

{% openapi-operation spec="openai-en-{{ENV}}" path="/v1/responses" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/en/openai.bundled.yaml)
{% endopenapi-operation %}
