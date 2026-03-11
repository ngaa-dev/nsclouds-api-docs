# Anthropic - Completions

### 1. Overview

Anthropic's text completion API, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `claude-haiku-4.5` (completion mode)
* `claude-opus-4.5` (completion mode)
* `claude-sonnet-4.5` (completion mode)
* `claude-opus-4.6` (completion mode)
* `claude-sonnet-4.6` (completion mode)

### Functionality Verification

| Function | Status | Description |
|----------|--------|-------------|
| Basic Request | ✅ Verified | - |
| Streaming Response | ⏳ Pending | - |

### 2. API Details

{% openapi-operation spec="anthropic-en" path="/v1/completions" method="post" %}
[OpenAPI Anthropic](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/anthropic.bundled.yaml)
{% endopenapi-operation %}