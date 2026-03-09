---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/chat-completion/volcengine-chat-completion
---

# ByteDance Doubao (volcengine)

### 1. Overview

ByteDance's intelligent dialogue large model, supporting advanced features such as multimodal interaction and function calling.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `volcengine/doubao-seed-1-8-251228` (Recommended, supports multimodal, function calling)
* `volcengine/doubao-seed-1-6-251015`
* `volcengine/doubao-seed-1-6-lite-251015`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -------------------------------------- |
| Basic Request | ✅ Verified | Supported |
| Streaming Response | ✅ Verified | Supported |
| Image Input | ✅ Verified | `volcengine/doubao-seed-1-8-251228` supported |
| Function Call | ✅ Verified | Supported |

### 2. API Details

{% openapi-operation spec="volcengine-en" path="/v1/chat/completions" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/volcengine.bundled.yaml)
{% endopenapi-operation %}
