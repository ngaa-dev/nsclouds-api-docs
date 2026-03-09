---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/embeddings/volcengine-embeddings
---

# 字节豆包(volcengine)

### 1. 概述

字节跳动推出的向量嵌入 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `volcengine/doubao-embedding-vision-250615`（支持视觉输入的嵌入模型）

### 功能验证说明

| 功能   | 状态    | 说明 |
| ---- | ----- | -- |
| 基础请求 | ⏳ 待验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="volcengine" path="/v1/embeddings" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/volcengine.bundled.yaml)
{% endopenapi-operation %}
