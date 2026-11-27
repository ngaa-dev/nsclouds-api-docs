# DashScope - Chat Completions

### 1. 概述

DashScope 在当前环境中提供的对话生成能力。

{% hint style="success" %}
本接口提供与 OpenAI Chat Completions 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。
{% endhint %}

**模型列表：**

* `MiniMax-M2.5`
* `MiniMax-M2.7`
* `qwen3.6-flash`
* `qwen3.6-max-preview`
* `qwen3.6-plus`
* `qwen3.7-max`


### 2. 接口详情

{% openapi-operation spec="dashscope-zh-global" path="/v1/chat/completions" method="post" %}
[OpenAPI DashScope](https://raw.githubusercontent.com/ngaa-dev/nsclouds-api-docs/main/docs/bundled/global/zh/dashscope.bundled.yaml)
{% endopenapi-operation %}
