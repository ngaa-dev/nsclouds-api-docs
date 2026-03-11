# Anthropic - Chat Completion

### 1. Overview

Anthropic's chat completion API, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `claude-haiku-4.5` (chat mode)
* `claude-opus-4.5` (chat mode)
* `claude-sonnet-4.5` (chat mode)
* `claude-opus-4.6` (chat mode)
* `claude-sonnet-4.6` (chat mode)

### Functionality Verification

| Function | Status | Description |
|----------|--------|-------------|
| Basic Request | ✅ Verified | - |
| Streaming Response | ✅ Verified | - |
| Image Input | ❌ Not Supported | - |
| Function Call | ⏳ Pending | - |

### 2. API Details

{% openapi-operation spec="anthropic-en" path="/v1/chat/completions" method="post" %}
[OpenAPI Anthropic](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/anthropic.bundled.yaml)
{% endopenapi-operation %}