# Moonshot AI API 测试记录

测试环境：`https://devaillm.nscloud.ai`

## 模型列表

从 `/v1/model/info` 获取的 moonshotai 模型：

- `kimi-k2.5` (chat 模式)
- `kimi-k2-thinking` (chat 模式)

## 功能测试

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2.5",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_completion_tokens": 50
  }'
```

**响应结果**:

```json
{
  "id": "chatcmpl-8415e78a-7989-99de-9e4f-2b0ec895f35f",
  "created": 1773224824,
  "model": "kimi-k2.5",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I help you today? 😊",
        "role": "assistant",
        "reasoning_content": ""
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 12,
    "prompt_tokens": 11,
    "total_tokens": 23,
    "completion_tokens_details": {
      "text_tokens": 12
    },
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 11
    }
  }
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
    "model": "kimi-k2.5",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "stream": true
  }'
```

**响应结果**:

```
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":"Hello","role":"assistant"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" there"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":"!"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" How"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" can"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" I"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" help"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" you"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":" today"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"index":0,"delta":{"content":"?"}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
data: {"id":"chatcmpl-907c71cf-c857-907c-bfd4-238a07d3888f","object":"chat.completion.chunk","created":1773224832,"model":"kimi-k2.5","choices":[{"finish_reason":"stop","index":0,"delta":{}}],"usage":{"completion_tokens":0,"prompt_tokens":0,"total_tokens":0}}
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
    "model": "kimi-k2.5",
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
  "id": "chatcmpl-f77d68cd-42dd-9576-b99d-4b8df9c6a3b2",
  "created": 1773224846,
  "model": "kimi-k2.5",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "I don't see any image in your message. Could you please share the image you'd like me to describe? You can upload it directly to our conversation.",
        "role": "assistant",
        "reasoning_content": ""
      },
      "provider_specific_fields": {}
    }
  ],
  "usage": {
    "completion_tokens": 31,
    "prompt_tokens": 15,
    "total_tokens": 46,
    "completion_tokens_details": {
      "text_tokens": 31
    },
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 15
    }
  }
}
```

**状态**: ❌ 不支持（模型无法识别图像输入）

---

### `/v1/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2.5",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.BadRequestError: OpenAIException - Error code: 404 - {'error': {'message': 'Unsupported model `kimi-k2.5` for OpenAI compatibility mode.', 'type': 'invalid_request_error', 'param': None, 'code': 'model_not_supported'}, 'request_id': 'f511ecf7-2c9e-97a8-aef3-48aa9dac8285'}. Received Model Group=kimi-k2.5\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "400"
  }
}
```

**状态**: ❌ 不支持（模型不支持 completions 端点）

---

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ | 验证通过 |
| 流式响应 | ✅ | 验证通过 |
| 图像输入 | ❌ | 不支持 |
| 函数调用 | ⏳ | 待验证 |
| completions 接口 | ❌ | 不支持 |

## 各模型详细验证

### kimi-k2.5

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| chat/completions 图像输入 | ❌ |
| chat/completions 函数调用 | ⏳ |
| completions | ❌ |

### kimi-k2-thinking

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ⏳ |
| chat/completions 流式 | ⏳ |
| chat/completions 图像输入 | ⏳ |
| chat/completions 函数调用 | ⏳ |
| completions | ⏳ |

---

## 总结

1. **已验证端点**:
   - `/v1/chat/completions` 基础请求 ✅
   - `/v1/chat/completions` 流式响应 ✅

2. **已验证功能**:
   - 基础对话生成
   - 流式响应

3. **不支持端点**:
   - `/v1/completions`（模型不支持 OpenAI 兼容模式）
   - `/v1/chat/completions` 图像输入（模型无法识别图像）

4. **模型特点**:
   - 所有 moonshotai 模型均为 chat 模式
   - 响应中包含 `reasoning_content` 字段（为空字符串）
   - 不支持 completions 端点