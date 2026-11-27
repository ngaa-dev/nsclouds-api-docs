# OpenAI - Chat Completions

### 1. Overview

OpenAI exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `gpt-5`
* `gpt-5.1`
* `gpt-5.2`
* `gpt-5.3-codex`
* `gpt-5.4`
* `gpt-5.4-mini`
* `gpt-5.5`


### 2. File Input Notes

{% hint style="info" %}
`/v1/chat/completions` supports base64 file input through `file_data` and keeps OpenAI-compatible `file_id`; it does not support `file_url`. Use the Responses API when you need to pass files by URL.
{% endhint %}

| Field | Support | Recommendation |
| --- | --- | --- |
| `file_data` | Supported | Recommended today for inline base64 file content |
| `file_id` | OpenAI-compatible field, in adaptation | Comes from a Files API upload; actual availability depends on file hosting and model-side support |
| `file_url` | Not supported | Use `/v1/responses` with `input_file.file_url` instead |

### 3. API Details

{% openapi-operation spec="openai-en-global" path="/v1/chat/completions" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
