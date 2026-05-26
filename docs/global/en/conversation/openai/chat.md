# OpenAI - Chat Completions

### 1. Overview

OpenAI exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `gpt-5`
* `gpt-5.1`
* `gpt-5.2`
* `gpt-5.3-codex`
* `gpt-5.4`
* `gpt-5.4-mini`
* `gpt-5.5`


### 2. API Details

{% openapi-operation spec="openai-en-global" path="/v1/chat/completions" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
