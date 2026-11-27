# DashScope - Audio Transcriptions

### 1. Overview

DashScope exposes audio transcription capabilities in this environment.

{% hint style="success" %}
This endpoint provides an OpenAI-compatible Audio Transcriptions path. Actual capabilities may vary by vendor and model.
{% endhint %}

**Supported models：**

* `qwen3-asr-flash`


### 2. API Details

{% openapi-operation spec="dashscope-en-global" path="/v1/audio/transcriptions" method="post" %}
[OpenAPI DashScope](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/en/dashscope.bundled.yaml)
{% endopenapi-operation %}
