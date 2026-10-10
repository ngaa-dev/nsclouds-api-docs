# OpenAI - 图像生成

### 1. 概述

OpenAI 在当前环境中提供的图像生成能力。

{% hint style="success" %}
本接口提供 OpenAI Images API 的 GPT Image 2 与 GPT Image 2.5 图像能力。
{% endhint %}

**模型列表：**

* `gpt-image-2`
* `gpt-image-2-oai`
* `gpt-image-2.5-flare`
* `gpt-image-2.5-flare-oai`
* `gpt-image-2.5-sunburst`
* `gpt-image-2.5-sunburst-oai`


### 2. 图像模型参数说明

#### 模型资源与计费方式

以下区别适用于本平台的模型名称，图像生成和图像编辑使用相同的计费规则。

带 `-oai` 后缀代表 OpenAI 直连资源，不带该后缀代表 AWS 资源。资源来源与计费方式分别如下：

| 模型 | 资源来源 | 计费方式 |
| --- | --- | --- |
| `gpt-image-2-oai` | OpenAI 直连 | 按实际 Token 用量计费 |
| `gpt-image-2` | AWS | 按图像张数计费，单张价格由像素规模和生成质量档位确定 |
| `gpt-image-2.5-flare-oai` | OpenAI 直连 | 仅支持 Token 计费 |
| `gpt-image-2.5-sunburst-oai` | OpenAI 直连 | 仅支持 Token 计费 |
| `gpt-image-2.5-flare` | AWS | 仅支持 Token 计费 |
| `gpt-image-2.5-sunburst` | AWS | 仅支持 Token 计费 |

GPT Image 2.5 全系列均按响应顶层 `usage` 的实际 Token 用量结算，分别计算文本输入、图片输入和图片输出。`size`、`quality` 可能影响实际 Token 消耗，但不使用独立的按张、像素或质量档位价格。

`gpt-image-2` 的费用按图像张数与对应档位的单张价格计算，不套用 Token 价格。`gpt-image-2-oai` 的 Token 在顶层 `usage` 汇总，不会为每个 `data[]` 图片单独返回。具体单价及缓存输入费率以所选模型的价格配置为准，GPT Image 2.5 的价格表不自动适用于 `gpt-image-2-oai`。

#### gpt-image-2

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

#### GPT Image 2.5

{% hint style="info" %}
推荐使用 `gpt-image-2.5-flare-oai` 进行快速图片生成，使用 `gpt-image-2.5-sunburst-oai` 进行精细图片编辑。所有带 `-oai` 后缀的 GPT Image 模型使用 OpenAI 直连资源，不带该后缀的模型使用 AWS 资源。GPT Image 2.5 全系列仅支持按 Token 计费，不支持按图像张数、像素或质量档位计费。
{% endhint %}

`quality` 支持 `low`、`medium`、`high`、`xhigh`、`max` 和 `auto`，默认值为 `auto`。透明背景需同时设置 `background="transparent"` 和 `output_format="png"` 或 `"webp"`。

费用按响应 `usage` 中的实际 token 用量计算（每 100 万 token）：

| 类型 | 输入 | 缓存输入 | 输出 |
| --- | ---: | ---: | ---: |
| 文本 | $5.00 | $1.25 | - |
| 图片 | $8.00 | $2.00 | $30.00 |

`usage.input_tokens_details` 区分文本、图片和缓存输入 token，`usage.output_tokens_details` 返回图片输出 token。token 仅在顶层 `usage` 汇总返回，不会附加到每个 `data[]` 图片对象。

### 3. 接口详情

{% openapi-operation spec="openai-zh-global" path="/v1/images/generations" method="post" %}
[OpenAPI OpenAI](https://raw.githubusercontent.com/liujia-hbu/nsclouds-api-docs/main/docs/bundled/global/zh/openai.bundled.yaml)
{% endopenapi-operation %}
