# OpenAI - 图像编辑

### 1. 概述

OpenAI 在当前环境中提供的图像编辑能力。

{% hint style="success" %}
本接口提供 OpenAI Images API 的 gpt-image-2 图像能力。
{% endhint %}

**模型列表：**

* `gpt-image-2`


### 2. gpt-image-2 参数说明

{% hint style="info" %}
`gpt-image-2` 支持基于一张或多张输入图像进行编辑。`mask` 为可选参数，透明区域代表需要编辑的区域。
{% endhint %}

| 参数 | 支持情况 |
| --- | --- |
| `image` | 必填，支持单图或多图；可传 URL、base64、data URI 或文件上传。 |
| `prompt` | 必填，最长参考为 32000 个字符。 |
| `mask` | 可选，透明区域代表编辑区域。 |
| `n` | 可选，范围参考为 1-10；实际返回图片数量可能少于请求数量。 |
| `size` | 可选，支持 `auto` 和下方列出的固定尺寸。 |
| `quality` | 可选，支持 `low`、`medium`、`high`；省略、`auto`、`standard` 按 `high` 计费。 |
| `background` | 可选，支持 `opaque`、`auto`。 |
| `output_format` | 可选，支持 `png`、`jpeg`。 |

支持尺寸：`auto`, `1024x1024`, `1024x1536`, `1536x1024`, `2048x2048`, `2048x1152`, `3840x2160`, `2160x3840`, `2048x1360`, `1360x2048`, `1152x2048`, `2048x1536`, `1536x2048`, `2048x880`, `880x2048`, `688x2048`, `2048x688`, `2048x1024`, `1024x2048`

### 3. 接口详情

{% openapi-operation spec="openai-zh-global" path="/v1/images/edits" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/openai.bundled.yaml)
{% endopenapi-operation %}
