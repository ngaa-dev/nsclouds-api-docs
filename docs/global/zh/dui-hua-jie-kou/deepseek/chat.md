# DeepSeek - Chat Completions

### 1. 概述

DeepSeek 在当前环境中提供的对话生成能力。

{% hint style="success" %}
本接口提供与 OpenAI Chat Completions 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。
{% endhint %}

**模型列表：**

* `deepseek/deepseek-v3.2`
* `deepseek/deepseek-v4-flash`
* `deepseek/deepseek-v4-pro`


### 2. 接口详情

{% openapi-operation spec="deepseek-zh-global" path="/v1/chat/completions" method="post" %}
[OpenAPI DeepSeek](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/deepseek.bundled.yaml)
{% endopenapi-operation %}
