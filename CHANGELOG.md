# Changelog

本仓库为 **AI 生图能力蒸馏包**：将实战验证过的生图规则打包成自包含 Skill，任何智能体读取即用。规则随每日实战反馈持续迭代。

## v2.0.1 — 2026-08-13

- **规则升级至 v2.0 相机物理审计范式**（对应 hermes-daily-image-training v5.x 方法论）
  - 核心发现：AI 不理解艺术史——它理解相机物理
  - ⛔ 致命词：摄影师名字 / cinematic / editorial / staged / 胶片型号 → 直接扣至 <60 分
  - ✅ 必须词：相机型号 + 镜头 + ISO / 自然光描述 / 纪实风格声明
- **新增 references**：
  - `camera-physics-methodology.md` — 相机物理定向方法论（9 种风格 9 投 9 中，零重试）
  - `gpt-image2-fatal-pitfalls.md` — gpt-image-2-high 致命坑位速查
- 题库条数同步更新：721 → **879 条**
- README 修正仓库用户名 `xuj-hub` → `xujie8867`

## v1.0.x — 2026-08-08

- 新增 24 条 X 社区高赞摄影 prompt
- 精选提示词库 `curated-prompts.json`（374 条摄影类：人像 155 / 风景 171 / 动物 27 / 街拍 21）
- 10 项审计评分细则 + `audit_prompt.py` 审计脚本
- 12 种肤色 × 9 款相机 × 12 种镜头 × 9 种布光知识库

## v1.0 — 2026-08-05

- 严格筛选：仅保留人像/风景/动物/摄影类高质量 prompt
- 相机物理审计核心框架（第一版）
