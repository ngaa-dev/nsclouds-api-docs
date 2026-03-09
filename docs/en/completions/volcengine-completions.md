---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/completions/volcengine-completions
---

# ByteDance Doubao (volcengine)

### 1. Overview

The text completion API launched by ByteDance, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `volcengine/doubao-seed-1-8-251228`
* `volcengine/doubao-seed-1-6-251015`
* `volcengine/doubao-seed-1-6-lite-251015`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ✅ Verified | Supported |
| Streaming Response | ✅ Verified | Supported |

### 2. API Details

{% openapi-operation spec="volcengine-en" path="/v1/completions" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/volcengine.bundled.yaml)
{% endopenapi-operation %}
