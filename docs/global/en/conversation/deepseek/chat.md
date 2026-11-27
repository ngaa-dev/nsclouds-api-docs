# DeepSeek - Chat Completions

### 1. Overview

DeepSeek exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `deepseek/deepseek-v3.2`
* `deepseek/deepseek-v4-flash`
* `deepseek/deepseek-v4-pro`


### 2. API Details

{% openapi-operation spec="deepseek-en-global" path="/v1/chat/completions" method="post" %}
[OpenAPI DeepSeek](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/en/deepseek.bundled.yaml)
{% endopenapi-operation %}
