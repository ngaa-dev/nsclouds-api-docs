---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/chat-completion/deepseek-chat-completion
---

# DeepSeek

### 1. Overview

DeepSeek's current most affordable domestic large model with low prompt/generation costs, very suitable for translation needs.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `deepseek-v3.1`
* `deepseek-v3.2`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | ---------------- |
| Basic Request | ✅ Verified | All models supported |
| Streaming Response | ✅ Verified | All models supported |
| Image Input | ✅ Verified | deepseek-v3.1 supported |
| Function Call | ✅ Verified | deepseek-v3.1 supported |

### 2. API Details

{% openapi-operation spec="deepseek-en" path="/v1/chat/completions" method="post" %}
[OpenAPI deepseek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/deepseek.bundled.yaml)
{% endopenapi-operation %}
