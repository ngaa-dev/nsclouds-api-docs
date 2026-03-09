# OpenAI - 文本补全

### 1. 概述

OpenAI 的文本补全 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-3.5-turbo-instruct`

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 已验证 | 支持 |
| 流式响应 | ✅ 已验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="openai-zh" path="/v1/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/openai.bundled.yaml)
{% endopenapi-operation %}
