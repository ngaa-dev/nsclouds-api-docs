---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/completions/openai-completions
---

# OpenAI

### 1. Overview

OpenAI's text completion API, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `gpt-3.5-turbo-instruct`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ✅ Verified | Supported |
| Streaming Response | ✅ Verified | Supported |

### 2. API Details

{% openapi-operation spec="openai-en" path="/v1/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/openai.bundled.yaml)
{% endopenapi-operation %}
