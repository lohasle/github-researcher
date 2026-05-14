# GitHub 趋势研究仓库

> 面向资深软件架构师的 GitHub 趋势持续跟踪与深度分析项目

---

## 最新研究摘要（2026-05-15）

**网络受限日 · Agent 生态进入整合期深读 · Spec-Driven Dev 范式变迁架构分析 · 本地推理三赛道分化复盘 · 安全赛道从漏洞驱动到平台化演进 · 3D 打印开放 vs 封闭之争的长期意义**

今日热榜新信号：
- **Hermes Agent**（~149K stars (推算)）：Agent 生态头部项目，147K→148K+ 日增 1.7K，定位从工具到长期伙伴
- **GitHub Spec Kit**（~99K stars (推算)）：GitHub 官方 Spec-Driven Development 工具链，97K→98K+ 日增 1K，开发范式级项目
- **Browser Harness**（~94K stars (推算)）：Self-healing 浏览器自动化，Agent 与 Web 交互层基础设施，25 天从 0 到 93K+

**→ [查看 2026-05-15 完整简报](daily/2026-05-15.md)**
**→ [查看 2026-05-14 完整简报](daily/2026-05-14.md)**
**→ [查看 2026-05-13 完整简报](daily/2026-05-13.md)**
**→ [查看 2026-05-12 完整简报](daily/2026-05-12.md)**

---

## 最近 7 天日报索引

| 日期 | 核心主题 | 重点项目数 |
|------|---------|----------|
| [2026-05-15](daily/2026-05-15.md) | 网络受限日 · Agent 生态进入整合期深读 · Spec-Driven De | 8 个深度分析 |
| [2026-05-14](daily/2026-05-14.md) | YellowKey BitLocker 绕过漏洞引爆安全社区 · OrcaSli | 6 个深度分析 |
| [2026-05-13](daily/2026-05-13.md) | 断网结束实测回归 · Open Design 38.4K 增速趋稳确认平台地位  | 8 个深度分析 |
| [2026-05-12](daily/2026-05-12.md) | 数据校正完成 · CC Switch 68K 确认基座地位 · MemPalac | 8 个深度分析 |
| [2026-05-11](daily/2026-05-11.md) | 数据校正完成 · Agent 基础设施层进入筛选期 · ds4.c 7.7K 超 | 8 个深度分析 |
| [2026-05-10](daily/2026-05-10.md) | 周度复盘：Agent 生态分层成型 · ds4.c 爆发破 7.7K 验证推理热 | 8 个深度分析 |
| [2026-05-09](daily/2026-05-09.md) | Linux 内核安全漏洞密集爆发 · Open Design 33.8K 确认平 | 7 个深度分析 |

---

## 当前最值得关注的趋势

1. **Agent 生态整合期：Hermes 148K+ / Browser Harness 93K+ / Open Design 39K+，三巨头确立头部格局，中腰部项目面临洗牌**：相关项目 hermes-agent, browser-harness, open-design。
2. **Spec-Driven Dev 范式变迁：Spec Kit 98K+ 确立新范式，从 prompt engineering 到 spec engineering 的架构级转变**：相关项目 spec-kit。
3. **本地推理三赛道复盘：ds4.c 原生层 / Terax AI 终端层 / Zero Native 框架层，Zig + Metal + CUDA 三线并行**：相关项目 ds4, terax-ai, zero-native。
4. **安全赛道平台化趋势：从 YellowKey 单漏洞到 DevSecOps Agent 链，安全研究从事件驱动转向工具链驱动**：相关项目 yellowkey, deepsec, copy-fail-cve-2026-31431。
5. **硬件生态开放 vs 封闭：OrcaSlicer-bambulab 社区分叉模式成为硬件开放运动的标志性事件**：相关项目 orcaslicer-bambulab。

---

## 当前最值得跟踪的项目

| 项目 | 分类 | 核心价值 | 状态 |
|------|------|---------|------|
| [Copy Fail CVE-2026-31431](projects/copy-fail-cve-2026-31431.md) | 安全 | Linux 内核 `algif_aead` page-cache 损坏漏洞的检测 | 持续跟踪 |
| [YellowKey](projects/yellowkey.md) | 安全研究 | Windows BitLocker 绕过漏洞 PoC，声称在 WinRE 中发现 | 持续跟踪 |
| [Dirty Frag](projects/dirtyfrag.md) | 安全研究 | 通用 Linux 本地提权漏洞利用（CVE-2026-43284/43500）， | 持续跟踪 |
| [MemPalace](projects/mempalace.md) | 基础设施候选 | 史上最高分 AI 记忆系统，LongMemEval 96.6% R@5，完全本地 | 持续跟踪 |
| [Open Design](projects/open-design.md) | 平台候选 | 开源 Claude Design 替代 — 71 个品牌级 Design Sys | 持续跟踪 |
| [cc-switch](projects/cc-switch.md) | 平台候选 | 跨平台桌面 All-in-One 助手工具，统一管理 Claude Code、C | 持续跟踪 |
| [ds4.c](projects/ds4.md) | 基础设施候选 | antirez（Redis 作者）开发的 DeepSeek V4 Flash M | 持续跟踪 |
| [GitHub Spec Kit](projects/spec-kit.md) | 基础设施候选 | GitHub 官方的 Spec-Driven Development 工具包—— | 持续跟踪 |
| [Browser Harness](projects/browser-harness.md) | 平台候选 | 让 LLM 通过裸 CDP 协议直接控制浏览器的 self-healing ha | 持续跟踪 |
| [Mirage](projects/mirage.md) | 基础设施候选 | 为 AI Agent 设计的统一虚拟文件系统（VFS），将 S3、Slack、G | 持续跟踪 |

---

## 数据统计

- 📊 项目档案：118 个
- 📅 日报总数：39 期
- 🔄 最近更新：2026-05-15

---

*本 README 由 `scripts/generate_readme.py` 自动生成，与实际数据保持同步。*
