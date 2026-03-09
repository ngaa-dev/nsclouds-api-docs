---
metaLinks:
  alternates:
    - >-
      https://app.gitbook.com/s/x8h0Gte093KpUAW4Bcpp/chat-completion/openai-chat-completion
---

# OpenAI

### 1. Overview

OpenAI is a world-leading AI research organization that provides powerful GPT series large language models, including GPT-4, GPT-3.5, etc., supporting various AI capabilities such as text generation, dialogue, and image generation.

{% hint style="success" %}
This API is compatible with OpenAI interface format.
{% endhint %}

**Model List:**

* `gpt-4`
* `gpt-4-turbo`
* `gpt-3.5-turbo`

### 2. API Details

{% openapi-operation spec="openai-en" path="/v1/chat/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/en/openai.bundled.yaml)
{% endopenapi-operation %}
