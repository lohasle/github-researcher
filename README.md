# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 今日研究摘要（2026-04-07）

**本日核心趋势：Multi-Agent Orchestration 生态爆发 + MCP 协议扩散**

今日热榜新信号：
- **GitNexus**（857 stars/day）：代码知识图谱 + MCP Server，让 AI Agent 获得深度代码库理解。CLI 一键索引，`npx gitnexus analyze` 即可为 Cursor/Claude Code/Codex 注入全代码库上下文。比 DeepWiki 更深，是 AI Coding Agent 的"感知层基础设施"。
- **qmd**（394 stars/day）：本地 CLI 搜索工具，BM25 + 向量 + LLM 重排，全本地运行，通过 MCP 暴露工具给 Agent。全程离线，隐私优先。
- **LiteRT-LM**：Google 生产级端侧 LLM 推理框架，已在 Chrome、Chromebook Plus、Pixel Watch 上跑。 Gemma 4 端侧部署，工具调用支持，跨 Android/iOS/Web/桌面/IoT。

持续跟踪项目无重大变化，hermes-agent（1,574 stars/day）、VibeVoice、shannon 维持昨日判断。

**→ [查看今日完整简报](daily/2026-04-07.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-04-07](daily/2026-04-07.md) | Multi-Agent Orchestration 爆发、MCP 协议扩散 | 4 个深度分析 + 5 个关注 |

---

## 当前最值得关注的趋势

1. **Multi-Agent Orchestration 团队化**：oh-my-claudecode 代表以"团队"为原子的新范式。Claude Code 正在变成 Multi-Agent 开发平台。
2. **AI Agent 记忆与自进化**：hermes-agent 的 Skill 自进化机制是少数真正触及"Agent 学习"核心的项目。
3. **Voice AI 基础设施化**：VibeVoice-ASR 进 HuggingFace Transformers 意味着 Voice AI 正在成为标准基础设施组件。
4. **MCP 协议扩散**：GitNexus、qmd 等项目将 MCP 作为核心接口，协议层基础设施地位确立。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [hermes-agent](projects/hermes-agent.md) | 基础设施候选 | Agent 自进化 + 跨会话记忆 | **深度跟踪 + PoC** |
| [oh-my-claudecode](projects/oh-my-claudecode.md) | 平台候选 | Multi-Agent 团队化编排 | 持续跟踪 |
| [VibeVoice](projects/VibeVoice.md) | 生产可用 | 微软 Voice AI，ASR 进 HF | 关注 ASR 部分 |
| [shannon](projects/shannon.md) | 泡沫型/学习型 | AI 渗透测试 | 关注技术思路即可 |

---

## 新增关注项目

| 项目 | 今日 Star | 本周 Star | 核心价值 | 建议 |
|------|----------|----------|---------|------|
| [GitNexus](projects/GitNexus.md) | 857 | — | 代码知识图谱 + MCP Server，AI Coding Agent 感知层 | **值得深挖** |
| [qmd](projects/qmd.md) | 394 | — | 本地文档搜索 + MCP 暴露，Agent 记忆基础设施 | 持续跟踪 |

---

## 目录结构

```
/daily/YYYY-MM-DD.md    # 每日研究简报
/indexes/trend-index.md  # 趋势指数（项目排名变化、关键判断）
/projects/{name}.md     # 项目档案（深度分析、评分）
/feedback/YYYY-MM-DD.md # 用户反馈记录
```

---

## 核心关注领域

- AI Agent / Multi-Agent / Coding Agent
- LLM Infra / RAG / 向量数据库 / 推理框架 / MCP / AI Runtime
- 开发工具链 / IDE / CLI / Copilot / DevEx
- 前端框架 / 全栈框架 / Serverless / Edge Runtime / BaaS
- 云原生 / K8s / 网关 / Service Mesh / 可观测性
- 自动化 / Browser Use / Workflow / RPA + AI
- 数据基础设施 / 数据同步 / 缓存 / 存储 / 实时计算
- 有潜力演变成平台、底座或基础设施标准的项目

---

## 趋势历史索引

- [趋势指数总表](indexes/trend-index.md)
- [项目档案索引](projects/)

---

*仓库初始化：2026-04-07 | 最后更新：2026-04-07*
