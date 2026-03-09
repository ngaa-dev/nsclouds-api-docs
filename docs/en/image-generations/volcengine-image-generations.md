---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/image-generations/volcengine-image-generations
---

# ByteDance Doubao (volcengine)

### 1. Overview

The image generation API launched by ByteDance, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `volcengine/doubao-seedream-4-5-251128`
* `volcengine/doubao-seedream-4-0-250828`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ⏳ Pending Verification | Supported |

### 2. API Details

{% openapi-operation spec="volcengine-en" path="/v1/images/generations" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/volcengine.bundled.yaml)
{% endopenapi-operation %}
