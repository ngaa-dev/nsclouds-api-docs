---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/embeddings/deepseek-embeddings
---

# DeepSeek

### 1. Overview

The vector embeddings API launched by DeepSeek, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `deepseek-embeddings`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ⏳ Pending Verification | Supported |

### 2. API Details

{% openapi-operation spec="deepseek-en" path="/v1/embeddings" method="post" %}
[OpenAPI deepseek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/deepseek.bundled.yaml)
{% endopenapi-operation %}
