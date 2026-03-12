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

* `gpt-5` (chat mode)
* `gpt-5.2` (chat mode)
* `gpt-5.4` (chat mode)
* `gpt-5.3-codex` (chat mode)

### Feature Verification

| Feature | Status | Description |
|:---------|:--------|:-------------|
| Basic Request | ✅ Verified | gpt-5, gpt-5.2 available |
| Streaming | ✅ Verified | Test successful, returns streaming data |
| Image Input | ✅ Verified | gpt-5.2 supports multimodal image input |
| Function Calling | ⚠️ Partial | Model recognizes function call request but doesn't execute actual call |

### 2. API Details

{% openapi-operation spec="openai-en-global" path="/v1/chat/completions" method="post" %}
[OpenAPI openai](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/openai.bundled.yaml)
{% endopenapi-operation %}
