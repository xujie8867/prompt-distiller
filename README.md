# Prompt Distiller — AI 生图能力蒸馏包

> 一个自包含的 AI 生图 Skill，任何智能体（Claude Code、Codex、Hermes）直接读取即用。

## 🌟 核心能力

- **🔍 自动审计** — 10项清单评分，0-100分
- **🔧 自动优化** — 注入缺失的相机/镜头/布光/皮肤/负向词
- **📷 大师级输出** — 相机参数 + 布光方案 + 真实皮肤 + 权威锚点
- **📚 完整知识库** — 12种肤色 × 9款相机 × 12种镜头 × 9种布光

## 📦 文件结构

```
prompt-distiller/
├── SKILL.md                          # 主 Skill（智能体入口）
├── README.md                         # 本文件
├── references/
│   ├── master-photography-techniques.md  # 大师摄影技巧全集
│   ├── sharp-photography-prompts-2026.md # 锐利Prompt模板
│   └── prompt-audit-scoring.md           # 10项审计评分细则
├── scripts/
│   └── audit_prompt.py                   # Prompt审计脚本
└── prompts/
    └── curated-prompts.json              # 精选高质量提示词库
```

## 🚀 使用方法

### 作为 Hermes Skill 安装

```bash
# 克隆到 skills 目录
git clone https://github.com/xuj-hub/prompt-distiller.git \
  ~/.hermes/skills/creative/prompt-distiller

# 或者通过 curator 安装
hermes curator install https://github.com/xuj-hub/prompt-distiller
```

### 作为 Claude Code / Codex Skill 安装

```bash
# Claude Code
/plugin marketplace add xuj-hub/prompt-distiller
/plugin install prompt-distiller@xuj-hub-skills

# Codex
npx skills@latest add xuj-hub/prompt-distiller --agent codex --copy
```

### 手动使用

任何智能体只需读取 `SKILL.md` + `references/` 即可掌握全部能力。

## 📊 数据支撑

从 2,456 条社区 prompt 审计发现：

| 指标 | 社区平均水平 | 本 Skill 要求 |
|------|:----------:|:----------:|
| 含具体相机型号 | 1.2% | ✅ 100% |
| 含镜头+光圈 | 0.2% | ✅ 100% |
| 含具体布光方案 | 5.6% | ✅ 100% |
| 含真实皮肤描述 | 2.7% | ✅ 100% |
| 含负向词 | 4.7% | ✅ 100% |

## 🎯 评分标准

| 分数 | 等级 | 处理 |
|------|------|------|
| 90-100 | 🏆 大师级 | 直接生成 |
| 70-89 | 👍 良好 | 可生成 |
| 40-69 | ⚠️ 需优化 | 自动注入 |
| 0-39 | ❌ 低质量 | 完全重写 |

## 📖 案例

输入：`"A beautiful portrait of a woman at sunset"`（评分 0/100）

输出：
```
Ultra-photorealistic portrait. Visible pores, microtexture — NOT flawless.
Golden hour side lighting: 45° warm sun, long shadows.
Sony A1, 85mm f/1.4, shallow DOF, tack-sharp eyes, creamy bokeh.
National Geographic style, 8K raw.
NEGATIVE: plastic skin, airbrushed, blurry, soft focus
```
（评分 98/100 🏆）

## 🔗 相关资源

- 核心参考：GitHub 社区 `jamez-bondos/awesome-gpt4o-images` (8.1K★)
- 技能参考：`wuyoscar/GPT-Image2-Skill` (4.1K★)
- X社区贡献：@miilesus, @ScaleWthAI, @MuseboxAi, @madamayo_

## 📄 License

MIT
