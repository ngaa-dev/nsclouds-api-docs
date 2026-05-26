# Google - Gemini Native

### 1. 概述

Gemini 原生协议接口，支持 `generateContent` 与 `streamGenerateContent`。

{% hint style="success" %}
本接口提供与 Google Gemini 原生协议兼容的请求路径。
{% endhint %}

### 2. 接口详情

{% openapi-operation spec="google-zh-{{ENV}}" path="/v1/models/{model}:generateContent" method="post" %}
[OpenAPI google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/google.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="google-zh-{{ENV}}" path="/v1beta/models/{model}:generateContent" method="post" %}
[OpenAPI google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/google.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="google-zh-{{ENV}}" path="/v1beta/models/{model}:streamGenerateContent" method="post" %}
[OpenAPI google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/{{ENV}}/zh/google.bundled.yaml)
{% endopenapi-operation %}
