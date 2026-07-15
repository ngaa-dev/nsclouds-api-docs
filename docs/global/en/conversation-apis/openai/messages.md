# OpenAI - Messages

### 1. Overview

OpenAI exposes Messages protocol capabilities in this environment.

{% hint style="success" %}
This endpoint provides an Anthropic Messages-compatible path. Actual behavior depends on current supported capabilities.
{% endhint %}

**Supported models：**

* `gpt-5.3-codex`
* `gpt-5.4-mini`


### 2. API Details

{% openapi-operation spec="openai-en-global" path="/v1/messages" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
