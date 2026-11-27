# DashScope - Messages

### 1. Overview

DashScope exposes Messages protocol capabilities in this environment.

{% hint style="success" %}
This endpoint provides an Anthropic Messages-compatible path. Actual behavior depends on current supported capabilities.
{% endhint %}

**Supported models：**

* `qwen3.6-flash`
* `qwen3.6-max-preview`
* `qwen3.6-plus`


### 2. API Details

{% openapi-operation spec="dashscope-en-cn" path="/v1/messages" method="post" %}
[OpenAPI DashScope](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/cn/en/dashscope.bundled.yaml)
{% endopenapi-operation %}
