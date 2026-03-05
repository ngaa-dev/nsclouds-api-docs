# OpenAI 对话生成 API

本文档提供了 OpenAI 对话生成 API 的详细参考，完全兼容 OpenAI 格式。

## API 端点

### POST /v1/chat/completions

创建聊天补全，基于输入的消息生成模型回复。

#### 请求示例

```json
{
  "model": "gpt-4",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "Hello!" }
  ],
  "temperature": 1,
  "max_completion_tokens": 50,
  "n": 1,
  "stream": false
}
```

### POST /v1/completions

创建文本补全，基于提供的提示生成一个或多个补全结果。

#### 请求示例

```json
{
  "model": "gpt-3.5-turbo-instruct",
  "prompt": "Once upon a time",
  "max_tokens": 50,
  "temperature": 0.7,
  "n": 1,
  "stream": false
}
```

## OpenAPI 规范

完整的 API 规范请参考 [openapi.json](openapi.json) 文件。
