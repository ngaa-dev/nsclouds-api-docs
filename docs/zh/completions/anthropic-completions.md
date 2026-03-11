# Anthropic - 文本补全

### 1. 概述

Anthropic 的文本补全 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `claude-haiku-4.5` (completion 模式)
* `claude-opus-4.5` (completion 模式)
* `claude-sonnet-4.5` (completion 模式)
* `claude-opus-4.6` (completion 模式)
* `claude-sonnet-4.6` (completion 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | - |
| 流式响应 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="anthropic-zh" path="/v1/completions" method="post" %}
[OpenAPI Anthropic](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/anthropic.bundled.yaml)
{% endopenapi-operation %}