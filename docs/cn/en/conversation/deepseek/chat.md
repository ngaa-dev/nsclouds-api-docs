# DeepSeek - Chat Completions

### 1. Overview

DeepSeek exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `deepseek-r1`
* `deepseek-v3.2`
* `deepseek-v4-flash`
* `deepseek-v4-pro`
* `volcengine/deepseek-v3-2-251201`


### 2. API Details

{% openapi-operation spec="deepseek-en-cn" path="/v1/chat/completions" method="post" %}
[OpenAPI DeepSeek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/cn/en/deepseek.bundled.yaml)
{% endopenapi-operation %}
