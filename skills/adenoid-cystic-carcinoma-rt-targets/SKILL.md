---
name: adenoid-cystic-carcinoma-rt-targets
description: "腺样囊性癌ACC术后放疗靶区勾画——面神经径路/颅底孔道、PNI追踪。Postoperative RT for adenoid cystic carcinoma — nerve pathway coverage, skull base foramen."
version: 1.7.1
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [head-neck, radiotherapy, target-delineation, adenoid-cystic-carcinoma, perineural, skull-base]
    triggers_on: [腺样囊性癌, 腺样囊性, ACC, 筛状型, 管状型, 实体型, 神经侵犯, 嗜神经, PNI, 神经内侵犯, 面神经径路, 三叉神经, V3神经, 卵圆孔, 圆孔, 翼腭窝, 海绵窦, 颅底孔道, Meckel腔, 腮腺ACC, 舌下腺ACC, 硬腭ACC, 鼻腔鼻窦ACC, ACC术后放疗, 腺样囊性癌复发, 骨寡转移, 肺转移, CAP方案, adenoid cystic carcinoma, perineural invasion, skull base foramen]
    related_skills: [salivary-gland-rt-targets, orbital-tumor-rt-targets, reirradiation-plan-recommend, head-neck-dvh-plan-review]
---
> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗中心原创知识产权。五大原创框架——间室放疗（门+隔壁）、淋巴逆流规则、QUANTEC 四维批判、口底铁律、化免新辅助后 PORT 降级三梯度——均为九院体系的组成部分。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.



# 头颈部腺样囊性癌术后放疗靶区勾画指南

## 🔴 铁律清单（出报告前逐条核验）

> **模型注意力焦点——以下规则在所有腺样囊性癌放疗靶区中自动适用，长报告中的靶区描述必须与之完全一致。**

| # | 铁律 | 触发条件 |
|:--:|------|---------|
| 1 | **感觉神经原则**：ACC 优先沿感觉神经（三叉神经支）扩散而非运动神经——腮腺 ACC 靶区沿 V3 径路（耳颞/舌/下牙槽神经）追踪至颅底，不走面神经颞骨径路 | 所有 ACC 靶区勾画，尤其腮腺原发 |
| 2 | **Tier 1 全海绵窦**：病理明确命名神经受侵 → 覆盖整个同侧海绵窦至 Meckel's cave 层面，60 Gy/30 fx | 病理命名主要神经受侵（下牙槽神经/舌神经/V3 分支等） |
| 3 | **Tier 2 海绵窦下缘**：仅报"神经周侵犯/小神经分支受侵"、未命名主要神经 → 覆盖至同侧海绵窦下缘，54–56 Gy/30 fx | 病理仅见小/末梢神经侵犯 |
| 4 | **神经内侵犯升级**：INTRANEURAL（肿瘤位于神经内）→ 升级按 Tier 1 处理（整个海绵窦 60 Gy），预后差于单纯神经周侵犯 | 病理区分 perineural 与 intraneural |
| 5 | **Tier 3 仍照颅底**：无 PNI 亦须沿三叉神经径路预防覆盖至颅底，50–54 Gy/30 fx，不可豁免神经径路 | 术后病理无神经侵犯 |
| 6 | **孔道全程勾画**：CTV 沿神经解剖径路逻辑连通原发灶与海绵窦——V3→卵圆孔→翼外板内侧→下颌孔→下牙槽管；V2→圆孔→翼腭窝→眶下管；径路外放 5–8 mm，骨性管道内收窄至 3–5 mm | 所有需神经径路覆盖的病例 |
| 7 | **腭部中线规则**：近中线/跨中线 + PNI+ → 对侧腭大孔→翼腭窝→圆孔必须预防照射，至少到圆孔开口（Tier 2 级高度）54 Gy；翼腭窝增宽/同侧神经症状 → 同侧照至海绵窦底（Tier 1 级），对侧仍至少到圆孔开口 | 硬腭 ACC 距中线 <1 cm 或跨中线 |
| 8 | **颈照射三指征**：实体型、口裂以下原发（舌/口底/颌下腺/舌下腺）、病理 LN+，任一条 → 同侧预防性 Ib+II+III | 满足任一指征 |
| 9 | **口裂以上不照颈**：口裂以上（硬腭/软腭/鼻腔/鼻窦/上牙龈）+ 非实体型（筛状/管状）+ 无 LN 转移 → 不做预防性颈照射 | 三条件同时满足 |
| 10 | **双侧颈铁律**：口底/舌下腺 + 实体型 + 同侧 LN+ → 双侧 Ib+II+III（口底为双侧淋巴引流枢纽，仅照同侧不够） | 舌下腺/口底近中线原发且已证转移 |
| 11 | **剂量分层**：高危（R1/R2 切缘、Tier 1 PNI）66 Gy/33 fx；中危（Tier 2）与 R0 无 PNI 均 60 Gy/30 fx；神经径路与颈部预防量 50–54 Gy | 按切缘状态与 PNI 层级定处方 |
| 12 | **面神经三域证据**：病理+面瘫+MRI 三者均确认 → 茎乳孔垂直段 60–66 Gy（上垂直段手术不可及）；未确认 → 垂直段仅预防 50–54 Gy，水平段（岩骨内）禁止照射（耳蜗 Dmean ≤45 Gy）；MRI 增粗≠肿瘤受侵 | 腮腺 ACC 面神经评估 |
| 13 | **鼻腔鼻窦 ACC 独立处理**：PNI 通路为 V2+V3+翼管神经，翼腭窝为必覆盖关键结构；切缘阳性对 OS/DFS 无显著影响（跳跃性 PNI）→ 更强调 PORT；多处切缘阳性/软组织受侵 → 66 Gy | 鼻腔/鼻窦 ACC |
| 14 | **CAP 化疗**：顺铂 50–80 mg/m² + 多柔比星 40–60 mg/m² + 环磷酰胺 400–600 mg/m²，d1，q3–4w | 快速生长、症状明显、不可切除、复发、转移性 ACC |
| 15 | **切缘阴性≠肿瘤床安全**：手术记录未描述但肿瘤曾临近"不易切净区"（茎乳孔/腮腺深叶/颅底/翼腭窝/颏结节/前上门牙-鼻底硬腭）仍需考虑加量；四类加量指征：①R1/R2 ②ENE+ ③不易切净区 ④不手术 T4/T4b 临近颅底/脑膜/眼眶/颈动脉 | 所有术后病例的加量决策 |

> ⚠️ 以上铁律即使正文未逐条提及也自动适用。

---

## Overview

Adenoid cystic carcinoma (ACC) of the head and neck is a rare salivary gland malignancy characterized by slow growth, high rates of perineural invasion, and low rates of lymphatic metastasis. Standard postoperative radiotherapy principles derived from squamous cell carcinoma do not adequately address ACC's unique biological behavior. 

This guide is based on clinical experience at Shanghai Ninth People's Hospital and published work in *Radiotherapy & Oncology* and *Chinese Journal of Radiation Oncology*, combined with general consensus guidelines (ICRU 83/91, QUANTEC, RTOG/EORTC contouring atlases).

## Core Principle: ACC Postoperative RT is NOT SCC PORT

| Feature | Squamous Cell Carcinoma | Adenoid Cystic Carcinoma |
|---------|------------------------|-------------------------|
| Growth rate | Rapid | Slow, indolent |
| Perineural invasion (PNI) | 5-20% | **40-60%** (hallmark feature) |
| Preferred nerve route | Mixed motor/sensory | **Strongly favors SENSORY nerves** (trigeminal branches) over motor nerves |
| Lymphatic metastasis | Common (15-40%) | **Uncommon (5-15%)** |
| Hematogenous metastasis | Late | Late (lung, bone, liver) |
| Surgical margins | Negative margins critical | **"Skip lesions" along nerves make clear margins unreliable** |
| Radiation sensitivity | Moderate | Moderate-high |

---

## Section 1 — Neural Pathway Coverage: The Ninth Hospital Approach

### 1.1 The Sensory Nerve Principle

ACC demonstrates a strong predilection for **sensory nerves** (particularly branches of the trigeminal nerve, CN V) rather than **motor nerves** (such as the facial nerve, CN VII). This is a critical departure from the conventional assumption that ACC follows "any nerve."

**Clinical example — Parotid gland ACC:**

| Nerve | Branch of | Likelihood of ACC involvement |
|-------|-----------|------------------------------|
| Auriculotemporal nerve | CN V3 (sensory) | **High** |
| Lingual nerve | CN V3 (sensory) | **High** |
| Inferior alveolar nerve | CN V3 (sensory) | **High** |
| Facial nerve (CN VII) | Motor | **Low** (despite passing through the parotid) |

This means the target volume for a parotid ACC should follow the **trigeminal nerve pathway to the skull base**, NOT the facial nerve pathway through the temporal bone.

### 1.2 The Three-Tier System for Neural Pathway Coverage

Based on postoperative pathology, ACC falls into one of three tiers dictating how aggressively the neural pathway should be irradiated:

```
┌─────────────────────────────────────────────────────┐
│   Post-op Pathology                  RT Coverage    │
├─────────────────────────────────────────────────────┤
│                                                     │
│  TIER 1: NAMED NERVE INVASION                       │
│  ┌─────────────────────────────────────────────┐   │
│  │ Pathology explicitly names an involved      │   │
│  │ nerve (e.g. "inferior alveolar nerve",     │   │
│  │ "lingual nerve", "V3 branch")              │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  → Cover the ENTIRE ipsilateral                    │
│    CAVERNOUS SINUS                                  │
│    (to the Meckel's cave level)                     │
│    60 Gy / 30 fx                                    │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  TIER 2: SMALL/TERMINAL NERVE INVASION ONLY         │
│  ┌─────────────────────────────────────────────┐   │
│  │ Pathology mentions "perineural invasion",   │   │
│  │ "nerve twig involvement", or "small nerve   │   │
│  │ branch involvement" WITHOUT naming a        │   │
│  │ specific major nerve                        │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  → Cover to the INFERIOR BORDER of the             │
│    IPSILATERAL CAVERNOUS SINUS                     │
│    54-56 Gy / 30 fx                                 │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  TIER 2B: INTRANEURAL vs PERINEURAL INVASION       │
│  ┌─────────────────────────────────────────────┐   │
│  │ PNI has TWO histological subtypes:          │   │
│  │ · Perineural: tumor surrounds nerve,        │   │
│  │   doesn't penetrate epineurium              │   │
│  │ · INTRANEURAL: tumor IS INSIDE the nerve    │   │
│  │   (within epineurium/perineurium)           │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  → INTRANEURAL invasion → upgrade to Tier 1       │
│    (cover entire cavernous sinus, 60 Gy)           │
│    Evidence: intraneural PNI carries worse         │
│    prognosis than perineural only (Teymoortash     │
│    Histopathology 2014; 朱奕 中国癌症杂志 2016)    │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  TIER 3: NO NEURAL INVASION                         │
│  ┌─────────────────────────────────────────────┐   │
│  │ No PNI detected on pathology                │   │
│  └─────────────────────────────────────────────┘   │
│                                                     │
│  → Prophylactic coverage to the SKULL BASE          │
│    following the trigeminal nerve pathway           │
│    50-54 Gy / 30 fx                                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 1.2B Contralateral Nerve Pathway Coverage — The Midline Rule

> **腭部 ACC 跨中线/近中线时，对侧腭大孔→翼腭窝→圆孔必须预防照射。** 与颈淋巴结的双侧规则逻辑一致——口底/腭部的神经血管网在近中线处双侧互通。

| 情形 | 同侧 | 对侧 |
|------|------|------|
| **硬腭偏一侧**（距中线 ≥1 cm）| 腭大孔→翼腭窝→圆孔（按 Tier 1/2/3 决定高度） | 不照 |
| **近中线/跨中线 + PNI+** | 同上 | **至少照到圆孔开口**（Tier 2 级高度）——预防量 54 Gy |
| **翼腭窝增宽 / 同侧神经症状** | 圆孔内 + 海绵窦底（Tier 1 级高度） | 按近中线规则，对侧仍至少到圆孔开口 |

> **解剖依据**：硬腭黏膜下双侧腭大孔的神经血管在切牙孔/腭中缝处有交通支。肿瘤近中线→可通过黏膜下神经丛扩散至对侧腭大神经→对侧翼腭窝→对侧 V2→圆孔。仅照同侧会遗漏这一扩散路径。

### 1.3 Anatomical Implementation: The Trigeminal Nerve Pathway

The CTV should follow the course of the relevant trigeminal branches from the primary site to the target level (cavernous sinus / skull base). Key anatomical reference points:

| Segment | Anatomical Landmarks to Cover |
|---------|------------------------------|
| **Primary site → Infratemporal fossa** | Pterygopalatine fossa, foramen rotundum (V2), foramen ovale (V3) |
| **Skull base foramina** | Foramen ovale (V3), foramen rotundum (V2), superior orbital fissure (V1) |
| **Cavernous sinus** | Lateral wall of the cavernous sinus, Meckel's cave |
| **Mandibular branch (V3)** | Foramen ovale → medial to lateral pterygoid plate → mandibular foramen → inferior alveolar canal |
| **Maxillary branch (V2)** | Foramen rotundum → pterygopalatine fossa → infraorbital canal |
| **Auriculotemporal nerve** | V3 → behind TMJ → upward along superficial temporal artery |

**Practical contouring technique:**
- Use a CTV of 5-8mm around the expected nerve pathway
- Narrow to 3-5mm within bony canals
- The pathway should logically connect the primary site to the cavernous sinus

---

## Section 2 — Neck Node Management in ACC

### 2.1 The Low Lymphatic Metastasis Principle

ACC has significantly lower rates of lymph node metastasis compared to SCC. Routine prophylactic neck irradiation is NOT indicated for the majority of ACC patients. Neck dissections are often not performed electively in ACC surgery.

### 2.2 When to Irradiate the Neck

The following situations warrant prophylactic ipsilateral neck irradiation (Ib + II + III):

| Indication | Rationale |
|-----------|-----------|
| **Solid-type ACC histology** | Solid subtype has higher aggression and metastatic potential |
| **Primary site BELOW the oral fissure** (tongue, floor of mouth, submandibular gland, sublingual gland) | These sites have richer lymphatic drainage |
| **Known pathological lymph node involvement** | Standard surgical bed coverage |

### 2.3 When NOT to Irradiate the Neck

Do NOT perform prophylactic neck irradiation when:

| Condition | Rationale |
|-----------|-----------|
| **Primary site ABOVE the oral fissure** (hard palate, soft palate, nasal cavity, paranasal sinuses, upper gingiva) AND **non-solid histology** | Lymphatic drainage from these sites is minimal |
| **Cribriform or tubular ACC subtype** without nodal involvement | Very low metastatic risk |

### 2.4 Neck Coverage Decision Algorithm

```
ACC Post-Op Neck Irradiation Decision
              │
    ┌─────────┴─────────┐
    │                   │
  Solid histology    Non-solid histology
    │                   │
    │              ┌────┴────┐
    │              │         │
    │         Below oral  Above oral
    │          fissure     fissure
    │              │         │
    │              │         │
    └──────┬───────┘         │
           │                 │
           │           DO NOT irradiate
           │           prophylactic neck
           │
    ┌──────┴──────┐
    │             │
  同侧 LN-     同侧 LN+
  (cN0/pN0)   (pN1+)
    │             │
    │        ┌────┴────┐
    │        │         │
    │   口底/舌下腺  其他口裂以下
    │   近中线原发    部位
    │        │         │
    │        │         │
    └──┬─────┘    ┌────┴────┐
       │          │         │
  照同侧        照同侧    照双侧
  Ib+II+III   Ib+II+III  Ib+II+III
  （低危，     （标危）   （高危——
   无LN+）              口底中线+
                        已证转移=
                        对侧风险）
```

> **新增规则：口底/舌下腺 + 实体型 + 同侧 LN+ → 双侧颈照射。** 舌下腺位于口底，口底是双侧淋巴引流的枢纽通道。实体型已证明具有转移能力——一旦同侧 LN+，对侧颈淋巴站通过口底血管网处于高危。此时仅照同侧是不够的。

### 2.5 Salivary Gland-Specific Considerations

| Primary Site | Typical Neck Management | Rationale |
|-------------|------------------------|-----------|
| **Parotid gland** | No prophylactic neck RT (unless solid type) | Lymphatic drainage from parotid is minimal |
| **Submandibular gland** | Consider prophylactic Ib + II (even non-solid) | This is at/below the oral fissure level |
| **Sublingual gland** | Prophylactic Ib + II (below oral fissure, rich lymphatic drainage). **If solid type + ipsilateral LN+ → bilateral neck.** | Sublingual gland = floor of mouth → bilateral lymphatic highway. Midline proximity + proven metastatic capacity = contralateral nodes at risk. |
| **Hard palate** | No prophylactic neck RT (unless solid type) | Above oral fissure, minimal lymphatic spread |
| **Minor salivary glands (buccal, palate)** | No prophylactic neck RT (unless solid type) | Above oral fissure |

---

## Section 3 — Dose and Fractionation for ACC

### 3.1 Postoperative Dose Levels


> **SBRT 后的常规分割补量**：如 ACC 首程采用 SBRT（5.5 Gy×5fx 等），需要后续常规分割补足根治剂量时，见 `reirradiation-plan-recommend` Skill §五"分割补量"。核心公式：累积 EQD2₁₀ = EQD2₁₀(SBRT) + EQD2₁₀(常规)，目标总量 ≥60 Gy。

| Risk Category | Dose | Fractionation | Indication |
|--------------|------|---------------|------------|
| **High-risk (R1/R2 resection, Tier 1 PNI)** | 66 Gy | 2.0 Gy × 33 fx | Named nerve invasion, positive margins |
| **Intermediate risk (Tier 2 PNI)** | 60 Gy | 2.0 Gy × 30 fx | Small nerve involvement |
| **Low-risk (Tier 3, R0 with no PNI)** | 60 Gy | 2.0 Gy × 30 fx | Complete resection, no PNI |
| **Neural pathway prophylaxis (Tier 3)** | 50-54 Gy | 1.67-1.8 Gy × 30 fx | Prophylactic along nerve |
| **Neck prophylaxis (if indicated)** | 50-54 Gy | 1.67-1.8 Gy × 30 fx | Prophylactic neck |

### 3.2 骨寡转移 SBRT 剂量（2026-08 飞书经验，窦圣金）

> 转移性 ACC 单发骨寡转移（oligometastasis）——SBRT 根治性局部处理。BED₁₀ 目标 ≥48-60 Gy。

| 病灶部位 | 推荐方案 | 说明 |
|---------|---------|------|
| 四肢/肋骨/骨盆等外周骨 | **30 Gy/3fx**（10 Gy×3） | BED₁₀=60 Gy |
| 脊柱（椎体/椎旁） | **30 Gy/5fx**（6 Gy×5） | 降低脊髓 Dmax，BED₁₀=48 Gy |
| 脊柱紧贴脊髓（<3mm） | 27 Gy/3fx 或 24 Gy/2fx | 脊髓 Dmax 目标 ≤14-15 Gy/次 |
| 颅骨/眼眶等头颈骨 | **30-35 Gy/5fx** | 视神经、晶状体保护优先 |

- 脊髓限量（3fx）：Dmax≤22.5 Gy、<0.35cc≤15.9 Gy；（5fx）：Dmax≤28 Gy、<0.35cc≤22 Gy
- GTV=MRI T1/T2 融合骨病灶+骨外软组织；CTV=GTV+3-5mm（不越骨皮质）；PTV=+3mm
- ⚠️ BED₃>130 Gy 时 ORN/椎体压缩风险——倾向 30-35 Gy/5fx 而非更高单次量
- 详见 `reirradiation-plan-recommend` Skill §五

### 3.3 Dose Considerations for ACC

- ACC is moderately radiosensitive. Cumulative doses of 60-66 Gy are generally required for microscopic residual disease.
- The cavernous sinus and skull base foramina can tolerate the prescribed doses (60 Gy at 2 Gy/fx is within tolerance of CN III, IV, V, VI).
- Special OAR attention: optic chiasm (Dmax ≤ 54 Gy), brainstem (Dmax ≤ 54 Gy), temporal lobe (Dmax ≤ 60 Gy).

---

## Section 4 — Site-Specific Contouring Guidelines

### 4.1 Parotid Gland ACC

| Component | Target |
|-----------|--------|
| **Tumor bed** | Parotid bed, including stylomastoid foramen if facial nerve was sacrificed |
| **Tier 1 (named nerve, e.g. auriculotemporal N.)** | Follow V3 → foramen ovale → **entire cavernous sinus** → 66 Gy to tumor bed, 60 Gy to cavernous sinus |
| **Tier 2 (small PNI only)** | Follow V3 pathway → to **inferior border of cavernous sinus** → 60 Gy |
| **Tier 3 (no PNI)** | Prophylactic along V3 to **skull base** → 54 Gy |
| **Neck nodes** | **No prophylactic neck RT** (unless solid type ACC) |

### 4.1B Parotid ACC — Facial Nerve (CN VII) Management

While ACC strongly favors sensory trigeminal branches over motor nerves, the facial nerve passes directly through the parotid gland and may show radiographic thickening on MRI. **Not all thickened facial nerves are tumor-involved.** The management of the facial nerve depends on the level of evidence for involvement, assessed across three domains:

| Evidence Level | Pathology | Symptoms | MRI |
|---------------|-----------|----------|-----|
| **Confirmed involvement** | Tumor in nerve on pathology | Facial palsy present | Nerve thickening on MRI |
| **Suspicious** | Not definitive | No palsy | Thickening present |

#### When facial nerve involvement IS confirmed (pathology + palsy + MRI)

The vertical (descending) segment of CN VII within the stylomastoid foramen must receive **high-dose irradiation (60-66 Gy)**:

```
Stylomastoid foramen
        │
        ▼
  Vertical segment (descending in temporal bone)
        │
        ├── Upper vertical segment (near stylomastoid foramen)
        │     → Surgically inaccessible — high risk of residual
        │     → **60-66 Gy radical dose**
        │
        └── Lower vertical segment
              → Include in high-dose CTV
```

**Rationale**: The upper vertical segment of CN VII lies within the bony stylomastoid canal immediately below the skull base. This area is extremely difficult to clear surgically during parotidectomy. Even with "nerve-sparing" techniques, microscopic tumor within the canal is likely.

#### When facial nerve involvement is NOT confirmed

| Segment | Action | Dose | Rationale |
|---------|--------|------|-----------|
| **Vertical segment (stylomastoid)** | **Prophylactic coverage** | 50-54 Gy | The proximal vertical segment is still a potential route but unconfirmed |
| **Horizontal (intratemporal) segment** | **DO NOT irradiate** | — | Irradiating the horizontal segment within the petrous temporal bone would significantly increase dose to the **cochlea and vestibular apparatus** → sensorineural hearing loss |

**Key distinction from V3 pathway**: The trigeminal pathway (V3 → foramen ovale → cavernous sinus) is the primary route of ACC perineural spread from the parotid. The facial nerve pathway (CN VII → stylomastoid foramen → internal acoustic meatus) is a secondary concern that requires rigorous evidence before escalating the CTV, because the cost of over-coverage is inner ear toxicity.

#### Contouring guidance —Stylomastoid vertical segment

| Boundary | Definition |
|----------|-----------|
| Entry point | Stylomastoid foramen (between styloid process and mastoid tip) |
| Course | Descends vertically approximately 10-15 mm within the temporal bone |
| CTV width | 5-8 mm around the nerve within the canal; 3-5 mm within the bony canal |
| OAR proximity | Cochlea lies anterior and medial — **verify cochlear Dmean ≤ 45 Gy** |

| **Neck nodes** | **No prophylactic neck RT** (unless solid type ACC) |

### 4.2 Submandibular / Sublingual Gland ACC

| Component | Target |
|-----------|--------|
| Primary → nerve | Lingual nerve (V3) → chorda tympani (CN VII, but follows V3 pathway to skull base) → foramen ovale |
| Neck nodes | **Prophylactic ipsilateral Ib + II** (at or below oral fissure) → 50-54 Gy |

### 4.3 Hard Palate / Palatal Minor Salivary Gland ACC

| Component | Target |
|-----------|--------|
| Primary → nerve | Greater and lesser palatine nerves → pterygopalatine fossa → V2 (maxillary division) → foramen rotundum → cavernous sinus |
| Neck nodes | **No prophylactic neck RT** (above oral fissure, unless solid type) |

### 4.4 Nasal Cavity / Paranasal Sinus ACC

| Component | Target |
|-----------|--------|
| Nerve pathways | Anterior ethmoidal nerve (V1) → cribriform plate; V2 via pterygopalatine fossa |
| Neck nodes | **No prophylactic neck RT** (unless solid type) |

---

## Section 5 — OAR Constraints Specific to ACC RT

Since ACC RT often extends to the skull base and cavernous sinus, special attention is required for:

| OAR | Constraint | Notes |
|-----|-----------|-------|
| **Optic chiasm** | Dmax ≤ 54 Gy | Close to cavernous sinus |
| **Brainstem** | Dmax ≤ 54 Gy | |
| **Temporal lobe** | Dmax ≤ 60 Gy | Especially for V2/V3 pathway coverage |
| **Pituitary/hypothalamus** | Dmean ≤ 45 Gy | Endocrine function |
| **Cochlea** | Dmean ≤ 45 Gy | |
| **Lacrimal gland** | Dmean ≤ 30 Gy | V1 pathway proximity |

## Section 5.5 — Sinonasal ACC: A Distinct Entity

> 鼻腔鼻窦 ACC 不同于唾液腺 ACC——实体型占比更高、PNI 通路更复杂、手术更难 R0。朱奕 104 例临床分析（复旦大学附属眼耳鼻喉科医院，中国癌症杂志 2016）。

| 特征 | 唾液腺 ACC | 鼻腔鼻窦 ACC |
|------|----------|------------|
| **实体型占比** | 较低 | 🔥 **更高**→侵袭性更强 |
| **PNI 通路** | V3（腮腺）、V2（腭部） | 🔥 **V2+V3+翼管神经**——翼腭窝是关键结构 |
| **手术** | 腮腺切除±面神经 | 🔥 **内镜手术复发率可能低于开放**（17.8% vs 38.5%，Meccariello 2016） |
| **切缘阳性** | 影响预后 | ⚠️ 九院数据——对 OS/DFS 无显著影响（跳跃性 PNI 是原因）→更强调 PORT |
| **颈部** | 实体型+口裂以下才照 | ⚠️ 不常规做颈清扫（LN 转移不常见），但中晚期/鼻咽侵犯/分化差时需讨论 |
| **剂量** | 60-66 Gy（术后） | 同——多处切缘阳性/软组织受侵→**66 Gy** |
| **化疗** | 无标准方案 | ⚠️ **CAP 方案**（顺铂+多柔比星+环磷酰胺）→晚期/复发/转移 |

> **参考**：朱奕, 等. 104例鼻腔鼻窦腺样囊性癌临床分析. 中国癌症杂志 2016;26(03):268-275.

### Section 5.6 — CAP Chemotherapy for Advanced ACC

| 方案 | 剂量 |
|------|------|
| **CAP** | 顺铂 50-80 mg/m² d1 + 多柔比星 40-60 mg/m² d1 + 环磷酰胺 400-600 mg/m² d1，q3-4w |
| **适应证** | 快速生长、症状明显、不可切除、复发、远处转移的 ACC |
| **同步 CRT** | 术后同步 CRT 可能提高局控率——但缺乏大样本 RCT |

---

## Section 6 — Key References

1. Jiang W, Xiao Y, Hu H, Li J, He Y, Han N, et al. Postoperative Intensity-Modulated radiotherapy with trigeminal nerve pathway delineation for head and neck adenoid cystic carcinoma. *Radiotherapy & Oncology*. 2025;200:111174. PMID: 41027510. DOI: 10.1016/j.radonc.2025.111174.
2. 朱国培, 等. 头颈部腺样囊性癌术后放疗靶区勾画研究. *中华放射肿瘤学杂志*. 2025;34(1):49-56.
3. ICRU Report 83: Prescribing, Recording, and Reporting Photon-Beam Intensity-Modulated Radiation Therapy (IMRT). 2010.
4. Gregoire V, et al. Delineation of the neck node levels for head and neck tumors. *Radiother Oncol*. 2014;110(1):172-181.
5. Lee NY, et al. OAR dose constraints for head and neck RT. *Int J Radiat Oncol Biol Phys*. 2018.
6. Garden AS, et al. Outcomes and patterns of care for adenoid cystic carcinoma of the head and neck. *Int J Radiat Oncol Biol Phys*. 2015.

---

## Section 7 — Future Directions & GitHub Repository

This skill is maintained as part of the Hermes Agent skills ecosystem, designed for clinical reference by radiation oncology residents and practitioners. Contributions are welcome to:

- Add site-specific nuances for rare ACC primary sites
- Refine the three-tier neural pathway coverage system with outcome data
- Incorporate emerging evidence on particle therapy (proton/carbon ion) for skull base ACC
- Develop automated scripting tools for nerve pathway contouring

**GitHub Repository**: https://github.com/NousResearch/hermes-agent (this skill is distributed under the `head-neck-target-delineation` skill family)

**To contribute**: Open a pull request or file an issue on the GitHub repository.

**Contact**: Zhu Guopei, MD — Department of Radiation Oncology, Shanghai Ninth People's Hospital, Shanghai Jiao Tong University School of Medicine. Email: antica@gmail.com

---

*This clinical framework was developed through the clinical experience and published research of the


---

## 附：靶区规划摘要（可复制粘贴入首次病程录）

> 治疗前写入住院病史"诊疗计划"。只列实际使用的 CTV 层级，每层附理由。豁免区和加量区均说明原因。

```
═══════════════════════════════
  放疗靶区规划
═══════════════════════════════
诊断：______  pT__N__M__（AJCC 第 9 版）
分期判断：______（为何 T__ 而非 T__：______）
手术：______
PORT 指征：______
降级依据：______（如适用）

方案：□ 术后 PORT  □ 根治性 RT   ___ Gy / ___ fx

CTV___：______（___ Gy — 理由：______）
加量：______  ___ Gy（理由：□R1/R2  □ENE+  □手术不易切净  □T4/N3 临近关键结构）
豁免：______（理由：______）

主治：______  日期：______
═══════════════════════════════

注：四类加量指征：①R1/R2切缘 ②ENE+淋巴结 ③手术不易切净区(茎乳孔/腮腺深叶/颅底/翼腭窝/颏结节/前上门牙-鼻底硬腭) ④不手术T4/T4b临近颅底/脑膜/眼眶/颈动脉。病理切缘阴性不等于肿瘤床绝对安全——手术记录中未描述但肿瘤曾临近上述区域时仍需考虑加量。
