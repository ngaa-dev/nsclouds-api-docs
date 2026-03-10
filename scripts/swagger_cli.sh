swagger-cli bundle docs/zh/openapi/deepseek.yaml -o docs/bundled/zh/deepseek.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/deepseek.bundled.yaml
swagger-cli bundle docs/zh/openapi/example.yaml -o docs/bundled/zh/example.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/example.bundled.yaml
swagger-cli bundle docs/zh/openapi/openai.yaml -o docs/bundled/zh/openai.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/openai.bundled.yaml
swagger-cli bundle docs/zh/openapi/volcengine.yaml -o docs/bundled/zh/volcengine.bundled.yaml -t yaml
swagger-cli validate docs/bundled/zh/volcengine.bundled.yaml

# English version
swagger-cli bundle docs/en/openapi/deepseek.yaml -o docs/bundled/en/deepseek.bundled.yaml -t yaml
swagger-cli validate docs/bundled/en/deepseek.bundled.yaml
swagger-cli bundle docs/en/openapi/example.yaml -o docs/bundled/en/example.bundled.yaml -t yaml
swagger-cli validate docs/bundled/en/example.bundled.yaml
swagger-cli bundle docs/en/openapi/openai.yaml -o docs/bundled/en/openai.bundled.yaml -t yaml
swagger-cli validate docs/bundled/en/openai.bundled.yaml
swagger-cli bundle docs/en/openapi/volcengine.yaml -o docs/bundled/en/volcengine.bundled.yaml -t yaml
swagger-cli validate docs/bundled/en/volcengine.bundled.yaml
