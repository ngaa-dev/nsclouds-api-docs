# Google - Completions

### 1. Overview

Google's text completion API, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `gemini-2.5-flash` (completion mode)
* `gemini-2.5-pro` (completion mode)
* `gemini-3-flash-preview` (completion mode)
* `gemini-3-pro-preview` (completion mode)

### Functionality Verification

| Function | Status | Description |
|----------|--------|-------------|
| Basic Request | ✅ Verified | - |
| Streaming Response | ⏳ Pending | - |

### 2. API Details

{% openapi-operation spec="google-en" path="/v1/completions" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/google.bundled.yaml)
{% endopenapi-operation %}