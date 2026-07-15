# DeepSeek - Messages

### 1. Overview

DeepSeek exposes Messages protocol capabilities in this environment.

{% hint style="success" %}
This endpoint provides an Anthropic Messages-compatible path. Actual behavior depends on current supported capabilities.
{% endhint %}

**Supported models：**

* `deepseek/deepseek-v3.2`
* `deepseek/deepseek-v4-flash`
* `deepseek/deepseek-v4-pro`


### 2. API Details

{% openapi-operation spec="deepseek-en-global" path="/v1/messages" method="post" %}
[OpenAPI DeepSeek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/deepseek.bundled.yaml)
{% endopenapi-operation %}
