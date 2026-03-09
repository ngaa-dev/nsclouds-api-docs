---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/completions/volcengine-completions
---

# 字节豆包(volcengine)

### 1. 概述

字节跳动推出的文本补全 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `volcengine/doubao-seed-1-8-251228`
* `volcengine/doubao-seed-1-6-251015`
* `volcengine/doubao-seed-1-6-lite-251015`

### 功能验证说明

| 功能   | 状态    | 说明 |
| ---- | ----- | -- |
| 基础请求 | ✅ 已验证 | 支持 |
| 流式响应 | ✅ 已验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="volcengine" path="/v1/completions" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/volcengine.bundled.yaml)
{% endopenapi-operation %}
