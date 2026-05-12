# Google - Gemini Native

### 1. 概述

Google 的 Gemini 原生协议能力。

{% hint style="success" %}
本 API 与 Gemini 原生接口格式兼容。
{% endhint %}

**模型列表：**

* `gemini-3-flash-preview`
* `gemini-3.1-flash-lite-preview`
* `gemini-3.1-pro-preview`


### 2. 接口详情

{% openapi-operation spec="google-zh-global" path="/v1/models/{model}:generateContent" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/google.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="google-zh-global" path="/v1beta/models/{model}:generateContent" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/google.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="google-zh-global" path="/v1beta/models/{model}:streamGenerateContent" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/google.bundled.yaml)
{% endopenapi-operation %}
