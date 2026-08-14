---
name: orbital-lymphoma-rt-targets
description: "眼淋巴瘤/眼眶MALT放疗靶区，4Gy2fx超低剂量。Use when 眼眶淋巴瘤/MALT/DLBCL。"
version: 1.0.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [head-neck, radiotherapy, orbital, lymphoma, MALT, DLBCL, eye, 4Gy/2fx]
    triggers_on: [眼眶淋巴瘤, 眼MALT, 眼淋巴瘤, 结膜淋巴瘤, 眶内淋巴瘤, 泪腺淋巴瘤, 4Gy/2fx, orbital lymphoma, ocular lymphoma, MALT, DLBCL, follicular lymphoma, 眼附属器淋巴瘤]
    related_skills: [orbital-tumor-rt-targets, head-neck-lymphoma-rt-targets]
    split_from: orbital-tumor-rt-targets
---

> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗中心原创知识产权。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.

# 眼眶淋巴瘤放疗靶区勾画

> 本模块从 `orbital-tumor-rt-targets` 拆出（2026-08-14）——淋巴瘤与实体瘤的靶区逻辑、剂量、治疗模式完全不同，独立成模块避免相互干扰。实体瘤（ACC/肉瘤/脑膜瘤/黑色素瘤等）见 `orbital-tumor-rt-targets`。

## 🔴 铁律（出报告前逐条核验）

| # | 铁律 | 触发条件 |
|:--:|------|---------|
| 1 | **术语精确**：眼前庭≠眼前节，泪腺≠泪膜 | 所有眼眶 RT |
| 2 | **4 Gy/2fx 超低剂量**：MALT 标准选项；对侧眼可同时照 | 眼眶 MALT 淋巴瘤 |
| 3 | **眶尖策略**：结膜局限 MALT 可不照眶尖；弥漫/深部病变照眶尖 | 按病变范围 |
| 4 | **眼科共管强制**：角膜+结膜+泪膜+眼睑全程共管 | 所有眼眶 RT |

## Overview

Orbital lymphoma is the most common orbital malignancy (MALT, DLBCL, follicular). Unlike solid orbital tumors, lymphoma is treated as a systemic disease with RT as local consolidative treatment — the target logic, doses, and fractionation differ fundamentally from orbital solid tumors.

**Key distinction**: Lymphoma RT is local consolidative — **nodal RT is not routinely indicated** (lymphoma is already systemic).

## 一、CTV 勾画——按病变范围

| Extent | CTV Definition | Notes |
|--------|---------------|-------|
| **Unilateral orbital involvement (IE)** | **CTV = entire ipsilateral bony orbital cavity** | Standard approach. Includes retrobulbar fat, extraocular muscles, lacrimal gland. Globe can be excluded if not involved. |
| **Bilateral orbital involvement** | CTV = bilateral bony orbital cavities | Requires independent lens sparing for each side |
| **Conjunctival-limited MALT** | CTV = conjunctival sac + anterior 1/3 of orbit | Can spare posterior orbit, optic nerve, and lacrimal gland — significant toxicity reduction |
| **Lacrimal gland primary** | CTV = lacrimal gland fossa + adjacent orbit (individualized) | Must include the entire gland; if extraorbital extension, expand accordingly |

**PTV expansion**: 3-5 mm isotropic (3 mm with daily IGRT; 5 mm without). Recommend thermoplastic mask + bite-block immobilization.

## 二、剂量与分割

| Histology | Standard Dose | Ultra-Low Dose Option | Notes |
|-----------|-------------|----------------------|-------|
| **MALT (indolent)** | 24-25.2 Gy / 12-14 fx | **4 Gy / 2 fx (2 Gy × 2, ≥48h apart)** | NCCN-endorsed ultra-low dose option; local control ~93% |
| **MALT (ultra-low → recurrence)** | — | Re-treat 4 Gy/2fx or escalate to 24 Gy | Cumulative OAR must remain within tolerance |
| **Follicular lymphoma** | 24-30 Gy / 12-15 fx | 4 Gy/2fx (emerging, less robust than MALT) | Limited evidence; use with caution |
| **DLBCL (post-chemo consolidation)** | 30-36 Gy / 15-18 fx | N/A | PET-adapted: Deauville 1-2 → 24-30 Gy sufficient |
| **DLBCL (definitive / bridging to CAR-T)** | 30-40 Gy / 15-20 fx | N/A | Bridging RT → CAR-T: 1.5 Gy BID × 10d (=30 Gy) if 2-week window |
| **Mantle cell lymphoma** | 30-36 Gy / 15-18 fx | N/A | |

**4 Gy/2fx 技术要点**:
- IMRT/VMAT still recommended despite low dose — lens/cornea/lacrimal gland receive 2 Gy vs 0 Gy matters
- Verify low-MU segment delivery accuracy on linac
- Point dose verification with ion chamber or diode recommended

## 三、OAR 约束（眼眶共管部分，详见 orbital-tumor-rt-targets §4）

| OAR | Conventional (1.8-2.0 Gy/fx) | Priority |
|-----|------------------------------|----------|
| **Lens** | Dmax < 4-5 Gy | 🔴 Critical |
| **Optic nerve / chiasm** | Dmax < 55 Gy (preferred), < 60 Gy (absolute max) | 🔴 Critical |
| **Cornea** | Dmax < 30 Gy, Dmean < 20 Gy | 🟡 Important |
| **Lacrimal gland** | Dmean < 25 Gy | 🟡 Important |

## 四、淋巴结处理

| Scenario | Nodal RT Recommendation |
|----------|------------------------|
| Orbital lymphoma | Lymphoma is systemic; RT is local consolidative — **nodal RT not routinely indicated** |

## 五、桥接/新辅助场景

| Scenario | Strategy |
|----------|----------|
| **Orbital lymphoma (DLBCL)** | R-CHOP, polatuzumab, CAR-T bridging — Standard of care; RT is consolidative after chemo |

## 参考文献

1. NCCN Guidelines: B-Cell Lymphomas (Orbital MALT/DLBCL). Version 3.2026.
2. ILROG Guidelines: Radiation Therapy for Orbital Lymphoma. *Int J Radiat Oncol Biol Phys*. 2021.
3. Pinnix CC, et al. Response-Adapted Ultralow-Dose Radiation Therapy for Orbital Indolent B-Cell Lymphoma: A Phase 2 Nonrandomized Controlled Trial. *JAMA Oncol*. 2024. PMID:38990564.
4. Yahalom J, et al. An International Lymphoma Radiation Oncology Group Study of RT for Bilateral Indolent Orbital Adnexal Lymphomas. *Int J Radiat Oncol Biol Phys*. 2025. PMID:40090468.
5. Chelius M, et al. The Role of Radiotherapy in Indolent Ocular Adnexal and Orbital Lymphomas. *Head Neck*. 2025. PMID:39487567.
6. Fasola CE, et al. Low-dose radiation therapy (2 Gy × 2) in orbital lymphoma. *Int J Radiat Oncol Biol Phys*. 2013;86(5):930-935.
7. 中国眼及附属器肿瘤放射治疗指南（2021版）. 陆雪官等. 中国医师协会放疗专委会.

> ⚠️ **免责声明**：本方案由 AI 辅助生成，最终临床决策由经治医师负责。
