# 厂家 API 验证规范

本文档描述了验证和更新厂家 API 文档的完整流程，以 DeepSeek 验证过程为参考。

## 前提条件

- 已有基础 OpenAPI 文件：`docs/zh/openapi/openai.yaml`
- 已创建厂家特定文件：`docs/zh/openapi/{vendor}.yaml`
- 测试环境地址已配置
- API Key 已设置到环境变量 `$NGAA_LLM_API_KEY`

## 验证流程

### 1. 获取模型信息

使用 `/v1/model/info` 接口获取所有模型信息：

```bash
curl -X GET "https://devaillm.nscloud.ai/v1/model/info" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY"
```

保存响应到 `test_openapi/model_info.json`：

```bash
curl -X GET "https://devaillm.nscloud.ai/v1/model/info" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -o test_openapi/model_info.json
```

提取目标厂家模型：

```bash
cat test_openapi/model_info.json | python3 -c "import json,sys; data=json.load(sys.stdin); models=[d['model_name'] for d in data['data'] if '{vendor}' in d['model_name'].lower()]; print('\n'.join(models))"
```

### 2. 验证端点功能

根据模型的 `mode` 字段验证对应端点。从 `model_info.json` 中提取模型的 `mode` 字段，确定需要验证的端点：

**提取模型及其 mode：**
```bash
cat test_openapi/model_info.json | python3 -c "import json,sys; data=json.load(sys.stdin); models=[(d['model_name'], d.get('mode','')) for d in data['data'] if '{vendor}' in d['model_name'].lower()]; print('\n'.join([f'{m[0]}: {m[1]}' for m in models]))"
```

常见 mode 类型及对应端点：
- `chat` → `/v1/chat/completions` 和 `/v1/completions`（两者都需要验证）
- `completion` → `/v1/completions`  
- `embedding` → `/v1/embeddings`
- `image_generation` → `/v1/images/generations`
- `audio_transcription` → `/v1/audio/transcriptions`

#### 2.1 Chat 模式验证 `/v1/chat/completions`

**基础请求测试：**

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_completion_tokens": 50
  }'
```

**流式响应测试：**

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "stream": true
  }'
```

**图像输入测试（如果支持）：**

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
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

**函数调用测试（如果支持）：**

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/chat/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
    "messages": [
      {"role": "user", "content": "What is the weather in Boston?"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_current_weather",
          "description": "Get the current weather in a given location",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto",
    "max_completion_tokens": 150
  }'
```

#### 2.2 Completion 模式验证 `/v1/completions`

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/completions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
    "prompt": "Say this is a test",
    "max_tokens": 7,
    "temperature": 0
  }'
```

#### 2.3 Embedding 模式验证 `/v1/embeddings`

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/embeddings" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
    "input": "The food was delicious and the waiter was very friendly."
  }'
```

#### 2.4 Image Generation 模式验证 `/v1/images/generations`

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/images/generations" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "{model_name}",
    "prompt": "A cat wearing a hat",
    "n": 1,
    "size": "1024x1024"
  }'
```

#### 2.5 Audio Transcription 模式验证 `/v1/audio/transcriptions`

```bash
curl -X POST "https://devaillm.nscloud.ai/v1/audio/transcriptions" \
  -H "Authorization: Bearer $NGAA_LLM_API_KEY" \
  -F "model={model_name}" \
  -F "file=@/path/to/audio.mp3"
```

### 3. 记录测试结果

将所有测试命令和响应结果记录到 `test_openapi/test_{vendor}.md`，格式如下：

```markdown
# {Vendor} API 测试记录

测试环境：`https://devaillm.nscloud.ai`

## 模型列表

从 `/v1/model/info` 获取的 {vendor} 模型：

- {model_name_1}
- {model_name_2}
- ...

## 功能测试

### `/v1/chat/completions` - 基础请求

**测试命令**:

```bash
{command}
```

**响应结果**:

```json
{response}
```

**状态**: ✅ 验证通过 / ❌ 不支持

---

### `/v1/chat/completions` - 流式响应

**测试命令**:

```bash
{command}
```

**响应结果**:

```json
{response}
```

**状态**: ✅ 验证通过 / ❌ 不支持

---

## 功能测试汇总

| 功能 | 状态 | 说明 |
|------|------|------|
| 基础请求 | ✅/❌ | 说明 |
| 流式响应 | ✅/❌ | 说明 |
| 图像输入 | ✅/❌ | 说明 |
| 函数调用 | ✅/❌ | 说明 |
| completions 接口 | ✅/❌ | 说明 |
| embeddings 接口 | ✅/❌ | 说明 |
| image generations 接口 | ✅/❌ | 说明 |
| audio transcriptions 接口 | ✅/❌ | 说明 |

## 各模型详细验证

### {model_name}

| 端点/功能 | 状态 |
|-----------|------|
| chat/completions 基础 | ✅/❌ |
| chat/completions 流式 | ✅/❌ |
| chat/completions 图像输入 | ✅/❌ |
| chat/completions 函数调用 | ✅/❌ |
| completions | ✅/❌ |
| embeddings | ✅/❌ |
| image generations | ✅/❌ |
| audio transcriptions | ✅/❌ |

---

## 总结

1. **已验证端点**:
   - 列出已验证的端点

2. **已验证功能**:
   - 列出已验证的功能

3. **不支持端点**:
   - 列出不支持的端点
```

### 4. 更新 API 文档

#### 4.1 更新 `{vendor}.yaml` 中的 examples

根据测试结果更新 `docs/zh/openapi/{vendor}.yaml`：

- 使用真实测试数据替换所有 examples
- 使用实际可用的模型名称
- 确保响应数据与实际测试结果一致
- **数据展示优化**：如果真实数据特别大（如流式响应的完整事件流或 embedding 的完整向量），examples 可以省略部分数据，使用 `...` 表示省略，确保文档简洁易读

**关键更新点：**

1. **Chat Completions 端点**（如果存在 chat 模式模型）：
   - 基础请求 example
   - 流式响应 example
   - 图像输入 example（如果支持）
   - 函数调用 example（如果支持）

2. **Completions 端点**（如果存在 completion 模式模型）：
   - 基础请求 example
   - 流式响应 example

3. **Embeddings 端点**（如果存在 embedding 模式模型）：
   - 基础请求 example

4. **Image Generations 端点**（如果存在 image_generation 模式模型）：
   - 基础请求 example

5. **Audio Transcriptions 端点**（如果存在 audio_transcription 模式模型）：
   - 基础请求 example

#### 4.2 更新厂家说明文档

根据模型类型，更新对应的功能点文档：

| 功能点 | 文档路径 | 说明 |
|--------|----------|------|
| 对话生成 | `docs/zh/chat-completion/{vendor}-chat-completion.md` | 更新 chat 模式模型和功能 |
| 文本补全 | `docs/zh/completions/{vendor}-completions.md` | 更新 completion 模式模型和功能 |
| 向量嵌入 | `docs/zh/embeddings/{vendor}-embeddings.md` | 更新 embedding 模式模型和功能 |
| 图像生成 | `docs/zh/image-generations/{vendor}-image-generations.md` | 更新 image_generation 模式模型和功能 |
| 音频转录 | `docs/zh/audio-transcriptions/{vendor}-audio-transcriptions.md` | 更新 audio_transcription 模式模型和功能 |

**更新内容：**
- 更新模型列表为实际可用的模型
- 更新功能验证说明表格，标记支持/不支持的功能
- 移除不支持的参数说明
- 添加实际测试结果和示例

#### 4.3 更新 Authorization 格式

确保 `{vendor}.yaml` 中的 security scheme 使用 Bearer 格式：

```yaml
securitySchemes:
  APIKeyHeader:
    type: http
    scheme: bearer
    bearerFormat: YOUR_API_KEY
    description: 在请求头中添加 Authorization: Bearer YOUR_API_KEY
```

### 5. 生成 Bundled YAML

运行脚本生成 bundled 文件：

```bash
bash scripts/swagger_cli.sh
```

这将：
- 生成 `docs/bundled/zh/{vendor}.bundled.yaml`
- 验证 YAML 格式正确性

### 6. 提交到远程仓库

```bash
git add docs/zh/openapi/{vendor}.yaml \
        docs/zh/chat-completion/{vendor}-chat-completion.md \
        docs/bundled/zh/{vendor}.bundled.yaml \
        test_openapi/model_info.json \
        test_openapi/test_{vendor}.md

git commit -m "docs({vendor}): 更新 {vendor} API 文档

- 更新 {vendor}.yaml examples 为真实测试数据
- 更新模型列表为实际可用的模型
- 移除不支持的参数 examples
- 添加测试记录文件"

git push origin main
```

## 注意事项

1. **测试环境**：
   - 使用测试环境 `devaillm.nscloud.ai` 进行验证
   - 正式环境地址不在文档中体现

2. **模型选择**：
   - 优先选择功能最全面的模型作为 example
   - completions 端点可能只有特定模型支持

3. **参数验证**：
   - 仔细测试每个参数是否支持
   - 不支持的参数必须从 examples 中移除

4. **数据准确性**：
   - 所有 examples 必须使用真实的测试数据
   - 包括真实的 id、created 时间戳、token 数量等

5. **文档一致性**：
   - 确保 YAML 文件和 Markdown 文档内容一致
   - 模型列表必须与实际可用的模型一致

6. **GitBook 显示**：
   - 确保 Authorization 格式正确显示为 `Bearer YOUR_API_KEY`
   - 所有 examples 在 GitBook 中正确渲染

## 验证检查清单

- [ ] 获取并保存 model_info.json
- [ ] 提取目标厂家所有模型及其 mode 类型
- [ ] 根据 mode 类型确定需要验证的端点
- [ ] 验证 chat/completions 基础请求（chat 模式）
- [ ] 验证 chat/completions 流式响应（chat 模式）
- [ ] 验证图像输入（chat 模式，如果支持）
- [ ] 验证函数调用（chat 模式，如果支持）
- [ ] 验证 completions 端点（completion 模式）
- [ ] 验证 embeddings 端点（embedding 模式）
- [ ] 验证 image generations 端点（image_generation 模式）
- [ ] 验证 audio transcriptions 端点（audio_transcription 模式）
- [ ] 记录所有测试命令和结果到 test_{vendor}.md
- [ ] 更新 {vendor}.yaml 中的 examples
- [ ] 移除不支持的参数 examples
- [ ] 更新 {vendor}-chat-completion.md 模型列表
- [ ] 更新功能验证说明
- [ ] 生成 bundled YAML
- [ ] 验证 YAML 格式正确性
- [ ] 提交到远程仓库

## 参考示例

完整的 DeepSeek 验证过程可参考：
- 测试记录：`test_openapi/test_deepseek.md`
- 模型信息：`test_openapi/model_info.json`
- API 文档：`docs/zh/openapi/deepseek.yaml`
- 说明文档：`docs/zh/chat-completion/deepseek-chat-completion.md`
