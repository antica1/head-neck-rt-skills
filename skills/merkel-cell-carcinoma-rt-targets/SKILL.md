---
name: merkel-cell-carcinoma-rt-targets
description: "皮肤默克尔细胞癌（MCC）放疗靶区勾画——SLNB 分水岭、原发灶+引流区。"
version: 1.0.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [head-neck, radiotherapy, target-delineation, merkel-cell-carcinoma, cutaneous, neuroendocrine]
    triggers_on: [默克尔细胞癌, 默克尔, MCC, Merkel, 皮肤神经内分泌癌, 皮肤神经内分泌, 神经内分泌癌皮肤, 前哨淋巴结活检, SLNB, merkel cell carcinoma, cutaneous neuroendocrine carcinoma]
    related_skills: [head-neck-sarcoma-rt-targets, sinonasal-rt-targets, head-neck-dvh-plan-review]
---

> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗中心整理。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.

# 皮肤默克尔细胞癌（MCC）放疗靶区勾画

> **MCC 是高度放射敏感、但局部区域复发率极高的皮肤神经内分泌癌。** 头颈部为好发部位之一。加载本 Skill 处理 MCC 的根治性/术后放疗靶区。
>
> ⚠️ **MCC 无 PNI 神经径路框架——不套用 ACC 的"沿神经追踪至海绵窦"规则。** 不同瘤种规则不互通。

---

## 何时用（触发）

- 病例为**皮肤默克尔细胞癌／皮肤神经内分泌癌（MCC）**，需要放疗靶区规划（根治性/术后/区域）；
- 用户问 **MCC 颈部预防性照射、SLNB、ENI vs 颈清扫、头颈部引流区、剂量**；
- 头颈部皮肤结节活检证实为 MCC，需判断靶区与颈部策略。

> 若为**鼻腔鼻窦**神经内分泌癌（非皮肤原发），叠加 `sinonasal-rt-targets`；若需合并其他头颈瘤种规则，先确认无规则冲突。

---

## 🔑 铁律清单

| # | 铁律 | 触发条件 |
|---|------|---------|
| 1 | **SLNB 是决策分水岭**——先做前哨淋巴结活检，再定颈部方案；未明确前无法定稿 | 所有 MCC |
| 2 | **MCC ≠ ACC/鳞癌**——播散以淋巴引流为主，不套用 PNI 神经径路框架 | 所有 MCC |
| 3 | **原发灶 CTV = 瘤床外放 3-5cm（皮肤表面）+ 深度 ≥1.5cm + in-transit 皮肤** | 原发灶靶区 |
| 4 | **必须加 bolus**——皮肤即靶区，无 bolus 表面剂量严重不足 | 原发灶靶区 |
| 5 | **头颈部 MCC 的 SLNB 假阴性率高（约 17-20%，因引流变异/多引流区）→ SLNB 未做/不可靠时，经验性区域 RT（ENI）是合理例外** | 头颈部 MCC |
| 6 | **ENI 能替代颈清扫的"治疗"作用，替代不了"分期"作用**——先 SLNB 分期，再决定 RT 或清扫 | 颈部决策 |
| 7 | **剂量分层**：未做 SLNB 亚临床预防 46-50；SLN 阳性未清扫 50-56；多发阳性/ENE+ 60-66 | 剂量 |
| 8 | **术后放疗 8 周内开始**（延迟显著增加局部区域失败） | 时机 |
| 9 | **高放射敏感**——体弱/合并症多者，中等甚至超大分割与常规分割疗效相当，可个体化选择 | 体弱患者 |
| 10 | **区域照射范围按皮肤淋巴显像结果**——头颈部引流多站、变异大，含非常规站（外颈静脉 EJ、面颊 perifacial） | 区域靶区 |

---

## 一、为什么 MCC 必须独立

| 维度 | 头颈鳞癌（SCC） | 其他头颈瘤种 | MCC |
|------|---------------|------------|-----|
| **播散方式** | 淋巴 + 局部 | ACC＝沿神经 PNI | **淋巴引流为主**（区域淋巴结第一站） |
| **放射敏感性** | 中 | 中-低 | **高度放射敏感** |
| **靶区焦点** | 瘤床 + 颈 | ACC＝神经径路 | **瘤床 + 引流淋巴结区 + in-transit 皮肤** |
| **颈部决策** | 按 N 分期 | ACC＝按 PNI Tier | **按 SLNB 状态** |
| **系统治疗** | 化疗 | — | **免疫治疗（avelumab/pembrolizumab）** |

> MCC 隐匿转移率高，凡原发灶任何大小的 cN0 均应行 SLNB 分期（AJCC 第 8 版）。分期用 PET-CT 优于 CT（约 17% 因 PET 升级）。

---

## 二、SLNB 决策分水岭（颈部策略按此三分）

| 情形 | 颈部处理 |
|------|---------|
| **① SLNB 阴性** | 不常规做区域 RT，观察（NCCN 首选）。头颈部假阴性率高 → MDT 可对高危者酌情区域 RT |
| **② SLNB 未做／无法做／不可靠**（头颈部复杂引流、免疫抑制、既往淋巴结手术） | **选择性颈部照射（ENI）是合理选项**，或补做颈清扫；二选一 |
| **③ SLNB 阳性／临床 N+** | 区域 RT（或清扫 + 术后 RT）；微转移 50-56 Gy；多发阳性/ENE+ 60-66 Gy |

> **循证**：唯一前瞻性随机试验（Jouary 2012, *Ann Oncol*，未做病理分期）——预防性区域 RT 显著降低区域复发（3 年区域复发 **0% vs 17%**），**但无生存获益**，属"降区域复发"决策。SLN 阳性时 RT 与补做性清扫结局相当（Lee 2019, PMID 30556118；PMID 30311164）。

---

## 三、原发灶靶区

| 项 | 内容 |
|---|---|
| **CTV 范围** | 瘤床外放 **3-5 cm**（皮肤表面，考虑解剖界限） |
| **深度** | **≥1.5 cm**（达皮下/浅层肌肉） |
| **必含** | **in-transit 皮肤**——原发灶与引流区之间的皮下淋巴管 |
| **技术** | **必须加 bolus**（皮肤是靶区）；浅表局限病灶可用电子线；涉区域淋巴结用 IMRT/VMAT + IGRT |
| **剂量** | 术后 **50-56 Gy / 25-28 fx**（Scottish/DEGRO）；R1 → 50-60 Gy；R2 → 50-66 Gy |
| **时机** | 术后 **8 周内**启动 |

---

## 四、区域淋巴结：ENI vs 颈清扫（功能区分）

| 颈清扫承担的功能 | ENI 能否替代 |
|---|---|
| **治疗**（清除亚临床/微转移） | ✅ 能——MCC 高度放射敏感，区域 RT 与清扫区域控制相当 |
| **分期**（提供病理 N） | ❌ 不能——照完仍是临床 N0，失去预后与后续决策依据 |

> **结论：先 SLNB 分期，再据结果决定 RT 还是清扫。** SLNB ≠ 颈清扫，二者不可混为一谈。头颈部 MCC 倾向 ENI（放疗敏感、清扫并发症多、可与原发灶连续覆盖 in-transit）。临床 N+、多发/ENE+ → 需清扫 + 术后 RT。

---

## 五、头颈部 MCC 引流区（按原发部位）

> 皮肤淋巴显像显示头颈部引流**多站、变异大**（PMID 27554510；*JPRAS* 2025）——**非常规站（外颈静脉 EJ、面颊 perifacial）在 MCC 靶区中重要，常规头颈分区会漏**。勾画前应参考 SLNB/淋巴显像结果。

| 原发部位 | 需覆盖的引流区（同侧） |
|---------|---------------------|
| **面颊／颧／颞** | 耳前／腮腺内（第一站）+ **Ⅱ**（最常见）+ ⅠB + **外颈静脉(EJ) + 面颊(perifacial)**；Ⅲ 一般含 |
| **额／头顶** | 耳前／腮腺 + Ⅱ + ⅡB + 耳后/枕后 |
| **鼻／唇** | 面颊(perifacial) + ⅠB + Ⅱ |
| **耳** | 耳前／腮腺 + ⅡB + 耳后 |
| **后枕／头皮** | 枕后 + 耳后 + Ⅴ |

> 对侧通常**不照**（除非跨中线或中线原发）。原发灶与上述各区之间以 in-transit 皮下淋巴管连续覆盖，全程加 bolus。

---

## 六、剂量速查（NCCN MCC v2.2026 / DEGRO 2026）

| 临床情形 | 剂量 |
|---------|------|
| 临床 N0、有亚临床风险（未做 SLNB） | **46-50 Gy** |
| SLNB 阳性、未清扫 | **50-56 Gy** |
| 清扫后多发阳性 / ENE+ | **60-66 Gy** |
| 原发灶术后 R0 | **50-56 Gy** |
| 原发灶 R1 / R2 | 50-60 / 50-66 Gy |
| 体弱/不宜长程（少分割） | 44-50 Gy/20 fx；30-35 Gy/10 fx；高度姑息 8 Gy×1 |

---

## 七、OAR 与常见陷阱

> OAR 按照射部位参考相应头颈/颅底常规约束（视路/脑干/颞叶/腮腺等）。技术：bolus + IGRT（IMRT/质子时）。

| 陷阱 | 处理 |
|------|------|
| **漏掉 in-transit 皮肤** | 原发灶↔引流区皮下淋巴管必含，连续覆盖 |
| **不加 bolus** | 皮肤表面剂量严重不足 → 加 bolus 保证皮肤剂量 |
| **未做 SLNB 却按 SCC 照全颈** | 优先 SLNB；未做/不可靠时才做 ENI，范围按皮肤淋巴显像 |
| **套用 ACC 的 PNI 神经径路** | MCC 走淋巴引流，不照神经径路至颅底——两瘤种不互通 |
| **遗漏非常规引流站** | EJ/面颊(perifacial)等站在面颊/颧病灶常被漏 |

---

## 八、全身治疗（MDT 协同）

- **辅助免疫**：II-III 期 MCC 的辅助免疫（avelumab/pembrolizumab，如 ADMEC-O/JAVELIN 体系）已进入标准讨论范围——放疗科宜与肿瘤内科协同。
- 化疗无辅助生存获益（放疗/化疗在 III 期均无显著 OS 获益）——鼓励入组（新）辅助系统治疗临床试验。

---

## 附：靶区规划摘要（可粘贴入首次病程录）

```
═══════════════════════════════
  放疗靶区规划 · 默克尔细胞癌
═══════════════════════════════
诊断：____（部位）皮肤默克尔细胞癌（MCC）  cT__N__M0（AJCC 第 8 版）
手术：____（WLE ± SLNB；SLNB：□已做 □未做 结果：____）
SLNB 假阴性风险：□头颈部（高） □其他

方案：□ 术后 PORT  □ 根治性 RT  □ 区域 RT   __ Gy / __ fx

原发灶 CTV：瘤床外放 3-5cm + 深度 ≥1.5cm + in-transit（___ Gy；加 bolus）
区域：□ 同侧耳前/腮腺 + ⅠB + Ⅱ(+Ⅲ) + EJ/面颊（___ Gy）  □ 不做区域 RT
豁免：______（理由：______）

主治：____________　日期：____________
═══════════════════════════════
```

---

## 参考文献

| 文献 | 来源／标识 |
|------|-----------|
| **NCCN Guidelines: Merkel Cell Carcinoma v2.2026** | NCCN（剂量分层、SLNB 与区域处理路径） |
| **ESMO–EURACAN CPG: Merkel-cell carcinoma** | Lugowska I, et al. 2024. DOI:10.1016/j.esmoop.2024.102977（SLNB 假阴性 17.1%、头颈/中线引流例外、50-60 Gy） |
| **Scottish Consensus Clinical Management Guideline: Merkel Cell Cancer** | *J Plast Reconstr Aesthet Surg* 2025（SLNB 不可靠时 ENI/清扫、PORT 50-60 Gy、CTV+3-5cm、≥1.5cm 深） |
| **DEGRO Dermatooncology Working Group** | Elsayad K, et al. *Strahlenther Onkol* 2026;202:1003-1010. PMID:42714572（剂量与分割、靶区 3-5cm、bolus、8 周内） |
| **Jouary T, et al.** | *Ann Oncol* 2012;23(4):1074-1080. DOI:10.1093/annonc/mdr318（唯一前瞻性随机：预防性区域 RT 3 年区域复发 0% vs 17%，无 OS 获益） |
| **Lee JS, et al.** | *Ann Surg Oncol* 2019;26(2):386-394. PMID:30556118（SLN 阳性 CLND vs RT 结局相当） |
| **Management of SLN metastasis in MCC (CLND vs RT vs both)** | *Ann Surg Oncol* 2019. PMID:30311164 |
| **Drainage patterns to nontraditional nodal regions & level IIB in cutaneous head/neck malignancy** | PMID:27554510（面颊/颧→EJ 站、perifacial、ⅡB） |
| **Oncoplastic surgery for cutaneous head and neck cancers (SNB)** | *JPRAS Open* 2025. DOI:10.1016/j.jpra.2025.10.007（颧/颊→耳前/腮腺、Ⅱ、ⅠB、Ⅴ） |

> ⚠️ 网络可得文献的 PMID/DOI 已逐条核对；正式引用前仍建议再核。
