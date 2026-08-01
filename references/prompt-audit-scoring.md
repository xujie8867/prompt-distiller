# Prompt 审计评分细则

## 10 项审计清单详解

### 1. 相机品牌（camera_brand）
- **权重**: 10%
- **检查方法**: 搜索 `sony|canon|nikon|hasselblad|leica|fujifilm|phase.?one`
- ❌: 无 / "professional camera" / "DSLR" / "high-end camera"
- ✅: `Sony A1` / `Hasselblad H6D-100c` / `Leica M11` / `Canon EOS R5`
- **0分**: 无任何相机提及 | **5分**: 模糊品牌 | **10分**: 具体型号

### 2. 镜头+光圈（lens_aperture）
- **权重**: 15%（高权重 — 直接决定景深和画面质感）
- **检查方法**: 搜索 `\d{2,3}mm\s+f/?\d`
- ❌: 无 / "portrait lens" / "good lens" / "professional optics"
- ✅: `85mm f/1.4` / `50mm f/1.2` / `100mm f/2.8 macro`
- **0分**: 无镜头 | **5分**: 有焦距无光圈 | **10分**: 焦距+光圈完整

### 3. 布光方案（lighting_scheme）
- **权重**: 15%（高权重 — 决定画面氛围和立体感）
- **检查方法**: 搜索 `rembrandt|butterfly|split.light|rim.light|golden.hour|window.light|softbox|chiaroscuro|key.light`
- ❌: "nice lighting" / "good light" / "beautiful light" / "well lit"
- ✅: `Rembrandt lighting: 45° key, triangle shadow on cheek`
- **0分**: 无光照 | **4分**: 模糊光照 | **8分**: 具体光照名 | **10分**: 光位+参数

### 4. 皮肤真实（skin_realism）人像类强制
- **权重**: 15%
- **检查方法**: 搜索 `pores|micro.?texture|peach.fuzz|imperfection|NOT.?flawless|NOT.?plastic`
- ❌: "perfect skin" / "flawless skin" / "beautiful complexion"
- ✅: `visible pores, skin microtexture, natural asymmetry — NOT flawless`
- **0分**: 无 | **5分**: 有 texture/realistic 模糊词 | **10分**: 具体毛孔+微纹理+NOT flawless

### 5. 负向词（negative）
- **权重**: 10%
- **检查方法**: 搜索 `blurry|motion.blur|soft.focus|plastic.skin|airbrush|flawless|oversmoothed`
- ❌: 完全不写负向词
- ✅: `NEGATIVE: blurry, plastic skin, airbrushed, oversmoothed, soft focus, low quality`
- **0分**: 无 | **5分**: 1-3项 | **10分**: 5+项覆盖

### 6. 锐度（sharpness）
- **权重**: 10%
- **检查方法**: 搜索 `tack.?sharp|razor.?sharp|crisp.focus|micro.?contrast|maximum.sharpness`
- ❌: "sharp" / "detailed"（太泛）
- ✅: `tack-sharp focus, high micro-contrast, razor-sharp detail`
- **0分**: 无 | **5分**: 简单 sharp | **10分**: tack-sharp + micro-contrast

### 7. 权威锚（authority）
- **权重**: 5%
- **检查方法**: 搜索 `national.geographic|vogue|annie.leibovitz|steve.mccurry|peter.lindbergh`
- ❌: "professional quality" / "award winning" / "world class"
- ✅: `National Geographic portrait style` / `Vogue editorial`
- **0分**: 无 | **10分**: 具体权威锚

### 8. 构图（composition）
- **权重**: 5%
- **检查方法**: 搜索 `shallow.depth|bokeh|catchlight|rule.of.thirds|leading.lines`
- ❌: 无构图描述
- ✅: `shallow depth of field, creamy bokeh, eyes with crisp catchlight`
- **0分**: 无 | **5分**: 简单提及 | **10分**: DOF+bokeh+catchlight

### 9. 分辨率（resolution）
- **权重**: 5%
- **检查方法**: 搜索 `8K|32K|hyper.?detailed|raw.photo|high.resolution`
- ❌: "HD" / "high quality"
- ✅: `8K hyper-detailed, raw photo, film grain`
- **0分**: 无 | **10分**: 8K+raw

### 10. 人像专项（portrait_specific）仅人像类
- **权重**: 10%
- **检查方法**: 搜索精确肤色词 → 见 `master-photography-techniques.md`
- ❌: "Asian woman" / "African man" / 泛泛人种
- ✅: `East African woman, rich deep ebony skin with warm undertones, high cheekbones`
- **0分**: 泛泛 | **5分**: 有大洲/国家 | **10分**: 精确肤色+面部特征

---

## 综合评分

| 分数 | 等级 | 处理 |
|------|------|------|
| 90-100 | 🏆 大师级 | 直接生成 |
| 70-89 | 👍 良好 | 可生成，微调 |
| 40-69 | ⚠️ 需优化 | 自动注入缺失元素 |
| 0-39 | ❌ 低质量 | 完全重写 |

## 评分示例

### 案例 1：不合格 Prompt
```
"A beautiful portrait of a woman at sunset with perfect skin"
```
| # | 检查项 | 评分 | 原因 |
|---|--------|------|------|
| 1 | 相机 | 0 | 无 |
| 2 | 镜头 | 0 | 无 |
| 3 | 布光 | 0 | "sunset"不算具体方案 |
| 4 | 皮肤 | 0 | "perfect skin"正是禁词 |
| 5 | 负向词 | 0 | 无 |
| 6 | 锐度 | 0 | 无 |
| 7 | 锚点 | 0 | 无 |
| 8 | 构图 | 0 | 无 |
| 9 | 分辨率 | 0 | 无 |
| 10 | 人像 | 0 | "a woman"太泛 |

**总分: 0/100 — ❌ 低质量，必须完全重写**

### 案例 2：优化后 Prompt
```
"Ultra-photorealistic portrait of a young East African woman, rich deep ebony skin with warm undertones, high cheekbones. Visible pores, natural skin microtexture — NOT flawless, NOT airbrushed. Golden hour side lighting: warm sun at 45°, long golden shadows. Shot on Sony A1 with 85mm f/1.4 lens, shallow DOF, tack-sharp focus on eyes, creamy bokeh. National Geographic style, 8K raw. NEGATIVE: plastic skin, airbrushed, blurry, soft focus"
```
| # | 检查项 | 评分 | 
|---|--------|------|
| 1 | 相机 | 10 |
| 2 | 镜头 | 10 |
| 3 | 布光 | 10 |
| 4 | 皮肤 | 10 |
| 5 | 负向词 | 8 |
| 6 | 锐度 | 10 |
| 7 | 锚点 | 10 |
| 8 | 构图 | 10 |
| 9 | 分辨率 | 10 |
| 10 | 人像 | 10 |

**总分: 98/100 — 🏆 大师级**
