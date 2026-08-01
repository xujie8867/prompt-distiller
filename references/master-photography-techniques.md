# 📷 大师级摄影提示词技巧全集

> 来源：GitHub/X 社区高赞仓库挖掘 + 实战验证
> 核心仓库：jamez-bondos/awesome-gpt4o-images (★8112)、wuyoscar/GPT-Image2-Skill (★4082)
> 社区贡献：@miilesus, @madamayo_, @ScaleWthAI, @MuseboxAi, @r4jjesh, @MahnoorAi12

---

## 一、各国/不同人种人像摄影大师级技巧 🌍

### 核心原则：指定种族特征 + 真实肤色 + 文化细节

```
[国家/种族] + [肤色 + 底色] + [面部特征] + [发型/发质] + [文化服饰细节]
```

### 肤色描述精确词库

| 人种/地区 | 肤色Prompt | 底色 | 面部特征 |
|-----------|-----------|------|---------|
| 西非 | `rich deep ebony skin with warm undertones` | warm golden-brown | high cheekbones, full lips, broad nose |
| 东非 | `dark brown skin with reddish undertones` | reddish-copper | elongated features, tall forehead |
| 北非/阿拉伯 | `olive-brown skin with golden undertones` | warm amber | defined brow, aquiline nose |
| 南亚(印度) | `warm medium-brown skin with golden undertones` | warm caramel | large almond eyes, defined jaw |
| 东亚(中日韩) | `fair porcelain skin with subtle warm undertones` | ivory-cream | epicanthic folds, straight black hair |
| 东南亚 | `tan golden skin with warm olive undertones` | warm honey | round face, full cheeks |
| 拉丁裔 | `warm olive skin with soft Latina facial structure` | warm tan | large eyes, soft jawline |
| 中东/波斯 | `light olive skin with warm golden undertones` | golden-ivory | strong brows, defined features |
| 北欧/白人 | `fair skin with cool pink undertones, visible freckles` | porcelain-rose | angular features, light eyes |
| 地中海 | `warm olive skin with natural tan` | golden-olive | dark hair, defined nose |
| 混血 | `ambiguous mixed-race features with warm neutral undertones` | neutral-warm | blended features |

### 文化服饰锚词（增强真实性）

- **非洲**: `intricate natural braids`, `colorful Ankara/kitenge fabric`, `Maasai beaded jewelry`
- **印度**: `rich maroon silk saree`, `traditional jhumka earrings`, `gold bangles`, `bindi`
- **中东**: `elegant black abaya with gold embroidery`, `intricate henna patterns`, `keffiyeh`
- **东亚**: `silk hanbok/qipao/kimono`, `jade jewelry`, `minimal elegant makeup`
- **拉丁**: `embroidered huipil blouse`, `colorful woven textiles`, `statement silver jewelry`

### 大师级人像Prompt模板（多民族）

```
Ultra-photorealistic editorial portrait of a [age]-year-old [国家/种族] [性别] with
[具体肤色描述], [面部特征], [发型/发质], [文化服饰]. [表情+姿态].

Hyper-detailed skin: visible pores, microtexture, subtle imperfections, natural sheen,
accurate melanin with [底色] undertones, subsurface scattering, realistic peach fuzz,
natural asymmetry — NOT flawless plastic skin.

[光照方案]. Shot on [相机] with [镜头], shallow depth of field, razor-sharp focus on eyes
with crisp catchlight, creamy bokeh. [权威锚点], 8K hyper-detailed, raw photo, film grain.
```

---

## 二、单反相机/镜头提示词控制技巧 📸

### 相机型号效果对照

| 相机型号 | 效果特征 | 适合场景 |
|---------|---------|---------|
| `Canon EOS R5` | 高锐度，色彩浓郁偏暖 | 商业人像、婚礼 |
| `Sony A1 / Sony A9 III` | 极高锐度，细节解析力强 | 风光、运动、产品 |
| `Hasselblad H6D-100c` | 中画幅，色彩深度极高 | 商业广告、时尚大片 |
| `Hasselblad H6D-400c` | 4亿像素多帧合成 | 顶奢产品、超精细人像 |
| `Leica M11` | 独特徕卡色彩、纪实感 | 街拍、纪实人文 |
| `Leica SL2-S` | 电影级色彩科学 | 时尚街拍、电影感 |
| `Phase One XF IQ4` | 1.5亿像素，顶级色彩 | 顶级商业/博物馆级 |
| `Fujifilm GFX 100S` | 中画幅胶片模拟 | 胶片感人像、风景 |
| `Nikon Z9` | 高速连拍风格 | 运动、野生动物 |

### 镜头型号效果对照

| 镜头 | 效果 | 适合 |
|------|------|------|
| `85mm f/1.4` | 奶油般虚化，肖像最佳 | 半身/头像 |
| `85mm f/1.8` | 锐利浅景深 | 人像通用 |
| `50mm f/1.2` | 电影感虚化 | 环境人像、街拍 |
| `50mm f/1.8` | 自然视角 | 生活纪实 |
| `35mm f/1.4` | 环境叙事 | 街拍、纪实 |
| `35mm f/2.8` | 锐利+环境 | 旅行、人文 |
| `24mm f/1.4` | 广角冲击力 | 风光、建筑 |
| `24mm f/8` | 全幅清晰 | 风光全焦 |
| `100mm f/2.8 macro` | 微距极致细节 | 产品、眼妆特写 |
| `70-200mm f/2.8` | 空间压缩 | 远摄人像、运动 |
| `135mm f/2` | 极致压缩+虚化 | 远摄特写 |

### 镜头效果关键词

```
shallow depth of field (浅景深)     deep focus (全焦段清晰)
creamy bokeh (奶油虚化)            busy bokeh (杂乱虚化)
tack-sharp focus (极度锐利)        slight lens distortion (轻微畸变)
chromatic aberration (色差真实感)   lens flare (镜头光晕)
anamorphic lens flare (宽银幕光晕)  handheld effect (手持效果)
camera grain (胶片颗粒)             full-frame sensor (全画幅)
prime lens (定焦)                  zoom lens (变焦)
```

### 光圈口诀

```
f/1.2-f/1.4  — 极致虚化，单眼对焦，电影感
f/1.8-f/2.8  — 浅景深，人像通用
f/4-f/8      — 中等景深，环境人像
f/8-f/16     — 全幅清晰，风光风景
```

---

## 三、人像真实感技巧（皮肤允许瑕疵）🎭

### 核心理念：❌ 完美无瑕塑料感 | ✅ 真实毛孔纹理

### 皮肤真实感关键词

**正面（必加）**
```
visible pores, realistic skin micro-texture, subtle imperfections,
natural asymmetry, authentic skin detail, subsurface scattering,
natural sheen/oiliness, realistic peach fuzz, facial texture,
slight skin discoloration, faint freckles, beauty marks,
fine wrinkles, laughter lines, natural skin tone variation
```

**绝对禁止（负向词每张必带）**
```
flawless skin, perfect skin, plastic skin, barbie doll skin,
airbrushed skin, overly smooth, waxy skin, doll-like,
oversmoothed, retouched, photoshopped, CGI-looking,
poreless, glass skin, unrealistic perfection
```

### 各年龄层皮肤特征

| 年龄 | 正面描述 | 负向词 |
|------|---------|--------|
| 20-30 | `natural youthful skin with subtle texture, faint pores, dewy finish` | 不用"flawless" |
| 30-45 | `visible fine lines, natural skin texture, laugh lines, subtle sun spots` | 不用"perfect" |
| 45-60 | `weathered skin with character lines, deep laugh lines, age spots, silver hair texture` | 不用"young skin" |
| 60+ | `deeply textured aged skin, visible wrinkles and character lines, natural aging, grey/white hair` | 不用"smooth skin" |

### 皮肤细节加强技巧

```
wet skin with water droplets running down → vivid specular highlights
matte skin with natural oil sheen → subtle highlights on nose/cheek
cold skin with visible goosebumps → tiny bumps texture
sweaty skin after exercise → dewy glow, micro droplets
freckled skin → individual freckles with varying sizes
acne-scarred skin → subtle uneven texture, authenticity
```

### 完整人像Prompt（真实皮肤）

```
Ultra-photorealistic close-up portrait, [人物描述].

SKIN: visible pores, realistic microtexture, subtle peach fuzz, natural asymmetry,
authentic skin detail — NOT flawless, NOT airbrushed, NOT plastic skin.
[额外皮肤条件: wet/matte/aged/freckled].

[光照方案] creating natural skin highlights and shadow falloff.

Shot on [相机] with [镜头], razor-sharp focus on eyes with crisp catchlight showing
iris details, shallow depth of field with creamy bokeh, [权威锚点], 8K raw photo,
cinematic color grading, natural imperfections preserved.

NEGATIVE: flawless skin, plastic skin, airbrushed, doll-like, waxy skin, oversmoothed,
blurry, soft focus, low quality, AI artifacts
```

---

## 四、光线设计大师级技巧 💡

### 9种经典人像布光方案

#### 1. Rembrandt Lighting（伦勃朗光）
```
Rembrandt lighting: strong side key light at 45° creating a crisp triangle of light
on the shadow-side cheek, deep contrasting shadows opposite, high contrast chiaroscuro,
dark background — shot on 85mm f/1.8, dramatic moody atmosphere
```
- 特征：暗侧面颊上的倒三角光斑
- 适合：戏剧性男性人像、艺术家肖像
- 相机：`85mm f/1.8, Hasselblad`

#### 2. Butterfly Lighting（蝴蝶光/派拉蒙光）
```
Butterfly lighting: key light centered above camera creating a butterfly-shaped shadow
under the nose, soft fill from below, even skin illumination — 85mm f/1.4, glamour
portrait, vintage Hollywood glamour, clean background
```
- 特征：鼻子下方蝴蝶形阴影
- 适合：女性时尚/魅力人像
- 相机：`85mm f/1.4, Canon R5`

#### 3. Loop Lighting（环形光）
```
Loop lighting: key light at 45° slightly above eye level creating a small loop shadow
from the nose to the cheek, soft natural look, gentle shadows, catchlights in both eyes
— 50mm f/1.8, natural portrait, warm ambient
```
- 特征：鼻影形成小环形
- 适合：通用人像、家庭照
- 相机：`50mm f/1.8, Sony A1`

#### 4. Split Lighting（分割光）
```
Split lighting: hard side light at exactly 90° splitting face into perfectly lit half
and deep shadow half, extreme contrast, dramatic mood, dark background — 85mm f/1.4,
chiaroscuro portrait, intense atmosphere
```
- 特征：脸部分为亮暗两半
- 适合：戏剧性、神秘感、力量感
- 相机：`85mm f/1.4, Leica SL2-S`

#### 5. Rim/Back Lighting（轮廓光）
```
Strong rim light from behind creating luminous golden/silver outline on hair and
shoulders, face in soft deep shadow with just a hint of detail, dark background,
ethereal atmosphere — 85mm f/1.8, silhouette meets detail
```
- 特征：主体边缘发光轮廓
- 适合：剪影+细节、氛围感人像
- 相机：`85mm f/1.8, Sony A1`

#### 6. Golden Hour Side Light（黄金时段侧光）
```
Golden hour side lighting: warm late-afternoon sun at 45° creating long golden shadows,
soft amber wraparound glow, volumetric god rays through atmosphere, warm tones and deep
shadows, natural outdoor portrait — 85mm f/1.4, Kodak Portra 400 palette
```
- 特征：日落前1小时的暖金色侧光
- 适合：户外自然光人像
- 相机：`85mm f/1.4, Fujifilm GFX`

#### 7. Window Light（窗光）
```
Soft natural window light from a large north-facing window, gentle diffused illumination,
subtle shadow falloff, dust motes floating in light beam, warm interior ambient —
50mm f/1.4, intimate portrait, Dutch Golden Age painting quality
```
- 特征：大面积柔光窗
- 适合：生活感、油画质感
- 相机：`50mm f/1.4, Leica M11`

#### 8. Cinematic Key + Fill + Rim（电影三点光）
```
Cinematic three-point lighting: soft warm key light from front-left, cool blue/magenta
ambient fill, subtle purple rim light from rear-right, shallow depth of field, creamy
bokeh with blurred nightlife background — 85mm f/1.8, premium editorial
```
- 特征：主光+补光+轮廓光
- 适合：电影感时尚、夜生活
- 相机：`85mm f/1.8, Sony A9 III`

#### 9. Vintage Flash（复古闪光灯）
```
Harsh vintage on-camera flash: warm front glow, cool faint bluish shadow behind,
strong specular highlights on skin, slight red-eye effect, party atmosphere,
snapshot aesthetic — 35mm f/2.8, 90s fashion editorial
```
- 特征：硬质直闪 + 冷暖色分离
- 适合：90年代时尚、派对
- 相机：`35mm f/2.8, 35mm film camera`

### 光线质量词库

```
硬光 (Hard Light): harsh, direct, strong shadows, high contrast, crisp edge shadow
柔光 (Soft Light): diffused, gentle, soft shadows, gradual falloff, wraparound
侧光 (Side Light): 45° key, long shadows, sculptural, dimensional
逆光 (Backlight): rim light, silhouette, halo, glowing edge
顶光 (Top Light): overhead, dramatic eye shadows, mysterious
底光 (Bottom Light): uplight, unsettling, horror, dramatic
混合光 (Mixed): warm key + cool fill, color contrast, cinematic
自然光 (Natural): window light, golden hour, blue hour, overcast
人工光 (Artificial): studio strobe, softbox, beauty dish, ring light
```

### 权威光线参考词

```
National Geographic golden hour lighting
Annie Leibovitz dramatic studio lighting technique  
Steve McCurry natural window light style
Mario Testino high-fashion lighting
Peter Lindbergh black and white natural light
Gregory Crewdson cinematic environmental lighting
```

---

## 五、完整集成模板（一键出片）

### 通用大师摄影模板

```json
{
  "camera": "[相机型号] with [镜头型号] f/[光圈] lens",
  "subject": {
    "ethnicity": "[国家/种族]",
    "skin": "[肤色描述] with [底色] undertones",
    "features": "[面部特征]",
    "hair": "[发型/发质]"
  },
  "skin_realism": "visible pores, microtexture, peach fuzz, natural asymmetry, subtle imperfections, subsurface scattering — NOT flawless, NOT airbrushed, NOT plastic",
  "lighting": {
    "type": "[9种布光之一]",
    "description": "[光照详细描述]"
  },
  "composition": "shallow depth of field, razor-sharp focus on eyes with crisp catchlight, creamy bokeh",
  "quality": "8K hyper-detailed, raw photo, film grain, [权威锚点]",
  "negative": "flawless skin, plastic skin, airbrushed, doll-like, waxy skin, oversmoothed, blurry, soft focus, low quality, AI artifacts, deformed"
}
```

### 100字浓缩版（gpt-image-2友好）

```
Ultra-photorealistic [种族] portrait. [肤色+特征]. Natural skin with visible pores
and microtexture — NOT flawless plastic. [9种布光方案选择一种]. Shot on [相机]
[镜头], razor-sharp focus on eyes with crisp catchlight, creamy bokeh.
[权威锚点], 8K raw. NEGATIVE: plastic skin, airbrushed, blurry, soft focus.
```

---

## 参考来源

| 来源 | Stars | 内容 |
|------|-------|------|
| jamez-bondos/awesome-gpt4o-images | 8,112 | 100+ GPT-4o 案例 |
| wuyoscar/GPT-Image2-Skill | 4,082 | Prompt gallery + agent skill + CLI |
| YouMind-OpenLab/awesome-nano-banana-pro-prompts | 13,024 | 10,000+ prompts |
| X社区 @miilesus | — | 结构化人像摄影 prompt 公式 |
| X社区 @madamayo_ | — | 灯光+皮肤+景深三大参数系统 |
| X社区 @ScaleWthAI | — | 3×3 布光测试表模板 |
| X社区 @MuseboxAi | — | 夜景电影感时尚人像 |
| X社区 @r4jjesh | — | 肤色+灯光+精确度 |
