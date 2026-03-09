---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/completions/deepseek-completions
---

# 深度求索(DeepSeek)

### 1. 概述

深度求索推出的文本补全 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `volcengine/deepseek-v3-1-terminus`

### 功能验证说明

| 功能   | 状态    | 说明 |
| ---- | ----- | -- |
| 基础请求 | ✅ 已验证 | 支持 |
| 流式响应 | ✅ 已验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="deepseek" path="/v1/completions" method="post" %}
[OpenAPI deepseek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/deepseek.bundled.yaml)
{% endopenapi-operation %}
