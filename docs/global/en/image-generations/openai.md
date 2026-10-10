# OpenAI - Image Generations

### 1. Overview

OpenAI exposes image generation capabilities in this environment.

{% hint style="success" %}
This endpoint provides GPT Image 2 and GPT Image 2.5 capabilities through the OpenAI Images API.
{% endhint %}

**Supported models：**

* `gpt-image-2`
* `gpt-image-2-oai`
* `gpt-image-2.5-flare`
* `gpt-image-2.5-flare-oai`
* `gpt-image-2.5-sunburst`
* `gpt-image-2.5-sunburst-oai`


### 2. Image Model Parameter Notes

#### Model Resources and Billing

The following distinction applies to model names on this platform, for both image generation and editing.

The `-oai` suffix identifies direct OpenAI resources; models without it use AWS resources. Resource origin and billing are listed separately below:

| Model | Resource origin | Billing method |
| --- | --- | --- |
| `gpt-image-2-oai` | Direct OpenAI | Actual token usage |
| `gpt-image-2` | AWS | Per image, with the unit price selected by pixel count and quality tier |
| `gpt-image-2.5-flare-oai` | Direct OpenAI | Token billing only |
| `gpt-image-2.5-sunburst-oai` | Direct OpenAI | Token billing only |
| `gpt-image-2.5-flare` | AWS | Token billing only |
| `gpt-image-2.5-sunburst` | AWS | Token billing only |

All GPT Image 2.5 variants are billed by actual tokens in top-level response `usage`, with separate text input, image input, and image output charges. `size` and `quality` may affect token consumption, but do not select separate per-image, pixel-based, or quality-tier prices.

The `gpt-image-2` charge is the image count multiplied by the applicable per-image tier price; token prices do not apply. For `gpt-image-2-oai`, tokens are aggregated in top-level `usage`, not reported for each `data[]` image. Use the selected model's pricing configuration for unit prices and cached-input rates; the GPT Image 2.5 price table does not automatically apply to `gpt-image-2-oai`.

#### gpt-image-2

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

#### GPT Image 2.5

{% hint style="info" %}
Use `gpt-image-2.5-flare-oai` for fast image generation and `gpt-image-2.5-sunburst-oai` for detailed image editing. All GPT Image models with the `-oai` suffix use direct OpenAI resources; models without the suffix use AWS resources. All GPT Image 2.5 variants support token billing only, not per-image, pixel-based, or quality-tier billing.
{% endhint %}

`quality` supports `low`, `medium`, `high`, `xhigh`, `max`, and `auto`, with `auto` as the default. For transparent backgrounds, set `background="transparent"` and use `output_format="png"` or `"webp"`.

Requests are billed from actual token usage in the response (per one million tokens):

| Modality | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| Text | $5.00 | $1.25 | - |
| Image | $8.00 | $2.00 | $30.00 |

`usage.input_tokens_details` separates text, image, and cached input tokens, while `usage.output_tokens_details` reports image output tokens. Tokens are aggregated in the top-level `usage` object and are not attached to individual `data[]` image objects.

### 3. API Details

{% openapi-operation spec="openai-en-global" path="/v1/images/generations" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
