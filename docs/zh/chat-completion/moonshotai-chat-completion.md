# Moonshot AI - 对话生成

### 1. 概述

Moonshot AI 的对话生成 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `kimi-k2.5` (chat 模式)
* `kimi-k2-thinking` (chat 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 验证通过 | - |
| 流式响应 | ✅ 验证通过 | - |
| 图像输入 | ❌ 不支持 | 模型无法识别图像输入 |
| 函数调用 | ⏳ 待验证 | - |

### 2. 接口详情

{% openapi-operation spec="moonshotai" path="/v1/chat/completions" method="post" %}
[OpenAPI Moonshot AI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/moonshotai.bundled.yaml)
{% endopenapi-operation %}