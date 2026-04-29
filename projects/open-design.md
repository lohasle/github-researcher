---
title: "Open Design"
slug: "open-design"
date_added: "2026-04-30"
category: "工具型"
emoji: "🎨"
stars: "4.1k stars"
stars_delta: "2天4.1K，极速增长"
language: "TypeScript"
score: 77
tags: ["design", "claude-code", "skill", "byok", "design-systems", "open-source"]
url: "https://github.com/nexu-io/open-design"
---

# Open Design

## 一句话定位
开源 Claude Design 替代 — 71 个品牌级 Design Systems + 19 个 Skills，让任何 Coding Agent 成为设计引擎。

## 它解决的问题
Anthropic 发布 Claude Design 后引爆了"AI 做设计"的需求，但 Claude Design 闭源、付费、云锁定、只支持 Anthropic 模型。Open Design 提供同等能力但完全开放。

目标用户：使用 Coding Agent 的设计师、前端开发者、产品经理。

## 为什么值得关注（2026-04-30）
- 2 天 4.1K stars，增速极快
- 整合了 huashu-design、guizang-ppt-skill、open-codesign 等多个热门项目的成果
- BYOK 全层，支持 Claude Code / Codex / Cursor / Gemini CLI / OpenCode / Qwen / Copilot

## 热度来源判断
**真实需求 + 生态聚合效应**。Claude Design 验证了市场，Open Design 满足了"我也要但不想被锁定"的需求。增速中部分来自关联项目的 Star 互带。

## 关键技术亮点

1. **71 个品牌级 Design Systems**：涵盖 Linear、Stripe、Vercel、Airbnb、Tesla、Notion、Apple 等，基于 awesome-design-md 导入。
2. **19 个 Composable Skills**：prototype、deck、mobile、dashboard、pricing、docs、blog、SaaS landing 等，按需组合。
3. **5 种视觉方向**（Editorial Monocle / Modern Minimal / Tech Utility / Brutalist / Soft Warm），每种自带 OKLch 色板 + 字体栈。
4. **Agent Runtime 架构**：本地 daemon 启动 CLI，Agent 获得真实的 Read/Write/Bash/WebFetch 能力，操作真实文件系统。

## 架构启发

**设计哲学**：不造 Agent，利用现有最强的 Coding Agent。Open Design 只做 Skill 层 + Design System 层 + Runtime 层。

**Trade-off**：依赖外部 Agent 的能力上限，设计质量受限于底层 LLM 的设计"品味"。

## 定位判断
**工具型**，有平台化潜力。目前是高质量工具，如果 Skill 生态持续繁荣，可能成为 Agent 设计工作流的标准框架。

## 风险 / 局限 / 泡沫点

1. **2 天 4K stars 的泡沫风险**：部分增长来自关联项目的 Star 互带，实际活跃用户数需要 2-4 周观察。
2. **依赖 LLM 设计能力**：设计质量的"天花板"完全取决于底层模型的视觉理解力，Skill 只能引导不能创造。
3. **维护负担**：71 个 Design Systems 的持续更新是长期挑战。

## 与同类项目的关系

| 项目 | 定位 | 差异 |
|------|------|------|
| Claude Design | Anthropic 官方 | 闭源，仅 Anthropic 模型 |
| open-codesign | 桌面 Electron 应用 | 聚焦桌面端，Open Design 是 Web + CLI |
| huashu-design | 单一设计 Skill | 被 Open Design 整合 |

## 是否值得持续跟踪
**是，中优先级**。Skill 生态整合方向正确，需要观察用户留存和 Design System 更新节奏。

## 后续观察点

1. 2 周后的 star 增速是否回落
2. 71 个 Design Systems 的实际使用率和反馈
3. 是否出现企业级用户案例

---
*首次记录：2026-04-30*
