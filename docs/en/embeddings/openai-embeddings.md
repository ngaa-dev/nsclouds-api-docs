---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/embeddings/openai-embeddings
---

# OpenAI

### 1. Overview

OpenAI's vector embeddings API, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `text-embedding-ada-002`
* `text-embedding-3-small`
* `text-embedding-3-large`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ✅ Verified | Supported |

### 2. API Details

{% openapi-operation spec="openai-en" path="/v1/embeddings" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/openai.bundled.yaml)
{% endopenapi-operation %}
