---
name: prompt-distiller
description: "Audit and optimize image prompts before generation."
version: "2.0.0"
---

# Prompt Distiller v2.0 — 相机物理审计

> **2026-08-05 范式转换**：AI 不理解艺术史——它理解相机物理。
> 不说"Gregory Crewdson cinematic staging"，说"Canon EOS R5, 85mm f/1.2, ISO 800"。
> 9 种风格，9 投 9 中，全部验证。

Repo: `https://github.com/xujie8867/prompt-distiller`

## 核心审计：相机物理定向（最高优先级）

### ⛔ 致命词——prompt 中出现则直接扣至 <60 分

以下词汇在 AI 生图中是「过度风格化指令」，而非摄影参考：

- **摄影师名字**：Gregory Crewdson, Annie Leibovitz, Sebastião Salgado, Steve McCurry, Fan Ho, Alex Webb, Saul Leiter, Roger Deakins, Wong Kar-wai, 等
- **风格标签**：cinematic, editorial, staged, theatrical, dramatic portrait, fashion editorial, 电影感, 舞台调度, 戏剧性
- **胶片型号（在 prompt 中）**：Kodak Portra 400, Cinestill 800T, Ilford HP5... → AI 把它们理解为「画成这个胶片的风格」，而非「用这个胶片拍」

### ✅ 必须词——prompt 中缺失则扣 20 分/项

- 相机型号 + 镜头 + ISO：`Canon EOS R5, 85mm f/1.2, ISO 800`
- 自然光描述：`overcast soft daylight` / `window light natural side` / `blue hour twilight`
- 纪实风格声明：`photojournalism, candid, unretouched, documentary style, raw photo`

### 范式对照

```
❌ Annie Leibovitz dramatic portrait, cinematic studio lighting
   → AI 画"一幅 Leibovitz 风格的画"

✅ Canon EOS R5, 85mm f/1.2, ISO 100, single large softbox 45° from left
   → AI 拍"85mm 定焦在柔光箱下的景深和质感"
```

---

## 10 项强制审计

每次生图前逐项过：

| # | 检查项 | 追问 |
|---|--------|------|
| ① | 相机型号+镜头+ISO | prompt 里有吗？缺则扣 20 分 |
| ② | 自然光描述 | overcast/window/blue hour/twilight？不能说 golden hour backlight + 浅色 |
| ③ | 致命词扫描 | 有摄影师名/film stock/cinematic/editorial/staged？→ 替换为相机参数 |
| ④ | 物理真实感 | 毛孔/绒毛/接触阴影/织造纹理？ |
| ⑤ | 精确肤色 | 冷白/象牙白/暖橄榄/蜜色？不要「白皙」 |
| ⑥ | 年龄-皮肤适配 | 20 岁和 50 岁的皮肤细节不同 |
| ⑦ | 负向词完整 | 见下方负向词库，人像加 staged portrait/fashion editorial |
| ⑧ | 光线-主体反差 | 浅色主体+逆光+浅背景？→ 换深色主体+硬侧光+深背景 |
| ⑨ | 黑白人像？ | 黑白纪实人像 → Codex 搞不定，切 Grok |
| ⑩ | 反射表面？ | 镜面/水面/盐沼/玻璃 → 避或切 Grok |

---

## 自动切 Grok 三场景

| 场景 | 信号 | 动作 |
|------|------|------|
| 低反差糊片 | 浅色主体 + 逆光 + 浅背景 | 切 Grok |
| 黑白假脸 | 黑白写实人像 | 切 Grok |
| 反射失真 | 盐沼/水面/玻璃/镜面 | 切 Grok |

切 Grok → 出单张 → 立即切回 Codex。不犹豫。

---

## 负向词库（每张必带，全量）

### 人像/动物/微距
```
NOT CGI, NOT 3D render, NOT airbrushed, NOT plastic skin, NOT waxy skin,
NOT doll-like, NOT beauty filter, NOT over-sharpened, NOT HDR glow,
NOT cinematic lighting, NOT staged portrait, NOT fashion editorial,
NOT oversaturated, NOT perfect symmetry, NOT digital art
```

### 纯风景
```
NOT CGI, NOT 3D render, NOT HDR, NOT over-sharpened, NOT oversaturated,
NOT digital art, NOT cinematic
```

### 传统负向（皮肤/解剖/物理/质量，按需叠加）
plastic skin, waxy skin, airbrushed, beauty filter, over-smoothed, poreless, glass skin, flawless, doll-like / CGI, 3D render, illustration, painting, cartoon, anime, oversaturated, HDR, glowing neon, lens flares, over-sharpened, perfect symmetry / deformed hands, extra fingers, bad anatomy, dead eyes, frozen expression, model pose, symmetrical face / painted water, floating objects, no contact shadows, smeared background / blurry, soft focus, low quality, jpeg artifacts, watermark

---

## 9 风格矩阵（Agent 选题参考，不写入 prompt）

| # | 风格 | 相机+ISO | 光线 | 类型 |
|---|------|---------|------|------|
| 1 | 新闻纪实 | R5 85/1.2, ISO 800-1600 | window/overcast/tungsten | portrait |
| 2 | 商业时装 | Hasselblad 80/1.9, ISO 100 | north window indirect | fashion |
| 3 | 旅行人文 | Leica M11 35/1.4, ISO 400-800 | sun through leaves | travel |
| 4 | 极简风光 | Sony 24/1.4, ISO 100, tripod | pre-dawn 30s | landscape |
| 5 | 街头快照 | Ricoh GR III 28/2.8, ISO 1600+ | mixed city no flash | street |
| 6 | 棚拍肖像 | R5 50/1.2, ISO 100 | softbox 45° white BG | studio |
| 7 | 自然风光 | Sony 24-70/2.8@35, ISO 200 | dawn mist | landscape |
| 8 | 野生动物 | Sony 400/2.8+TC, ISO 800 | rim light frost | wildlife |
| 9 | 昆虫微距 | R5 100/2.8 macro 1:1, ISO 400 | morning leaf | macro |

---

## 胶片+相机速查（⚠️ Agent 选题用，不写入 prompt）

胶片和机身的物理特性用于 Agent 选题时推算画质特征（如 Portra 400 = 暖调偏黄、ISO 400 的颗粒度），**不直接写进 prompt**。写进 prompt 的是相机参数组合。

| 胶片 | 用途 | Agent 参考特征 |
|------|------|--------------|
| Kodak Portra 400 | 暖调人像 | 自然肤色、柔和反差 → 搭配 R5 85/1.2 |
| Cinestill 800T | 霓虹夜景 | 红色 halation → 搭配 Leica M11 35/1.4, ISO 3200 |
| Kodak Gold 200 | 复古暖调 | 偏黄颗粒 → 搭配 Sony 24-70, golden hour |
| Ilford HP5 | 黑白纪实 | 丰富灰阶 → 直接切 Grok，不用 Codex |

| 机身 | 适用场景 |
|------|---------|
| Canon EOS R5 | 人像/运动/微距 |
| Sony A7R V | 高分辨率风光/人像 |
| Leica M11 | 街头/旅行人文 |
| Hasselblad X2D | 商业时装/建筑 |
| Ricoh GR III | 街头快照 |

---

## 参考资源
- `references/camera-physics-methodology.md` — 相机物理定向方法论（2026-08-05）
- `references/master-photography-techniques.md` — 相机/镜头/布光/肤色速查
- `references/gpt-image2-fatal-pitfalls.md` — gpt-image-2-high 致命坑位速查
- [hermes-daily-image-training](https://github.com/xujie8867/hermes-daily-image-training) — 9 风格完整验证 + 示例图
- 当前提示词库：`all-prompts.json` = 879 条（image-generation 347 / landscape 171 / portrait 155 / photography-miraivfx 98 / illustration-miraivfx 40 / wildlife 27 / street 21 / artistic-photography 10 / 其他 10）
