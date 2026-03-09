---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/image-generations/openai-image-generations
---

# OpenAI

### 1. 概述

OpenAI 的图像生成 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `dall-e-3`
* `dall-e-2`

### 功能验证说明

| 功能   | 状态    | 说明 |
| ---- | ----- | -- |
| 基础请求 | ✅ 已验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="openai" path="/v1/images/generations" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/openai.bundled.yaml)
{% endopenapi-operation %}
