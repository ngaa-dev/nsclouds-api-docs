# 字节豆包(volcengine) API 测试记录

测试环境：`https://devaillm.nscloud.ai`

## 模型列表

从 `/v1/model/info` 获取的字节豆包模型：

- `volcengine/doubao-seed-1-6-251015`
- `volcengine/doubao-seed-1-6-lite-251015`
- `volcengine/doubao-seed-1-8-251228`
- `volcengine/doubao-seedream-4-5-251128`
- `volcengine/doubao-embedding-vision-250615`
- `volcengine/doubao-seedream-4-0-250828`
- `volcengine/doubao-asr-flash-1-6-251015`

## 功能测试

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "volcengine/doubao-seed-1-8-251228",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_completion_tokens": 50
  }'
```

**响应结果**:

```json
{
  "id": "021772864435690b7e0a86771f3aae54bdc5a127ef95baa9c2b48",
  "created": 1772864438,
  "model": "volcengine/doubao-seed-1-8-251228",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello there! 😊 How can I assist you today?",
        "role": "assistant",
        "reasoning_content": "用户说\"Hello!\"，我需要回应一个友好的问候。首先，保持自然亲切，比如\"Hello there! 😊 How can I assist you today?\"这样既回应了问候，又表达了愿意帮忙的态度，符合AI的角色设定。检查一下，语言简洁友好，带有表情符号更生动，应该没问题。"
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 83,
    "prompt_tokens": 50,
    "total_tokens": 133,
    "completion_tokens_details": {
      "reasoning_tokens": 71
    },
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "service_tier": "default"
}
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 流式响应

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "volcengine/doubao-seed-1-8-251228",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "stream": true
  }'
```

**响应结果**:

```
data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"自然","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"和","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"热情","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"，","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"比如","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"\"","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"Hello","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" there","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"!","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" 😊","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" How","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" can","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" I","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" assist","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" you","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":" today","content":""}}],"service_tier":"default"}

data: {"id":"021772864453949134a33f22921f0bc01c0430890f5ffa37aa326","created":1772864454,"model":"doubao-seed-1-8-251228","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"reasoning_content":"?\"","content":""}}],"service_tier":"default"}

data: [DONE]
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 图像输入

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "volcengine/doubao-seed-1-8-251228",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_5_imageToimage.png"
            }
          }
        ]
      }
    ],
    "max_completion_tokens": 300
  }'
```

**响应结果**:

```json
{
  "id": "021772864507442454c0d8025bd4547674d07aeb10e65a37260a1",
  "created": 1772864518,
  "model": "volcengine/doubao-seed-1-8-251228",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "This is a futuristic, surreal, cyberpunk-style digital or 3D-rendered artwork:\n1.  The central subject is a humanoid figure, appearing feminine, posed dynamically with their head tilted back, arms outstretched, in front of a simple studio white backdrop on black support rigs.\n2.  The figure is covered in a **glossy, reflective liquid chrome/silver metallic substance** that forms an organic, fragmented \"garment\" with sharp, tendril-like, drippy edges, and also coats their head, forming spiky, wet-look \"hair\", arms, and hands. The material looks like it's in a state of transformation, as if melting or solidifying onto the body.\n3.  The bright studio lighting emphasizes the highly reflective, polished surface of the metallic coating, creating strong highlights and deep shadows that give the material a viscous, molten appearance.\n4.  The overall aesthetic is sci-fi, futuristic high-fashion, with a biomechanical, otherworldly, almost \"liquid metal being\" vibe, recalling cyborg or synthetic entity concepts.",
        "role": "assistant",
        "reasoning_content": "Got it, let's break down this image. First, it's a futuristic, cyberpunk-style 3D (or AI-generated) art piece of a figure (appears to be a woman) in a studio setting, in front of a white backdrop stand.\n\nThe figure is covered in a **liquid-like, reflective metallic (silver/chrome) substance** that forms a fragmented, organic \"dress\" with sharp, tendril-like, drippy edges, and also covers her head (spiky, wet-looking chrome hair/coating) and parts of her arms. Her pose is dramatic: head tilted back, arms outstretched, looking upward, giving a sense of transformation or a futuristic, otherworldly vibe.\n\nThe lighting is bright, studio-style, highlighting the reflective, glossy surface of the chrome material, creating strong highlights and shadows that emphasize the liquid, sculpted texture. The overall aesthetic is sci-fi, futuristic fashion, with a surreal, biomechanical/liquid metal feel, like a being made of or covered in a shifting, molten chrome substance."
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 452,
    "prompt_tokens": 540,
    "total_tokens": 992,
    "completion_tokens_details": {
      "reasoning_tokens": 224
    },
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "service_tier": "default"
}
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - 函数调用

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d @test_openapi/function_call.json
```

**响应结果**:

```json
{
  "id": "02177286456308318cc8b35e794a1d5ce66758b690d3ae1fd30df",
  "created": 1772864571,
  "model": "volcengine/doubao-seed-1-8-251228",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "tool_calls",
      "index": 0,
      "message": {
        "content": "",
        "role": "assistant",
        "tool_calls": [
          {
            "function": {
              "arguments": " {\"location\": \"Boston, MA\"}",
              "name": "get_current_weather"
            },
            "id": "call_xlu24zqz1ptz3git9mwjmn9x",
            "type": "function"
          }
        ],
        "reasoning_content": "Got it, let's see. The user is asking about the weather in Boston. The function available is get_current_weather, which requires location and optionally unit. The location here is Boston, so I need to specify that. Wait, do I need to include state? The example uses \"San Francisco, CA\", but Boston is in Massachusetts, so maybe \"Boston, MA\" is better, but maybe just \"Boston\" works too? Wait, the function's location parameter says city and state, but maybe if I just put Boston, it might still get it, but to be precise, I should include MA. Also, the unit isn't specified by the user, so I can either leave it out (since it's not required) or ask? Wait no, the required parameter is location, so unit is optional. So I can call the function with location \"Boston, MA\" and maybe not include unit, or let it default? Wait the function parameters say unit is optional, so I can omit it, but maybe the user would prefer a specific unit? But since they didn't ask, I just call with location first. Let me structure the function call correctly. So the function name is get_current_weather, parameters location is \"Boston, MA\". Let me write that in the required format."
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 301,
    "prompt_tokens": 459,
    "total_tokens": 760,
    "completion_tokens_details": {
      "reasoning_tokens": 266
    },
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "service_tier": "default"
}
```

**状态**: ✅ 验证通过

---

### `/v1/chat/completions` - logprobs（不支持）

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "volcengine/doubao-seed-1-8-251228",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_completion_tokens": 10,
    "logprobs": true,
    "top_logprobs": 2
  }'
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.BadRequestError: VolcengineException - Reasoning model does not support n > 1, logit_bias, logprobs, top_logprobs Request id: 0217728645885098cf12c1a4b092384500fba0fc49677b085d7e5. Received Model Group=volcengine/doubao-seed-1-8-251228\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "400"
  }
}
```

**状态**: ❌ 不支持

---

### `/v1/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "volcengine/doubao-seed-1-8-251228",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
```

**响应结果**:

```json
{
  "id": "0217728646073678cf12c1a4b092384500fba0fc49677b04d2fb3",
  "object": "text_completion",
  "created": 1772864610,
  "model": "volcengine/doubao-seed-1-8-251228",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "text": "This is a test",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 119,
    "prompt_tokens": 53,
    "total_tokens": 172,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 115,
      "rejected_prediction_tokens": null,
      "text_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": null,
      "image_tokens": null
    }
  }
}
```

**状态**: ✅ 验证通过

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ 已验证 | 支持 |
| 流式响应 | ✅ 已验证 | 支持 |
| 图像输入 | ✅ 已验证 | 支持 |
| 函数调用 | ✅ 已验证 | 支持 |
| logprobs | ❌ 不支持 | Reasoning model does not support |
| completions 接口 | ✅ 已验证 | 支持 |

## 各模型详细验证

### volcengine/doubao-seed-1-8-251228

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| chat/completions 图像输入 | ✅ |
| chat/completions 函数调用 | ✅ |
| chat/completions logprobs | ❌ |
| completions | ✅ |

---

## 总结

1. **已验证端点**:
   - `/v1/chat/completions` - 支持所有测试功能
   - `/v1/completions` - 支持文本补全

2. **已验证功能**:
   - ✅ 基础请求
   - ✅ 流式响应
   - ✅ 图像输入（多模态）
   - ✅ 函数调用
   - ❌ logprobs（不支持）

3. **特殊特性**:
   - 所有响应包含 `reasoning_content` 字段，提供模型的推理过程
   - 支持详细的 token 使用情况统计

4. **不支持端点**:
   - 尚未验证其他端点（embeddings、image generations 等）