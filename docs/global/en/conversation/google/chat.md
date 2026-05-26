# Google - Chat Completions

### 1. Overview

Google exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `gemini-3-flash-preview`
* `gemini-3.1-flash-lite-preview`
* `gemini-3.1-pro-preview`


### 2. API Details

{% openapi-operation spec="google-en-global" path="/v1/chat/completions" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/google.bundled.yaml)
{% endopenapi-operation %}
