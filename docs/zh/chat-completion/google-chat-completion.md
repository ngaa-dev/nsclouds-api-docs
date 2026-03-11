# Google - 对话生成

### 1. 概述

Google 的对话生成 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `gemini-2.5-flash` (chat 模式)
* `gemini-2.5-pro` (chat 模式)
* `gemini-3-flash-preview` (chat 模式)
* `gemini-3-pro-preview` (chat 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | - |
| 流式响应 | ✅ 验证通过 | - |
| 图像输入 | ✅ 验证通过 | - |
| 函数调用 | ✅ 验证通过 | 内容被过滤 |

### 2. 接口详情

{% openapi-operation spec="google" path="/v1/chat/completions" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/google.bundled.yaml)
{% endopenapi-operation %}