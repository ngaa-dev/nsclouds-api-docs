# OpenAI - 图像生成

### 1. 概述

OpenAI 在当前环境中提供的图像生成能力。

{% hint style="success" %}
本接口提供 OpenAI Images API 的 gpt-image-2 图像能力。
{% endhint %}

**模型列表：**

* `gpt-image-2`


### 2. gpt-image-2 参数说明

{% hint style="info" %}
`gpt-image-2` 支持文本生成图像。`n` 可请求 1-10 张图像，实际返回数量可能少于请求数量。
{% endhint %}

| 参数 | 支持情况 |
| --- | --- |
| `prompt` | 必填，最长参考为 32000 个字符。 |
| `n` | 可选，范围参考为 1-10；实际返回图片数量可能少于请求数量。 |
| `size` | 可选，支持 `auto` 和下方列出的固定尺寸。 |
| `quality` | 可选，支持 `low`、`medium`、`high`；省略、`auto`、`standard` 按 `high` 计费。 |
| `background` | 可选，支持 `opaque`、`auto`。 |
| `moderation` | 可选，仅图像生成接口支持，支持 `low`、`auto`。 |
| `output_format` | 可选，支持 `png`、`jpeg`。 |
| `output_compression` | 可选，范围 0-100，仅 `jpeg` 使用；`png` 应省略或设为 100。 |

支持尺寸：`auto`, `1024x1024`, `1024x1536`, `1536x1024`, `2048x2048`, `2048x1152`, `3840x2160`, `2160x3840`, `2048x1360`, `1360x2048`, `1152x2048`, `2048x1536`, `1536x2048`, `2048x880`, `880x2048`, `688x2048`, `2048x688`, `2048x1024`, `1024x2048`

### 3. 接口详情

{% openapi-operation spec="openai-zh-global" path="/v1/images/generations" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/openai.bundled.yaml)
{% endopenapi-operation %}
