swagger-cli bundle docs/zh/openapi/deepseek.yaml -o docs/bundled/zh/deepseek.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/deepseek.bundled.yaml
swagger-cli bundle docs/zh/openapi/openai.yaml -o docs/bundled/zh/openai.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/openai.bundled.yaml
swagger-cli bundle docs/zh/openapi/volcengine.yaml -o docs/bundled/zh/volcengine.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/volcengine.bundled.yaml
