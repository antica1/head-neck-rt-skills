---
name: head-neck-rt-methodology
description: "头颈放疗靶区规划通用方法论——分期四态验证、侧性肿瘤对侧照射三层框架、SER增敏修正、手术不易切净区加量。Universal methodology for head-neck RT planning."
version: 1.0.2
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [head-neck, radiotherapy, methodology, staging, contouring]
    triggers_on: [分期四态, cT pT ypT rT, 对侧照射, 侧性肿瘤, SER增敏, 手术不易切净区, 靶区方法论, 总纲, 通用方法论, staging prefix, contralateral target]
    related_skills: [port-oral-postop, port-oropharynx-postop, larynx-rt-targets, hypopharynx-rt-targets, npc-rt-target-delineation, hncup-rt-targets, adenoid-cystic-carcinoma-rt-targets, orbital-tumor-rt-targets, head-neck-sarcoma-rt-targets]
---

# 头颈放疗靶区规划——通用方法论

> 本 Skill 是8个瘤种特异性靶区 Skill 的总纲。在加载任何具体 Skill 之前，这里的规则作为默认行为应用。

---

## 一、分期四态——绝不混淆

| 前缀 | 数据来源 | DOI？ |
|------|---------|:--:|
| cT（临床）| 体检+影像 | ❌ |
| pT（病理）| 手术标本 | ✅ |
| ypT（新辅助后）| 新辅助后标本 | 看残留 |
| rT（复发）| 复发影像 | ❌ |

**铁律**：DOI 仅用于 pT。cT 用影像大小+侵犯范围。ypT0 = 无残留 = 无 DOI。同一标本不能同时出现 p 和 yp。

---

## 二、侧性肿瘤对侧照射——三层决策框架

任何单侧肿瘤需要判断是否照对侧时，按以下三层依次检查：

### 第一层：原发灶跨中线/近中线

| 跨中线结构 | 典型肿瘤 | 对侧触发条件 |
|-----------|---------|------------|
| 鼻咽顶 | NPC | 默认双侧 |
| 硬腭/软腭 | 硬腭癌 | 近中线或跨中线 |
| 舌根/口底 | 舌癌/口底癌/舌下腺 | 距中线≤1 cm |
| 杓会厌皱襞 | 声门上喉癌 | 跨中线 |

### 第二层：淋巴链逆流

| 触发条件 | 对侧范围 |
|---------|---------|
| 多区 LN+（≥2站）| 对侧ⅠB+Ⅱ |
| ENE+ | 对侧同站+下游 |
| N2c 或 N3 | 对侧全颈 |

### 第三层：手术引流改变

| 手术操作 | 对侧补偿 |
|---------|---------|
| 单侧颈清扫 | 对侧ⅠB+Ⅱ |
| 口底未处理 | 对侧口底+对侧ⅠB |

---

## 三、手术不易切净区——加量规则

以下区域即使病理切缘阴性，肿瘤曾临近时仍需考虑加量（60→66 Gy）：

1. 前上门牙-鼻腔底硬腭
2. 颏结节（口底肌附着）
3. 颅底/翼腭窝/翼板根部
4. 腮腺深叶-茎乳孔
5. 眼眶/脑膜

四类加量指征：R1/R2 | ENE+ | 手术不易切净 | T4/N3 临近关键结构

---

## 四、SBRT 后补量——SER 修正

### BED 公式
```
EQD2 = 总剂量 × (1 + d/αβ) / (1 + 2/αβ)
累积 EQD2 = EQD2(SBRT) × SER + EQD2(补量) × SER_residual
```

### SER 衰减
- 同期用药：SER = 1.1-1.3（抗 EGFR ADC）
- 停药 <4 周：SER ≈ 1.05-1.10
- 停药 >12 周：SER ≈ 1.0

### 速查表

| 首程 SBRT | EQD2₁₀ 已有 | 补量至 60 Gy | 补量至 66-70 Gy（根治）|
|-----------|:--:|------|------|
| 5 Gy × 5 = 25 Gy | 31.3 Gy | 28-30 Gy / 14-15 fx | 34-38 Gy / 17-19 fx |
| 6 Gy × 5 = 30 Gy | 40.0 Gy | 20 Gy / 10 fx | 26-30 Gy / 13-15 fx |
| 8 Gy × 3 = 24 Gy | 36.0 Gy | 24 Gy / 12 fx | 30-34 Gy / 15-17 fx |

---

## 五、靶区规划摘要——统一格式

每次分析结尾输出可粘贴进病程录的摘要。只列实际 CTV 层级，每层附理由。豁免和加量均说明原因。不含 OAR 限量（物理师负责）。

```
═══════════════════════════════
  放疗靶区规划
═══════════════════════════════
诊断：______  pT__N__M__（AJCC 第 9 版）
分期判断：______
手术：______
PORT 指征：______
降级依据：______（如适用）

方案：□ 术后 PORT  □ 根治性 RT   ___ Gy / ___ fx

CTV___：______（___ Gy — 理由：______）
加量：______  ___ Gy（理由：□R1/R2 □ENE+ □手术不易切净 □T4/N3）
豁免：______（理由：______）

主治：______  日期：______
═══════════════════════════════
```

---

## 技能索引

本 Skill 不覆盖瘤种特异性内容。遇到具体病例时，按瘤种加载对应 Skill：

> 研究方案草稿的统计自洽核查（精确二项上限、误停率、把握度）→ `references/protocol-statistical-consistency.md`

| Skill | 覆盖内容 |
|-------|---------|
| 口腔口咽术后 | 舌/口底/牙龈/颊/硬腭/扁桃体/舌根 |
| 腺样囊性癌 (ACC) | 面神经径路/颅底孔道/PNI 追踪 |
| 喉癌/下咽癌 | 软骨侵犯/Stoma/RP/Ⅵ区 |
| 鼻咽癌 (NPC) | 颅底孔道/海绵窦/逐级 CTV |
| 眼眶肿瘤 | 间室放疗/眼前庭共管 |
| 原发不明转移癌 | 选择性黏膜/EBV/HPV 分层 |
| 唾液腺癌 | 腮腺/颌下腺/淋巴上皮癌 CRT |
| 再程放疗 | Quad-Shot/SBRT+IO/SBRT 补量 |
| DVH 计划审核 | 双轨制/QUANTEC 四维/硬约束 vs 软约束 |
