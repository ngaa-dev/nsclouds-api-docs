# DashScope - Chat Completions

### 1. Overview

DashScope exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `MiniMax-M2.5`
* `MiniMax-M2.7`
* `qwen3.6-flash`
* `qwen3.6-max-preview`
* `qwen3.6-plus`
* `qwen3.7-max`


### 2. API Details

{% openapi-operation spec="dashscope-en-global" path="/v1/chat/completions" method="post" %}
[OpenAPI DashScope](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/en/dashscope.bundled.yaml)
{% endopenapi-operation %}
