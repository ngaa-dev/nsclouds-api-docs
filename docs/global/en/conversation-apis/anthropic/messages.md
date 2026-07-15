# Anthropic - Messages

### 1. Overview

Anthropic exposes Messages protocol capabilities in this environment.

{% hint style="success" %}
This endpoint provides an Anthropic Messages-compatible path. Actual behavior depends on current supported capabilities.
{% endhint %}

**Supported models：**

* `claude-haiku-4-5-20251001`
* `claude-haiku-4.5`
* `claude-opus-4.5`
* `claude-opus-4.6`
* `claude-opus-4.7`
* `claude-opus-4.8`
* `claude-sonnet-4.5`
* `claude-sonnet-4.6`


### 2. API Details

{% openapi-operation spec="anthropic-en-global" path="/v1/messages" method="post" %}
[OpenAPI Anthropic](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/en/anthropic.bundled.yaml)
{% endopenapi-operation %}
