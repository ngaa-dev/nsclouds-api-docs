# 深度求索(DeepSeek) - 音频转录

### 1. 概述

深度求索推出的音频转录 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `deepseek-audio-transcription`

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ⏳ 待验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="deepseek-zh" path="/v1/audio/transcriptions" method="post" %}
[OpenAPI deepseek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/deepseek.bundled.yaml)
{% endopenapi-operation %}
