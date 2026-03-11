# Google - 文本补全

### 1. 概述

Google 的文本补全 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `gemini-2.5-flash` (completion 模式)
* `gemini-2.5-pro` (completion 模式)
* `gemini-3-flash-preview` (completion 模式)
* `gemini-3-pro-preview` (completion 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | - |
| 流式响应 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="google-zh" path="/v1/completions" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/google.bundled.yaml)
{% endopenapi-operation %}