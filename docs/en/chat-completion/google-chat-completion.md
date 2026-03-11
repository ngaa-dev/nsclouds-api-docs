# Google - Chat Completion

### 1. Overview

Google's chat completion API, compatible with OpenAI interface format.

**Model List:**

* `gemini-2.5-flash` (chat mode)
* `gemini-2.5-pro` (chat mode)
* `gemini-3-flash-preview` (chat mode)
* `gemini-3-pro-preview` (chat mode)

### Functionality Verification

| Function | Status | Description |
|----------|--------|-------------|
| Basic Request | ✅ Verified | - |
| Streaming Response | ✅ Verified | - |
| Image Input | ✅ Verified | - |
| Function Call | ✅ Verified | Content filtered |

### 2. API Details

{% openapi-operation spec="google" path="/v1/chat/completions" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/google.bundled.yaml)
{% endopenapi-operation %}