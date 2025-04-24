# Gemini Balance - Gemini API 代理和负载均衡器

> ⚠️ 本项目采用 CC BY-NC 4.0（署名-非商业性使用）协议，禁止任何形式的商业倒卖服务，详见 LICENSE 文件。

> 本人从未在各个平台售卖服务，如有遇到售卖此服务者，那一定是倒卖狗，大家切记不要上当受骗。

> 感谢原仓库 [Gemini Balance - Gemini API 代理和负载均衡器](https://github.com/snailyp/gemini-balance)，具体参数请参考原仓库

---

## _2025-4-24 修改内容_

- 数据库 MYSQL 修改为 SQLITE
- 使用步骤
  - `git clone https://github.com/noonisy/gemini-balance-sqlite.git`
  - `cd gemini-balance-sqlite`
  - `cp .env.example .env`
  - `在 .env 中，修改 API_KEYS、ALLOWED_TOKENS 等参数`
  - `在 docker-compose.yml 中，修改 ports 等参数`
  - `sh docker.sh`

## 🙏 感谢贡献者

感谢所有为本项目做出贡献的开发者！

[![Contributors](https://contrib.rocks/image?repo=noonisy/gemini-balance-sqlite)](https://github.com/noonisy/gemini-balance-sqlite/graphs/contributors)

## 许可证

本项目采用 CC BY-NC 4.0（署名-非商业性使用）协议，禁止任何形式的商业倒卖服务，详见 LICENSE 文件。
