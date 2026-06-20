# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-06-21）

**Agent Skill 训练正式化——SkillOpt 用 epoch/lr/val gate 训练 skill 文档（6 benchmark × 52 cell 全第一 + Sleep 离线进化） · Agent 元框架混战升级（Omnigent 4.2K meta-harness + Vercel Eve 1.8K 文件系统优先 + ECC 218K 登顶） · 本地推理引擎专业化（antirez/ds4 14.8K DeepSeek V4 专用 inference + SSD 流式 KV cache） · Epic Games 开源下一代 VCS（Lore 5.1K 内容寻址 + Merkle Tree + 大二进制优先） · Agent 增强工具爆发（CodexPlusPlus 20.4K + html-anything 7K + shadcn/improve 5.8K）**

今日热榜新信号：
- **EpicGames/lore**（5,105 stars）：Epic Games 下一代开源 VCS——内容寻址 + Merkle Tree + 大二进制优先 + 按需 hydration + 全 API 覆盖
- **BigPizzaV3/CodexPlusPlus**（20,363 stars）：CodexApp 增强工具——Rust 实现，专注让 Codex 更好用、更舒服、更高效
- **microsoft/SkillOpt**（8,448 stars）：微软 Agent Skill 优化器——像训练神经网络一样训练 skill 文档，epoch/lr/val gate + Sleep 离线进化

**→ [查看 2026-06-21 完整简报](daily/2026-06-21.md)**
**→ [查看 2026-06-20 完整简报](daily/2026-06-20.md)**
**→ [查看 2026-06-19 完整简报](daily/2026-06-19.md)**
**→ [查看 2026-06-15 完整简报](daily/2026-06-15.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-06-21](daily/2026-06-21.md) | Agent Skill 训练正式化——SkillOpt 用 epoch/lr/v | 5 个深度分析 |
| [2026-06-20](daily/2026-06-20.md) | LLM Token 经济学基础设施爆发（headroom 38K⭐ 日增 3,9 | 5 个深度分析 |
| [2026-06-19](daily/2026-06-19.md) | Agent Skill 经济学验证完成（ponytail 36K⭐ 一周暴涨 4 | 4 个深度分析 |
| [2026-06-15](daily/2026-06-15.md) | Agent Skills 杀手级应用涌现（last30days-skill 42 | 4 个深度分析 |
| [2026-06-14](daily/2026-06-14.md) | Agent Skills 全栈基础设施化：分发层(agent-skills 58 | 6 个深度分析 |
| [2026-06-13](daily/2026-06-13.md) | Agent 架构分层加速：shadcn/improve 贵模型审计+廉模型执行分 | 6 个深度分析 |
| [2026-06-12](daily/2026-06-12.md) | Agent Skills 生态爆发：addyosmani/agent-skill | 5 个深度分析 |

---

## 当前最值得关注的趋势

1. **Agent Skill 训练范式正式化：SkillOpt 8.4K⭐（微软出品）将 skill 文档视为可训练状态——epoch、learning rate、validation gate、rejected-edit buffer，像训练神经网络一样训练 skill，6 benchmark × 52 cell 全第一。新增 Sleep 模块实现夜间离线 skill 进化。shadcn/improve 5.8K⭐ 用强模型审计代码库为弱模型写执行计划——模型分工协作。Skill 不再是手写提示词，而是可优化、可验证、可部署的训练产物**：相关项目 skillopt, shadcn-improve, ponytail。
2. **Agent 元框架/meta-harness 混战升级：Omnigent 4.2K⭐（Claude Code/Codex/Cursor 统一编排 + 沙箱 + 策略治理 + 手机协作），Vercel Eve 1.8K⭐（文件系统即 Agent 接口——instructions.md / tools/ / skills/ / channels/ / schedules/），ECC 218K⭐ 登顶最大 Agent harness。三种完全不同的 Agent 框架哲学在同一天热门：元编排 vs 文件系统约定 vs 性能优化**：相关项目 omnigent, vercel-eve, affaan-m-ecc。
3. **本地推理引擎专业化：antirez/ds4（DwarfStar）14.8K⭐——DeepSeek V4 Flash/PRO 专用本地推理引擎，不通用、不包装，一个模型做到极致。SSD 流式 KV cache 重新定义'模型是否需要装入 RAM'的边界——从硬性截止变成速度连续谱。Metal/CUDA/ROCm 三后端 + 自带 GGUF + coding agent 集成**：相关项目 ds4, zerolang。
4. **Epic Games 开源下一代 VCS：Lore 5.1K⭐——内容寻址 + Merkle Tree + 大二进制优先 + 去重 + 按需 hydration。不是 git 替代品，而是面向游戏/娱乐产业的 VCS，解决 git 处理大二进制文件的根本性痛点。UEFN 内置 VCS 的开源版本。C/C++/C#/Rust/Go/Python/JS 全 API 覆盖**：相关项目 epicgames-lore。
5. **Coding Agent 增强工具爆发：CodexPlusPlus 20.4K⭐（CodexApp 增强——Rust 重写体验优化），html-anything 7K⭐（75 Skills × 9 Surfaces 的 Agentic HTML 编辑器，零 API key + 本地运行）， ponytail 43K⭐（让 AI agent 像最懒的 senior dev 一样思考——YAGNI 理念注入）。Agent 不需要更强，需要更好的工具和约束**：相关项目 codexplusplus, html-anything, ponytail。

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

- 📊 项目档案：217 个
- 📅 日报总数：72 期
- 🔄 最近更新：2026-06-21

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*
