---
name: prompt-distiller
description: "AI image generation mastery: auto-audit prompts, inject photography technique (camera+lens+lighting+skin), optimize weak prompts, and generate professional-grade images. Works with any image generation model."
version: "1.0.0"
category: image-generation
---

# Prompt Distiller — AI 生图能力蒸馏包

> 把 Hermes 的生图能力打包成自包含的 Skill，任何智能体读取即用。

## 一、核心原理

生图质量的差距不在模型，在 prompt。一段优秀的 prompt 必须包含 **六大摄影元素**：

```
[相机型号] + [镜头+光圈] + [布光方案] + [真实皮肤/材质] + [精确构图] + [负向词]
```

**数据证明**：从 2,456 条社区 prompt 审计发现：
- 仅 1.2% 含具体相机型号
- 仅 0.2% 含光圈参数（如 f/1.4）
- 仅 5.6% 含具体布光方案
- 仅 2.7% 含真实皮肤描述
- → **90%+ 的 prompt 都是模糊描述，不可能出好图**

## 二、优秀 Prompt 判断标准（10 项审计清单）

| # | 检查项 | ❌ 不合格 | ✅ 合格 |
|---|--------|---------|--------|
| 1 | 相机品牌 | 无 / "professional camera" | `Sony A1` / `Hasselblad H6D-100c` |
| 2 | 镜头+光圈 | 无 / "portrait lens" | `85mm f/1.4` / `100mm f/2.8 macro` |
| 3 | 布光方案 | 无 / "good lighting" | `Rembrandt lighting: 45° key, triangle shadow` |
| 4 | 皮肤真实 | 无 / "perfect skin" | `visible pores, microtexture, NOT flawless` |
| 5 | 负向词 | 无 | `blurry, plastic skin, airbrushed, oversmoothed` |
| 6 | 锐度 | 无 | `tack-sharp focus, high micro-contrast` |
| 7 | 权威锚 | 无 | `National Geographic style` / `Vogue editorial` |
| 8 | 构图 | 无 | `shallow DOF, creamy bokeh, eyes in focus` |
| 9 | 分辨率 | 无 | `8K hyper-detailed, raw photo` |
| 10 | 人像专项 | 泛泛 "Asian woman" | 精确 `East African, rich ebony skin, warm undertones` |

**评分规则**：
- 10/10 → 大师级，直接生成
- 7-9/10 → 良好，可生成
- 4-6/10 → 需优化，注入缺失元素
- 0-3/10 → 低质量，完全重写

**参考来源**：[`references/master-photography-techniques.md`](references/master-photography-techniques.md)

## 三、Prompt 优化工作流

### 步骤 1：审计原始 Prompt

读取用户/系统的原始 prompt，对照 10 项审计清单打分。

### 步骤 2：注入缺失元素

根据缺失项，从知识库注入对应元素：

| 缺失项 | 注入方式 |
|--------|---------|
| 相机 | 从[相机词库](references/master-photography-techniques.md#二单反相机镜头提示词控制技巧-)匹配 |
| 镜头 | 从[镜头词库](references/master-photography-techniques.md#镜头型号效果对照)按场景选择 |
| 布光 | 从[9种布光方案](references/master-photography-techniques.md#9种经典人像布光方案)匹配一个 |
| 皮肤 | 注入 `visible pores, microtexture — NOT flawless` |
| 负向词 | 注入 `blurry, plastic skin, airbrushed, oversmoothed, soft focus` |
| 种族肤色 | 从[12种肤色词库](references/master-photography-techniques.md#肤色描述精确词库)匹配 |

### 步骤 3：人像专项处理

如果 prompt 涉及人物，强制执行：
1. **皮肤真实性**：必带 `visible pores, microtexture, natural asymmetry`
2. **负向词**：必带 `plastic skin, airbrushed, flawless, waxy skin`
3. **年龄适配**：参照[各年龄层皮肤特征](references/master-photography-techniques.md#各年龄层皮肤特征)
4. **种族肤色**：如涉及特定国家/种族，使用精确肤色词

### 步骤 4：生成

优化后的 prompt 通过 `image_generate` 工具生成。默认参数：
- 比例：2:3 portrait
- 最小边长：2000px（自动放大）
- 负向词：自动追加到 prompt 尾部

### 步骤 5：质量反馈

生成后检查是否糊了（gpt-image-2-high 先天偏软）：
- 用户说「糊了」→ 切 xAI Grok 重出
- 检查[锐度保障规则](references/sharp-photography-prompts-2026.md)

## 四、生图引擎选择

| 条件 | 引擎 | 原因 |
|------|------|------|
| 含中文文字 | gpt-image-2-high (OpenAI Codex) | 中文渲染最强 |
| 纯视觉/摄影 | gpt-image-2-high → 糊了用 Grok | Codex优先，糊了补发 |
| 有参考图编辑 | Codex CLI --image | 脸部/Logo保留率最高 |
| 批量多主题 | 逐张 image_generate | 每张等结果 |

## 五、自动优化示例

### 输入（不合格 prompt）：
```
A beautiful portrait of a woman at sunset
```

### 审计结果（1/10）：
- ❌ 无相机 ❌ 无镜头 ❌ 无布光 ❌ 无皮肤 ❌ 无负向词 ❌ "beautiful"空洞 ❌ 无锐度 ❌ 无构图 ❌ 无权威锚

### 自动优化后（10/10）：
```
Ultra-photorealistic portrait of a woman at golden hour.
Visible pores, natural skin microtexture, subtle imperfections — NOT flawless, NOT airbrushed.
Golden hour side lighting: warm sun at 45° creating long golden shadows, soft amber wraparound glow.
Shot on Sony A1 with 85mm f/1.4 lens, shallow depth of field, razor-sharp focus on eyes with crisp catchlight, creamy bokeh.
National Geographic portrait style, 8K hyper-detailed, raw photo, film grain.
NEGATIVE: plastic skin, airbrushed, flawless, waxy skin, blurry, soft focus, oversaturated, low quality
```

## 六、关键约束

1. **固定比例 2:3 portrait**：不生成 landscape/square
2. **最小边长 2000px**：自动 Lanczos 放大
3. **prompt < 250 字中文**：gpt-image-2-high 安全上限
4. **跨日不重复**：检查 7 天历史，视觉模式词共享 ≥2 则跳大类
5. **负向词每张必带**：`blurry, plastic skin, airbrushed, oversmoothed, soft focus`
6. **锐度标签必加**：`tack-sharp focus, high micro-contrast`

## 参考文档

| 文档 | 内容 |
|------|------|
| [`master-photography-techniques.md`](references/master-photography-techniques.md) | 12种肤色词库、9款相机对照、12种镜头对照、9种布光方案、各年龄层皮肤特征 |
| [`sharp-photography-prompts-2026.md`](references/sharp-photography-prompts-2026.md) | 锐利Prompt模板×5、锐利关键词清单、经典Prompt公式 |
| [`prompt-audit-scoring.md`](references/prompt-audit-scoring.md) | 10项审计清单详细说明 + 评分示例 |
