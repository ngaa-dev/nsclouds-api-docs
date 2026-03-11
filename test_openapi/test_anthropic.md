# Anthropic API 测试记录

测试环境：`https://devaillm.nscloud.ai`

## 模型列表

从 `/v1/model/info` 获取的 Anthropic 模型：

- `claude-haiku-4.5`
- `claude-opus-4.5`
- `claude-sonnet-4.5`
- `claude-opus-4.6`
- `claude-sonnet-4.6`

## 功能测试

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"claude-opus-4.6","messages":[{"role":"user","content":"Hello!"}],"max_completion_tokens":50}'
```

**响应结果**:

```json
{
  "id": "chatcmpl-02VKOdtBIb7RkHb97f0WePbsjjQkB",
  "created": 1773222937,
  "model": "claude-opus-4-6",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How are you doing today? Is there something I can help you with? 😊",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 23,
    "prompt_tokens": 9,
    "total_tokens": 32
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
  -d '{"model":"claude-opus-4.6","messages":[{"role":"user","content":"Hello!"}],"stream":true}'
```

**响应结果**:

```json
data: {"id":"chatcmpl-WWcxVVS3hexiKVbk3QCGSMV5wToGL","created":1773222960,"model":"claude-opus-4-6","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"Hello! How are","role":"assistant"}}]}
data: {"id":"chatcmpl-WWcxVVS3hexiKVbk3QCGSMV5wToGL","created":1773222960,"model":"claude-opus-4-6","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" you doing today? Is there anything I"}}]}
data: {"id":"chatcmpl-WWcxVVS3hexiKVbk3QCGSMV5wToGL","created":1773222960,"model":"claude-opus-4-6","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" can help you with?"}}]}
data: {"id":"chatcmpl-WWcxVVS3hexiKVbk3QCGSMV5wToGL","created":1773222960,"model":"claude-opus-4-6","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":" "}}]}
data: {"id":"chatcmpl-WWcxVVS3hexiKVbk3QCGSMV5wToGL","created":1773222960,"model":"claude-opus-4-6","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"😊"}}]}
data: {"id":"chatcmpl-WWcxVVS3hexiKVbk3QCGSMV5wToGL","created":1773222960,"model":"claude-opus-4-6","object":"chat.completion.chunk","choices":[{"finish_reason":"stop","index":0,"delta":{}}]}
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
  -d $'{"model":"claude-opus-4.6","messages":[{"role":"user","content":[{"type":"text","text":"What\'s in this image?"},{"type":"image_url","image_url":{"url":"https://i.imgur.com/Example.jpg"}}]}],"max_completion_tokens":100}'
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.APIConnectionError: KscloudException - {\"error\":{\"type\":\"Bad Request\",\"message\":\"InvokeModel: operation error Bedrock Runtime: InvokeModel, https response error StatusCode: 400, RequestID: 29d6c396-1836-40ea-855a-be449158a05f, ValidationException: ***.***.***.***.***.source.base64.media_type: Field required (request id: 20260311095621641193734kaU2zINu)\"},\"type\":\"error\"}. Received Model Group=claude-opus-4.6\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "500"
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
  -d '{"model":"claude-opus-4.6","prompt":"Say this is a test","max_tokens":16,"temperature":0}'
```

**响应结果**:

```json
{
  "id": "msg_01MMX9dbQ7ZPgjhMhgLPRuCz",
  "object": "text_completion",
  "created": 1773223039,
  "model": "mco-4",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "text": "This is a test.",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 8,
    "prompt_tokens": 12,
    "total_tokens": 20,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": null,
      "image_tokens": null,
      "cached_tokens_details": {}
    },
    "claude_cache_creation_5_m_tokens": 0,
    "claude_cache_creation_1_h_tokens": 0,
    "web_search_queries": 0
  }
}
```

**状态**: ✅ 验证通过

---

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ | chat/completions 基础请求验证通过 |
| 流式响应 | ✅ | chat/completions 流式响应验证通过 |
| 图像输入 | ❌ | chat/completions 图像输入不支持 |
| 函数调用 | ⏳ 待验证 | 未测试 |
| completions 接口 | ✅ | completions 端点验证通过 |
| embeddings 接口 | ⏳ 待验证 | 未测试 |
| image generations 接口 | ⏳ 待验证 | 未测试 |
| audio transcriptions 接口 | ⏳ 待验证 | 未测试 |

## 各模型详细验证

### claude-opus-4.6

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| chat/completions 图像输入 | ❌ |
| chat/completions 函数调用 | ⏳ 待验证 |
| completions | ✅ |
| embeddings | ⏳ 待验证 |
| image generations | ⏳ 待验证 |
| audio transcriptions | ⏳ 待验证 |

---

## 总结

1. **已验证端点**:
   - `/v1/chat/completions` (基础请求和流式响应)
   - `/v1/completions`

2. **已验证功能**:
   - Chat 模式基础请求
   - Chat 模式流式响应
   - Completions 接口

3. **不支持端点**:
   - `/v1/chat/completions` 图像输入 (不支持)
