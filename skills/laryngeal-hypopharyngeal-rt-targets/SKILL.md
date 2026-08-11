---
name: laryngeal-hypopharyngeal-rt-targets
description: "Laryngeal/hypopharyngeal radiotherapy master index — split into 2 self-contained modules (PORT + definitive RT). v2.0.0 redirect."
version: 2.0.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [head-neck, radiotherapy, larynx, hypopharynx, index]
    triggers_on: [喉癌, 下咽癌, 喉靶区, 下咽靶区, larynx, hypopharynx, 喉放疗, 下咽放疗, 喉癌靶区, 下咽癌靶区, 声门上喉癌, 声门型喉癌, 声门下喉癌, 梨状窝, 环后区, 喉咽后壁, 喉保留, 喉功能保留, 喉癌术后, 下咽癌术后, 喉癌根治, 下咽癌根治]
    related_skills: [larynx-hypopharynx-postop, larynx-hypopharynx-definitive]
    split_into: [larynx-hypopharynx-postop, larynx-hypopharynx-definitive]
---

> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗中心原创知识产权。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.

# 喉癌与下咽癌放疗靶区勾画——总索引（v2.0.0）

> ⚠️ **v2.0.0：按治疗场景拆分为 2 个自包含模块。** 原 v1.3.0 内容已全部迁移。

## 模块索引

| # | Skill | 场景 |
|:-:|-------|------|
| 1 | `larynx-hypopharynx-postop` | 喉/下咽术后 PORT（全喉/部分喉/咽重建） |
| 2 | `larynx-hypopharynx-definitive` | 喉/下咽根治性 RT（SIB、保声、GTV+内镜） |

## 拆分原因

原 v1.3.0 将 PORT（Stoma、咽吻合口、部分喉切除）和根治性 RT（SIB 70/63/56、内镜 GTV、DAHANCA 5mm）混在同一文件中。与口腔口咽 Skill 相同的问题——模型在 PORT 场景中被根治性 SIB 规则干扰，反之亦然。

## 典型加载路径

| 病例 | 加载 |
|------|------|
| 全喉切除+颈清扫 PORT | `larynx-hypopharynx-postop` |
| 梨状窝癌全喉术后 PORT + 化免 pCR | `larynx-hypopharynx-postop` + `neoadjuvant-deescalation` |
| T1 声门癌保声根治性 RT | `larynx-hypopharynx-definitive` |
| 声门上癌同步放化疗 | `larynx-hypopharynx-definitive` |

## 化免降级

两个模块均引用 `neoadjuvant-deescalation`。喉/下咽特有差异：
- **喉癌 pCR**→降范围优先（对侧颈/Ⅵ 可缩）
- **下咽癌 pCR**→降剂量优先（RP+Ⅵ 基线风险太高，不能缩野）

---

> 朱国培 · 上海交通大学医学院附属第九人民医院口腔颌面-头颈肿瘤科
