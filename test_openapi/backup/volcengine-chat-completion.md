# 字节豆包(volcengine)

### 1. 概述

字节跳动推出的智能对话大模型，支持多模态交互、函数调用等高级功能。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `volcengine/doubao-seed-1-8-251228`（推荐，支持多模态、函数调用）
* `volcengine/doubao-seed-1-6-251015`
* `volcengine/doubao-seed-1-6-lite-251015`
* `volcengine/doubao-seedream-4-5-251128`
* `volcengine/doubao-embedding-vision-250615`（嵌入模型）
* `volcengine/doubao-seedream-4-0-250828`
* `volcengine/doubao-asr-flash-1-6-251015`

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 已验证 | 支持 |
| 流式响应 | ✅ 已验证 | 支持 |
| 图像输入 | ✅ 已验证 | `volcengine/doubao-seed-1-8-251228` 支持 |
| 函数调用 | ✅ 已验证 | 支持 |
| logprobs | ❌ 不支持 | Reasoning model does not support |
| completions 接口 | ✅ 已验证 | 支持 |
| embeddings 接口 | ⏳ 待验证 | `volcengine/doubao-embedding-vision-250615` 支持 |
| 图像生成 | ⏳ 待验证 | 待验证 |
| 图像编辑 | ⏳ 待验证 | 待验证 |

### 2.接口详情

{% openapi-operation spec="volcengine" path="/v1/chat/completions" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/volcengine.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="volcengine" path="/v1/completions" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/volcengine.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="volcengine" path="/v1/embeddings" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/volcengine.bundled.yaml)
{% endopenapi-operation %}

{% openapi-operation spec="volcengine" path="/v1/images/generations" method="post" %}
[OpenAPI volcengine](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/volcengine.bundled.yaml)
{% endopenapi-operation %}