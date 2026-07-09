# Chat Completions

### 1. Overview

Z.AI exposes conversation capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Chat Completions path. Actual parameter support may vary by vendor and model.
{% endhint %}

**Supported models：**

* `glm-4.6`
* `glm-4.6v`
* `glm-4.7`
* `glm-5`
* `glm-5.1`
* `glm-5.2`

### 2. API Details

{% openapi-operation spec="zai-en-cn" path="/v1/chat/completions" method="post" %}
[OpenAPI zai-en-cn](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/csy-api-docs/docs/bundled/cn/en/zai.bundled.yaml)
{% endopenapi-operation %}
