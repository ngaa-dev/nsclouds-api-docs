# Google - 图像生成

### 1. 概述

Google 的图像生成 API，与 OpenAI 接口格式兼容。

**模型列表：**

* `imagen-3.0-generate-001` (image_generation 模式)
* `imagen-3.0-generate-002` (image_generation 模式)
* `imagen-3.0-fast-generate-001` (image_generation 模式)
* `gemini-2.5-flash-image` (image_generation 模式)
* `gemini-3-pro-image-preview` (image_generation 模式)
* `gemini-3.1-flash-image-preview` (image_generation 模式)

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ❌ 服务端错误 | Too Many Requests |
| 图像编辑 | ❌ 服务端错误 | Too Many Requests |

### 2. 接口详情

{% openapi-operation spec="google" path="/v1/images/generations" method="post" %}
[OpenAPI Google](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/google.bundled.yaml)
{% endopenapi-operation %}