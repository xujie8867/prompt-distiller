# 相机物理定向方法论

> **发现日期**：2026-08-05  
> **验证精度**：9 种风格，9 投 9 中，零重试  
> **来源**：用户反馈「找不到感觉」→ 分析 prompt 差异 → 发现艺术引用 vs 物理参数的输出质量鸿沟

## 核心洞察

AI 生图模型（gpt-image-2-high / grok-imagine-image）在**光学物理层面推理，不在艺术史层面推理**。

| 你说 | AI 理解为 |
|------|----------|
| "Gregory Crewdson cinematic staging" | "画一幅 Crewdson 风格的**画**" |
| "Canon EOS R5, 85mm f/1.2, ISO 800" | "通过 f/1.2 的浅景深、ISO 800 的噪点水平渲染" |

**关键差异**：摄影师名字 + 风格标签是「风格化指令」——AI 会对输出进行二次风格叠加。相机参数是「物理约束」——AI 在噪声/景深/色彩科学的参数空间内直接渲染。

## 实验证据

### 对照组：艺术引用风格
```
Prompt: Gregory Crewdson cinematic staging, golden hour backlight, 
        Kodak Portra 400, fashion editorial
结果: 糊片、塑料皮肤、AI 感重
用户: "找不到之前生图的那种感觉了"
```

### 实验组：相机物理风格
```
Prompt: Canon EOS R5, 85mm f/1.2, ISO 800, blue hour twilight, 
        single tungsten bulb above doorway, photojournalism candid
结果: 真实、自然、皮肤可见毛孔
用户: "很真实，非常棒"
```

### 全矩阵验证（2026-08-05）

| # | 风格 | 镜头 | 光线 | 结果 |
|---|------|------|------|------|
| 1 | 新闻纪实 | R5 85/1.2 | 胡同蓝调+钨丝灯 | ✅ |
| 2 | 商业时装 | Hasselblad 80/1.9 | 北向窗光 | ✅ |
| 3 | 旅行人文 | Leica M11 35/1.4 | 橄榄树叶漏光 | ✅ |
| 4 | 极简风光 | Sony 24/1.4 | 黎明前长曝光 | ✅ |
| 5 | 街头快照 | Ricoh GR III 28/2.8 | 城市混合光 ISO 3200 | ✅ |
| 6 | 棚拍肖像 | R5 50/1.2 | 柔光箱 45° | ✅ |
| 7 | 自然风光 | Sony 24-70@35 | 桂林晨雾 | ✅ |
| 8 | 野生动物 | Sony 400/2.8+TC | 霜原金色时刻 | ✅ |
| 9 | 昆虫微距 | R5 100/2.8 macro | 晨光透叶片 | ✅ |

**结论**：与风格/主题无关——只要是相机参数+自然光写法，全部一次通过。

## 三层架构

```
第一层：生成 prompt（给 AI 模型，≤150 字）
├── 场景+人物
├── 自然光线描述
├── 相机+镜头+ISO（必须）
├── 皮肤/纹理细节
└── 纪实风格声明（photojournalism/candid/documentary）

第二层：知识库（Agent 自己用）
├── 721 条 prompt 库
├── 348 条拉鲁斯
├── 摄影大师技巧全集
└── → Agent 从中选题，翻译成第一层语言

第三层：负向词（给 AI 模型）
└── NOT CGI, NOT staged, NOT cinematic...
    → 只告诉 AI「不要什么」，不管它「怎么做」
```

## 为什么以前 721 条 prompt 越学越差

那些 prompt 来自摄影社区——它们是为**人**写的：摄影师名、胶片型号、风格流派是人类的速记符号。人类读到 "Crewdson cinematic staging" 能自动翻译成「精心布景、戏剧化单光源、电影画幅比」。

AI 读到同一句话，翻译成「把这张图风格化成 Gregory Crewdson 的画风」——这是完全不同的操作。

直白的相机物理参数反而是 AI 最能精确执行的指令。

## 适用边界

- ✅ gpt-image-2-high (OpenAI Codex)：上述 9 种全部验证
- ✅ grok-imagine-image (xAI Grok)：锐度更高，用于 Codex 三坑场景
- ⚠️ 其他模型未测试，但原理（物理参数 > 艺术引用）应该是通用的
