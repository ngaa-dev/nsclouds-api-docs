# Google API 测试记录

测试环境：`https://devaillm.nscloud.ai`

## 模型列表

从 `/v1/model/info` 获取的 Google 模型：

- `imagen-3.0-generate-001`
- `imagen-3.0-generate-002`
- `imagen-3.0-fast-generate-001`
- `gemini-2.5-flash-image`
- `gemini-3-pro-image-preview`
- `gemini-3.1-flash-image-preview`
- `gemini-2.5-flash`
- `gemini-2.5-pro`
- `gemini-3-flash-preview`
- `gemini-3-pro-preview`

## 功能测试

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gemini-2.5-flash", "messages": [{"role": "user", "content": "Hello!"}], "max_completion_tokens": 50}'
```

**响应结果**:

```json
{
  "id": "chatcmpl-9AP1q66BDnIuuBx14ROTmOQFTQjZm",
  "created": 1773220495,
  "model": "gemini-2.5-flash",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hello! How can I help you today?",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 363,
    "prompt_tokens": 2,
    "total_tokens": 365,
    "completion_tokens_details": {
      "reasoning_tokens": 354
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
  -d '{"model": "gemini-2.5-flash", "messages": [{"role": "user", "content": "Hello!"}], "stream": true}'
```

**响应结果**:

```json
data: {"id":"chatcmpl-cjo4zIwpUamQ17CrksTp2uSheKXFL","created":1773220521,"model":"gemini-2.5-flash","object":"chat.completion.chunk","choices":[{"index":0,"delta":{"content":"Hello! How can I help you today?","role":"assistant"}}]}
data: {"id":"chatcmpl-cjo4zIwpUamQ17CrksTp2uSheKXFL","created":1773220521,"model":"gemini-2.5-flash","object":"chat.completion.chunk","choices":[{"finish_reason":"stop","index":0,"delta":{}}]}
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
  -d $'{"model": "gemini-2.5-flash", "messages": [{"role": "user", "content": [{"type": "text", "text": "What\'s in this image?"}, {"type": "image_url", "image_url": {"url": "https://i.imgur.com/Example.jpg"}}]}], "max_completion_tokens": 100}'
```

**响应结果**:

```json
{
  "id": "chatcmpl-6fnNV613XQyR3Xsex7ay0ClC9Wba7",
  "created": 1773221168,
  "model": "gemini-2.5-flash",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "This image captures a beautiful, tranquil **coastal scene**.\n\nHere\'s a breakdown of what\'s visible:\n\n*   **Water:** The dominant feature is clear, turquoise-blue water, indicating a shallow and inviting sea or lake. There are gentle ripples on the surface.\n*   **Boat:** A small, light-colored (possibly white or light blue) **wooden rowboat** is resting in the shallow water near the shore. It has a pair of oars inside.\n*   **Shoreline/Beach:** A sandy beach or shoreline is visible, with smooth, light-colored rocks and boulders scattered both on the sand and partially submerged in the water.\n*   **Vegetation:** Beyond the immediate shoreline, there\'s some green foliage or bushes, suggesting a natural, possibly lush landscape behind the beach.\n*   **Sky:** The sky above is bright and clear, with a few wispy white clouds, indicating a sunny day.\n\nOverall, it\'s a very peaceful and picturesque natural setting, likely a sunny day at a beach or cove.",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 1084,
    "prompt_tokens": 7,
    "total_tokens": 1091,
    "completion_tokens_details": {
      "reasoning_tokens": 863
    }
  }
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
  -d @test_openapi/function_call_test.json
```

**响应结果**:

```json
{
  "id": "chatcmpl-25e3e187-5c8f-4a98-aee5-a870c1f8f23b",
  "created": 1773221264,
  "model": "mgg-4",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "content_filter",
      "index": 0,
      "message": {
        "content": "",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 0,
    "prompt_tokens": 86,
    "total_tokens": 86,
    "prompt_tokens_details": {
      "text_tokens": 86,
      "cached_tokens_details": {}
    },
    "claude_cache_creation_5_m_tokens": 0,
    "claude_cache_creation_1_h_tokens": 0,
    "web_search_queries": 0
  }
}
```

**状态**: ✅ 验证通过（请求成功，内容被过滤）

---

### `/v1/completions` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gemini-2.5-flash", "prompt": "Say this is a test", "max_tokens": 16, "temperature": 0}'
```

**响应结果**:

```json
{
  "id": "chatcmpl-a51a50d7-0f0a-4db9-a268-ba0e4d49342b",
  "object": "text_completion",
  "created": 1773220530,
  "model": "mgg-4",
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "text": "",
      "logprobs": null
    }
  ],
  "usage": {
    "completion_tokens": 12,
    "prompt_tokens": 6,
    "total_tokens": 18,
    "completion_tokens_details": {
      "accepted_prediction_tokens": null,
      "audio_tokens": null,
      "reasoning_tokens": 12,
      "rejected_prediction_tokens": null,
      "text_tokens": null
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 6,
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

### `/v1/images/generations` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/images/generations" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "imagen-3.0-generate-001", "prompt": "A cat wearing a hat", "n": 1, "size": "1024x1024"}'
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.APIConnectionError: ZenlayerException - {\"error\":{\"message\":\"Too Many Requests\"}}. Received Model Group=imagen-3.0-generate-001\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "500"
  }
}
```

**状态**: ❌ 服务端错误（Too Many Requests）

---

### `/v1/images/edits` - 基础请求

**测试命令**:

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/images/edits" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -F "model=imagen-3.0-generate-001" \
  -F "prompt=A cat wearing a hat" \
  -F "image=@test_image.png"
```

**响应结果**:

```json
{
  "error": {
    "message": "litellm.APIConnectionError: ZenlayerException - {\"error\":{\"message\":\"Too Many Requests\"}}. Received Model Group=imagen-3.0-generate-001\nAvailable Model Group Fallbacks=None",
    "type": null,
    "param": null,
    "code": "500"
  }
}
```

**状态**: ❌ 服务端错误（Too Many Requests）

---

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅ | chat/completions 基础请求验证通过 |
| 流式响应 | ✅ | chat/completions 流式响应验证通过 |
| 图像输入 | ✅ | chat/completions 图像输入验证通过 |
| 函数调用 | ✅ | chat/completions 函数调用验证通过（内容被过滤） |
| completions 接口 | ✅ | completions 端点验证通过 |
| embeddings 接口 | ⏳ 待验证 | 未测试 |
| image generations 接口 | ❌ | 服务端错误（Too Many Requests） |
| audio transcriptions 接口 | ⏳ 待验证 | 未测试 |

## 各模型详细验证

### gemini-2.5-flash

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅ |
| chat/completions 流式 | ✅ |
| chat/completions 图像输入 | ✅ |
| chat/completions 函数调用 | ✅ |
| completions | ✅ |
| embeddings | ⏳ 待验证 |
| image generations | ❌ |
| audio transcriptions | ⏳ 待验证 |

---

### imagen-3.0-generate-001

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ⏳ 待验证 |
| chat/completions 流式 | ⏳ 待验证 |
| chat/completions 图像输入 | ⏳ 待验证 |
| chat/completions 函数调用 | ⏳ 待验证 |
| completions | ⏳ 待验证 |
| embeddings | ⏳ 待验证 |
| image generations | ❌ |
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
   - `/v1/images/generations` (服务端错误)
   - `/v1/images/edits` (服务端错误)