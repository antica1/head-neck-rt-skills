---
name: hncup-rt-targets
metadata:
  hermes:
    tags: [head-neck, radiotherapy, cup, cervical, unknown-primary]
    triggers_on: [原发不明, 原发灶不明, 颈部转移癌, 不明原发灶, 颈部淋巴结转移, 颈部转移, CUP, HNCUP, cervical CUP, unknown primary, 颈部转移性癌, 颈部转移癌靶区, 颈部不明原发, EBV相关转移, HPV相关转移, 选择性黏膜照射, 选择性黏膜勾画, 逆流规则, 双侧颈部, 对侧颈预防, NPC筛查, 鼻咽镜阴性, PET阴性]
    related_skills: [head-neck-dvh-plan-review, npc-rt-target-delineation]
description: "原发不明颈部转移癌HNCUP靶区勾画——选择性黏膜、EBV/HPV分层、颈清后逆流规则。True CUP RT target delineation — selective mucosal irradiation."
version: 1.0.0
author: Dou Shengjin, Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
---
> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗组原创知识产权。五大原创框架——间室放疗（门+隔壁）、淋巴逆流规则、QUANTEC 四维批判、口底铁律、化免新辅助后 PORT 降级三梯度——均为九院体系的组成部分。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.



# 颈部原发不明转移性癌 — 放疗靶区勾画指南

## Overview

Cervical carcinoma of unknown primary (CUP) is defined as histologically confirmed metastatic carcinoma in cervical lymph nodes for which no primary tumor is identified despite exhaustive diagnostic workup. 

In China, the epidemiological profile differs fundamentally from Western populations: **nasopharyngeal carcinoma (NPC)** is endemic, and a substantial proportion of cervical CUP cases represent occult NPC. This mandates a diagnostic and therapeutic strategy distinct from international guidelines.

This guide is based on clinical experience at Shanghai Ninth People's Hospital and published work (Oncotarget 2016; Cancer Medicine 2020).

---

## Section 0 — Core Principles: How We Differ from International Guidelines

| Principle | Western / NCCN Approach | Ninth Hospital Approach |
|-----------|------------------------|------------------------|
| **Diagnostic threshold** | Includes cases where primary is "suspected but not proven" | True CUP only: **exhaustive efforts must have failed to find any primary** |
| **Epidemiology** | HPV+ oropharyngeal cancer dominates | EBV+ nasopharyngeal carcinoma is the leading occult source |
| **Mucosal irradiation** | Whole pharyngeal axis + oral cavity (pan-mucosal) | **Selective mucosal irradiation** — only the likely origin site(s) |
| **Neck irradiation** | Bilateral neck (often) | **Ipsilateral neck only** unless contralateral nodes are positive |
| **Surgical approach** | Neck dissection as first step | Two-step: Step 1 exclude NPC → Step 2 selective neck dissection + mucosal RT |

---

## Section 1 — Definition: True CUP vs. Pseudo-CUP

### 1.1 True CUP — Strict Diagnostic Criteria

A case qualifies as true CUP only when ALL of the following have been exhausted without identifying a primary:

| Diagnostic Step | Modality |
|----------------|----------|
| Comprehensive clinical exam | Including fiberoptic nasopharyngoscopy, laryngoscopy, and oral cavity palpation |
| Cross-sectional imaging | Contrast-enhanced MRI of the head and neck (preferred) or CT with contrast |
| PET/CT | FDG PET/CT from skull base to thighs |
| Panendoscopy with directed biopsies | Including bilateral nasopharyngeal biopsies, tonsillectomy (or deep tonsil biopsies), base of tongue biopsies, and biopsies of any suspicious mucosal areas |
| Viral testing | EBV DNA (plasma) and HPV DNA / p16 IHC on nodal tissue |

**Cases that suspect a primary but fail to biopsy it are NOT true CUP.** If imaging shows any mucosal irregularity, asymmetry, or suspicious area — even if biopsy was negative — the case should be managed as that suspected primary, NOT as CUP.

### 1.2 The Chinese Epidemiological Reality

```
                     Western CUP               Chinese CUP
                         │                         │
              ┌──────────┴──────────┐    ┌─────────┴─────────┐
              │                     │    │                   │
         HPV+ Oropharynx       Others    EBV+ NPC      HPV+ Oropharynx
           (~60-70%)          (~30-40%)  (~50-60%)      (~20-30%)
                                              │
                                    Requires different
                                    diagnostic & therapeutic
                                    strategy from the outset
```

---

## Section 2 — Diagnostic Algorithm: The Two-Step Decision Process

### Step 1: Rule Out Occult Nasopharyngeal Carcinoma

This is the single most important decision point in the Chinese population. The following features strongly suggest an NPC origin:

#### 2.1 Nodal Location Clues

| Cervical Node Location | Most Likely Primary Origin |
|------------------------|---------------------------|
| **Level IIb** (posterior to IJV) | Nasopharynx, oropharynx |
| **Level V** (posterior triangle, especially upper V) | **Nasopharynx** (highly suggestive) |
| **Retropharyngeal nodes** (C1-C3 level) | **Nasopharynx** (pathognomonic) |
| **High cervical nodes above C1 level** | **Nasopharynx** |
| **Level IIa** | Multiple possible origins (NPC, OPC, oral cavity) |
| **Level Ib** | Oral cavity (anterior), submandibular gland |
| **Level III / IV** (isolated, no upper cervical nodes) | Hypopharynx, larynx, thyroid, esophagus |

#### 2.2 Anatomical Basis: Why Pharyngeal Primaries Are More Easily Hidden

There is a fundamental biological difference between pharyngeal and oral cavity mucosa that explains the high prevalence of occult pharyngeal primaries in CUP:

| Feature | Pharyngeal Mucosa (Nasopharynx, Oropharynx, Hypopharynx) | Oral Cavity Mucosa |
|---------|----------------------------------------------------------|---------------------|
| **Epithelial thickness** | Thick, multi-layered, with abundant submucosal lymphoid tissue (Waldeyer's ring) | Thin, stratified squamous epithelium directly overlying muscle/bone |
| **Lymphatic density** | Extremely rich — the pharynx is the most lymph-rich mucosal surface in the head and neck | Sparse to moderate |
| **Surface visibility** | Deep, recessed locations (Rosenmüller fossa, tonsillar crypts, pyriform sinus apex) | Fully visible on routine oral examination |
| **Submucosal spread potential** | High — tumor can spread extensively beneath an intact mucosal surface | Low — tumor becomes exophytic or ulcerated early, visible to the naked eye |
| **Detection threshold** | A 5-10 mm submucosal tumor can be invisible on endoscopy and MRI | A 3-5 mm lesion is usually visible and palpable |

**Clinical consequence**: A microscopic primary measuring only a few millimeters can already produce clinically evident cervical lymph node metastases when located in the pharynx, yet remain completely undetectable on every imaging and endoscopic modality. This is exceedingly rare for oral cavity primaries, which declare themselves at a much smaller size.

#### 2.3 Site-Specific Lymphatic Drainage Atlas — Reverse-Engineering the Primary

Each head and neck squamous cell carcinoma subsite has its own characteristic pattern of first-echelon and subsequent lymph node drainage. When a cervical node is positive, its anatomical level provides strong probabilistic evidence about the primary site:

| Primary Site (Subsite) | First-Echelon Nodes | Second-Echelon / Advanced | Key Discriminating Features |
|------------------------|---------------------|--------------------------|----------------------------|
| **Nasopharynx** | RP (lateral), IIb, upper V | IIa, III, IV, lower V | RP involvement is nearly pathognomonic; Level V involvement with no oral/oropharyngeal primary |
| **Soft palate** | IIa, IIb, RP | III | Often bilateral even for lateralized primaries |
| **Tonsil** | IIa, IIb | III, RP | Level II predominance; RP possible with T3-T4 |
| **Base of tongue** | IIa, IIb, III | RP, IV | Level II-III transition zone involvement |
| **Pharyngeal wall (OPC)** | RP, IIa, IIb | III | RP involvement is common |
| **HPV+ Oropharynx (any subsite)** | IIa, IIb, III | IV, RP | Often cystic nodal appearance on imaging |
| **Oral tongue (anterior 2/3)** | Ib, IIa, III | Contralateral Ib (midline tumors) | Level Ib involvement with no submandibular gland primary |
| **Floor of mouth** | Ia, Ib | IIa | Ia involvement is suggestive |
| **Buccal mucosa** | Ib, IIa | — | Primarily Level Ib |
| **Lower gingiva** | Ib, IIa | — | Perineural spread along inferior alveolar nerve |
| **Hard palate** | IIa (via palatine lymphatics) | RP (via V2 pathway) | Level II without obvious oropharyngeal primary |
| **Supraglottic larynx** | IIa, IIb, III | IV, VI | Bilateral drainage even for lateralized tumors; Level III is key |
|| **Glottic larynx (T1-T2)** | **None** — true vocal cords have NO intrinsic lymphatics | VI (Delphian node), only when advanced | **Critical for CUP**: glottic primaries are essentially excluded as CUP sources. The vocal cord is lymphatic-free; a glottic primary does not metastasize to neck nodes until it invades the paraglottic space or crosses the ventricle into the supraglottis (T3-T4). If a neck node is present with no visible laryngeal mass, the primary is NOT glottic. |
| **Subglottic larynx** | VI, IV | VII (upper mediastinum) | Level VI + Level IV without upper cervical nodes |
| **Hypopharynx (pyriform sinus)** | IIa, IIb, III, RP | IV, VI, VII | RP + Level III-IV with no nasopharyngeal primary |
| **Hypopharynx (posterior wall)** | RP, II, III | IV | RP involvement characteristic |
| **Hypopharynx (postcricoid)** | VI, RP, IV | VII | Level VI involvement prominent |
| **Thyroid (papillary)** | VI, III, IV | II, VII | Level VI is classic; calcifications on CT |
| **Skin (scalp/face)** | V, IIb (parotid nodes) | — | Level V + parotid with no mucosal primary |

#### 2.4 Special Lymphatic Zones — Critical Diagnostic Clues

##### 2.4.1 The Glottic Exclusion Principle

True vocal cords are **lymphatic-free**. The glottic mucosa contains no intrinsic lymphatic channels. A glottic SCC confined to the cord (T1-T2) cannot produce cervical lymph node metastases. Lymphatic spread from the glottis occurs only when the tumor invades:

- **Paraglottic space** (T3) → access to supraglottic lymphatic network
- **Across the ventricle into the supraglottis** → access to Level II-III drainage
- **Through the anterior commissure into the subglottis** → access to Level VI/VII

**Clinical implication for CUP**: If a patient presents with a palpable cervical lymph node and no visible laryngeal mass on laryngoscopy, the primary is **NOT** a glottic cancer. A glottic primary large enough to metastasize is large enough to be visible. Unlike pharyngeal primaries that can hide beneath thick mucosa, the vocal cord's thin mucosa and exposed surface make a T3+ glottic tumor impossible to miss. Therefore, **the glottis should be excluded from the mucosal CTV in all CUP cases** — unless the patient specifically has a visible, biopsy-proven glottic tumor.

This is consistent with the anatomical principle in Section 2.2: the pharynx hides primaries; the oral cavity and glottis do not. The glottis is the "oral cavity equivalent" of the larynx — an exposed, thin, lymphatic-sparse surface where tumors declare themselves early.

##### 2.4.2 Superficial Transit Nodes — Levels VIII, IX, X

These nodal stations communicate between the superficial and deep lymphatic systems. Under normal physiological conditions, they function as **transit stations** — lymphatic fluid passes through them on its way to deep cervical nodes, but they rarely become clinically enlarged because flow-through is unimpeded.

| Level | Location | Normal Function | When They Enlarge |
|-------|----------|----------------|-------------------|
| **VIII** | Parotid region (superficial parotid nodes, preauricular nodes) | Drains scalp, face, external ear → deep cervical system | Post-neck-dissection: disrupted downward flow → retrograde filling |
| **IX** | Upper carotid sheath, near skull base/jugular foramen | Transition zone between intracranial and extracranial lymphatics | Post-neck-dissection: upward retrograde flow along the carotid sheath |
| **X** | Retroauricular / occipital region | Drains posterior scalp → deep cervical system | Post-neck-dissection: collateral pathway activation |

**Clinical implication for CUP**:

- In the **primary/definitive setting** (no prior neck surgery), these transit nodes are almost never involved and do NOT require prophylactic irradiation.
- In the **post-neck-dissection setting**, especially with heavy nodal burden (ECE+, ≥3 LN+, LN ≥3 cm), the disrupted downward lymphatic gradient may cause retrograde or collateral filling of these stations. This is the same mechanism described in the "retrograde flow rule" (Section 3.5 extension). In this scenario, **Levels VIII and IX should be considered for inclusion in the ipsilateral CTV**.

##### 2.4.3 Level VI — The Anterior Oral Cavity Beacon

Level VI (anterior cervical compartment) receives lymphatic drainage primarily from:

- **Anterior floor of mouth**
- **Anterior lower gingiva / mandibular alveolus**
- **Anterior oral tongue tip**
- **Sublingual gland**

Level VI involvement is **rare** in most HNSCC presentations. When it does appear, it carries strong localizing value:

| Level VI Finding | Most Likely Source |
|------------------|-------------------|
| Isolated Level VI node | Anterior oral cavity (floor of mouth, anterior tongue, lower anterior gingiva) |
| Level VI + Level IV (no upper cervical nodes) | Subglottic larynx, cervical esophagus, thyroid |
| Level VI + Level II-III | Supraglottic larynx, or advanced oral cavity with downward spread |

**Pitfall**: In isolation, Level VI involvement without upper cervical nodes is a very specific but uncommon presentation. It should prompt a focused re-examination of the anterior oral cavity and laryngeal subglottis, but in the absence of a visible primary, the mucosal CTV should cover the anterior floor of mouth (crossing midline at the tongue base, per Section 3.3) and the subglottic larynx.

#### 2.5 Ancillary Testing

| Test | NPC-indicative result | Action if positive |
|------|----------------------|--------------------|
| **Plasma EBV DNA** | Detectable or elevated (>0 copies/mL) | Strongly favors NPC origin → proceed as occult NPC |
| **Nodal tissue EBER (ISH)** | Positive | Confirms EBV association → treat as NPC |
| **Nodal tissue p16 IHC** | Positive | Suggests HPV+ OPC (but note: a subset of NPC is also p16+) |
| **MRI nasopharynx** | Asymmetry, mucosal irregularity | Even if biopsy negative, consider NPC treatment |

#### 2.3 Decision Branch: NPC Pathway

```
If ANY of the following are present:
  ├── Level IIb, V, or RP nodal involvement
  ├── Level above C1 involvement
  ├── Plasma EBV DNA positive
  └── Nodal tissue EBER positive

      ↓

TREAT AS OCCULT NASOPHARYNGEAL CARCINOMA

      ↓
  ┌── Nasopharyngeal irradiation (full NPC target volumes)
  ├── Bilateral neck irradiation (as per NPC protocol)
  ├── Chemotherapy as indicated (concurrent ± induction, per NPC stage)
  └── NO neck dissection required unless bulky/multiple nodes
```

### Step 2: If NPC Is Ruled Out — Selective Mucosal Irradiation

If NPC has been excluded through the above pathway:

1. **Selective ipsilateral neck dissection** (levels dictated by nodal location)
2. **Postoperative selective mucosal irradiation** (see Section 3)
3. **Ipsilateral neck irradiation only** (unless contralateral nodes are positive)

---

## Section 3 — Selective Mucosal Irradiation: The Ninth Hospital Technique

### 3.1 The Problem with Pan-Mucosal Irradiation

International guidelines often recommend irradiating the **entire pharyngeal axis** (nasopharynx + oropharynx + hypopharynx + larynx) plus the oral cavity. This approach:

- Results in severe acute mucositis (Grade 3-4 in 40-60% of patients)
- Causes long-term xerostomia and dysphagia
- Irradiates mucosa that has a near-zero probability of harboring the primary

### 3.2 The Selective Mucosal Principle

The primary in CUP is, by definition, **microscopic** — too small to be seen on imaging or endoscopy. It is almost certainly confined to **one anatomical subsite**. Irradiating only the likely subsite(s) achieves local control rates approaching **100%** while dramatically reducing toxicity.

### 3.3 The Four Crossing-Midline Mucosal Structures

Only four mucosal structures in the head and neck normally cross the midline. These define the boundaries for contralateral extension of the CTV:

| Structure | Crossing Pattern | Clinical Implication |
|-----------|-----------------|---------------------|
| **1. Nasopharyngeal roof / posterior wall** | Midline structure by nature | CTV extends across midline to cover the contralateral Rosenmüller fossa |
| **2. Soft palate / hard palate** | Continuous across midline | CTV extends 1-2 cm past midline |
| **3. Tongue base / oral tongue / floor of mouth** | Lingual septum is incomplete anteriorly | CTV extends across midline for tongue base primaries |
| **4. Aryepiglottic fold / epiglottis** | Epiglottis is a midline structure | CTV can cross to contralateral side if supraglottic origin suspected |

**Critical rule**: The mucosal CTV crosses the midline at these four structures — but **the neck CTV remains ipsilateral**. Contralateral neck irradiation is performed ONLY when contralateral nodes are pathologically positive.

### 3.4 Site-Specific Mucosal CTV Templates

#### Suspected NPC Origin (most common in Chinese CUP)

| PTV | Coverage | Dose |
|-----|----------|------|
| PTV-70 | Nasopharynx (bilateral, including both Rosenmüller fossae) | 69.96 Gy / 33 fx |
| PTV-63 | High-risk CTV: parapharyngeal space, skull base | 63 Gy / 33 fx |
| PTV-56 | Low-risk CTV: bilateral II-V + RP (standard NPC field) | 56 Gy / 33 fx |

#### Suspected Oropharyngeal Origin

| PTV | Coverage | Dose |
|-----|----------|------|
| PTV-66 | Ipsilateral tonsillar fossa + tongue base + soft palate (crosses midline 1-2 cm at soft palate) | 66 Gy / 33 fx |
| PTV-60 | Ipsilateral II-IV (unilateral neck only) | 60 Gy / 33 fx |
| Contralateral neck | NOT irradiated unless pathologically positive | — |

#### Suspected Oral Cavity Origin

| PTV | Coverage | Dose |
|-----|----------|------|
| PTV-66 | Ipsilateral oral tongue + floor of mouth (crosses midline at tongue base) | 66 Gy / 33 fx |
| PTV-60 | Ipsilateral Ib + II + III (unilateral neck only) | 60 Gy / 33 fx |
| Contralateral neck | NOT irradiated unless pathologically positive | — |

#### Suspected Hypopharyngeal / Laryngeal Origin

| PTV | Coverage | Dose |
|-----|----------|------|
| PTV-66 | Ipsilateral pyriform sinus + ipsilateral aryepiglottic fold (crosses midline via epiglottis) | 66 Gy / 33 fx |
| PTV-60 | Ipsilateral II-IV + RP (unilateral neck only) | 60 Gy / 33 fx |

### 3.5 The Ipsilateral Neck Principle

Since the primary is microscopic (T0 or Tis-equivalent), the risk of contralateral neck metastasis from the primary itself is negligible. Bilateral neck irradiation is needed only when:

| Scenario | Neck RT |
|----------|---------|
| NPC pathway | Bilateral (standard NPC protocol) |
| Non-NPC pathway + contralateral cN0 | **Ipsilateral only** |
| Non-NPC pathway + contralateral cN(+) | Bilateral |

---

## Section 4 — Treatment Outcomes (Ninth Hospital Data)

Based on the two-step decision process and selective mucosal irradiation (Dou S et al, Oncotarget 2016; Cancer Med 2020):

| Outcome | Result |
|---------|--------|
| **Mucosal control rate** | **~100%** (no emergence of primary in irradiated mucosa) |
| **Emergence of new primary outside RT field** | **~0%** in the NPC pathway; rare in non-NPC pathway |
| **Acute toxicity (≥Grade 3 mucositis)** | **Significantly lower** than pan-mucosal irradiation |
| **Late xerostomia** | Markedly reduced (ipsilateral parotid spared in unilateral cases) |
| **Overall survival** | Comparable or superior to pan-mucosal approaches in published series |

---

## Section 5 — Dose and Fractionation

| Setting | Dose | Fractionation |
|---------|------|---------------|
| Occult NPC pathway (nasopharynx) | 69.96 Gy | 33 fx (SIB) |
| Selective mucosal irradiation (non-NPC) | 66 Gy | 33 fx |
| Ipsilateral elective neck | 54 Gy | 30-33 fx |
| Contralateral neck (if indicated) | 54 Gy | 30-33 fx |
| Neck dissection bed (high-risk) | 60-66 Gy | 30-33 fx |

---

## Section 6 — OAR Constraints for CUP RT

Since the mucosal target is significantly smaller than pan-mucosal irradiation, OARs are better protected:

| OAR | Constraint | Why Better Protected |
|-----|-----------|---------------------|
| Contralateral parotid | ≤ 26 Gy (easily achieved) | Contralateral neck is not irradiated |
| Ipsilateral parotid | ≤ 30-35 Gy | Smaller mucosal target → less exit dose |
| Pharyngeal constrictors | ≤ 50 Gy | Not the entire pharyngeal axis is in the field |
| Oral cavity (uninvolved mucosa) | ≤ 30-40 Gy | Only suspected subsite is irradiated |
| Spinal cord | ≤ 45 Gy | Standard |
| Brainstem | ≤ 54 Gy | Standard |

---

## Section 7 — Integration with International and Domestic Guidelines

This section demonstrates how the Ninth Hospital approach aligns with and extends major international and Chinese clinical practice guidelines for cervical CUP. **There are no contradictions** — the Ninth Hospital strategy is a logical refinement that addresses the specific epidemiological realities of the Chinese population while remaining consistent with the core principles of all major guidelines.

### 7.1 Guideline Summary and Alignment Table

| Guideline / Consensus | Year | Core Recommendation | Ninth Hospital Alignment |
|------------------------|------|---------------------|--------------------------|
| **NCCN (Head and Neck Cancers: Occult Primary)** | 2025 | ① Exhaustive workup (EUA, tonsillectomy, BOT biopsies, NP biopsies) ② Neck dissection ± mucosal RT ③ Pan-pharyngeal mucosal RT considered | ✅ Same exhaustive workup — but adds: EBV DNA, EBER testing as mandatory (not mentioned in NCCN due to low NPC prevalence in the West) |
| **AHNS Guideline (Head Neck, PMID:29159978)** | 2018 | ① Systematic diagnostic evaluation ② Neck dissection as primary surgical management ③ Adjuvant RT decisions based on nodal stage | ✅ Consistent — but adds: nodal location-based algorithm for NPC screening before neck dissection |
| **CSCO 头颈肿瘤诊疗指南** | 2025 | ① PET/CT + 内镜 + 双侧鼻咽活检 + 扁桃体切除 ② 颈部淋巴结清扫 ± 术后放疗 ③ 黏膜腔照射（高危区选择性照射） | ✅ Fully aligned — CSCO already recommends selective mucosal irradiation for the Chinese population |
| **中国医师协会放疗分会 头颈肿瘤共识** | 2023 | ① 强调鼻咽镜检查+EBV检测的重要性 ② 推荐对可疑黏膜区进行选择性照射 ③ 双侧颈部照射仅在高危时 | ✅ Consistent — our two-step NPC-first algorithm operationalizes the Consensus' emphasis on NPC screening |
| **UK National Guidelines (NICE / BAHNO)** | 2020 | ① EUA + ipsilateral tonsillectomy + BOT mucosectomy ② PET/CT ③ Pan-mucosal RT or neck dissection ± RT | ✅ Approach differs in pan-mucosal RT — but this reflects different epidemiology (UK: 70% HPV+ OPC; China: 50%+ NPC) |
| **ASCO/ASTRO (Emerging Consensus)** | 2024 | ① HPV/p16 testing on nodal tissue ② Nodal location guides primary site suspicion ③ De-escalation of mucosal RT volume being investigated | ✅ Fully aligned — ASCO's "nodal location → primary suspicion" principle is exactly what our algorithm formalizes |
| **ESMO (SCCUP genomic landscape, PMID:40499462)** | 2025 | Genomic profiling may aid tissue-of-origin identification; current clinical utility limited | ✅ Consistent — genomic testing is complementary to, not a replacement for, anatomical reasoning |

### 7.2 The Ninth Hospital Approach as a Logical Extension

Rather than contradicting any guideline, the Ninth Hospital approach addresses three gaps in the existing literature:

#### Gap 1: Western guidelines do not account for high NPC prevalence

NCCN, AHNS, and UK guidelines were developed in populations where HPV+ oropharyngeal cancer accounts for 60-70% of CUP cases. NPC is rare (<5%) in these populations, so EBV testing and nasopharyngeal-focused investigation receive minimal emphasis. In China, where NPC is endemic and occult NPC may account for 50%+ of CUP cases, the diagnostic algorithm must be restructured to place NPC screening as the **first decision point**, not an afterthought.

#### Gap 2: Pan-mucosal RT is a one-size-fits-all solution with significant toxicity

International guidelines historically recommended irradiating the entire pharyngeal axis plus the oral cavity. This approach achieves high mucosal control but at the cost of severe acute and late toxicity. The Ninth Hospital data demonstrate that **selective mucosal irradiation achieves equivalent mucosal control (~100%)** while dramatically reducing toxicity. This is consistent with the emerging global trend toward treatment de-intensification (e.g., ECOG 3311 for HPV+ OPC).

#### Gap 3: The lymphatic drainage atlas is underutilized in existing guidelines

While all guidelines acknowledge that nodal location provides clues about the primary site, none provide a systematic, comprehensive lymphatic drainage atlas. The site-specific atlas in Section 2.3 of this skill fills this gap, enabling clinicians to formalize the probabilistic reasoning that experienced specialists do intuitively.

### 7.3 Position Statement

The Ninth Hospital approach to cervical CUP:

1. **Adheres to the same diagnostic rigor** mandated by all major guidelines (exhaustive workup, panendoscopy, directed biopsies, advanced imaging)
2. **Adds NPC-specific screening** (EBV DNA, EBER ISH, nodal location algorithm) as a mandatory first-step decision point — a necessary adaptation for Chinese populations
3. **Refines mucosal irradiation** from pan-pharyngeal to selective — consistent with the global trend toward de-escalation and supported by Ninth Hospital's published outcomes
4. **Formalizes reverse-engineering of the primary** through a comprehensive lymphatic drainage atlas — a tool that enhances, rather than contradicts, guideline-directed care

This approach is fully compatible with all major guidelines and represents a population-specific refinement that should be considered for inclusion in future editions of Chinese national guidelines.

---

## Section 8 — Key References

1. Dou S, Qian W, Ji Q, Wang Z, Zhu G, et al. Tailored multimodality therapy guided by a two-step decision making process for head-and-neck cancer of unknown primary. *Oncotarget*. 2016;7(26):40077-40087. PMID: 27223430. DOI: 10.18632/oncotarget.9492.

2. Dou S, et al. Long-term results of elective mucosal irradiation for head and neck cancer of unknown primary in Chinese population: The Shanghai Ninth People's Hospital experience. *Cancer Medicine*. 2020;9(5):1721-1729. PMID: 31953927. DOI: 10.1002/cam4.2856.

3. NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers — Occult Primary. Version 3.2025.

4. Gregoire V, et al. Delineation of the neck node levels for head and neck tumors. *Radiother Oncol*. 2014;110(1):172-181.

5. Lee NY, et al. OAR dose constraints for head and neck RT. *Int J Radiat Oncol Biol Phys*. 2018.

---

## Section 9 — Clinical Algorithm Flowchart

```
Cervical lymph node — metastatic carcinoma
                 │
    ┌────────────┴────────────┐
    │                         │
  Exhaustive workup        Primary found
  (MRI, PET, EUA,           → Treat as known
   bilateral NP Bx,          primary
   tonsillectomy,
   BOT biopsies,
   EBV DNA, HPV/p16)
    │
    │  Primary NOT found
    │
    ▼
┌─────────────────────────────────────┐
│  STEP 1: Is this Occult NPC?        │
│  ┌─────────────────────────────────┐│
│  │ Nodal location:                 ││
│  │  Level IIb / V / RP / >C1?      ││
│  │  AND/OR                         ││
│  │  EBV DNA (+) / EBER (+) ?       ││
│  └─────────────────────────────────┘│
│                                     │
│         YES ────────┐     NO ───────┐
└─────────────────────┼───────────────┘
                      │               │
                      ▼               ▼
              ┌──────────────┐  ┌──────────────────┐
              │ TREAT AS     │  │ STEP 2: Selective │
              │ OCCULT NPC   │  │ Neck Dissection   │
              │              │  │ + Selective       │
              │ Full NPC RT  │  │ Mucosal RT        │
              │ Bilateral    │  │ (ipsilateral      │
              │ neck + NP    │  │ neck only)        │
              │ neck + NP    │  │ neck only)        │
              └──────────────┘  └──────────────────┘
```

---

## Section 10 — Emerging Evidence (2021-2026): Literature Supporting the Selective Approach

The past five years have seen a decisive global shift toward the selective, individualized approach embodied in this skill. Below is a summary of key publications and how their findings align with — and in some cases independently validate — the Ninth Hospital methodology.

### 10.1 Evidence for Selective Mucosal Irradiation (Not Pan-Mucosal)

| Study | Year | Journal | Key Finding |
|-------|------|---------|-------------|
| **Ghatasheh et al.** PMID:35905781 | 2022 | *Radiother Oncol* | IMRT enables risk-tailored individualized mucosal and nodal CTVs in HNCUP. Outcomes with selective approach are favorable. **Conclusion**: "Risk-tailored CTV selection is feasible and achieves excellent disease control." |
| **Chen et al.** PMID:37844736 | 2023 | *Radiother Oncol* | Title: "No longer cutting down the tree to get an apple." Comprehensive review of RT paradigm refinement for CUP in the HPV era. **Key message**: Pan-mucosal RT is historical; modern RT should target only the most probable mucosal site(s). |
| **Nielsen et al. (DAHANCA)** PMID:41016667 | 2025 | *Radiother Oncol* | Danish national study analyzing failure patterns in HNSCCUP. Two strategies evaluated: mucosal RT vs omission with targeted salvage. **Key finding**: Both strategies are viable; HPV and EBV status should guide which is chosen. The study validates that mucosal RT omission is safe in selected patients. |

**Integration into skill**: These three studies independently confirm the core principle of Section 3 (Selective Mucosal Irradiation). The Danish national data specifically validate that HPV and EBV status — exactly the two viral markers in our Step 1/Step 2 algorithm — should determine mucosal RT strategy.

### 10.2 Evidence for Unilateral (Not Bilateral) Neck Irradiation

| Study | Year | Journal | Key Finding |
|-------|------|---------|-------------|
| **Oebel et al.** PMID:38192301 | 2024 | *Clin Transl Radiat Oncol* | Explicitly asked: "Is bilateral RT necessary for unilateral SCC-CUP?" Systematic review. **Conclusion**: Contralateral neck failure rates are very low (<5%) in patients with unilateral disease treated with ipsilateral-only RT. Bilateral RT provides no oncologic benefit for truly unilateral presentations. |
| **Holm et al.** PMID:37815913 | 2023 | *Acta Oncol* | Proton vs photon planning study for HNCUP. **Incidental finding**: "New data suggest that omission of the contralateral nCTV and mCTV results in few recurrences." This was a secondary observation in a dosimetric study — yet it independently validates the ipsilateral approach. |
| **Ludwig et al.** PMID:40415030 | 2025 | *Sci Rep* | Probabilistic model of bilateral lymphatic spread in HNSCC. **Finding**: Contralateral occult involvement probability is extremely low (<3%) for lateralized primary tumors with unilateral clinical nodal disease. The model supports personalized, risk-based CTV-N selection rather than routine bilateral coverage. |

**Integration into skill**: The 2024 Oebel study directly asks the same question as our Section 3.5 (Ipsilateral Neck Principle) and arrives at the same answer — contralateral failure <5%. The 2025 Ludwig probabilistic model provides mathematical support: contralateral risk for lateralized primaries is below 3%. This moves the burden of proof: bilateral RT must now be justified, rather than being the default.

### 10.3 Evidence for Post-Neck-Dissection Target Volumes

| Study | Year | Journal | Key Finding |
|-------|------|---------|-------------|
| **Iqbal et al.** PMID:38545823 | 2024 | *Clin Otolaryngol* | Comprehensive narrative review of RT target volumes after neck dissection for HNSCCUP. **Key findings**: (1) Post-dissection CTV should include the dissected nodal basin plus one adjacent uninvolved level. (2) Mucosal RT target selection is independent of surgical approach and should be based on the same risk stratification used in definitive RT. (3) Evidence for routine contralateral neck RT after unilateral neck dissection is weak. |

**Integration into skill**: This review directly supports our post-dissection approach in Section 3.5 extension (Retrograde Flow Rule) — the principle that dissected basins need wider coverage, but mucosal targets and contralateral decisions remain driven by the same diagnostic algorithm. The review's recommendation to include "one adjacent uninvolved level" aligns with our concept of abnormal post-dissection lymphatic flow.

### 10.4 Evidence for Standardized Diagnostic Algorithms

| Study | Year | Journal | Key Finding |
|-------|------|---------|-------------|
| **Townes et al.** PMID:42059064 | 2026 | *Otolaryngol Head Neck Surg* | Evaluated the impact of implementing a standardized institutional diagnostic algorithm for HPV-associated HNSCCUP. **Key finding**: Algorithm implementation significantly improved primary site detection rates and led to more consistent treatment selection. |

**Integration into skill**: This study supports the very premise of this skill — that a standardized algorithmic approach improves diagnostic accuracy and treatment consistency. Our two-step algorithm (Step 1: exclude occult NPC → Step 2: reverse-engineer from nodal location + viral status) is precisely the type of structured decision tool that this study validates.

### 10.5 Summary: The Global Trend Aligns with the Ninth Hospital Approach

| Principle | Ninth Hospital (established) | Recent Literature (2021-2026) |
|-----------|---------------------------|-------------------------------|
| Selective over pan-mucosal RT | ✅ Since 2016 | ✅ Validated: Ghatasheh 2022, Chen 2023, Nielsen 2025 |
| Ipsilateral neck over bilateral | ✅ Core principle | ✅ Validated: Oebel 2024, Holm 2023, Ludwig 2025 |
| Post-dissection CTV extension | ✅ Retrograde flow rule | ✅ Supported: Iqbal 2024 |
| Standardized diagnostic algorithm | ✅ Two-step decision | ✅ Validated: Townes 2026 |
| Viral status (EBV/HPV) guides strategy | ✅ Step 1/Step 2 | ✅ Validated: Nielsen 2025 (DAHANCA) |

**Bottom line**: The principles embedded in this skill since 2016 — selective mucosal RT, ipsilateral neck, viral-guided stratification — are now being independently validated by international multicenter studies. The global standard is moving toward the Ninth Hospital approach, not away from it.

---

*This clinical framework was developed through the clinical experience and published research of the Department of Radiation Oncology, Shanghai Ninth People's Hospital, Shanghai Jiao Tong University School of Medicine. It is intended for educational and clinical reference purposes.*


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
