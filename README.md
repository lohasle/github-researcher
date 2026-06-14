# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-06-15）

**Agent Skills 杀手级应用涌现（last30days-skill 42K⭐ + taste-skill 44K⭐ 周增均超 8K——Skills 从基础设施走向真实应用） · 上下文工程工具链三位一体（headroom 压缩 + turbovec 向量索引 + LMCache KV 缓存——压缩→索引→缓存完整管道成型） · 本地多模态 AI 运行时扩展（whichllm 选型 + Open-LLM-VTuber 语音 + MoneyPrinterTurbo 视频）**

今日热榜新信号：
- **mvanhorn/last30days-skill**（41,943 stars）：Agent Skills 第一个杀手级应用——跨 10+ 平台聚合研究数据，周增 12.6K 持续爆发
- **LMCache/LMCache**（9,043 stars）：LLM 推理 KV Cache 加速层，PagedAttention 之后的推理基础设施新原语
- **Leonxlnx/taste-skill**（43,637 stars）：AI 输出质量守门员——阻止 AI 生成 generic slop，周增 8K 持续爆发

**→ [查看 2026-06-15 完整简报](daily/2026-06-15.md)**
**→ [查看 2026-06-14 完整简报](daily/2026-06-14.md)**
**→ [查看 2026-06-13 完整简报](daily/2026-06-13.md)**
**→ [查看 2026-06-12 完整简报](daily/2026-06-12.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-06-15](daily/2026-06-15.md) | Agent Skills 杀手级应用涌现（last30days-skill 42 | 4 个深度分析 |
| [2026-06-14](daily/2026-06-14.md) | Agent Skills 全栈基础设施化：分发层(agent-skills 58 | 6 个深度分析 |
| [2026-06-13](daily/2026-06-13.md) | Agent 架构分层加速：shadcn/improve 贵模型审计+廉模型执行分 | 6 个深度分析 |
| [2026-06-12](daily/2026-06-12.md) | Agent Skills 生态爆发：addyosmani/agent-skill | 5 个深度分析 |
| [2026-06-11](daily/2026-06-11.md) | Agent 编排分层：shadcn/improve 745⭐ 顾问模式引爆 Ag | 5 个深度分析 |
| [2026-06-10](daily/2026-06-10.md) | LLM Token 压缩从优化变基础设施：headroom 20.4K 周增 1 | 5 个深度分析 |
| [2026-06-09](daily/2026-06-09.md) | Coding Agent 工具链基础设施化：cc-switch 95K + co | 5 个深度分析 |

---

## 当前最值得关注的趋势

1. **Agent Skills 杀手级应用涌现：last30days-skill 42K⭐ 周增 12.6K 证明 Skill 不是实验概念而是有真实杀手级用例（跨平台研究聚合），taste-skill 44K⭐ 周增 8K 让 AI 输出质量可控，compound-engineering-plugin 21K⭐ 将工程实践编码为插件。Skills 从'有没有'进入'好不好用'阶段**：相关项目 last30days-skill, taste-skill, compound-engineering-plugin。
2. **上下文工程工具链三位一体：headroom 27K⭐ 做 Token 压缩（60-95% 节省），turbovec 11.5K⭐ 做向量索引（Rust+SIMD+TurboQuant），LMCache 9K⭐ 做 KV Cache 加速——压缩→索引→缓存形成完整 context engineering 管道，LLM 推理成本控制从单点优化走向系统化**：相关项目 headroom, turbovec, lmcache。
3. **本地多模态 AI 运行时扩展：whichllm 4.7K⭐ 做本地 LLM 硬件选型，Open-LLM-VTuber 11.3K⭐ 做语音交互+Live2D，MoneyPrinterTurbo 87.8K⭐ 做短视频生成——本地 AI 从文本推理扩展到语音、视频、多模态交互，端侧 AI 运行时生态加速成型**：相关项目 whichllm, open-llm-vtuber, moneyprinterturbo。
4. **安全工具 AI 化与图分析化：NVIDIA SkillSpector 5.2K⭐ 扫描 Agent Skill 漏洞，flowsint 6.6K⭐ 做图形化安全调查，maigret 33K⭐ 做 OSINT 用户名追踪——AI 安全从理论走向工具化，安全从业者的 AI 原生工具栈初步浮现**：相关项目 nvidia-skillspector, flowsint, maigret。
5. **垂直领域 AI 基础模型萌芽：Kronos 金融市场基础模型登日榜，openmed 3.5K⭐ 周增 2K 做开源医疗 AI——基础模型从通用走向垂直，金融和医疗是最先发力的两个赛道**：相关项目 kronos, openmed。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [12-Factor Agents](projects/12-factor-agents.md) | 基础设施候选 | 构建足够好到可以交给专业用户使用的 LLM 驱动软件的 12 条工程原则，Age | 持续跟踪 |
| [Understand-Anything](projects/understand-anything.md) | 平台候选 | 将任意代码转换为交互式知识图谱，支持探索、搜索和问答，兼容 Claude Cod | 持续跟踪 |
| [Headroom](projects/headroom.md) | 基础设施候选 | AI Agent 与 LLM 之间的 Token 压缩中间件，60-95% To | 持续跟踪 |
| [NVIDIA OpenShell](projects/openshell.md) | 基础设施候选 | NVIDIA 出品的 Agent 安全运行时沙箱——Rust 实现，四层策略防御 | 持续跟踪 |
| [agentmemory](projects/agentmemory.md) | 基础设施候选 | AI Coding Agent 的统一持久记忆服务，支持全平台（Claude C | 持续跟踪 |
| [Claude Plugins Official](projects/claude-plugins-official.md) | 平台候选 | Anthropic 官方管理的高质量 Claude Code 插件目录，Agen | 持续跟踪 |
| [Copy Fail CVE-2026-31431](projects/copy-fail-cve-2026-31431.md) | 安全 | Linux 内核 `algif_aead` page-cache 损坏漏洞的检测 | 持续跟踪 |
| [last30days-skill](projects/last30days-skill.md) | 生产可用 | AI agent 跨平台搜索技能，聚合 Reddit/X/YouTube/Tik | 持续跟踪 |
| [MoneyPrinterTurbo](projects/moneyprinterturbo.md) | 平台候选 | 利用 AI 大模型一键生成高清短视频，从脚本到成片的完整自动化流程。 | 持续跟踪 |
| [Microsoft SkillOpt](projects/skillopt.md) | 平台候选 | 文本空间技能优化器——为冻结的 LLM Agent 训练可复用的自然语言技能，产 | 持续跟踪 |

---

## 数据统计

- 📊 项目档案：205 个
- 📅 日报总数：69 期
- 🔄 最近更新：2026-06-15

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*
