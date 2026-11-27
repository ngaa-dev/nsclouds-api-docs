# OpenAI - Responses

### 1. Overview

OpenAI exposes Responses capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Responses path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `gpt-5`
* `gpt-5.1`
* `gpt-5.2`
* `gpt-5.3-codex`
* `gpt-5.4`
* `gpt-5.4-mini`
* `gpt-5.5`


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

{% openapi-operation spec="openai-en-global" path="/v1/responses" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
