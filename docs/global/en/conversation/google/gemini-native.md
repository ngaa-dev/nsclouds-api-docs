# Google - Gemini Native

### 1. Overview

Google exposes Gemini native protocol capabilities in this environment.

{% hint style="success" %}
This endpoint provides a Google Gemini native-compatible path.
{% endhint %}

**Supported models：**

* `gemini-3-flash-preview`
* `gemini-3.1-flash-lite-preview`
* `gemini-3.1-pro-preview`


### 2. API Details

{% openapi-operation spec="google-en-global" path="/v1/models/{model}:generateContent" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/google.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="google-en-global" path="/v1beta/models/{model}:generateContent" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/google.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="google-en-global" path="/v1beta/models/{model}:streamGenerateContent" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/google.bundled.yaml)
{% endopenapi-operation %}
