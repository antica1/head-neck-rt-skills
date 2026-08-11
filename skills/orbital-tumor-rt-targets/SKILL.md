---
name: orbital-tumor-rt-targets
description: "眼眶肿瘤放疗靶区勾画——间室放疗(门+隔壁比喻)、眼前庭共管。Orbital RT — compartment irradiation, lacrimal apparatus, orbital apex."
version: 1.0.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [head-neck, radiotherapy, orbital, eye, lymphoma, SBRT]
    triggers_on: [眼眶, 眶内, 眼肿瘤, 眼MALT, 眼淋巴瘤, 泪腺, 视神经, 眼黑色素瘤, 睑板腺癌, 视网膜母细胞瘤, 葡萄膜, 4Gy/2fx, 眼前庭, 间室放疗, 眶尖, 眼球, 角膜, 结膜, 泪囊, 鼻泪管, orbital, lacrimal, uveal, retinoblastoma, MALT, 眼眶放疗, 眼眶靶区, 眼眶靶区勾画]
    related_skills: [adenoid-cystic-carcinoma-rt-targets, reirradiation-plan-recommend, npc-rt-target-delineation, head-neck-dvh-plan-review]

---

> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗中心原创知识产权。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.

# 眼眶肿瘤放疗靶区勾画指南

## 🔴 铁律清单（出报告前逐条核验）

> **模型注意力焦点——每条铁律都是"不照=复发或不可逆损伤"的硬规则。**

| # | 铁律 | 触发条件 |
|:--:|------|---------|
| 1 | **术语精确**：眼前庭≠眼前节，泪腺≠泪膜——禁用"前节""泪膜" | 所有眼眶 RT |
| 2 | **间室放疗**：照全受累解剖间室，非 mm 扩边 | 所有眼眶 RT |
| 3 | **门+隔壁**：眶尖=低级预防砌墙（50-54 Gy）；海绵窦=高级别根治（60-66 Gy） | 眶内恶性肿瘤 |
| 4 | **眶尖必照（视神经管+眶上裂）**：眼眶恶性肿瘤→眶尖必照；良性病变/结膜局限淋巴瘤→根据风险评估决定。完全不照眶尖仅在前部结膜局限 MALT 淋巴瘤和 Graves 眼病时可接受。 | 所有眼眶 RT |
| 5 | **VIII→IX→IIa 级联**：眶外侵犯→同侧腮腺/面动脉旁/上颈深链预防 | 眶外扩展 |
| 6 | **骨受侵→66 Gy**：手术无骨切→骨切缘假定阳性。全层骨+5mm外放 | 影像/术中发现骨侵犯 |
| 7 | **脑膜邻近→宁宽勿窄**：眶顶/眶尖/蝶骨嵴→硬膜在 CTV 内。此处复发不可补救 | 高位/后位肿瘤 |
| 8 | **眼前庭共管强制**：角膜+结膜+泪膜+眼睑——放疗全程眼科共管 | 所有眼眶 RT |
| 9 | **骨受侵→不用 SBRT**：骨-软组织界面的 SBRT 剂量分布不可预测 | 骨侵犯 |
| 10 | **鼻泪管全径**：泪囊→鼻泪管→下鼻道，三平面（矢+冠+轴）追踪 | 泪囊/内眦肿瘤 |
| 11 | **4 Gy/2fx 超低剂量**：MALT 标准选项；对侧眼可同时照 | 眼眶 MALT 淋巴瘤 |
| 12 | **眼科共管时间表**：基线→每周→1月→3月→6月→每年×8年 | 所有眼眶 RT |

> ⚠️ 以上铁律即使正文未逐条提及也自动适用。靶区描述必须与铁律完全一致——铁律优先于模型"自由裁量"。

---

## Overview

The orbit is the most OAR-dense anatomical region in radiation oncology. Within ~30 cm³, a single IMRT plan must simultaneously protect the lens, cornea, retina, optic nerve, lacrimal gland, and extraocular muscles — while delivering curative or consolidative doses to the tumor. This skill codifies the target delineation principles and dose constraints for the three major categories of orbital radiotherapy:

1. **Orbital lymphoma** — the most common indication (MALT, DLBCL, follicular)
2. **Orbital solid malignancies** — ACC, sarcoma, meningioma, metastases
3. **Benign/semi-benign entities** — schwannoma, pseudotumor, Graves' orbitopathy

Based on clinical practice at Shanghai Ninth People's Hospital and published evidence (QUANTEC, TG-101, NCCN, ILROG).

---

## Section 0 — Intraocular vs. Orbital vs. Extraorbital: A Critical Distinction

### 0.1 Three Compartments, Three Different Biologies

Ocular tumors are not a single entity. The compartment of origin fundamentally determines the risk of regional lymphatic spread:

| Compartment | Examples | Lymphatic Drainage | Nodal Risk |
|------------|----------|-------------------|-----------|
| **Intraocular** (globe-confined) | Uveal melanoma, retinoblastoma | **None** — the globe has no intrinsic lymphatics | **Near zero** unless transscleral extension |
| **Orbital** (confined to bony orbit) | Orbital lymphoma, ACC, meningioma | Minimal within the orbit itself | **Low** (except lymphoma which is already a systemic disease) |
| **Extraorbital** (beyond bony orbit into eyelid, conjunctiva, periorbital skin, sinuses) | Advanced ACC, SCC, melanoma with eyelid/skin involvement | **Rich** — eyelid skin, conjunctiva, and periorbital soft tissues drain to regional nodes | **Significant** for moderate-to-high-grade malignancies |

**Bottom line**: An intraocular melanoma confined to the globe does not need nodal evaluation. But a lacrimal gland ACC extending through the orbital septum into the eyelid — that is a fundamentally different disease that demands nodal assessment.

### 0.2 The Orbital → Extraorbital Lymphatic Cascade

When a malignant orbital tumor breaches the bony confines and invades extraorbital structures (eyelid skin, conjunctival surface, periorbital soft tissues, lacrimal drainage apparatus), it gains access to the regional lymphatic network. The first-echelon nodes follow a predictable sequence:

```
Extraorbital extension
        │
        ▼
First-echelon nodes:
  ├── Level VIII (superficial parotid / preauricular nodes)
  │     — Drains lateral eyelid, lateral canthus, conjunctiva
  │     — Often the FIRST clinically detectable node
  │
  └── Level IX (peri-facial artery / buccal nodes)
        — Drains medial eyelid, medial canthus, lacrimal sac
        — Along the facial artery near the mandibular margin
        │
        ▼
Second-echelon:
  └── Level IIa (upper deep jugular chain)
        — The common downstream station for both VIII and IX
```

### 0.3 Why Ophthalmologists Miss These Nodes

The Level VIII and IX nodal basins are NOT routinely examined in standard ophthalmic follow-up:

- **Level VIII** (parotid region) — hidden behind the parotid fascia; palpable only when significantly enlarged
- **Level IX** (peri-facial artery) — lies along the mandibular margin near the facial artery pulsation, easily mistaken for a prominent vessel or submandibular gland
- Standard ophthalmic examination focuses on the globe, orbit, and visual function — not the periparotid or submandibular regions
- Radiological follow-up (orbital MRI) often stops at the orbital apex and does not extend inferiorly enough to cover IIa

**Clinical consequence**: By the time a Level IIa node becomes clinically apparent, the patient may have already progressed through VIII/IX silently.

### 0.4 When to Include Nodal Irradiation

| Scenario | Nodal RT Recommendation |
|----------|------------------------|
| Intraocular tumor, no extraorbital extension | **No nodal evaluation or RT needed** |
| Orbital lymphoma | Lymphoma is systemic; RT is local consolidative — nodal RT not routinely indicated |
| Orbital ACC, sarcoma, or SCC **confined to bony orbit** | No prophylactic nodal RT (orbit lacks lymphatics) |
| Orbital malignant tumor **with extraorbital extension** (eyelid, skin, conjunctival surface) AND moderate-to-high grade | **Consider ipsilateral Level VIII + IX + IIa inclusion in CTV** |
| Known VIII/IX/IIa nodal involvement | Full ipsilateral neck evaluation ± RT (as per primary pathology) |

### 0.5 Practical Contouring Guidance for Nodal Coverage

When nodal RT is indicated for extraorbital extension:

```
Include in ipsilateral CTV-N:

Level VIII: Superficial parotid region
  └── From zygomatic arch superiorly to angle of mandible inferiorly
      Anterior to the tragus, extending to the parotid tail

Level IX: Peri-facial artery nodes
  └── Along the facial artery, from mandibular margin down 2-3 cm
      At the anterior border of the masseter muscle

Level IIa: Upper deep jugular chain
  └── Standard Robbins IIa boundaries (see neck node atlas)
```

**Dose**: 50-54 Gy / 30 fx (prophylactic); escalate to 60-66 Gy if known involvement.

### 0.6 Two Perspectives on Orbital Invasion — See Companion Document

The assessment of orbital invasion severity differs fundamentally between specialties:

| Specialty | Question | Staging |
|-----------|---------|---------|
| **Ophthalmology** | Has the intraocular tumor breached the sclera? How far? | AJCC Uveal Melanoma T1-T4 |
| **ENT / Maxillofacial Surgery** | Has the sinonasal tumor penetrated through orbital walls into orbital fat and muscles? Can we save the eye? | Sinonasal Orbital Invasion Grade I-IV |

> **Full comparison document**: `眼眶侵犯程度分期_眼科vs五官科双视角.md` — includes AJCC T-staging, Grade I-IV criteria, MRI findings, eye preservation decision tree, and RT target implications for each grade.

---

## Section 1 — Orbital Anatomy and OAR Atlas

### 1.1 Bony Orbit Boundaries

| Wall | Bones | Key Foramina |
|------|-------|-------------|
| **Roof** | Frontal bone, lesser wing of sphenoid | Supraorbital notch |
| **Floor** | Maxilla, zygomatic, palatine | Infraorbital groove → canal |
| **Medial wall** | Ethmoid, lacrimal, maxilla, sphenoid | Anterior/posterior ethmoidal foramina |
| **Lateral wall** | Zygomatic, greater wing of sphenoid | — |
| **Apex** | Lesser wing, body of sphenoid | **Optic canal, superior orbital fissure** |

### 1.2 OAR Contouring Requirements

| OAR | Must Contour? | Key Plane | Tips |
|-----|--------------|-----------|------|
| **Lens (bilateral)** | ✅ Always | Axial + sagittal | ~9 mm diameter biconvex structure; easily identified on CT |
| **Cornea** | ✅ **Always** (add proactively) | Axial anterior orbit | Most TPS OAR lists omit cornea — add manually |
| **Retina (bilateral)** | ✅ Always | Axial | Posterior 2/3 of globe wall; include macula as substructure if feasible |
| **Optic nerve (bilateral)** | ✅ Always | Axial + coronal + sagittal | Must be continuous from globe to chiasm; ≤3 mm slice thickness |
| **Optic chiasm** | ✅ Always | Coronal + sagittal | Junction anterior to pituitary stalk |
| **Lacrimal gland** | ✅ Always | Axial + coronal | Superolateral orbit; ~20×12×5 mm |
| **Lens (contralateral)** | ✅ Always | — | Even when treating ipsilateral only |
| **Extraocular muscles** | Recommended | Axial + coronal | Superior/inferior/medial/lateral rectus + superior oblique |
| **Brainstem** | ✅ If target near apex | Axial + sagittal | |

### 1.3 MRI Fusion Requirement

| Tumor Type | MRI Sequences |
|-----------|---------------|
| Lymphoma (any) | T1+C fat-suppressed (for soft tissue extent) |
| ACC / solid malignancy | T1+C fat-suppressed + T2/STIR (perineural spread) |
| Meningioma | T1+C fat-suppressed + FIESTA/CISS (dural tail) |
| Optic nerve glioma | T2/STIR + T1+C (nerve thickening) |

---

## Section 2 — Target Volume Delineation by Tumor Type

### 2.1 Orbital Lymphoma — CTV

| Extent | CTV Definition | Notes |
|--------|---------------|-------|
| **Unilateral orbital involvement (IE)** | **CTV = entire ipsilateral bony orbital cavity** | Standard approach. Includes retrobulbar fat, extraocular muscles, lacrimal gland. Globe can be excluded if not involved. |
| **Bilateral orbital involvement** | CTV = bilateral bony orbital cavities | Requires independent lens sparing for each side |
| **Conjunctival-limited MALT** | CTV = conjunctival sac + anterior 1/3 of orbit | Can spare posterior orbit, optic nerve, and lacrimal gland — significant toxicity reduction |
| **Lacrimal gland primary** | CTV = lacrimal gland fossa + adjacent orbit (individualized) | Must include the entire gland; if extraorbital extension, expand accordingly |

**PTV expansion**: 3-5 mm isotropic (3 mm with daily IGRT; 5 mm without). Recommend thermoplastic mask + bite-block immobilization.

### 2.2 Orbital Solid Tumors — CTV

| Tumor Type | GTV → CTV Expansion | Special Considerations |
|-----------|---------------------|----------------------|
| **ACC (post-op)** | GTV-TB + 10-15 mm (along nerve pathways if PNI+) + 5-8 mm elsewhere | Follow V1/V2 branches to cavernous sinus if PNI present (see ACC skill) |
| **Meningioma (definitive/post-op)** | GTV + 5-10 mm (bone invasion → include hyperostotic bone) | Include dural tail if present on MRI |
| **Sarcoma (post-op)** | GTV-TB + 15-20 mm (wide microscopic spread) | Post-operative CTV must include all surgical planes |
| **Orbital invasion from NPC/sinonasal** | GTV + 5-10 mm | Often requires combined orbit + primary site plan |

**PTV expansion**: 3 mm (daily IGRT, thermoplastic mask + bite-block).

---

## Section 2.5 — Neoadjuvant Strategies for Eye Preservation

### 2.5.1 The Paradigm: Preoperative Debulking

When a malignant orbital tumor threatens the eye — either by direct invasion of critical structures (optic nerve, extraocular muscles, orbital apex) or by making R0 resection incompatible with globe preservation — the traditional choice is orbital exenteration. Neoadjuvant therapy offers a third path: **shrink the tumor preoperatively to convert an eye-sacrificing scenario into an eye-sparing R0 resection**.

```
Candidate for exenteration
        │
        ▼
  ┌─ Tumor is drug-sensitive?
  │
  ├─ YES → Neoadjuvant systemic therapy
  │         (chemotherapy, targeted therapy, immunotherapy)
  │         → Tumor regression
  │         → Eye-sparing R0 resection
  │         → Post-op RT as indicated
  │
  └─ NO (no effective systemic agent)
        │
        ▼
  ┌─ Neoadjuvant short-course SBRT / hypofractionated RT
  │    → 25-35 Gy in 5 fractions (within OAR tolerance)
  │    → 2-6 week surgical window
  │    → Tumor regression
  │    → Eye-sparing R0 resection
  │    → Post-op RT boost if needed (cumulative dose accounting)
  │
  └─ If BOTH systemic + RT are ineffective
       → Exenteration (no other option)
```

### 2.5.2 Neoadjuvant Systemic Therapy — When the Tumor Has a Drug Target

| Tumor Type | Potential Sensitive Agent | Evidence |
|-----------|--------------------------|----------|
| **Orbital lymphoma (DLBCL)** | R-CHOP, polatuzumab, CAR-T bridging | Standard of care; RT is consolidative after chemo |
| **Rhabdomyosarcoma (pediatric)** | VAC/IVA chemotherapy | Standard; neoadjuvant chemo → eye-sparing surgery + RT |
| **Orbital melanoma (BRAF+)** | BRAF/MEK inhibitors (dabrafenib/trametinib) | Dramatic responses reported; neoadjuvant window |
| **NTRK-fusion sarcoma** | Larotrectinib / entrectinib | Exceptional responders |
| **ACC** | Currently no validated systemic neoadjuvant | Active research; clinical trials only |

**Radiation oncologist's role**: If the medical oncologist achieves a deep response but not a complete one, post-operative RT target volumes may be reduced — but the **pre-treatment GTV should still be referenced** for the CTV-TB.

### 2.5.3 Neoadjuvant Hypofractionated RT — When No Drug Is Available

| Parameter | Recommendation |
|-----------|---------------|
| **Indication** | Orbital malignancy with no effective systemic agent, where upfront surgery would require exenteration |
| **Dose / Fractionation** | 25-35 Gy in 5 fractions (SRT/SBRT) |
| **Alternative** | 30-40 Gy in 10-15 fractions (if OAR proximity demands more fractionation) |
| **Technique** | IMRT/VMAT (preferred) or proton therapy if available |
| **OAR constraints (5-fx SRT)** | Optic nerve D0.03cc < 23 Gy; lens Dmax < 2 Gy/fx; retina Dmax < 25 Gy |
| **Surgical window** | 2-6 weeks post-RT (peak tumor regression; before fibrosis sets in) |
| **Post-op RT** | May need boost to tumor bed if R1/R2; cumulative dose must be calculated from neoadjuvant RT plan |

Key technical points:
- **Dose accounting**: Use neoadjuvant DICOM RT Dose file for cumulative DVH
- **Response assessment**: Post-neoadjuvant MRI at 2-4 weeks; ≥30% volume reduction = meaningful response
- **Surgical timing**: 2-6 weeks (too early = inflammation; too late = fibrosis)
- **Pathology**: Treatment effect (fibrosis, necrosis) complicates margin assessment — coordinate with pathologist

### 2.5.4 Eye Preservation Decision Summary

| Scenario | Neoadjuvant Strategy | Expected Outcome |
|----------|---------------------|-----------------|
| Drug-sensitive tumor (lymphoma, RMS, BRAF+ melanoma) | Systemic therapy first | Eye preservation in 70-90% |
| Drug-insensitive, RT-sensitive (ACC, meningioma, sarcoma) | SBRT 25-35 Gy/5 fx → surgery | Eye preservation in 50-70% |
| Both drug- and RT-resistant | Exenteration | — |
| Low-grade, anatomically favorable | Upfront surgery | Eye preservation >90% |

---

## Section 2.6 — Bone Involvement and Meningeal Proximity: The Surgical-RT Gap

### 2.6.1 The Fundamental Problem: Ophthalmologists Don't Resect Bone

Orbital surgeons are trained to operate within the soft-tissue confines of the orbit. When a tumor involves or abuts the orbital bones — the roof (frontal bone), medial wall (ethmoid), floor (maxillary), lateral wall (zygomatic/sphenoid), or apex (sphenoid body) — the surgical approach differs fundamentally from that of a head-and-neck or skull-base surgeon:

| Surgical Specialty | Approach to Orbital Bone Involvement |
|-------------------|--------------------------------------|
| **Ophthalmologist / Orbital surgeon** | Preserves bone; may "scrape" or "curette" tumor off bone surface. Does NOT perform en-bloc bone resection. |
| **ENT / Maxillofacial surgeon** | May perform partial maxillectomy, ethmoidectomy, or orbital wall resection with margins. |
| **Neurosurgeon** | For orbital roof / sphenoid wing involvement; can perform craniotomy with bone resection. |

**The clinical consequence**: When an ophthalmologist describes "gross total resection" of an orbital tumor involving bone, the bone itself was almost certainly NOT resected. The periosteum may have been stripped, but microscopic tumor within Haversian canals, along the diploic space, or at the bony margin is likely left behind. This is NOT an R0 resection in the oncologic sense.

### 2.6.2 High-Risk Anatomical Zones for Inadequate Resection

| Zone | Bone(s) Involved | Adjacent Critical Structures | Why Surgery Is Incomplete |
|------|-----------------|---------------------------|--------------------------|
| **Orbital roof** | Frontal bone, lesser wing of sphenoid | **Dura mater** of anterior cranial fossa (1-2 mm above) | Stripping periosteum from the roof does NOT clear tumor from the diploic space; dura is immediately above |
| **Medial wall** | Ethmoid (lamina papyracea), lacrimal bone | Ethmoid air cells, cribriform plate | Bone is paper-thin; tumor easily penetrates into ethmoid sinuses |
| **Orbital apex** | Body of sphenoid, lesser wing | **Optic canal**, superior orbital fissure, cavernous sinus | The most surgically inaccessible region; even "maximal safe resection" leaves microscopic disease |
| **Lateral wall** | Greater wing of sphenoid, zygomatic | Temporal lobe dura (middle cranial fossa) | Bone involvement here means potential middle fossa extension |
| **Floor** | Maxillary orbital plate | Maxillary sinus mucosa | Roof of maxillary sinus; stripped periosteum ≠ clear margin |

### 2.6.3 RT Implications of Bone Involvement

When pre-operative imaging or surgical findings suggest bone involvement, the following adjustments to the RT plan are mandatory:

#### CTV Expansion

| Situation | Recommendation |
|-----------|---------------|
| Tumor abutted bone periosteum (no gross erosion) | CTV includes the **full thickness** of the involved bone segment + **5 mm beyond** the radiologically involved area |
| Tumor eroded through bone (gross bone destruction on CT) | CTV includes the entire affected bone + **adjacent bone segment** (e.g., if lamina papyracea eroded → include entire ipsilateral ethmoid complex) |
| Bone involvement at the orbital apex | CTV must include the optic canal, superior orbital fissure, and the bony margins of these foramina |
| Roof involvement → proximity to dura | If roof erosion present → **discuss with neurosurgeon** whether the dura should be included in CTV or managed surgically first |

#### Dose Prescription

| Bone Involvement | Minimum Dose | Rationale |
|-----------------|-------------|-----------|
| Periosteal abutment only (no erosion) | 60 Gy / 30 fx | Microscopic residual in bone surface |
| Gross bone erosion, likely R1/R2 | **66 Gy / 33 fx** | Bone invasion = R1/R2 equivalent |
| Orbital apex with bone involvement | 66 Gy / 33 fx | Highest risk of local failure |

#### Meningeal Proximity

When the orbital roof or lateral wall is involved, the dura is millimeters away:

| Scenario | Action |
|----------|--------|
| No radiographic dural enhancement | CTV includes bony roof/lateral wall + 3 mm toward dura; dura NOT in CTV but receives dose due to proximity |
| Dural enhancement / thickening on MRI | **Dura must be included in CTV**; discuss craniotomy + dura resection/repair before RT |
| Leptomeningeal enhancement (rare) | Palliative intent; whole-brain considerations apply |

### 2.6.4 The "No Saw, No R0" Rule

> **If the operative report does not describe a bone cut (osteotomy, craniotomy, maxillectomy), assume the bone margin is microscopically positive.**

This clinical rule has direct RT consequences:
- Bone-involved region → **PTV-66** (not PTV-60)
- CTV covers the **entire bone segment** (not just the soft tissue interface)
- Adjacent bony structures that could serve as tumor conduits (e.g., pterygopalatine fossa for V2 pathway tumors) should be included
- Single-fraction or hypofractionated SBRT should NOT be used for bone-involved orbital tumors — the bone/soft-tissue interface has unpredictable dose distribution with very high doses per fraction

### 2.6.5 The "Better Too Wide Than Too Narrow" Principle for Meningeal-Adjacent Tumors

For orbital tumors abutting or involving the skull base, dura, or cavernous sinus — **there is no salvage option if RT fails at the margin**.

> **Rule**: When a tumor approaches or involves the meninges, **err on the side of a larger, more generous CTV**. A marginal recurrence in the orbital apex, cavernous sinus, or dura is almost always fatal — surgery is impossible, re-irradiation is constrained by prior OAR doses, and systemic therapy rarely controls gross disease in these locations.

This contrasts with most other head-and-neck sites where a marginal recurrence can be surgically salvaged:

| Site | Marginal Recurrence Salvageability |
|------|-----------------------------------|
| Oral cavity, oropharynx, larynx | Salvage surgery often possible |
| Neck recurrence after RT | Salvage neck dissection often possible |
| **Orbital apex / cavernous sinus / dura** | **Essentially unsalvageable** — no surgical corridor, OAR limits preclude re-RT |

**Practical application**:

| When in doubt about... | Action |
|------------------------|--------|
| Whether a bony foramen should be in CTV | **Include it** — the consequence of missing it is far worse than the consequence of including it |
| Whether the dura should be covered | If any radiographic suspicion → **cover it** |
| Whether to extend CTV to the next anatomical barrier | **Extend it** — stop at the next logical barrier (contralateral cavernous sinus wall, cribriform plate, pituitary stalk), not at an arbitrary margin |
| Whether 60 Gy or 66 Gy | If bone involved → **66 Gy** |
| Whether to "trim" the PTV to spare a critical OAR | ONLY if the OAR dose would be absolutely prohibitive (brainstem Dmax > 54 Gy, optic chiasm Dmax > 55 Gy). Otherwise, slight OAR constraint violations are preferable to a marginal miss. |

**Clinical corollary**: The most common cause of treatment failure in orbital/skull-base tumors is NOT inadequate dose to the GTV — it is **inadequate CTV coverage of the true microscopic extent**. The tumor has already demonstrated its ability to track along nerves, through bone, and along dura. Your CTV must respect this biology.

**Application to orbital apex**: This principle applies regardless of tumor grade. Even low-grade tumors near the orbital apex warrant prophylactic coverage of the apex (optic canal + superior orbital fissure) at elective dose (50-54 Gy). Complete omission of the apex is never safe — the superior orbital fissure is a direct conduit to the cavernous sinus, and a microscopic skip metastasis here is unsalvageable regardless of histology. The key difference between high-grade and low-grade is **dose**, not coverage:
- High-grade: full apex + ipsilateral cavernous sinus at radical dose (60-66 Gy)
- Low-grade: apex at elective dose (50-54 Gy), cavernous sinus NOT routinely included

---

## Section 2.6.6 — Two Philosophies of Prophylactic Irradiation: Distance vs. Compartment

### The Distance Principle (Standard HN Approach)

For tumors treated definitively with RT — most notably nasopharyngeal carcinoma — the prophylactic CTV follows a **distance gradient**:

> "The closer to GTV, the more aggressively covered. The farther away, the safer it is to omit."

This is the standard "GTV + 5-10 mm → CTV → PTV" logic. Risk decays with distance from the known tumor. If the tumor is 20 mm from a structure, the probability of microscopic involvement is negligible. This approach works for mucosal surfaces where microscopic spread follows predictable radial patterns and salvage surgery remains possible at most sites.

### The Compartment Principle (Skull Base / Orbit / Post-Op Approach)

For skull base and orbital tumors — **especially after incomplete surgery** — a fundamentally different logic applies:

> "Once a tumor has invaded an anatomical compartment, the **entire compartment** — and the door to the next one — must be irradiated."

This is **compartment-based irradiation** (间室放疗), not distance-based. The rationale:

| Principle | Rationale |
|-----------|----------|
| **Anatomical compartments are natural barriers** | The orbital apex is a compartment. The cavernous sinus is a compartment. The superior orbital fissure is the door between them. |
| **Surgery disrupts compartments** | Post-operative planes are NOT the same as pre-operative anatomy. Tumor cells may be displaced, seeded, or tracked along surgical corridors — distance-based logic fails in this setting. |
| **Skip metastases follow anatomical highways** | Perineural spread, dural tracking, and fascial plane migration don't respect millimeter-based margins — they follow pre-existing anatomical pathways. |
| **Salvage is impossible** | A recurrence at the superior orbital fissure or cavernous sinus has no surgical option and re-RT is constrained by prior dose. The stakes are absolute. |

### Practical Application: The "Door and Next Room" Analogy

```
ORBIT (known involvement)
    │
    ├── The "door": SUPERIOR ORBITAL FISSURE / OPTIC CANAL
    │     │
    │     └── Low-grade: Irradiate the door (50-54 Gy elective)
    │         → BLOCK the path → prevent tumor from crossing
    │
    └── The "next room": CAVERNOUS SINUS
          │
          └── High-grade: The door has likely been breached
              → Irradiate the next room too (60-66 Gy radical)
              → Treat cavernous sinus as a high-risk compartment
```

**Why low-grade still needs the door**: The low-grade tumor hasn't *probably* crossed into the cavernous sinus, but the orbital apex itself is only millimeters away from the superior orbital fissure. Irradiating the apex (the "door") at elective dose creates a firewall — even if a few cells have reached the fissure, 50-54 Gy is likely sufficient to sterilize them. You're not treating a known involvement; you're building a biological barrier.

**Why high-grade needs the next room**: The high-grade tumor has a statistically meaningful probability of already being in the cavernous sinus — tracking along V1/V2 branches, along dural reflections, or via direct extension through the fissure. By the time you see it on MRI, it's already too late. Therefore, the cavernous sinus must be irradiated as a high-risk compartment, not as a distant elective region.

### Comparison Table

| | Distance Principle | Compartment Principle |
|---|---|---|
| **Typical tumors** | NPC, OPC, larynx (definitive RT) | Skull base, orbit, post-op residual |
| **CTV logic** | GTV + N mm margin | Entire involved compartment(s) |
| **Prophylaxis basis** | Distance from GTV | Anatomical continuity |
| **Salvageability** | Usually salvageable | Usually unsalvageable |
| **Risk of under-coverage** | Marginal recurrence → salvage surgery | Marginal recurrence → death |
| **Consequence of over-coverage** | Increased toxicity | Managed OAR toxicity |
| **Decision rule** | "How far from GTV is safe?" | "Which compartment does this anatomy belong to?" |

---

## Section 2.7 — Three-Plane Contouring: Why Axial Alone Is Dangerous for the Orbit

### 2.7.1 The Problem: The Orbit Is a Horizontal Cone, Not a Sphere

The bony orbit is shaped like a horizontally oriented cone — narrow at the apex, wide at the anterior opening, with a curved roof, a sloping floor, and walls of dramatically different thickness. Contouring on axial slices alone systematically misses disease in three dimensions:

| Missed on Axial Alone | Why | Which Plane Catches It |
|----------------------|-----|----------------------|
| Tumor extension to the orbital roof / frontal sinus | Axial slices run parallel to the roof | **Sagittal** — shows the roof curvature and frontal sinus relationship |
| Tumor extension through the orbital floor into the maxillary sinus | Axial slices run parallel to the floor | **Sagittal + Coronal** — shows the floor slope and maxillary sinus interface |
| Full extent of the orbital apex, optic canal, superior orbital fissure | Axial may show partial foramina but misses the cranial entry | **Sagittal** — shows the complete apex-to-cranium trajectory |
| Infraorbital canal/foramen enlargement → anterior cheek extension | Axial may miss the vertical component | **Coronal** — shows the infraorbital canal in cross-section |
| Medial wall → ethmoid sinus extension | Axial shows some but misses vertical spread | **Coronal** — shows the full height of the lamina papyracea |
| Nasolacrimal duct full pathway | Axial shows only cross-sections; misses the vertical duct trajectory | **Sagittal + Coronal** — required to trace the duct from lacrimal sac to inferior meatus |
| Dural thickening above the orbital roof | Axial runs parallel to roof; enhancement can be subtle | **Sagittal T1+C** — shows the dura in profile against the frontal lobe |
| Lateral wall bone invasion depth | Axial shows the wall thickness but not the full anterior-posterior extent | **Coronal** — confirms whether the greater wing of sphenoid is involved to the middle fossa |

### 2.7.2 Mandatory Three-Plane Checklist for Orbital Contouring

Before finalizing any orbital CTV, verify the following on **all three planes**:

| Structure | Sagittal Check | Coronal Check | Axial Check |
|-----------|---------------|---------------|-------------|
| **Orbital roof** | Is the entire roof curvature covered, from anterior rim to apex? Is there frontal sinus contact? | Is the roof included bilaterally? Any asymmetry? | Baseline coverage |
| **Orbital floor** | Does the floor slope downward into the maxillary sinus roof? Is the maxillary sinus mucosa thickened? | Is the infraorbital canal enlarged? Any asymmetry? | Baseline coverage |
| **Medial wall (lamina papyracea)** | — | Is the full height of the ethmoid covered? Any ethmoid air cell opacity? | Is the paper-thin bone expanded? |
| **Lateral wall** | — | Does the bone extend to the temporalis fossa? Any middle fossa contact? | Is the greater wing of sphenoid involved? |
| **Orbital apex** | Does CTV extend through the optic canal to the prechiasmatic cistern? Through the superior orbital fissure to the cavernous sinus? | Are both foramina encompassed? | Baseline coverage |
| **Infraorbital nerve / canal (V2)** | Trace the canal from the orbital floor to the infraorbital foramen → is the foramen enlarged? → Does tumor extend anteriorly into the cheek? | Cross-section of the canal at each level | Foramen at the anterior maxillary face |
| **Nasolacrimal duct** | Trace from lacrimal sac → nasolacrimal canal → inferior meatus (entire pathway) | Cross-section of the duct at each level | Cross-sections at sac, canal, and meatus |
| **Dura / meninges** | T1+C sagittal: is there linear dural enhancement above the orbital roof? Any nodular dural thickening? | Coronal: symmetrical dural enhancement? | — |
| **Periorbital soft tissues** | — | — | Any extraconal extension beyond the bony orbit? |

### 2.7.3 Special Rules for Bone Coverage

| Rule | Rationale |
|------|----------|
| **Lacrimal gland tumors with lateral wall involvement** | CTV must extend **≥5 mm beyond the outer cortex of the lateral orbital wall** into the temporalis fossa soft tissues — do NOT stop at the periosteum. The bone itself must receive full prescription dose through its entire thickness. |
| **Medial wall involvement** | If the lamina papyracea is eroded, **include the entire ipsilateral ethmoid complex** in the CTV — tumor can track through multiple ethmoid air cells without radiological evidence until late. |
| **Orbital floor involvement** | CTV must include the **full thickness of the maxillary roof bone** + the adjacent maxillary sinus mucosa. If the sinus mucosa is thickened on MRI, it should be considered potentially involved. |
| **Infraorbital foramen enlargement** | Trace V2 forward to the foramen → if the foramen is widened, CTV should extend **anteriorly along the infraorbital nerve to the cheek soft tissues** for at least 5 mm beyond the foramen. |
| **Nasolacrimal duct involvement** | Surgery usually only removes the proximal duct. The entire distal nasolacrimal canal (from the lacrimal sac to the inferior meatus under the inferior turbinate) must be contoured and included in the CTV if the tumor involved the lacrimal system. |

### 2.7.4 Common Contouring Misses (Pitfalls to Avoid)

| Miss | Why It Happens | How to Prevent It |
|------|---------------|-------------------|
| **CTV stops at the orbital rim anteriorly** | Axial view makes the rim appear as the "end" of the orbit | Check sagittal: the lid and conjunctiva extend beyond the rim → if eyelid or conjunctival involvement, CTV extends anteriorly beyond the bony rim |
| **CTV misses the orbital roof curvature** | Axial slices show the roof as a thin line; the upward dome is invisible | Sagittal: trace the curved roof from rim to apex — the entire dome must be inside CTV |
| **CTV does not cover the cribriform plate** | Medial wall tumors are contoured on axial only; the superior extension to the olfactory region is missed | Coronal: trace the medial wall superiorly to the cribriform plate; sagittal confirms |
| **Inferior orbital fissure is outside CTV** | The IOF is a diagonally oriented gap between the lateral wall and floor — it is not part of the "bony orbit" contour | Coronal + sagittal: the IOF connects the orbit to the pterygopalatine fossa — if posterolateral tumor, include it |
| **Nasolacrimal duct stopped halfway** | The duct disappears into the bony nasolacrimal canal and is not visible on standard CT windows | Use bone window + sagittal reconstruction; trace the canal from orbit to inferior meatus |

---

### 2.3 Benign / Low-Grade Tumors

| Entity | GTV → CTV | Notes |
|--------|----------|-------|
| **Schwannoma (post-op residual)** | GTV + 3-5 mm | FSRT preferred (25-27.5 Gy/5 fx) |
| **Optic nerve sheath meningioma** | GTV + 3-5 mm along nerve sheath | FSRT/SRT; preserve vision |
| **Pseudotumor (refractory)** | GTV + 5 mm | Low dose (20 Gy/10 fx) |
| **Graves' orbitopathy** | Retrobulbar fat + muscles (spare lens, globe) | 20 Gy/10 fx; bilateral |

---

## Section 3 — Dose and Fractionation

### 3.1 Orbital Lymphoma

| Histology | Standard Dose | Ultra-Low Dose Option | Notes |
|-----------|-------------|----------------------|-------|
| **MALT (indolent)** | 24-25.2 Gy / 12-14 fx | 4 Gy / 2 fx (2 Gy × 2, ≥48h apart) | NCCN-endorsed ultra-low dose option; local control ~93% |
| **MALT (ultra-low → recurrence)** | — | Re-treat 4 Gy/2fx or escalate to 24 Gy | Cumulative OAR must remain within tolerance |
| **Follicular lymphoma** | 24-30 Gy / 12-15 fx | 4 Gy/2fx (emerging, less robust than MALT) | Limited evidence; use with caution |
| **DLBCL (post-chemo consolidation)** | 30-36 Gy / 15-18 fx | N/A | PET-adapted: Deauville 1-2 → 24-30 Gy sufficient |
| **DLBCL (definitive / bridging to CAR-T)** | 30-40 Gy / 15-20 fx | N/A | Bridging RT → CAR-T: 1.5 Gy BID × 10d (=30 Gy) if 2-week window |
| **Mantle cell lymphoma** | 30-36 Gy / 15-18 fx | N/A |

**Technical note for 4 Gy/2fx delivery**:
- IMRT/VMAT still recommended despite low dose — lens/cornea/lacrimal gland receive 2 Gy vs 0 Gy matters
- Verify low-MU segment delivery accuracy on linac
- Point dose verification with ion chamber or diode recommended

### 3.2 Orbital Solid Malignancies

| Histology | Dose | Fractionation |
|-----------|------|---------------|
| **ACC (R0 post-op)** | 60 Gy | 30 fx |
| **ACC (R1/R2, PNI+)** | 66 Gy | 33 fx |
| **Sarcoma (R0)** | 60-66 Gy | 30-33 fx |
| **Sarcoma (R1)** | 66-70 Gy | 33-35 fx |
| **Meningioma (WHO I, definitive)** | 50.4-54 Gy | 28-30 fx |
| **Meningioma (WHO II-III)** | 59.4-60 Gy | 30-33 fx |
| **NPC orbital invasion** | 66-70 Gy | 33-35 fx |

### 3.3 Benign / SBRT Indications

| Entity | Dose | Technique |
|--------|------|-----------|
| **Schwannoma (post-op residual)** | 25-27.5 Gy / 5 fx | FSRT (preferred over single-fraction SRS) |
| **Optic nerve sheath meningioma** | 25-27 Gy / 5 fx | FSRT; D0.03cc optic nerve <23 Gy |
| **Pseudotumor** | 20 Gy / 10 fx | Conventional RT |
| **Graves' orbitopathy** | 20 Gy / 10 fx | Bilateral; lens shielding mandatory |

---

## Section 4 — OAR Dose Constraints (Orbit-Specific)

### 4.1 Mandatory Constraints

| OAR | Conventional (1.8-2.0 Gy/fx) | SRS (1 fx) | SRT (3-5 fx) | Priority |
|-----|------------------------------|------------|-------------|----------|
| **Lens** | Dmax < 4-5 Gy | — | — | 🔴 Critical |
| **Optic nerve / chiasm** | Dmax < 55 Gy (preferred), < 60 Gy (absolute max) | Dmax ≤ 8 Gy (<10 Gy acceptable) | D0.03cc < 23 Gy | 🔴 Critical |
| **Brainstem** | Dmax < 54 Gy | Dmax < 12 Gy | — | 🔴 Critical |
| **Cornea** | Dmax < 30 Gy, Dmean < 20 Gy | — | — | 🟡 Important |
| **Retina** | Dmax < 45 Gy | — | — | 🟡 Important |
| **Macula** | Dmax < 40 Gy | — | — | 🟡 Important |
| **Lacrimal gland** | Dmean < 25 Gy | — | — | 🟡 Important |
| **Whole orbit (cumulative)** | < 36 Gy | — | — | 🟡 (prevent ischemic retinopathy/glaucoma) |

### 4.2 Risk-Adjusted Constraint Tightening

| Risk Factor | Adjustment |
|------------|-----------|
| Age > 70 years | Optic nerve Dmax: reduce by 5-8 Gy |
| Diabetes / hypertension / vasculopathy | Optic nerve Dmax < 50 Gy |
| Prior orbital surgery | Conservative threshold (microischemia may already exist) |
| Concurrent platinum/vinca alkaloid chemo | Reduce OAR limits by 5-10% |
| Single functional eye | Contralateral lens/cornea/retina: **aim for 0 Gy** |

### 4.3 Lens Protection Techniques

| Technique | When to Use | Expected Lens Dose |
|-----------|------------|-------------------|
| Anterior oblique / lateral beam entry | Orbit anterior tumors | < 3 Gy |
| Electron beam + lead shield (4-6 mm Pb on eyelid) | Conjunctival / eyelid limited lymphoma | < 1 Gy |
| Gaze deviation (patient looks away from tumor) | Posterior / superolateral tumors | Increases distance, reduces dose |
| VMAT with ring avoidance structure around lens | All IMRT/VMAT plans | < 3-5 Gy achievable |
| Proton therapy (Bragg peak) | ACC, sarcoma, young patients | Contralateral: ~0 Gy |

---

## Section 5 — Technology Selection Decision Tree

```
Orbital tumor requiring RT
        │
        ├─ Lymphoma (MALT/DLBCL)
        │    ├─ Anterior (conjunctival) → Electron + Pb shield
        │    └─ Posterior / whole orbit → IMRT/VMAT
        │
        ├─ Solid malignant (ACC/Sarcoma)
        │    ├─ Dose ≥ 60 Gy, OAR compromise expected → Proton / Carbon ion (preferred)
        │    └─ Dose < 60 Gy, OAR achievable with IMRT → IMRT/VMAT
        │
        ├─ Benign (Schwannoma/Meningioma)
        │    └─ FSRT (25-27.5 Gy/5 fx) — preferred over SRS for orbital apex lesions
        │
        └─ Salvage / Re-irradiation
             ├─ Tumor ≤ 3 cm, well-defined → I-125 seed implant
             └─ Tumor > 3 cm, diffuse → Proton / Carbon ion
```

### I-125 Seed Implantation Specifics

| Parameter | Value |
|-----------|-------|
| Seeds | I-125, ~0.5 mCi per seed |
| Seed count formula | (L+W+H)/3 × 5 ÷ 0.5 mCi |
| Spacing | Equidistant arrangement |
| Implant depth | Nasolacrimal duct or subperiosteal plane — **NEVER directly on sclera** (risk: sterile endophthalmitis → enucleation) |
| OAR sparing mechanism | Inverse-square law distance falloff + orbital bone shielding |
| Dry eye rate | ~30% (mild) vs >90% with EBRT |
| Cataract rate | ~0% vs ~50% with EBRT |
| Indications | Salvage after prior EBRT; boost after EBRT; small (<3 cm) well-defined residual |

---

## Section 6 — Surgery-to-RT Coordination (Five "RT-Friendly" Surgical Practices)

| # | Practice | Why It Matters for RT |
|---|----------|----------------------|
| 1 | **Describe residual in anatomical detail** | "8×5 mm soft tissue 3 mm medial to optic canal" — NOT "some residual at apex" |
| 2 | **Place ≥2 titanium clips** at positive margins / residual | ≥1 cm apart for 3D CT localization |
| 3 | **Protect lacrimal gland vasculature** | Surgical devascularization + RT = compounded dry eye risk |
| 4 | **Post-op MRI within 48-72 hours** | Gold standard for residual assessment; after 72h, inflammatory enhancement mimics tumor |
| 5 | **Drain large hematomas before CT simulation** | Fluid alters dose distribution (especially for low-energy photons) |

---

## Section 7 — Key References

1. NCCN Guidelines: B-Cell Lymphomas (Orbital MALT/DLBCL). Version 3.2025.
2. ILROG Guidelines: Radiation Therapy for Orbital Lymphoma. *Int J Radiat Oncol Biol Phys*. 2021.
3. Fasola CE, et al. Low-dose radiation therapy (2 Gy × 2) in the treatment of orbital lymphoma. *Int J Radiat Oncol Biol Phys*. 2013;86(5):930-935.
4. QUANTEC: Quantitative Analyses of Normal Tissue Effects in the Clinic. *Int J Radiat Oncol Biol Phys*. 2010;76(3 Suppl).
5. AAPM TG-101: Stereotactic Body Radiation Therapy. *Med Phys*. 2010;37(8):4078-4101.
6. Shanghai Proton and Heavy Ion Center (SPHIC): Orbital tumor outcomes with particle therapy. 2022.
7. ICRU Report 83: Prescribing, Recording, and Reporting IMRT. 2010.

---

## Section 8 — Anterior Segment Toxicity and Eye Care During Orbital RT

### 8.1 The Neglected Anterior Segment

While radiotherapy planning focuses on the posterior visual pathway (optic nerve, chiasm, retina), the anterior segment — cornea, conjunctiva, tear film, eyelids — is often the dominant source of acute suffering for the patient. These structures are:

- **Highly radiosensitive** (corneal epithelium turnover: 7-10 days; conjunctival epithelium: 5-7 days)
- **Exquisitely symptomatic** when injured (pain, photophobia, discharge, blurred vision)
- **Visible to the patient and family** (red eye, eyelid edema, purulent discharge) — causing psychological distress beyond the physical symptoms
- **Capable of causing permanent visual loss** if severe (corneal ulcer → perforation → endophthalmitis)

### 8.2 The Anterior Segment Toxicity Cascade

```
RT to cornea/conjunctiva/tear film unit
        │
        ▼
  ┌─ Corneal epithelial cell loss → punctate keratitis → ulceration
  │
  ├─ Conjunctival inflammation → conjunctival injection, chemosis
  │
  ├─ Goblet cell loss → mucin deficiency → tear film instability
  │
  ├─ Lacrimal gland irradiation → aqueous tear deficiency → severe dry eye
  │
  ├─ Meibomian gland irradiation → lipid layer loss → evaporative dry eye
  │
  └─ Eyelid margin inflammation → blepharitis, trichiasis, ectropion
        │
        ▼
  Combined: severe dry eye + corneal erosion + eyelid malposition
        │
        ▼
  Corneal ulcer → infection → scarring → permanent visual loss
```

### 8.3 Strategies for Anterior Segment Protection

#### 8.3.1 Physical Techniques (RT Technologist-Level)

| Technique | How It Works | Effectiveness |
|-----------|-------------|---------------|
| **Gaze deviation** | Patient fixates gaze away from the tumor (e.g., look left for a right lateral tumor) — the cornea and lens move away from the beam path | Highly effective for lateralized tumors; requires cooperative patient |
| **3D lens-bone matching** | RT technologist verifies lens position relative to bony landmarks (lateral canthus, nasion) on daily CBCT before each fraction | Reduces setup error; prevents unintended lens/cornea dose creep |
| **Thermoplastic mask + bite-block** | Standard immobilization; bite-block stabilizes the maxilla → more reproducible globe position | Mandatory for IMRT/VMAT |
| **Electron beam + custom lead shield** | 4-6 mm lead contact shield placed directly on the closed eyelid for anterior conjunctival/eyelid tumors | Reduces lens dose to <1 Gy (cornea partially shielded) |
| **Prone or lateral decubitus positioning** | For very anterior tumors, non-supine positioning can exploit gravity to move the globe away | Rarely used; complex setup |

#### 8.3.2 Treatment Planning Strategies

| Strategy | Details |
|----------|---------|
| **Anterior oblique beam entry** | Avoid AP beams that transit the cornea and lens directly |
| **Non-coplanar arcs (VMAT)** | Posterior arc that enters through the cranium rather than through the globe |
| **Ring avoidance structure around cornea** | Create a 3-5 mm ring structure around the corneal surface; assign high optimization priority to push dose away |
| **Corneal Dmax constraint** | Set Dmax < 30 Gy as a hard optimization goal; Dmean < 20 Gy |
| **Lacrimal gland Dmean < 25 Gy** | Use optimization weighting to prioritize lacrimal gland sparing |
| **Tear film unit protection** | This requires protecting cornea (epithelium), conjunctiva (goblet cells), lacrimal gland (aqueous), and meibomian glands (lipid) simultaneously — prioritize cornea and lacrimal gland |

### 8.4 The Mandatory Ophthalmology Co-Management Protocol

Orbital RT should NEVER be delivered without an ophthalmologist on the MDT. The following co-management schedule is recommended:

| Time Point | Ophthalmology Action | RT Team Action |
|-----------|---------------------|----------------|
| **Pre-RT (baseline)** | Comprehensive eye exam: visual acuity, slit lamp, corneal staining, Schirmer test, tear breakup time, OCT RNFL, fundoscopy. Treat pre-existing blepharitis/demodex. | Record baseline; set individualized OAR constraints based on pre-existing conditions |
| **RT week 1-2** | Start preservative-free artificial tears QID; lid hygiene; warm compresses | CBCT verification; assess setup reproducibility |
| **RT week 3-4** | Assess for early keratitis; upgrade to gel/lubricant at night; consider punctal plugs if severe dry eye emerging | Verify cumulative dose to cornea/lacrimal gland is on track |
| **RT week 5-6** | Daily or alternate-day slit lamp if corneal staining present; topical antibiotic if epithelial defect; consider temporary tarsorrhaphy for severe exposure | Final cumulative DVH check |
| **RT end + 1 month** | Full exam: compare to baseline; assess for persistent keratitis, dry eye severity, cataract formation | Review plan vs delivered dose |
| **RT end + 3 months** | OCT RNFL vs baseline — first assessment of subclinical optic neuropathy | — |
| **RT end + 6 months** | Cataract screening (LOCS III); dry eye grading (DEWS); lacrimal syringing if epiphora | — |
| **Annually thereafter** | Annual comprehensive exam; RION surveillance up to 8 years | Coordinate if re-RT is considered |

### 8.5 Practical Eye Care During RT — What the Patient Needs

| Symptom | First-Line Intervention | Escalation |
|---------|------------------------|-----------|
| Dryness / gritty sensation | Preservative-free artificial tears (sodium hyaluronate 0.1-0.3%) Q2H while awake | Punctal plugs (silicone); autologous serum tears 20% |
| Redness / injection | Cold compresses; topical low-dose steroid (fluorometholone 0.1%, under ophthalmology supervision) | Short-course topical steroid; rule out infection |
| Mucoid / purulent discharge | Lid hygiene (dilute baby shampoo + warm water); topical antibiotic (tobramycin or moxifloxacin) if bacterial superinfection | Culture-guided antibiotics; check for nasolacrimal duct obstruction |
| Eyelid crusting / blepharitis | Warm compresses BID + lid massage; tea tree oil wipes if demodex suspected | Oral doxycycline 50-100 mg daily (anti-inflammatory + anti-demodex) |
| Photophobia | Dark glasses; reduce screen time; lubricating gel at night | Cycloplegic drops (cyclopentolate 1%) for severe ciliary spasm |
| Corneal ulcer / epithelial defect | **STOP RT** → urgent ophthalmology: topical antibiotics Q1H, cycloplegic, lubricating ointment, eye shield | Temporary tarsorrhaphy; amniotic membrane graft |

### 8.6 The "Invisible Toxicity" — Why This Matters Beyond Physics

A DVH cannot capture the patient experience of orbital RT. A patient with conjunctival injection, purulent discharge, and photophobia for 6 weeks:

- Cannot work
- Cannot drive
- Cannot read
- Appears visibly unwell to family (red eye + discharge)
- May refuse to complete RT

> **The anterior segment deserves the same meticulous planning attention as the optic nerve. A perfect plan that controls the tumor but blinds the cornea is a failed plan.**

---

## Section 8B — Nasolacrimal Duct: Dose Constraints and Toxicity Management

### 8B.1 Why the Nasolacrimal Duct Matters

The nasolacrimal duct (NLD) drains tears from the lacrimal sac → nasolacrimal canal → inferior meatus of the nasal cavity. It runs diagonally through the medial orbital wall and maxillary bone — a trajectory that places it within or near the CTV for:

- Medial orbital tumors
- Lacrimal sac / canalicular tumors
- Maxillary sinus tumors invading the orbital floor
- Any whole-orbit irradiation

Radiation-induced NLD stenosis or obstruction causes **epiphora** (overflow tearing) — a symptom that is often underreported by patients and underappreciated by radiation oncologists, yet profoundly impacts quality of life.

### 8B.2 Dose Constraints

| Structure | Constraint | Rationale |
|-----------|-----------|----------|
| **Nasolacrimal duct** | Dmax < 50 Gy (conventional fx) | Mucosal stenosis threshold |
| **Nasolacrimal duct** | Dmean < 30 Gy | Minimize chronic fibrotic stricture |
| **Lacrimal sac** | Dmax < 45 Gy | More radiosensitive than the bony canal segment |

### 8B.3 Prevention and Surveillance

| Time Point | Action |
|-----------|--------|
| **Pre-RT** | Assess NLD patency (dye disappearance test, lacrimal syringing); if pre-existing stenosis → consider prophylactic silicone intubation |
| **RT planning** | Contour the NLD from lacrimal sac to inferior meatus; use IMRT to push dose away if tumor location permits |
| **RT follow-up** | At each visit: ask specifically about tearing/watery eye (patients rarely volunteer this symptom); if epiphora → lacrimal syringing to assess patency |

### 8B.4 Management of NLD Toxicity

| Severity | Intervention |
|----------|-------------|
| **Acute dacryocystitis** (pain, swelling at medial canthus, purulent discharge) | Warm compresses TID; topical antibiotic (tobramycin); oral antibiotics (amoxicillin-clavulanate 7-10 days) |
| **Chronic dacryocystitis** | Lacrimal syringing 1-2×/week; topical moxifloxacin QID |
| **Complete NLD obstruction** | Dacryocystorhinostomy (DCR) — definitive surgical bypass |

---

## Section 8C — Nodal Irradiation Indications for High-Risk Orbital/Adnexal Histologies

### 8C.1 General Principle

Orbital and adnexal tumors that breach the orbital confines gain access to the VIII→IX→IIa lymphatic cascade (Section 0.2). Prophylactic nodal irradiation should be considered for the following high-risk scenarios:

### 8C.2 Histology-Specific Nodal Risk

| Histology | Nodal Risk | Prophylactic Nodal RT Recommendation |
|-----------|-----------|--------------------------------------|
| **Sebaceous carcinoma (睑板腺癌)** | **High** (20-30% regional LN metastasis) | ✅ **Strongly consider** — ipsilateral VIII + IX + Ib + II + III |
| **Squamous cell carcinoma (G3, PNI+, LVI+)** | **High** | ✅ Consider ipsilateral VIII + IX + IIa |
| **Melanoma (conjunctival/orbital)** | Moderate-High | ✅ If Breslow >2 mm or ulceration → sentinel node biopsy ± RT |
| **Merkel cell carcinoma (eyelid)** | **Very high** (>30%) | ✅ Ipsilateral VIII + IX + Ib + II + III |
| **Adenoid cystic carcinoma** | Low | ❌ Unless extraorbital extension + solid type (see ACC skill) |
| **Basal cell carcinoma** | Very low (<1%) | ❌ Not indicated |
| **Lymphoma** | Systemic disease | RT is local consolidative — not for nodal prophylaxis |

### 8C.3 Nodal CTV Template for High-Risk Orbital/Adnexal Cancers

When prophylactic nodal RT is indicated:

```
CTV-N (ipsilateral):
  ├── Level VIII  (superficial parotid / preauricular)
  ├── Level IX   (peri-facial artery / buccal nodes)
  ├── Level Ib   (submandibular)
  ├── Level IIa  (upper deep jugular)
  └── Level III  (mid-deep jugular — if high nodal burden or multiple positive nodes)
```

**Dose**: 50-54 Gy / 30 fx (prophylactic); 60-66 Gy (known involvement).

---

## Section 8D — Brachytherapy Boost Indications for Orbital Tumors

Brachytherapy (I-125 seed implant or episcleral plaque) serves as a valuable boost or salvage tool in specific scenarios:

| Indication | Technique | Dose |
|-----------|-----------|------|
| **Post-op microscopic residual (R1)** after EBRT | I-125 seed implant to surgical bed | Adds ~160 Gy local dose with rapid falloff |
| **Standard EBRT dose would cause prohibitive toxicity** (e.g., corneal ulcer risk, pre-existing severe dry eye) | Brachytherapy alone or as primary modality | 60-70 Gy at 5 mm depth (LDR) |
| **Inoperable tumor / patient refuses exenteration** | Episcleral plaque (Ru-106, I-125) for anterior intraocular tumors | 85-100 Gy to tumor apex |
| **Recurrence after prior EBRT** (cumulative OAR tolerance reached) | Brachytherapy salvage | Dose per prior EBRT cumulative limits |

**Contraindications**: Tumor > 3 cm (dose falloff inadequate); tumor involving the optic nerve head (plaque can't cover); bone invasion (I-125 seed spacing unpredictable).

---

## Section 8E — Pre-RT Simulation Requirements

### 8E.1 Immobilization

| Requirement | Rationale |
|------------|----------|
| **Head-and-neck thermoplastic mask** (not head-only) | Orbital tumors often extend inferiorly; neck nodes (VIII/IX/IIa) must be immobilized if in field |
| **Bite-block** | Stabilizes maxilla → reproducible globe position |
| **Knee bolster** | Comfort for extended simulation and treatment |

### 8E.2 CT Simulation

| Parameter | Specification |
|-----------|--------------|
| Scan range | Vertex → 2 cm below sternal notch (cover VIII/IX/IIa if nodal RT planned) |
| Slice thickness | ≤ 3 mm |
| Contrast | IV contrast unless contraindicated |

### 8E.3 MRI Fusion

| Sequence | Purpose |
|----------|---------|
| T1+C fat-suppressed | Tumor extent, perineural spread, dural enhancement |
| T2/STIR | Edema vs tumor, cystic components |
| FIESTA/CISS | Cranial nerve visualization in cavernous sinus/orbital apex |

---

## Section 8F — Retinoblastoma Post-Enucleation RT

### 8F.1 Indications

Post-enucleation RT is indicated when pathology demonstrates high-risk features:

- Tumor at optic nerve cut margin
- Transscleral extension
- Choroidal invasion (massive)
- Anterior chamber involvement

### 8F.2 Target Volume

| Parameter | Specification |
|-----------|--------------|
| CTV | Entire ipsilateral bony orbit (including orbital apex, optic canal to chiasm if nerve margin positive) |
| PTV | CTV + 3-5 mm |
| Dose | 45-46 Gy / 23-25 fx (R0); boost to 50-54 Gy if R1 |

---

## Section 8G — Eye Preservation Quantification Model

To facilitate MDT decision-making, the following semi-quantitative framework can be used to balance competing priorities:

| Index | Formula | Components |
|-------|---------|-----------|
| **Eye Preservation Index** | EPI = Expected survival (years) × Vision preservation probability × Patient psychological weight (0-1) | How much life-quality benefit does saving the eye provide? |
| **Radicality Index** | RI = Tumor aggressiveness score × Recurrence risk × Distant metastasis probability | How dangerous is an R1/R2 resection? |

**Decision rule**:
- EPI >> RI → pursue eye preservation aggressively (neoadjuvant RT/chemo → eye-sparing surgery)
- EPI << RI → exenteration is warranted
- EPI ≈ RI → MDT discussion; may trial neoadjuvant approach with clear "stop rules" (e.g., if tumor response <30% at 4 weeks post-neoadjuvant RT → proceed to exenteration)

---

## Section 9 — Key References

**Orbital Lymphoma**
1. Pinnix CC, et al. Response-Adapted Ultralow-Dose Radiation Therapy for Orbital Indolent B-Cell Lymphoma: A Phase 2 Nonrandomized Controlled Trial. *JAMA Oncol*. 2024. PMID:38990564.
2. Yahalom J, et al. An International Lymphoma Radiation Oncology Group Study of RT for Bilateral Indolent Orbital Adnexal Lymphomas. *Int J Radiat Oncol Biol Phys*. 2025. PMID:40090468.
3. Chelius M, et al. The Role of Radiotherapy in Indolent Ocular Adnexal and Orbital Lymphomas. *Head Neck*. 2025. PMID:39487567.
4. Shelukar S, et al. High local control and low ocular toxicity using ultra-low-dose "boom-boom" radiotherapy for indolent orbital lymphoma. *Chin Clin Oncol*. 2022. PMID:36632978.
5. Fasola CE, et al. Low-dose radiation therapy (2 Gy × 2) in orbital lymphoma. *Int J Radiat Oncol Biol Phys*. 2013;86(5):930-935.

**Lacrimal Gland Adenoid Cystic Carcinoma**
6. Woog JJ, et al. Adenoid cystic carcinoma of the lacrimal gland — A major review. *Indian J Ophthalmol*. 2025. PMID:40995894.
7. Ahmad SM, et al. Disease-specific and overall survival for patients with lacrimal gland ACC. *Br J Ophthalmol*. 2026. PMID:40866108.
8. Role of radiotherapy in the multidisciplinary treatment of lacrimal gland ACC. *Ther Adv Med Oncol*. 2026. PMID:41602513.

**Uveal Melanoma / Proton Therapy**
9. Hrbacek J, et al. Three years of ocular proton therapy in the Netherlands. *Acta Ophthalmol*. 2026. PMID:42393916.
10. Long-term follow-up of iris melanomas treated by proton beam therapy. *Eye*. 2025. PMID:40676200.

**Orbital Rhabdomyosarcoma**
11. Orbital Rhabdomyosarcoma: A Comprehensive Review. *Clin Exp Ophthalmol*. 2026. PMID:41698361.

**Sebaceous Carcinoma**
12. Timing of nodal metastasis in eyelid sebaceous carcinoma. *Br J Ophthalmol*. 2025. PMID:40010760.

**Toxicity / Late Effects**
13. Dose-toxicity relationship for ophthalmological OARs in pediatric patients. *Clin Transl Radiat Oncol*. 2026. PMID:42404299.
14. Late-Onset Ocular Morbidity: A Proposed 10-Year Survivorship Protocol. *Cancers*. 2026. PMID:42192992.

**Guidelines / Consensus**
15. NCCN Guidelines: B-Cell Lymphomas (Orbital MALT/DLBCL). Version 3.2026.
16. ILROG Guidelines: Radiation Therapy for Orbital Lymphoma. 2021.
17. QUANTEC: Quantitative Analyses of Normal Tissue Effects in the Clinic. *Int J Radiat Oncol Biol Phys*. 2010.
18. AAPM TG-101: Stereotactic Body Radiation Therapy. *Med Phys*. 2010.
19. 中国眼及附属器肿瘤放射治疗指南（2021版）. 陆雪官等. 中国医师协会放疗专委会.
20. CSCO头颈肿瘤诊疗指南. 2025.

---

## Section 10 — Literature Review (2021-2026): Key Findings and Skill Integration

### 10.1 Ultra-Low Dose RT for Orbital Lymphoma — The New Standard

The past 5 years have seen ultra-low-dose RT (4 Gy/2fx) move from an experimental option to a guideline-endorsed standard for indolent orbital MALT lymphoma:

| Study | Year | N | Key Finding |
|-------|------|---|-------------|
| Pinnix CC et al. (JAMA Oncol) | 2024 | Phase 2 | First prospective trial: response-adapted 4 Gy/2fx → CR 92%; residual → additional 20 Gy |
| ILROG (Yahalom J et al., IJROBP) | 2025 | Multicenter | Bilateral orbital lymphoma: ultra-low-dose RT safe and effective bilaterally |
| Shelukar S et al. (Chin Clin Oncol) | 2022 | — | "Boom-boom" RT (4 Gy/2fx): high control, minimal toxicity |

**Skill integration**: The ultra-low-dose option is now firmly established in Section 3.1. The ILROG bilateral data validates that bilateral orbital irradiation using 4 Gy/2fx does not compound toxicity significantly — consistent with our approach to bilateral orbital lymphoma.

### 10.2 Lacrimal Gland ACC — RT Is Central to Multimodality Care

| Study | Year | Finding |
|-------|------|---------|
| Woog JJ et al. (Indian J Ophthalmol) | 2025 | Major review: RT improves local control in all stages of lacrimal gland ACC |
| Ahmad SM et al. (Br J Ophthalmol) | 2026 | Disease-specific survival improving with modern RT (IMRT/proton/CIRT) |
| Ther Adv Med Oncol | 2026 | RT role in multidisciplinary ACC treatment is expanding |

**Skill integration**: Confirms our approach of aggressive post-operative RT (66 Gy/33 fx) for lacrimal gland ACC with PNI. The growing evidence for proton/CIRT for orbital ACC supports Section 5's technology selection tree.

### 10.3 Ocular Proton Therapy — Evidence Base Maturing

| Study | Year | Finding |
|-------|------|---------|
| Hrbacek J et al. (Acta Ophthalmol) | 2026 | Netherlands: 3-year national data on ocular proton therapy — high local control, acceptable toxicity |
| Eye (Lond) | 2025 | Proton beam for iris melanoma: long-term follow-up confirms safety |

**Skill integration**: Supports Section 5's proton therapy recommendation for young patients and radioresistant tumors. The Dutch national data (2026) provides the first systematic evidence that proton therapy for orbital tumors achieves the expected OAR-sparing advantage in routine practice, not just in dosimetric studies.

### 10.4 Late Toxicity — The 10-Year Horizon

| Study | Year | Finding |
|-------|------|---------|
| Late-Onset Ocular Morbidity Protocol (Cancers) | 2026 | Proposed 10-year functional survivorship protocol for pediatric orbital RT |
| Dose-toxicity relationship (Clin Transl Radiat Oncol) | 2026 | Pediatric OAR dose-toxicity modeling |

**Skill integration**: Supports Section 8's co-management protocol. The 10-year survivorship protocol concept aligns with our recommendation for annual ophthalmology follow-up extending to 8+ years.

### 10.5 National Guidelines and Consensus

| Document | Year | Publisher |
|----------|------|-----------|
| **中国眼及附属器肿瘤放射治疗指南** | 2021 | 中国医师协会放疗专委会（陆雪官等） |
| CSCO头颈肿瘤诊疗指南 | 2025 | 中国临床肿瘤学会 |
| NCCN B-Cell Lymphomas | 2026 | NCCN |

**Skill integration**: The 2021 Chinese national guideline is the foundational document for orbital RT in China. Our skill extends it with:

| Guideline Content | Our Skill Extension |
|-------------------|-------------------|
| Target delineation principles | Detailed section-by-section CTV definitions (Section 2) |
| Dose recommendations | Ultra-low-dose 4 Gy/2fx protocol with technical execution details (Section 3.1) |
| Basic OAR constraints | Risk-adjusted constraint tightening + individual patient factors (Section 4.2) |
| — | Orbital bone involvement management (Section 2.6 — unique contribution) |
| — | VIII/IX/IIa lymphatic cascade for extraorbital tumors (Section 0 — unique contribution) |
| — | Neoadjuvant strategies for eye preservation (Section 2.5 — unique contribution) |
| — | Three-plane contouring technique (Section 2.7 — unique contribution) |
| — | Ophthalmology co-management protocol (Section 8 — unique contribution) |

---

*This clinical framework was developed through the clinical experience of the Department of Radiation Oncology, Shanghai Ninth People's Hospital, Shanghai Jiao Tong University School of Medicine. It is intended for educational and clinical reference purposes.*


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
```
