# OpenAI - Image Generations

### 1. Overview

OpenAI exposes image generation capabilities in this environment.

{% hint style="success" %}
This endpoint provides gpt-image-2 image capabilities through the OpenAI Images API.
{% endhint %}

**Supported models：**

* `gpt-image-2`


### 2. gpt-image-2 Parameter Notes

{% hint style="info" %}
`gpt-image-2` supports text-to-image generation. `n` may request 1-10 images, and the actual number of returned images can be lower than requested.
{% endhint %}

| Parameter | Support |
| --- | --- |
| `prompt` | Required. Reference maximum length is 32000 characters. |
| `n` | Optional. Reference range is 1-10; the actual number of returned images can be lower than requested. |
| `size` | Optional. Supports `auto` and the fixed sizes listed below. |
| `quality` | Optional. Supports `low`, `medium`, and `high`; omitted, `auto`, and `standard` are billed as `high`. |
| `background` | Optional. Supports `opaque` and `auto`. |
| `moderation` | Optional. Supported only on image generations; accepts `low` and `auto`. |
| `output_format` | Optional. Supports `png` and `jpeg`. |
| `output_compression` | Optional. Range is 0-100 and applies only to `jpeg`; omit it for `png` or set it to 100. |

Supported sizes: `auto`, `1024x1024`, `1024x1536`, `1536x1024`, `2048x2048`, `2048x1152`, `3840x2160`, `2160x3840`, `2048x1360`, `1360x2048`, `1152x2048`, `2048x1536`, `1536x2048`, `2048x880`, `880x2048`, `688x2048`, `2048x688`, `2048x1024`, `1024x2048`

### 3. API Details

{% openapi-operation spec="openai-en-global" path="/v1/images/generations" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
