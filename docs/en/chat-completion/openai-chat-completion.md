---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/chat-completion/openai-chat-completion
---

# OpenAI

### 1. 概述

OpenAI 是全球领先的 AI 研究机构，提供强大的 GPT 系列大语言模型，包括 GPT-4、GPT-3.5 等，支持文本生成、对话、图像生成等多种 AI 能力。

{% hint style="success" %}
本 API 与 OpenAI 接口格式兼容。
{% endhint %}

**模型列表：**

* `gpt-4`
* `gpt-4-turbo`
* `gpt-3.5-turbo`

### 2.接口详情

{% openapi-operation spec="openai" path="/v1/chat/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/zh/openai.bundled.yaml)
{% endopenapi-operation %}
