---
title: "Centaur"
slug: "centaur"
date_added: "2026-05-23"
category: "基础设施候选"
emoji: "🐴"
stars: "364 stars"
stars_delta: "364/5天（创建于 2026-05-18）"
language: "Python"
score: 84
tags: ["Agent平台", "K8s", "Slack", "团队协作", "沙箱", "Paradigm"]
url: "https://github.com/paradigmxyz/centaur"
last_seen_date: "2026-05-23"
---

# Centaur

## 一句话定位
多人自托管 Agent 平台，让团队通过 Slack 共享 Agent，Agent 在 Kubernetes 沙箱中执行任务。

## 它解决的问题
目标用户：需要团队共享 Agent 能力的工程团队。

痛点：
- 当前 Agent 工具几乎都是个人级的（本地终端运行）
- 企业需要安全隔离（Agent 不能直接访问生产环境）
- 团队成员需要共享工具、凭证、工作流
- Agent 执行的任务可能需要长时间运行、中断恢复

## 为什么值得关注（2026-05-23）
Centaur 是第一个明确将 Agent 从「个人工具」升级为「团队基础设施」的开源项目。K8s 沙箱 + 凭证边界 + Slack 原生交互的组合，直接瞄准了企业部署的核心痛点。Paradigm（知名 crypto VC）出品，工程质量有保障。

## 热度来源判断
364 stars / 5 天，增速不高但考虑到：
- 目标用户是工程团队而非个人开发者，受众更窄
- Paradigm 品牌效应带来初始关注
- 解决的问题非常具体（团队共享 Agent），不是泛化项目

不是泡沫 — 但市场可能比个人 Agent 工具小得多。

## 关键技术亮点

### 1. K8s 沙箱隔离
每个对话一个独立 Kubernetes 沙箱，预装 Python/Node/Bun/常用开发工具。Agent 在沙箱中执行所有操作，完全隔离。

### 2. Bring your own harness
不重新造 Agent，而是让团队使用已有的 Agent harness（Amp、Claude Code、Codex 等）。Centaur 只负责基础设施层。

### 3. 凭证边界
Agent 可使用已批准的服务，但不直接持有 raw API key。凭证通过平台层代理，Agent 只知道「你有权限用 X 服务」。

### 4. 持久工作流
支持 sleep/resume/等待事件/启动子 Agent/服务重启不丢失状态。适合长时间运行的任务（如 CI/CD、数据处理）。

### 5. Organization overlays
团队可以在不 fork 基础平台的情况下，叠加自己的工具、工作流、人设、技能和提示词。

## 架构启发
Centaur 展示了企业 Agent 平台的正确架构层次：

```
Slack/Web UI（交互层）
    ↓
Centaur API（编排层）
    ↓
K8s Sandbox（执行层）
    ↓
Agent Harness（任务层）
    ↓
Shared Tools（工具层）
```

这种分层设计让每层都可以独立替换。企业可以保留自己的 Slack 集成，换掉 K8s 为 Docker，或使用不同的 Agent harness。

## 定位判断
**基础设施候选。** 如果企业要部署团队级 Agent，Centaur 的架构是最接近生产可用的开源方案。

## 风险 / 局限 / 泡沫点

1. **Paradigm crypto 背景**：虽然是通用平台，但 crypto 行业的特殊需求可能影响设计决策
2. **K8s 依赖**：K8s 沙箱的资源消耗和启动延迟可能不适合小团队
3. **364 stars 非常早期**：项目可能随时停止维护
4. **Slack 绑定**：目前只支持 Slack，缺少 Teams/Discord/飞书等集成

## 与同类项目的关系
| 项目 | 定位 | 核心差异 |
|------|------|---------|
| ECC | 个人 Agent Harness | 个人级工具，非团队平台 |
| OpenCode | 个人编码 Agent | 终端级，无团队协作 |
| LobeHub | Agent 运营平台 | 偏 Agent 编排和运营 |
| Centaur | 团队 Agent 基础设施 | K8s 沙箱 + Slack + BYOH |

## 是否值得持续跟踪
**是，建议持续跟踪。** 团队级 Agent 平台是企业落地的关键方向。Centaur 的架构设计值得企业内部参考，即使不直接使用。

## 后续观察点
1. Centaur 是否会添加更多聊天平台集成（Teams、飞书等）
2. K8s 沙箱的启动延迟和资源消耗是否可接受
3. 是否有企业开始用 Centaur 做内部 PoC

---
*首次记录：2026-05-23*
