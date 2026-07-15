# Anthropic - Chat Completions

### 1. 概述

Anthropic 在当前环境中提供的对话生成能力。

{% hint style="success" %}
本接口提供与 OpenAI Chat Completions 兼容的请求路径。不同厂家和模型的实际参数支持范围可能不同。
{% endhint %}

**模型列表：**

* `claude-haiku-4-5-20251001`
* `claude-haiku-4.5`
* `claude-opus-4.5`
* `claude-opus-4.6`
* `claude-opus-4.7`
* `claude-opus-4.8`
* `claude-sonnet-4.5`
* `claude-sonnet-4.6`


### 2. 接口详情

{% openapi-operation spec="anthropic-zh-global" path="/v1/chat/completions" method="post" %}
[OpenAPI Anthropic](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/anthropic.bundled.yaml)
{% endopenapi-operation %}
