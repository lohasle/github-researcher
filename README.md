# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-04-08）

**本日核心趋势：claw-code 爆炸式增长 · Edge AI 加速落地 · Claude Code 生态持续扩张**

今日热榜新信号：
- **claw-code**（168.7K stars，+10K/week）：史上最快突破 100K stars 的项目，2 小时达 50K。Rust 构建，自主维护（非人工），代表 AI Coding Agent 赛道天花板远未触及。
- **LiteRT**（google-ai-edge）：TensorFlow Lite 继任者，Google 生产级端侧 ML 框架，已在 Chrome、Pixel Watch 等生产环境落地。配合 Gemma-4 端侧部署，端侧 LLM 推理正在成为现实。
- **oh-my-codex**（+14K/week）：Claude Code 生态增长最快的组件之一，与 oh-my-claudecode 形成双平台覆盖。

MCP 协议从概念走向生产：GitNexus（代码知识图谱）、qmd（本地文档搜索）、hermes-agent（MCP Gateway）均在用 MCP 构建实际产品。

**→ [查看 2026-04-08 完整简报](daily/2026-04-08.md)**
**→ [查看 2026-04-07 完整简报](daily/2026-04-07.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-04-08](daily/2026-04-08.md) | claw-code 爆炸式增长、Edge AI 落地、Claude Code 生态扩张 | 7 个深度分析 |
| [2026-04-07](daily/2026-04-07.md) | Multi-Agent Orchestration 爆发、MCP 协议扩散 | 4 个深度分析 + 5 个关注 |

---

## 当前最值得关注的趋势

1. **AI Coding Agent 生态爆发**：claw-code 史上最快破 100K stars，oh-my-codex/oh-my-claudecode 形成双平台覆盖，AI Coding Agent 赛道天花板远未触及。
2. **Edge AI / 端侧推理生产化**：Google LiteRT + Gemma-4 端侧部署构成完整端侧 AI 推理栈，端侧 LLM 推理正在进入真实产品。
3. **MCP 协议基础设施化**：GitNexus、qmd、hermes-agent 用 MCP 构建实际产品，MCP 从"AI Agent 协议"演化为"AI Native 应用协议层"。
4. **Multi-Agent Orchestration 团队化**：oh-my-claudecode 代表以"团队"为原子的新范式。
5. **Voice AI 组件化**：VibeVoice ASR 进 HuggingFace Transformers，Voice AI 正在成为标准基础设施组件。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [claw-code](projects/claw-code.md) | 头部项目 | 史上最快破100K stars，AI Coding Agent | **必须持续跟踪** |
| [hermes-agent](projects/hermes-agent.md) | 基础设施候选 | Agent 自进化 + 跨会话记忆 + MCP Gateway | **深度跟踪 + PoC** |
| [oh-my-codex](projects/oh-my-codex.md) | 平台候选 | Claude Code Codex 版，+14K/week | 持续跟踪 |
| [LiteRT](projects/litert.md) | 基础设施候选 | Google 端侧 ML 框架，TFLite 继任者 | 关注端侧推理赛道 |
| [GitNexus](projects/GitNexus.md) | 工具型 | 代码知识图谱 + MCP Server | **值得深挖** |
| [VibeVoice](projects/VibeVoice.md) | 生产可用 | 微软 Voice AI，ASR 进 HF | 关注 ASR 部分 |
| [oh-my-claudecode](projects/oh-my-claudecode.md) | 平台候选 | Multi-Agent 团队化编排 | 持续跟踪 |

---

## 新增关注项目（2026-04-08）

| 项目 | Stars | 核心价值 | 建议 |
|------|-------|---------|------|
| [claw-code](projects/claw-code.md) | 168.7K | 史上最快破100K，AI Coding Agent | **头部项目** |
| [oh-my-codex](projects/oh-my-codex.md) | 18K | Claude Code Codex 版，+14K/week | 持续跟踪 |
| [LiteRT](projects/litert.md) | 2K+ | Google 端侧 ML 框架 | 关注端侧赛道 |
| [claw-code-parity](projects/claw-code-parity.md) | 新项目 | claw-code 重写版本 | 观察架构差异 |

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

*仓库初始化：2026-04-07 | 最后更新：2026-04-08*
