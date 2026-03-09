# OpenAI - 向量嵌入

### 1. 概述

OpenAI 的向量嵌入 API，与 OpenAI 接口格式兼容。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `text-embedding-ada-002`
* `text-embedding-3-small`
* `text-embedding-3-large`

### 功能验证说明

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 已验证 | 支持 |

### 2. 接口详情

{% openapi-operation spec="openai-zh" path="/v1/embeddings" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/openai.bundled.yaml)
{% endopenapi-operation %}
