---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/audio-transcriptions/openai-audio-transcriptions
---

# OpenAI

### 1. 概述

OpenAI 的音频转录 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `whisper-1`
* `whisper-large-v3`

### 功能验证说明

| 功能   | 状态    | 说明 |
| ---- | ----- | -- |
| 基础请求 | ✅ 已验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="openai" path="/v1/audio/transcriptions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/openai.bundled.yaml)
{% endopenapi-operation %}
