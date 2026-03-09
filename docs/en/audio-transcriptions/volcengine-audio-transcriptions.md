---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/audio-transcriptions/volcengine-audio-transcriptions
---

# ByteDance Doubao (volcengine)

### 1. Overview

The audio transcription API launched by ByteDance, compatible with OpenAI interface format.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `volcengine/doubao-asr-flash-1-6-251015`

### Feature Verification

| Feature | Status | Description |
| ---- | ----- | -- |
| Basic Request | ⏳ Pending Verification | Supported |

### 2. API Details

{% openapi-operation spec="volcengine-en" path="/v1/audio/transcriptions" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/volcengine.bundled.yaml)
{% endopenapi-operation %}
