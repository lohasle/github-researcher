# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-06-20）

**LLM Token 经济学基础设施爆发（headroom 38K⭐ 日增 3,938——压缩即基础设施 + codebase-memory-mcp 8K 用知识图谱替代 grep） · Agent Skill 安全生态成型（NVIDIA SkillSpector 64 类漏洞检测——Skill 供应链安全的 SAST 时刻） · Agent 框架第二轮混战（Astro flue 沙箱框架 + BuilderIO agent-native 应用框架 + Kilo 22.9K 开源 Coding Agent——三种范式争夺开发者心智） · 基础模型超越文本（Google TimesFM 2.5 时间序列基础模型已部署 BigQuery/Sheets/Vertex） · Coding Agent 可观测性赛道启动（agentsview 2.9K 本地化 20+ Agent 分析）**

今日热榜新信号：
- **chopratejas/headroom**（38,394 stars）：LLM Token 压缩基础设施——60-95% 压缩 + Proxy/Library/MCP 三模式 + 跨 Agent 内存 + 输出 token 削减
- **DeusData/codebase-memory-mcp**（8,119 stars）：代码知识图谱 MCP——tree-sitter 158 语言索引 + sub-ms 查询 + 120x token 削减 + 单静态二进制
- **NVIDIA/SkillSpector**（8,251 stars）：Agent Skill 安全扫描器——64 类漏洞 × 16 分类 + AST + taint tracking + YARA + MCP 投毒检测

**→ [查看 2026-06-20 完整简报](daily/2026-06-20.md)**
**→ [查看 2026-06-19 完整简报](daily/2026-06-19.md)**
**→ [查看 2026-06-15 完整简报](daily/2026-06-15.md)**
**→ [查看 2026-06-14 完整简报](daily/2026-06-14.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-06-20](daily/2026-06-20.md) | LLM Token 经济学基础设施爆发（headroom 38K⭐ 日增 3,9 | 5 个深度分析 |
| [2026-06-19](daily/2026-06-19.md) | Agent Skill 经济学验证完成（ponytail 36K⭐ 一周暴涨 4 | 4 个深度分析 |
| [2026-06-15](daily/2026-06-15.md) | Agent Skills 杀手级应用涌现（last30days-skill 42 | 4 个深度分析 |
| [2026-06-14](daily/2026-06-14.md) | Agent Skills 全栈基础设施化：分发层(agent-skills 58 | 6 个深度分析 |
| [2026-06-13](daily/2026-06-13.md) | Agent 架构分层加速：shadcn/improve 贵模型审计+廉模型执行分 | 6 个深度分析 |
| [2026-06-12](daily/2026-06-12.md) | Agent Skills 生态爆发：addyosmani/agent-skill | 5 个深度分析 |
| [2026-06-11](daily/2026-06-11.md) | Agent 编排分层：shadcn/improve 745⭐ 顾问模式引爆 Ag | 5 个深度分析 |

---

## 当前最值得关注的趋势

1. **LLM Token 经济学基础设施爆发：headroom 38K⭐ 日增 3,938（60-95% 压缩 + 跨 Agent 内存 + 输出 token 削减 + CacheAligner），codebase-memory-mcp 8K⭐ 日增 1,055（tree-sitter 知识图谱 + 158 语言 + sub-ms 查询 + 120x token 削减）。压缩和索引不再是优化，而是 Agent 时代的基础设施层**：相关项目 headroom, codebase-memory-mcp, agentsview。
2. **Agent Skill 安全生态成型：NVIDIA SkillSpector 8.2K⭐ 周增 5,505，64 类漏洞检测覆盖 16 分类（prompt injection / 数据泄露 / 供应链 / 权限越界 / MCP 投毒），研究显示 26.1% Skills 有漏洞、5.2% 恶意——Skill 供应链安全的 SAST 时刻到来**：相关项目 nvidia-skillspector, headroom, agent-reach。
3. **Agent 框架第二轮混战：Astro 团队 flue（沙箱 Agent 框架 + 持久执行 + CRDT 多人协作）5.8K⭐，BuilderIO agent-native（Agent 原生应用框架 + 共享 action + MCP/A2A/AG-UI 全协议）1K⭐，Kilo Code 22.9K⭐ 日增 1,217（开源 Coding Agent + VS Code/JetBrains/CLI 三端 + 500+ 模型）——三种完全不同的 Agent 范式在同一天热门**：相关项目 withastro-flue, builderio-agent-native, kilo-code。
4. **基础模型超越文本：Google TimesFM 2.5（200M 参数 + 16K context + 连续分位数预测）日增 1,516⭐，已在 BigQuery ML / Google Sheets / Vertex Model Garden 生产部署。时间序列基础模型不再是研究——是 Google 生产线上的工具**：相关项目 google-timesfm, lightricks-ltx-2。
5. **Coding Agent 可观测性赛道启动：agentsview 2.9K⭐ 周增 1,382，支持 20+ Agent 的会话搜索/分析/成本统计，ccusage 的 100x 替代。单一二进制、全本地化、DuckDB mirror——轻量级 Agent 可观测性的最佳实践**：相关项目 agentsview, headroom。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [12-Factor Agents](projects/12-factor-agents.md) | 基础设施候选 | 构建足够好到可以交给专业用户使用的 LLM 驱动软件的 12 条工程原则，Age | 持续跟踪 |
| [DietrichGebert/ponytail](projects/ponytail.md) | 工具型 | 让 AI Agent 像最懒的资深工程师一样思考——YAGNI 极简主义 Ski | 持续跟踪 |
| [Understand-Anything](projects/understand-anything.md) | 平台候选 | 将任意代码转换为交互式知识图谱，支持探索、搜索和问答，兼容 Claude Cod | 持续跟踪 |
| [NVIDIA OpenShell](projects/openshell.md) | 基础设施候选 | NVIDIA 出品的 Agent 安全运行时沙箱——Rust 实现，四层策略防御 | 持续跟踪 |
| [agentmemory](projects/agentmemory.md) | 基础设施候选 | AI Coding Agent 的统一持久记忆服务，支持全平台（Claude C | 持续跟踪 |
| [Claude Plugins Official](projects/claude-plugins-official.md) | 平台候选 | Anthropic 官方管理的高质量 Claude Code 插件目录，Agen | 持续跟踪 |
| [Copy Fail CVE-2026-31431](projects/copy-fail-cve-2026-31431.md) | 安全 | Linux 内核 `algif_aead` page-cache 损坏漏洞的检测 | 持续跟踪 |
| [last30days-skill](projects/last30days-skill.md) | 生产可用 | AI agent 跨平台搜索技能，聚合 Reddit/X/YouTube/Tik | 持续跟踪 |
| [MoneyPrinterTurbo](projects/moneyprinterturbo.md) | 平台候选 | 利用 AI 大模型一键生成高清短视频，从脚本到成片的完整自动化流程。 | 持续跟踪 |
| [Microsoft SkillOpt](projects/skillopt.md) | 平台候选 | 文本空间技能优化器——为冻结的 LLM Agent 训练可复用的自然语言技能，产 | 持续跟踪 |

---

## 数据统计

- 📊 项目档案：215 个
- 📅 日报总数：71 期
- 🔄 最近更新：2026-06-20

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*
