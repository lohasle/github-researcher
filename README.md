# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 目的

持续跟踪 GitHub 最火的项目和技术趋势，从"架构设计、工程效率、AI Agent、开发范式、基础设施演进"的角度，输出高价值研究成果。

不是热榜搬运，而是**趋势判断 + 架构分析 + 泡沫识别 + 潜力评估**。

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

## 判断原则

不只看 star。综合：
- 热度质量（增速 vs 总量）
- 技术创新度（真实创新 vs 概念包装）
- 工程成熟度（文档、测试、部署可行性）
- 架构启发价值（对架构师有价值的思路）
- 企业落地潜力（能否进生产）
- 中期趋势概率（6-18个月后还在吗）

---

## 当前重点跟踪

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| hermes-agent | 基础设施候选 | Agent 自进化 + 跨会话记忆 | **深度跟踪 + PoC** |
| oh-my-claudecode | 平台候选 | Multi-Agent 团队化编排 | 持续跟踪 |
| VibeVoice | 生产可用 | 微软 Voice AI，ASR 进 HF | 关注 ASR 部分 |

---

## 历史趋势判断

### 2026-04-07 — Multi-Agent Orchestration 爆发

三大项目同周爆发：
- oh-my-claudecode（7832/week）
- oh-my-codex（14247/week）
- hermes-agent（9662/week）

判断：**以"团队"为原子的多 Agent 协作正在从概念走向工程化**

---

*仓库初始化：2026-04-07*
