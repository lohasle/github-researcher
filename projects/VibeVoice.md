# VibeVoice

> Open-Source Frontier Voice AI — Microsoft

## 基本信息

- **仓库：** [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)
- **Star：** 36,938
- **本周新增：** 8,392
- **语言：** Python
- **归档状态：** 活跃

## 核心定位

微软开源的 Voice AI 家族，包含三大模型：
- **VibeVoice-ASR-7B**：60分钟长音频单遍 ASR，含说话人分离、时间戳、用户自定义热词
- **VibeVoice-TTS-1.5B**：90分钟长音频 TTS，4人对话，支持中英文
- **VibeVoice-Realtime-0.5B**：实时流式 TTS，0.5B 参数，300 tokens/s

## 技术亮点

1. **连续 Tokenizer @ 7.5 Hz**：超低帧率保持音频保真度，同时大幅提升长序列处理效率
2. **Next-token Diffusion**：LLM 理解语义 + Diffusion Head 生成高保真声学细节
3. **60分钟单遍 ASR**：不是分段拼接，是真正的长上下文识别
4. **HuggingFace Transformers 官方集成**：ASR 已进 v5.3.0，基础设施级别认可
5. **vLLM 推理支持**：生产级推理性能

## 重要事件

- 2025-09-05：TTS 代码因"与开源初衷不符的使用案例"被移除，说明存在社会责任风险
- 2026-03-06：ASR 被 HuggingFace Transformers 官方收录
- ICLR 2026 Oral：TTS 论文被接收

## 泡沫点

- TTS 曾被部分撤除，企业使用需评估合规性
- ASR 虽进 HF，但 7B 参数对端侧部署仍偏大
- Realtime TTS 的"experimental speakers"说明产品化程度有限

## 架构启发

7.5 Hz Tokenizer 设计对音频 Tokenizer 研究有参考价值。连续 Tokenizer 思路可能是未来多模态融合的重要方向。

## 评分

| 维度 | 得分 | 理由 |
|------|------|------|
| 热度质量 | 8 | 稳健，37k 总数，大厂背书 |
| 技术创新度 | 8 | 7.5 Hz Tokenizer + Next-token Diffusion，有研究价值 |
| 工程成熟度 | 7 | ASR 已进 HF，TTS 有合规问题待解 |
| 架构启发价值 | 7 | 对语音模型设计有参考价值 |
| 企业落地潜力 | 7 | ASR 部分可直接用，TTS 需评估合规 |
| 中期趋势概率 | 7 | Voice AI 是持续趋势 |
| 平台化潜力 | 6 | 更偏模型而非平台 |
| 基础设施潜力 | 7 | 进 HF Transformers 说明已是事实基础设施 |
| **总分** | **57/80** | |

## 归类

**生产可用 | 关注 ASR 部分，合规评估后落地**

---

*首次记录：2026-04-07*
