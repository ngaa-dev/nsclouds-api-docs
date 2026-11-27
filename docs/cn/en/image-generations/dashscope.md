# DashScope - Image Generations

### 1. Overview

DashScope exposes image generation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Images path. Actual capabilities may vary by vendor and model.
{% endhint %}

**Supported models：**

* `qwen-image-2.0`
* `qwen-image-2.0-pro`


### 2. API Details

{% openapi-operation spec="dashscope-en-cn" path="/v1/images/generations" method="post" %}
[OpenAPI DashScope](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/cn/en/dashscope.bundled.yaml)
{% endopenapi-operation %}
