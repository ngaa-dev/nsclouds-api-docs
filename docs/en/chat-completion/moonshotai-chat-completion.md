# Moonshot AI - Chat Completion

### 1. Overview

Moonshot AI's chat completion API, compatible with OpenAI interface format.

**Model List:**

* `kimi-k2.5` (chat mode)
* `kimi-k2-thinking` (chat mode)

### Functionality Verification

| Function | Status | Description |
|----------|--------|-------------|
| Basic Request | ✅ Verified | - |
| Streaming Response | ✅ Verified | - |
| Image Input | ❌ Not Supported | Model cannot recognize image input |
| Function Call | ⏳ Pending | - |

### 2. API Details

{% openapi-operation spec="moonshotai" path="/v1/chat/completions" method="post" %}
[OpenAPI Moonshot AI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/moonshotai.bundled.yaml)
{% endopenapi-operation %}
