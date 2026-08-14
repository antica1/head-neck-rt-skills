---
name: head-neck-lymphoma-rt-targets
description: "头颈部淋巴瘤放疗靶区勾画——ISRT/INRT框架、亚型剂量、颈部解剖与OAR。"
version: 1.1.0
author: 朱国培 / Shanghai Ninth People's Hospital
license: CC BY-NC-SA 4.0
metadata:
  hermes:
    tags: [lymphoma, hodgkin, non-hodgkin, radiotherapy, head-neck, ISRT, INRT]
    triggers_on: [淋巴瘤, 霍奇金, 非霍奇金, ISRT, INRT, 受累部位放疗, 受累淋巴结放疗, ENKTL, 鼻型NK/T, 眼眶MALT, lymphoma, hodgkin, non-hodgkin]
    related_skills: [head-neck-rt-methodology]
---

> **原创声明**：本 Skill 所含临床框架为上海交通大学医学院附属第九人民医院口腔颌面头颈肿瘤科放疗中心原创知识产权。授权采用 CC BY-NC-SA 4.0（署名-非商业-相同方式共享）。引用：朱国培, 上海九院放疗中心. 头颈肿瘤放疗靶区勾画 Skill 系列 [OL]. GitHub: antica1, 2026.

---

# 头颈部淋巴瘤放疗靶区勾画 Skill

> 头颈部淋巴瘤包括霍奇金淋巴瘤（HL）和非霍奇金淋巴瘤（NHL）。放疗以 **ISRT（受累部位放疗）** 和 **INRT（受累淋巴结放疗）** 为核心框架，与头颈部鳞癌的 ENI（全颈预防照射）有本质区别。

---

## 一、适用范围

| 适用 | 不适用 |
|------|--------|
| 🔘 头颈部结内淋巴瘤（HL & NHL） | ❌ 结外淋巴瘤（MALT 等另行处理） |
| 🔘 颈淋巴结受累（Ib-VI区） | ❌ Waldeyer 环原发淋巴瘤（单独 Skill） |
| 🔘 放疗作为巩固/根治手段 | ❌ 全身系统治疗决策 |
| 🔘 ISRT/INRT 靶区勾画 | ❌ 化疗方案选择 |

---

## 二、ISRT vs INRT：核心框架

```
现代头颈部淋巴瘤放疗 = ISRT（第1选择）或 INRT（化疗前PET可用时）
```

| 概念 | ISRT（Involved Site RT） | INRT（Involved Node RT） |
|------|-------------------------|-------------------------|
| 定义 | 化疗前**整个受累淋巴结站/结外区** | 化疗前**单个阳性淋巴结**本身 |
| 前提 | 化疗前 PET/CT 可用 | 化疗前高质量 PET/CT **必须**可用 |
| 靶区大小 | 整个解剖室（如整个右Ib区） | 阳性LN外扩 + 解剖修剪 |
| 适用场景 | 绝大多数场景（NHL + HL） | 化疗前PET精确显示单站单发小LN |
| 剂量 | 20-36 Gy（亚型有关） | 同 ISRT |
| 安全性 | 设边界宽松，**推荐首选** | 要求极严格QA，无使用经验时慎用 |

### 铁律

> **ISRT = 按化疗前 PET/CT 上的受累区，经解剖边界修剪后作为 CTV**
>
> ❌ 不是照整个淋巴链
> ❌ 不是预防下级淋巴引流区
> ❌ 不是照对侧
> ✅ 只照受累的那一站/区

---

## 三、HL vs NHL：分层决策树

```
┌─────────────────────────────────────────────┐
│      头颈淋巴瘤 → 先辨 HL vs NHL            │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
     HL                    NHL
──────────────────────────────────────────────
│ 蔓延模式 │                     │
 连续性（相邻站依次）           跳跃性（可跨站）
│ ISRT范围 │                     │
 包整个受累解剖室              包受累LN本身 + 相邻
                              小LN（同站内）
│ 剂量 │                        │
 20-30 Gy（极低剂量）          24-36 Gy（亚型决定）
│ 晚期效应 │                    │
 极重要（年轻患者为主）        重要（中老年为主）
│ OAR重点 │                     │
 第二原发、心血管、甲状腺      口腔黏膜、下颌骨、唾液腺
└──────────────────────────────┘
```

---

## 四、NHL 头颈部 ISRT 靶区勾画

### 4.1 常见亚型与剂量

| 亚型 | 化疗后CR（巩固） | 化疗后PR（根治） | 单纯放疗 |
|------|:---------------:|:---------------:|:--------:|
| **DLBCL** | 30 Gy / 15 fx | 30-36 Gy / 15-18 fx | 36-40 Gy |
| **滤泡性淋巴瘤（FL）** 1-2级 | 24 Gy / 12 fx | 24-30 Gy / 12-15 fx | 24-30 Gy |
| **FL 3级** | 30 Gy / 15 fx | 30-36 Gy / 15-18 fx | 30-36 Gy |
| **MALT（结外边缘区）** | 24-30 Gy / 12-15 fx | — | 24-30 Gy |
| **套细胞淋巴瘤（MCL）** | 30-36 Gy | 30-36 Gy | — |
| **Burkitt** | 一般不做RT巩固 | — | — |
| **淋巴母细胞淋巴瘤** | 一般不单独用RT | — | — |

### 4.1B DLBCL 风险分层放疗决策（2024 JNCC 荟萃分析，李晔雄团队）

> 🔥 **DLBCL 放疗决策从"一刀切巩固"走向风险分层个体化**。Wang J, Li Yexiong et al. J Natl Cancer Cent 2024;4:249-9（7 RCT + 52 回顾性，59 项）。

```
DLBCL 化疗后 → 按 PFS 率风险分层决策放疗：
  高危（PFS≤40%）   → 辅助 RT 强烈获益（OS 绝对获益 ~21%，HR 0.48）✅ 必做
  中危（40-80%）    → 获益递增（60-80%：HR 0.79；40-60%：HR 0.47）✅ 建议
  低危（PFS>80%）   → 绝对获益 <5%（利妥昔单抗时代 HR 0.70）→ 可豁免 RT ✅ 去强化
```

| 风险层（CT 后 PFS 率） | RT 的 OS 获益 | 决策 |
|:--:|:--:|:--:|
| >80%（低危） | 绝对获益 <5%（HR 0.70，0.51-0.97） | **可豁免 RT**——降强度减毒 |
| 60-80% | HR 0.73（0.59-0.91） | 建议 RT |
| 40-60% | HR 0.47（0.32-0.71） | 强烈建议 RT |
| ≤40%（高危） | **绝对获益 ~21%**（HR 0.48，0.36-0.63） | **必做 RT** |

> **要点**：RT 带来的 PFS 获益与 OS 获益显著正相关（r=0.639-0.882，P<0.001）——PFS 获益可转化为 OS 获益。**低危早期 DLBCL 豁免辅助 RT** 是去强化方向；中高危必须 RT。

### 4.2 NHL ISRT 靶区构建三步法

```
STEP 1：确定化疗前 GTV
        └─ 化疗前 PET/CT 上的 FDG-avid 阳性区域
           （淋巴结或结外受累区）

STEP 2：解剖约束 → CTV
        └─ 以自然解剖屏障修剪：
           ✅ 骨皮质边界 → 外扩中止
           ✅ 筋膜/肌肉边界 → 不跨过
           ✅ 空腔器官边界 → 不向腔内延伸
           ✅ 同站内紧邻的小LN（3-5mm内）→ 纳入
           
        └─ ❌ 不做跨站预防：
           右侧Ib受累 → 不包右侧II区
           右侧Ib受累 → 不包对侧颈
            
STEP 3：ITV（呼吸运动，适用时）
        └─ 颈下部/锁骨上区需考虑
           
STEP 4：PTV
        └─ 3-5mm（每日IGRT可缩至3mm）
```

### 4.3 颈部各区特异要点

| 区 | NHL ISRT 要点 |
|----|--------------|
| **Ia（颏下）** | 罕见单发。双侧Ia可受累（中线结构） |
| **Ib（颌下）** | 单侧受累不包对侧。注意保护对侧颌下腺 |
| **II（颈上深）** | Ib+II同时受累→照Ib+II各自ISRT区 |
| **III（颈中深）** | II+III同时受累→照II+III各自ISRT区 |
| **IV（颈下深）** | 注意锁骨上/胸廓入口 |
| **V（颈后三角）** | 注意斜方肌前缘边界 |
| **VI（颈前/气管食管沟）** | 注意甲状腺保护 |
| **咽后** | 头颈NHL可累及。照受累侧咽后间隙单侧 |

---

## 五、HL 头颈部 ISRT 靶区勾画

### 5.1 剂量体系

| 场景 | 剂量 | 分割 |
|------|:----:|:----:|
| **早期（IA-IIA）预后良好 + PET-CR** | **20 Gy** | 10 fx × 2 Gy |
| 早期预后不良 + PET-CR | 30 Gy | 15 fx × 2 Gy |
| 晚期（III-IV）化疗后巩固 | 30 Gy | 15 fx × 2 Gy |
| 残留/PR（非CR） | 30-36 Gy | 15-18 fx（可SIB） |
| 单纯放疗（极少数IA） | 30-36 Gy | 15-18 fx |

> **HL 是所有成人恶性肿瘤中放疗剂量最低的一类。**
> 
> 20 Gy 即可根治化疗后CR的早期预后良好 HL（RAPID、H10、EORTC 方案）。

### 5.2 HL ISRT vs NHL 的区别

HL 的**连续性蔓延**特性导致其 ISRT 范围略宽于 NHL：

| | NHL | HL |
|:-:|:---:|---|
| CTV | 阳性LN + 相邻小LN | 受累**整个解剖室** |
| 举例 | 右Ib 单发LN 2cm → 包该LN+3mm+解剖修剪 | 右Ib 单发LN 2cm → 包**整个右Ib室** |
| 相邻站 | ❌ 不预防 | ⚠️ 一般不预防，但受累区大时自然延伸可能触及 |

### 5.3 预后分组（EORTC/GHSG 2025）

```
┌────────────────────────────────────────────────┐
│ 早期（I-II）HL 预后分层（用于剂量决策）          │
├────────────────────────────────────────────────┤
│                                                  │
│ 预后良好（无风险因素）→ 20 Gy                    │
│ 预后不良（≥1个风险因素）→ 30 Gy                  │
│                                                  │
│ 风险因素：                                        │
│ ① 巨块病（纵隔比>0.33 或 LN > 5cm）             │
│ ② 结节硬化型                                     │
│ ③ B症状（发热/盗汗/体重下降）                    │
│ ④ ESR ≥ 30（有B症状）或 ≥ 50（无B症状）          │
│ ⑤ ≥3个淋巴站受累（GHSG标准）                     │
│ ⑥ 年龄 ≥ 50岁                                    │
│                                                  │
└────────────────────────────────────────────────┘
```

---

## 六、颈部常见受累站的 ISRT 靶区解剖

### 6.1 Level Ib（颌下区）ISRT

```
上界：下颌舌骨肌上缘
下界：舌骨水平
前界：二腹肌前腹前缘
后界：颌下腺后缘 / 下颌骨升支前缘
外界：下颌骨内侧骨皮质
内界：舌骨舌肌 / 茎突舌骨肌

☞ 右Ib单发LN → 包整个右Ib室（HL）或LN+修剪（NHL）
☞ ⚠️ 不包对侧Ib
☞ ⚠️ 颌下腺无法避开——口干必然
☞ ⚠️ 舌下神经在舌骨舌肌表面走行
```

### 6.2 Level II（颈上深区）ISRT

```
上界：颈静脉孔下缘 / 颅底
下界：舌骨下缘
前界：下颌骨升支后缘 / 颌下腺后缘
后界：胸锁乳突肌后缘 / 头夹肌前缘
外界：胸锁乳突肌深面
内界：颈内动脉内缘

☞ II+III均受累→各自ISRT区并拢
☞ 颈静脉孔附近注意舌下神经和第IX-XI颅神经
☞ 腮腺尾叶通常在II区前方——剂量低时一般无临床影响
```

### 6.3 咽后间隙（RPN）ISRT

```
上界：颅底
下界：舌骨上缘
前界：咽缩肌后壁
后界：颈长肌前筋膜
外界：颈内动脉内侧

☞ 单侧受累→照单侧咽后间隙（不强制包双侧）
☞ 注意颈交感干——Horner综合征风险
☞ 咽后LN与Ib区不通，分别勾画
```

---

## 七、OAR 优先级与约束

### 7.1 NHL（中老年为主）OAR

| OAR | 约束 | 级别 |
|-----|:----:|:----:|
| 同侧腮腺 Dmean | ≤ 26 Gy | ★★★ |
| 对侧腮腺 Dmean | ≤ 20-24 Gy | ★★★ |
| 对侧颌下腺 | 尽量避开 | ★★ |
| 口腔 Dmean | ≤ 30 Gy | ★★ |
| 下颌骨 Dmax | ≤ 50 Gy（骨坏死） | ★★ |
| 脊髓 Dmax | ≤ 40 Gy | ★★★ |

### 7.2 HL（年轻为主）OAR

| OAR | 约束 | 级别 | 晚期效应 |
|-----|:----:|:----:|:---------|
| 甲状腺 Dmean | ≤ 20 Gy | ★★★ | 甲减（TSH终身监测） |
| 颈动脉 Dmean | ≤ 10 Gy | ★★★ | 心血管事件（10-20年后） |
| 乳腺（年轻女性） | 远离子野 | ★★★ | 第二原发乳腺癌 |
| 口腔/下颌骨 | 同NHL | ★★ | |
| 食管入口 | Dmean ≤ 15 Gy | ★★ | 吞咽困难 |
| 脊髓 Dmax | ≤ 36 Gy（HL 更低更安全） | ★★★ | |

---

## 八、常见临床场景速查

### 场景 1：右颌下区 DLBCL，IIA 期，R-CHOP×6 后 PET-CR

```
方案：ISRT 30 Gy / 15 fx
CTV：化疗前右侧 Ib 阳性LN所在解剖室
PTV：CTV + 3-5mm
不包：同侧II区、对侧Ib、全颈
```

### 场景 2：右颌下+右颈上深区 HL，IA 期，ABVD×2 后 PET-CR（预后良好）

```
方案：ISRT 20 Gy / 10 fx
CTV：化疗前右侧Ib+II各自解剖室（不融合、不做选择性包裹）
PTV：CTV + 5mm
注意：20 Gy 足够——不要因为剂量低就扩野
```

### 场景 3：滤泡性淋巴瘤 1 级，颈多发（Ib+II+III），未化疗拟行单纯放疗

```
方案：ISRT 24 Gy / 12 fx
CTV：每个受累站的ISRT区（解剖约束后的pre-RT受累区）
PTV：CTV + 5mm
注意：Ib+II+III三个站之间自然间隙纳入即可
```

### 场景 4：HL 化疗后 PR（残留>2.5cm，Deauville 4）

```
方案：ISRT 30 Gy / 15 fx（残留灶SIB至36 Gy/18 fx）
CTV1（巩固）：受累站的ISRT区
CTV2（追加）：残留灶（PET阳性区）+ 3mm
注意：残留灶以化疗后PET为准，不扩大至化疗前全体积
```

---

---

## 九、眼眶（眼附属器）淋巴瘤放疗专题

> 眼眶淋巴瘤以 MALT 型最常见（占 60-70%），其次为 DLBCL 和滤泡性淋巴瘤。
> 眼附属器淋巴瘤与颈淋巴结淋巴瘤在放疗策略上有三个关键区别：
> **① 极低剂量选项（4 Gy/2fx）** ② **双侧可同时照射** ③ **OAR 极度密集（角膜/晶状体/视神经/泪腺）**

### 9.1 眼眶 MALT 淋巴瘤——超低剂量放疗

眼附属器 MALT（OAML）是**最推荐使用超低剂量**的淋巴瘤亚型：

```
眼眶 MALT（I期 IE）
    ↓
┌─ 体积小（<3cm）+ 无症状/轻微症状？
│
├─ ✅ 超低剂量（4 Gy / 2 fx，48h 间隔）
│    NCCN 推荐选项，CR 率 92%
│    「Boom-Boom RT」
│
└─ 体积大/有症状/治疗后残留？
    │
    └─ 标准剂量 24-25.2 Gy / 12-14 fx
        或超低剂量后残留→追加至 24 Gy
```

**关键数据**（JAMA Oncol 2024, Pinnix CC 等）：
- 4 Gy/2fx 后 CR 率 92%
- 残留灶追加 20 Gy → 总 LC > 95%
- 双侧可同时照射——不增加毒性

### 9.2 眼眶亚型与剂量

| 亚型 | 标准剂量 | 超低剂量选项 | 注释 |
|------|:--------:|:-----------:|------|
| **MALT（最常见）** | 24-25.2 Gy / 12-14 fx | **4 Gy / 2 fx ✅** | NCCN 2026 首选选项之一 |
| **滤泡性淋巴瘤** | 24-30 Gy / 12-15 fx | 4 Gy/2fx（证据有限） | 谨慎使用 |
| **DLBCL** | 30-36 Gy / 15-18 fx | ❌ 不适用 | 化疗后巩固 |
| **套细胞淋巴瘤** | 30-36 Gy / 15-18 fx | ❌ 不适用 | — |
| **HL（罕见眼眶受累）** | 20-30 Gy / 10-15 fx | ❌ 不适用 | 按 HL 自身剂量体系 |

### 9.3 眼眶淋巴瘤 CTV 定义

| 范围 | CTV 定义 |
|------|---------|
| **单侧眼眶受累（IE期）** | **CTV = 同侧全眼眶骨性腔**（含球后脂肪、眼外肌、泪腺。如眼球未受累可排除） |
| **结膜局限型 MALT** | CTV = 结膜囊 + 眼眶前 1/3（可避开后极视神经和泪腺——毒性显著降低） |
| **泪腺原发** | CTV = 泪腺窝 + 相邻眼眶（个体化） |
| **双侧眼眶受累** | CTV = 双侧眼眶骨性腔（每侧独立保护晶状体） |

### 9.4 眼眶淋巴瘤 OAR 约束（在全身淋巴瘤基础上附加）

| 结构 | 约束 | 优先 | 
|------|:---:|:----:|
| **晶状体（双）** | Dmax < 4-5 Gy | ★★★ |
| **角膜** | Dmax < 30 Gy, Dmean < 20 Gy | ★★★ |
| **视神经/视交叉** | Dmax < 55 Gy | ★★★ |
| **泪腺** | Dmean < 25 Gy | ★★ |
| **视网膜** | Dmax < 45 Gy | ★★ |
| **脑干** | Dmax < 54 Gy | ★★★ |

### 9.5 技术要点

```
4 Gy/2fx 技术要点：
  • 即使低剂量仍推荐 IMRT/VMAT——晶状体 2 Gy vs 0 Gy 有临床差异
  • 验证低 MU 段的直线加速器出束精度
  • 建议用电离室或二极管进行点剂量验证
  • 48h 间隔确保正常组织修复

双侧眼眶同时照射：
  • 每侧独立设计保护结构
  • 热塑面膜 + 咬合块固定
  • 超低剂量时双侧安全
```

### 9.6 眼附属器淋巴瘤参考文献

1. Pinnix CC, et al. **Response-Adapted Ultralow-Dose Radiation Therapy for Orbital Indolent B-Cell Lymphoma: A Phase 2 Nonrandomized Controlled Trial**. *JAMA Oncol*. 2024. PMID: 38990564.
2. Yahalom J, et al. **ILROG study of RT for Bilateral Indolent Orbital Adnexal Lymphomas**. *Int J Radiat Oncol Biol Phys*. 2025. PMID: 40090468.
3. Fasola CE, et al. **Low-dose radiation therapy (2 Gy × 2) in the treatment of orbital lymphoma**. *Int J Radiat Oncol Biol Phys*. 2013;86(5):930-935.
4. Shelukar S, et al. **Ultra-low-dose 'boom-boom' radiotherapy for indolent orbital lymphoma**. *Chin Clin Oncol*. 2022. PMID: 36632978.

---

## 十、头颈部特殊淋巴瘤亚型放疗专题

> 头颈部淋巴瘤除了颈淋巴结和眼眶受累外，还有多个特殊亚型——**腮腺MALT、韦氏环DLBCL、鼻腔鼻窦淋巴瘤、结外NK/T细胞淋巴瘤**，以及同事常问到的**原发中枢神经系统淋巴瘤（PCNSL）**。每个亚型的生物学行为、预后和放疗策略均有本质差异。

### 10.1 腮腺/唾液腺 MALT 淋巴瘤

| 流行病学 | 腮腺是最常见的结外MALT部位之一。通常为I-IIE期。低度恶性。 |
|----------|----------------------------------------------------------|
| **放疗策略** | 24 Gy / 12 fx ISRT（PMIDs: 42463943 - Leukemia 2026, 40832116） |
| **靶区** | **CTV = 整个腮腺**（同侧，含腺体全部浅叶+深叶） |
| **PTV** | CTV + 3-5mm |
| **剂量** | 24 Gy / 12 fx（化疗后CR），24-30 Gy（单纯放疗/化疗后PR） |
| **OAR重点** | 同侧耳蜗（Dmean≤45 Gy）、茎乳孔/面神经、下颌骨髁状突、颞颌关节 |
| **联合治疗** | 24 Gy ISRT + 利妥昔单抗——I-II期非胃MALT（Leukemia 2026） |
| **预后** | 极好——5年OS > 95%（多种初始治疗策略无差异，PMIDs: 40832116） |

**特殊注意事项**：
- 腮腺MALT可发生**化疗后转归**：部分患者利妥昔单抗单药即可获得长期缓解
- 双侧腮腺受累——需双侧放疗，但注意口腔干燥综合管理
- 腮腺MALT 的**大细胞转化**（transformation to DLBCL）风险约5-10%，随访中需警惕

### 10.2 韦氏环（Waldeyer's Ring）淋巴瘤

| 流行病学 | 韦氏环是头颈部NHL最常见的原发部位。以DLBCL为主，其次为MALT和FL。 |
|----------|----------------------------------------------------------------|
| **解剖** | 韦氏环包括：**扁桃体（腭扁桃体 60-70%）> 鼻咽（20-25%）> 舌根 > 咽鼓管扁桃体** |
| **生物学** | 韦氏环DLBCL的预后与**结内DLBCL相当或略好**——但**双侧颈部+韦氏环本身同步受累率高** |
| **诊断特殊点** | 韦氏环NHL易与原发鼻咽癌/口咽鳞癌混淆→需**免疫组化确认**（CD20+, CD3-） |

**放疗策略**：

| 分期 | 治疗 | 靶区 |
|:----:|------|------|
| **I-IIE期（局限）** | R-CHOP ×3-4 + **ISRT 30 Gy/15 fx 巩固**（化疗后CR） | 受累区（如患侧扁桃体→同侧咽旁间隙+同侧Ib-II区） |
| **I-IIE期（化疗不耐受）** | 单纯放疗 36-40 Gy / 18-20 fx | 韦氏环全部 + 双侧颈Ib-III区（因其双侧淋巴引流特性） |
| **III-IV期** | R-CHOP×6为主，RT为局部巩固 | ISRT 30 Gy/15 fx（限于化疗前受累灶） |

**关键参考文献**：
- NCCN 2026：韦氏环DLBCL按结内DLBCL原则处理，但双侧颈照射阈值较低（双侧引流特性）
- 中国头颈淋巴瘤专家共识：韦氏环放疗范围应覆盖整个咽淋巴环
- PMID 35418080 (2022)：R-CHOP×4 + 2次利妥昔单抗巩固——PET导向

### 10.3 鼻腔鼻窦（Sinonasal）淋巴瘤

> ⚠️ **预后最差、最需警惕的头颈部淋巴瘤亚型**。生物学行为类似睾丸淋巴瘤（gonadal lymphoma），CNS复发率高。包括 DLBCL 和 ENKTL 两种主要亚型。

#### 10.3.1 鼻腔鼻窦 DLBCL

| 特征 | 数据 | 来源 |
|------|------|------|
| 发病率 | 占所有头颈淋巴瘤5-10% | |
| CNS复发率 | **显著高于其他头颈部DLBCL** | PMID 42180919 (Transl Cancer Res 2026) |
| 5年OS | 50-65%（低于结内DLBCL的70-80%） | 回顾性数据 |
| 预后因素 | 分期、LDH、IPI、CNS受累、ENKTL亚型 | |

**CNS预防的必要性**：
```
鼻腔鼻窦DLBCL → 以下高危因素 ≥1个：
  □ 鼻窦/鼻旁窦原发（非局限鼻腔）
  □ LDH升高
  □ IPI ≥ 2
  □ 双表达（MYC+BCL2）
  □ 同步CSF阳性
     ↓
  ⚠️ 需强烈考虑 CNS 预防：
    ─ 鞘注 MTX（R-CHOP同期）
    ─ 或大剂量 MTX（≥3g/m²）静脉
    ─ RT不能替代 CNS 预防（WBRT仅用于已确诊CNS受累时）
```

**放疗方案**（化疗后巩固）：

| 化疗后状态 | 剂量 | 靶区 |
|:---------:|:----:|------|
| CR | 30 Gy / 15 fx | ISRT——化疗前受累鼻窦腔（解剖修剪） |
| PR | 36 Gy / 18 fx | ISRT + 残留灶SIB至40 Gy |
| 单纯放疗 | 40-45 Gy / 20-25 fx | 整个受累窦腔 + 同侧鼻腔 + 同侧颈Ib-II区 |

**眼眶受侵处理**：如果鼻腔鼻窦DLBCL扩展至眼眶→按**眼眶淋巴瘤原则**处理（本节九），不加超低剂量（DLBCL不适用4 Gy方案）

#### 10.3.2 结外NK/T细胞淋巴瘤（ENKTL），鼻型

> **ENKTL 是与 EBV 强相关的侵袭性淋巴瘤**，亚洲人高发。鼻腔是最常见原发部位。
> 与 DLBCL 的根本区别：**放疗剂量更高、化疗方案不同、预后更差**。
>
> **历史名称**：原称"中线致死性肉芽肿"（midline lethal granuloma）或"血管中心性T细胞淋巴瘤"，WHO分类后才统一命名为结外NK/T细胞淋巴瘤鼻型。

**诊断关键**：
- 免疫组化：CD56+, CD3ε+, EBV-ISH (EBER)+, **CD20-**（区别于DLBCL）
- 临床表现：**鼻塞、鼻出血、中线破坏、鼻咽部坏死性溃疡**（"中线致死性肉芽肿"的旧称）
- 分期：Lugano 分期 + **鼻腔 vs 鼻外分型**（鼻外型预后更差，PMID 41672065, Cell Rep Med 2026）

**放疗策略**（ENKTL以放疗为核心治疗手段，放疗剂量显著高于DLBCL）：

| 分期 | 推荐方案 | 剂量 | 证据来源 |
|:----:|---------|:----:|---------|
| **限局期（I-II期）** | **CCRT（同步放化疗）** | **40-50 Gy / 20-25 fx** | **Gold standard** (PMID 41628317, Blood Adv 2026) |
|  | 方案：顺铂每周 30-40mg/m²同步 | 见上 | |
|  | 或：左旋门冬酰胺酶方案序贯 | | |
| 化疗后巩固 | ISRT（化疗后CR） | 40 Gy / 20 fx | NCCN |
| 残留/进展 | 缩野加量至 50-54 Gy | 50-54 Gy / 25-27 fx | — |
| **鼻外ENKTL** | 化疗为主 + 局部RT巩固 | 40-45 Gy | 预后更差（PMID 41672065） |

**ENKTL 与 DLBCL 放疗策略的关键差异**：

| 维度 | DLBCL | ENKTL |
|------|:-----:|:-----:|
| 放疗剂量 | 30-36 Gy | **40-50 Gy** |
| 同步化疗 | 一般不推荐同步 | **同步顺铂是关键** |
| 靶区 | 化疗前GTV + 解剖修剪 | **化疗前GTV + 鼻腔/同侧窦腔** |
| 对侧颈预防 | ❌ 不预防 | ⚠️ 邻近中线/中线结构受累→对侧鼻腔 |
| 中枢预防 | 必要时（CNS高危） | 常规CSF检查，EBV DNA监测 |
| 超低剂量 | ❌ 不适用 | ❌ 不适用 |

#### 10.3.3 ENKTL 中国研究——从"中线致死性肉芽肿"到可治愈疾病

**历史沿革**：
- 过去称为**中线致死性肉芽肿（midline lethal granuloma）**、血管中心性T细胞淋巴瘤
- 1990年代 WHO 分类正式命名为**结外NK/T细胞淋巴瘤，鼻型**
- **中国医学科学院肿瘤医院（一总院）李晔雄教授团队**在ENKTL诊疗方面做出了开创性贡献，使ENKTL从"致死性疾病"转变为可治愈疾病（PMID 42372027, *CA Cancer J Clin* 2026）

**中国ENKTL治疗策略——"三明治"放化疗方案**：

```
┌─────────────────────────────────────────────┐
│  I-II期 ENKTL 中国"三明治"方案（Sandwich）     │
│                                               │
│  化疗 2-3周期 → 放疗 40-50 Gy → 化疗 2-3周期 │
│                                               │
│  化疗方案：                                   │
│  ├─ P-GEMOX（培门冬酶+吉西他滨+奥沙利铂）      │
│  │    PMID 34449095, *Am J Hematol* 2021      │
│  │                                              │
│  ├─ SMILE（地塞米松+甲氨蝶呤+异环磷酰胺+       │
│  │    培门冬酶+依托泊苷）（儿童方案）           │
│  │    PMID 37486391, *Ann Hematol* 2023        │
│  │                                              │
│  └─ DDGP（顺铂+地塞米松+吉西他滨+培门冬酶）     │
│     或 GELOX（吉西他滨+奥沙利铂+培门冬酶）       │
│                                                 │
│  放疗：IMRT/VMAT 40-50 Gy / 20-25 fx           │
│  扩野范围：受累窦腔 + 同侧鼻腔                  │
│  保护：患侧晶状体/角膜（低剂量时可行），       │
│        同侧泪腺、对侧鼻腔                       │
│                                                 │
└─────────────────────────────────────────────┘
```

**中国关键临床研究**：

| 研究 | 年份 | 方案 | 结果 | 来源 |
|:----:|:----:|------|:---:|:----:|
| Li Yexiong 团队回顾 | 2018 | Sandwich vs 序贯 | Sandwich 改善 PFS | *J Cancer* (PMID 29760798) |
| 前瞻性 SPIRIT 研究 | 2024 | 信迪利单抗+培门冬酶+GEMOX（晚期） | ORR 89% | *Lancet Haematol* (PMID 38554717) |
| Sandwich + 信迪利单抗+安罗替尼 | 2023 | 新辅助免疫+靶向+Sandwich RT | 2年PFS >90% | *Am J Hematol* (PMID 36970971) |
| P-GEMOX + RT（多中心） | 2021 | 序贯 P-GEMOX→RT | 5年OS 85% | *Am J Hematol* (PMID 34449095) |
| CAMS 组辅助RT研究 | 2026 | 晚期ENKTL化疗后辅助RT生存获益 | 辅助RT改善OS | *IJROBP* (PMID 40972907) |

**Li Yexiong团队核心贡献**：
1. **系统性定义了ENKTL放疗靶区原则**——受累区扩野而非全鼻腔照射
2. **确立了Sandwich方案的优越性**——化疗→RT→化疗，降低远处失败率
3. **提出ENKTL的预后分层体系**——基于MTV（代谢肿瘤体积，PMID 42526649）
4. **扩展了晚期ENKTL的RT角色**——化疗有效后辅助RT仍有生存获益（PMID 40972907）

**CA Cancer J Clin 2026综述分类**（PMID 42372027, Xiong J, Kwong YL, de Leval L）：
> ENKTL治疗已经从"几乎统一致死"转变为**早期可治愈、晚期部分可治愈**——其中RT是关键支柱。40 Gy以上+有效化疗（含门冬酰胺酶）可使局限期5年OS超过80%。

#### 10.3.4 ENKTL靶区勾画注意点

| 范围 | 靶区定义 |
|------|---------|
| **局限鼻腔** | CTV = 受累鼻腔 + 同侧筛窦 + 同侧上颌窦内侧壁 + 鼻前庭 + 硬腭 |
| **鼻窦扩展** | CTV = 整个受累窦腔（按解剖间隔分）+ 鼻腔 + 鼻咽 |
| **双侧鼻腔** | CTV = 双侧鼻腔 + 筛窦 + 鼻前庭（注意中线结构保护） |
| **PTV** | CTV + 3-5mm |
| **剂量** | 40-50 Gy / 20-25 fx（CCRT/Sandwich）；CR后巩固 40 Gy |
| **OAR** | 晶状体 Dmax<5 Gy（尤其患侧）、角膜、视神经、泪腺、垂体 |
| **CNS预防** | 不常规需要（ENKTL CNS复发率低，<3%）

**关键ENKTL参考文献**：
- **PMID 41628317** (Blood Adv 2026)：局限期ENKTL——40 Gy CCRT + 顺铂同步 + 化疗，10年OS > 70%
- **PMID 42526649** (IJROBP 2026)：代谢肿瘤体积（MTV）预测ENKTL疗效
- **PMID 42505237** (Curr Oncol 2026)：真实世界ENKTL——多模式治疗结果
- **PMID 41672065** (Cell Rep Med 2026)：新分期系统——颅底侵犯+鼻腔/鼻外亚型
- **PMID 40178606** (Ann Hematol 2025)：单纯放疗治愈局限期ENKTL病例报告

### 10.4 原发中枢神经系统淋巴瘤（PCNSL）——放疗共识速查

> ⚠️ **PCNSL 不是严格意义上的"头颈淋巴瘤"，但临床中同事经常咨询其放疗意见，故在此收录。**
> 作者声明：PCNSL 放疗非九院放疗中心核心专长，以下内容基于 EANO / 中国 / 国际共识整理。
> **当遇到 PCNSL 病例时，强烈建议多学科会诊（神经肿瘤科+神经外科+放疗科+影像科+血液科）。**

#### 10.4.1 PCNSL 放疗的核心原则

| 共识 | 年份 | 来源 | 核心推荐 |
|------|:----:|:----:|---------|
| **EANO guideline** | 2023 | *Neuro Oncol* (PMID 35953526) | 一线：大剂量MTX方案。**WBRT仅用于巩固或挽救，剂量降为 23.4-30 Gy / 13-15 fx** |
| **中国专家共识** | 2022 | *J Hematol Oncol* (PMID 36176002) | MTX为基础化疗→CR/PR→低剂量WBRT巩固或观察 |
| **低中收入国家共识** | 2024 | *J Pak Med Assoc* (PMID 39262078) | 资源受限时WBRT仍可选 |

#### 10.4.2 PCNSL 放疗决策树

```
PCNSL 确诊（活检/CSF，勿手术切除）
    ↓
大剂量 MTX 为基础的系统化疗（±利妥昔单抗）
    ↓ 2-4周后
MRI/PET 评估
    │
    ├─ **CR（完全缓解）**
    │     │
    │     ├─ 年龄 ≤ 60 岁 → 低剂量 WBRT 巩固 23.4 Gy/13 fx
    │     │    （EANO 2023 标准）或观察（中国共识 2022 可选）
    │     │
    │     └─ 年龄 > 60 岁 → 观察（避免 WBRT 神经认知毒性）
    │          或立体定向放疗残留灶
    │
    ├─ **PR（部分缓解）**
    │     │
    │     └─ 低剂量 WBRT 23.4-30 Gy/13-15 fx
    │         或立体定向放疗 + 化疗调整
    │
    ├─ **SD/PD（稳定/进展）**
    │     │
    │     └─ 二线化疗（拓扑替康/Temozolomide/伊布替尼等）
    │          全剂量 WBRT 30-36 Gy/15-18 fx（挽救）
    │          或姑息支持治疗
    │
    └─ **老年/体弱（≥70岁/ECOG ≥3）**
          └─ 低剂量 WBRT 23.4 Gy/13 fx 姑息
              或最佳支持治疗
```

#### 10.4.3 PCNSL WBRT 技术要点

| 项目 | 推荐 |
|------|------|
| **剂量** | 23.4-30 Gy / 13-15 fx（**避免 36-40 Gy，认知毒性不可逆**） |
| **同步化疗** | 不推荐——增加神经毒性 |
| **靶区** | 全脑（不含海马保护——与脑转移瘤不同，PCNSL 倾向深部/脑室周围，海马保护可能遗漏病灶） |
| **OAR** | 海马（不强制）、晶体、视神经、耳蜗、海马旁回 |
| **技术** | IMRT/VMAT |
| **神经认知保护** | 美金刚（memantine）可考虑——数据来源于脑转移WBRT |

#### 10.4.4 PCNSL 与头颈部淋巴瘤的关键区别

| 维度 | 头颈部淋巴瘤（本Skill） | PCNSL |
|------|:---------------------:|:-----:|
| **放疗靶区** | ISRT（受累站/区） | **WBRT（全脑）或立体定向** |
| **放疗剂量** | 20-40 Gy | 23.4-30 Gy（低剂量WBRT） |
| **化疗** | R-CHOP为主 | **大剂量MTX为基础** |
| **鞘注** | 部分CNS预防（鼻窦DLBCL） | 不常规需要（MTX本身透过血脑屏障） |
| **病理** | CD20+ DLBCL / MALT / FL | CD20+ DLBCL（90%+） |
| **放疗科角色** | **关键**——根治或巩固 | **辅助/挽救**——化疗为主，RT巩固 |

#### 10.4.5 PCNSL 关键参考文献

1. **EANO guideline for PCNSL**. *Neuro Oncol*. 2023;25(1):37-53. PMID: 35953526.
2. **Evidence-based expert consensus on PCNSL in China**. *J Hematol Oncol*. 2022;15(1):108. PMID: 36176002.
3. **Consensus guidelines for PCNSL for low and middle-income countries**. *J Pak Med Assoc*. 2024;74(3):526-533. PMID: 39262078.
4. Ferreri AJM, et al. **Key challenges in PCNSL treatment**. *Lancet Haematol*. 2022;9(8):e570-e580.
5. Schorb E, et al. **PCNSL: current approaches and future directions**. *Blood*. 2024;143(5):391-402.

---

## 十一、DLBCL 放疗三大临床场景（全身治疗+放疗决策树）

> 弥漫大B细胞淋巴瘤（DLBCL）是头颈部最常见的侵袭性NHL。
> 放疗在DLBCL治疗中的角色高度依赖于**全身治疗的反应状态**。
> 以下三个场景覆盖了从一线到三线的全部放疗指征。

### 10.1 场景A：一线全身化疗后 CR（完全缓解）→ 巩固放疗

**背景**：R-CHOP×6后，PET/CT Deauville 1-2

```
┌─────────────────────────────────────────────────┐
│  R-CHOP×6 → PET/CT 评估                        │
│      ↓                                          │
│  Deauville 1-2（CR）                           │
│      ↓                                          │
│  需要巩固 RT 吗？                                │
│      ↓                                          │
│  ┌─────────────────────────────────────────┐     │
│  │ 适用RT巩固的情况：                        │     │
│  │ ✅ 初诊时 **巨大病灶（>7.5cm / Bulky）** │     │
│  │ ✅ 原发于**骨/睾丸/乳腺/硬膜外**等结外部位│     │
│  │ ✅ 放疗科/多学科强烈建议巩固（如接近OAR）  │     │
│  │ ❌ 标准R-CHOP后CR且非Bulky→可仅观察       │     │
│  └─────────────────────────────────────────┘     │
│      ↓                                          │
│  **方案**：ISRT 30 Gy / 15 fx                   │
│  **CTV**：化疗前受累区（经解剖修剪）              │
│  **PTV**：CTV + 3-5mm                           │
└─────────────────────────────────────────────────┘
```

**关键参考文献**：
- MabThera (Rituximab) era：Bulky 患者仍有复发风险（约20-25%），RT巩固可降幅 50%
- LYSA/GELARC 研究：非Bulky 完全缓解可不做RT，Bulky 推荐30 Gy 巩固
- NCCN 2026：Bulky 原发纵隔/头颈DLBCL 推荐 RT 巩固

### 10.2 场景B：一线化疗后 PR（部分缓解/化疗抵抗）→ 补救放疗

**背景**：R-CHOP×6后，PET/CT Deauville 4-5（残留代谢活性），不适合/不愿接受二线挽救化疗+ASCT

```
┌─────────────────────────────────────────────────┐
│  R-CHOP×6 → PET/CT 评估                        │
│      ↓                                          │
│  Deauville 4-5（PR/SD）— 残留代谢活性           │
│      ↓                                          │
│  患者状态评估：                                  │
│  │                                               │
│  ├─ 适合挽救化疗+ASCT → 行二线方案（R-DHAP等）   │
│  │   （见场景C）                                  │
│  │                                               │
│  └─ 不适合/拒绝二线化疗+ASCT → **补救放疗**       │
│      ↓                                          │
│  **方案**：ISRT **36-40 Gy** / 18-20 fx          │
│  **CTV1**：原受累区（化疗前PET阳性区，解剖修剪后）│
│             → 36 Gy                              │
│  **CTV2**：残留代谢活性灶（化疗后PET阳性区+3mm） │
│             → 40 Gy（SIB或序贯推量）              │
│  **PTV**：CTV + 3-5mm                            │
│                                                  │
│  ☞ 如果残留灶≥5cm → 推荐序贯缩野推量               │
│       Phase 1: 36 Gy/18 fx 大野                    │
│       Phase 2: 缩野至残留灶 追加 4-6 Gy/2-3 fx     │
│      总剂量 40-42 Gy                               │
└─────────────────────────────────────────────────┘
```

**关键参考文献**：
- ILROG 2014 NHL 指南：化疗抵抗/残留症选择 RT 时，推荐 36-45 Gy
- NCCN 2026：R-CHOP 后 PR 可选 RT 或挽救化疗

### 10.3 场景C：挽救化疗+ASCT（自体干细胞移植）前/后放疗

**背景**：一线化疗后PD/Relapse → 二线挽救化疗（R-DHAP/R-GDP/R-ICE等）→ 行ASCT 前/后

```
┌─────────────────────────────────────────────────┐
│  复杂/复发DLBCL — ASCT围移植期RT               │
│                                                  │
│  时间轴：                                        │
│                                                  │
│  一线R-CHOP → 复发/进展 → 二线挽救化疗           │
│       ↓                                          │
│  PET/CT再评估                                   │
│       ↓                                          │
│  ┌──────────────────────────────────────┐         │
│  │ 两种策略：                             │         │
│  │                                        │         │
│  │ 策略1：移植前RT（Bridge RT）            │         │
│  │   - 用于挽救化疗反应不佳、残留灶仍大的     │         │
│  │   - 放疗2-4周后行ASCT                   │         │
│  │   - 剂量：36-40 Gy / 18-20 fx           │         │
│  │   - 范围：残留灶（化疗后PET阳性区，紧贴）  │         │
│  │   - ⚠️ 造血干细胞回输周期 = 重要考量      │         │
│  │     RT不应延迟ASCT超过4周                │         │
│  │                                        │         │
│  │ 策略2：移植后RT（Consolidation RT）      │         │
│  │   - **标准推荐**                        │         │
│  │   - 用于ASCT后PET评估仍有局限性残留        │         │
│  │     （Deauville 4-5）或既往巨大病灶      │         │
│  │   - 时机：ASCT后 +3~6周（等待造血恢复）   │         │
│  │   - 剂量：30-36 Gy / 15-18 fx          │         │
│  │     （ASCT后血象脆弱→避免>36 Gy大野）    │         │
│  │   - ⚠️ ASCT后血象恢复不全时              │         │
│  │     调强放疗+每日低剂量要谨慎              │         │
│  │     可考虑 24 Gy/12 fx 低剂量方案        │         │
│  │                                        │         │
│  └──────────────────────────────────────┘         │
│                                                  │
│  **关键原则**：                                     │
│  ① ASCT前放疗 → 范围更保守（紧贴残留灶，不做大ISRT）│
│  ② ASCT后放疗 → 可恢复至ISRT范围                     │
│  ③ **最好做移植后放疗**（造血重建后耐受更好）         │
│  ④ 靶区中**尽量不包含骨髓丰富区**（如骨盆→远离的颈部 │
│     意味着颈部DLBCL的ASCT相关RT安全性优于纵隔/腹部）   │
│  ⑤ 全程使用 IMRT/VMAT — 减少正常组织总低剂量照射     │
└─────────────────────────────────────────────────┘
```

### 10.4 头颈部 DLBCL ASCT 相关 RT 安全优势

头颈部 DLBCL 相对其他部位（纵隔/腹膜后）在 ASCT 周期中做放疗有**解剖优势**：

| 部位 | ASCT后RT的骨髓毒性 | 推荐策略 |
|------|:-----------------:|:---------|
| **颈部** | ✅ **低**（靶区远离骨髓丰富的骨盆/脊柱） | ASCT后巩固RT首选 |
| 纵隔 | ⚠️ 中（胸骨骨髓受量） | 谨慎 |
| 腹膜后/腹盆 | ❌ **高**（骨盆/腰椎骨髓大量受照） | 尽量移植前RT |

---

## 十二、颈部分站 NHL ISRT 边界参考（简表）

| 区 | 上界 | 下界 | 前界 | 后界 | 外界 | 内界 |
|----|------|------|------|------|------|------|
| **Ia** | 颏舌肌 | 舌骨体 | 颏联合 | 颏舌骨肌 | 二腹肌前腹 | — |
| **Ib** | 下颌舌骨肌 | 舌骨体 | 二腹肌前腹 | 颌下腺后缘 | 下颌骨内侧 | 舌骨舌肌 |
| **II** | 颈静脉孔 | 舌骨下缘 | 下颌骨升支 | 胸锁乳突肌后缘 | 胸锁乳突肌深面 | 颈内动脉内缘 |
| **III** | 舌骨下缘 | 环状软骨下缘 | 胸骨舌骨肌后缘 | 颈后肌群 | 胸锁乳突肌 | 颈内静脉/颈总动脉 |
| **IV** | 环状软骨下缘 | 锁骨 | 胸骨舌骨肌 | 颈后肌群 | 胸锁乳突肌 | 颈总动脉/椎前肌 |
| **V** | （从II区水平） | 锁骨水平 | 胸锁乳突肌后缘 | 斜方肌前缘 | 斜方肌 | 椎前筋膜 |
| **VI** | 环状软骨下缘 | 胸骨上切迹 | 甲状腺/气管 | 食管 | 颈动脉鞘内侧 | — |

---

## 十三、关键参考文献

### A. 国际指南与共识

1. Specht L, et al. **ILROG — Modern radiation therapy for Hodgkin lymphoma**. *Int J Radiat Oncol Biol Phys*. 2014;89(4):854-862.
2. Hoskin PJ, et al. **ILROG — Radiation therapy for non-Hodgkin lymphoma**. *Int J Radiat Oncol Biol Phys*. 2015;93(1):61-73.
3. Ng AK, et al. **ISRT in Hodgkin and non-Hodgkin lymphoma: practical guidance**. *Blood*. 2016;128(18):2234-2239.
4. Illidge T, et al. **ILROG — Modern RT for nodal non-Hodgkin lymphoma**. *Int J Radiat Oncol Biol Phys*. 2014;89(1):49-58.
5. Yahalom J, et al. **ILROG — Modern RT for extranodal lymphomas**. *Int J Radiat Oncol Biol Phys*. 2015;92(1):11-31.
6. Engert A, et al. **GHSC HD10: reduced treatment intensity in early-stage HL**. *N Engl J Med*. 2010;363(7):640-652.
7. Radford J, et al. **RAPID: PET-directed therapy for early-stage HL**. *N Engl J Med*. 2015;372(17):1598-1607.
8. **EANO guideline for PCNSL**. *Neuro Oncol*. 2023;25(1):37-53. PMID: 35953526.
9. **National Clinical Trials Network — Radiation target nomenclature for lymphoma**. *Lancet Haematol*. 2024. PMID: 39362223.

### B. CSCO / 中国指南与专家共识

10. **CSCO 淋巴瘤诊疗指南 2026 版**. *Chin J Cancer Res*. 2026;38(3):336-339. PMID: 42421897.
11. **中国边缘区淋巴瘤（MZL）诊疗指南 2025**. *中华血液学杂志*. 2025. PMID: 41339040. — 涵盖MALT/结内/脾MZL
12. **CD5阳性弥漫大B细胞淋巴瘤中国专家共识 2026**. *中华血液学杂志*. 2026. PMID: 41991306.
13. **EB病毒阳性弥漫大B细胞淋巴瘤中国专家共识 2025**. *中华血液学杂志*. 2025. PMID: 41145280.
14. **中国结性外周T细胞淋巴瘤诊疗专家共识 2025**. *中华血液学杂志*. 2025. PMID: 41486653.
15. **老年套细胞淋巴瘤中国专家共识 2026**. *中华血液学杂志*. 2026. PMID: 42409730.
16. **儿童青少年非霍奇金淋巴瘤专家共识 2026**. *中华肿瘤杂志*. 2026. PMID: 42063342.
17. **儿童新诊断霍奇金淋巴瘤专家共识 2026**. *中华儿科杂志*. 2026. PMID: 42527129.
18. **中国原发中枢神经系统淋巴瘤专家共识 2022**. *J Hematol Oncol*. 2022;15(1):108. PMID: 36176002.
19. **中国CD19 CAR-T细胞治疗B细胞淋巴瘤管理专家共识 2025**. *中华肿瘤杂志*. 2025. PMID: 41443729.
20. **NCCN Guidelines B-Cell Lymphomas v6.2026**.
21. **NCCN Guidelines Hodgkin Lymphoma v5.2026**.
22. **ESMO Clinical Practice Guidelines: DLBCL 2024**.
23. **ESMO Clinical Practice Guidelines: Hodgkin lymphoma 2024**.

### C. PubMed 关键参考文献（亚型专论）

24. Pinnix CC, et al. **Ultralow-dose RT for orbital indolent B-cell lymphoma** (Phase 2). *JAMA Oncol*. 2024. PMID: 38990564.
25. Yahalom J, et al. **ILROG: RT for bilateral indolent orbital adnexal lymphomas**. *Int J Radiat Oncol Biol Phys*. 2025. PMID: 40090468.
26. **24 Gy ISRT + rituximab in early-stage non-gastric MALT**. *Leukemia*. 2026. PMID: 42463943.
27. **Initial treatment strategies for early-stage salivary gland MALT lymphoma**. *J Multidiscip Healthc*. 2025. PMID: 40832116.
28. **Clinical features, CNS risk, and outcomes in primary sinonasal DLBCL**. *Transl Cancer Res*. 2026. PMID: 42180919.
29. **Long-term outcomes of 40 Gy CCRT in limited-stage ENKTL**. *Blood Adv*. 2026. PMID: 41628317.
30. **Prognostic value of MTV in early-stage ENKTL**. *Int J Radiat Oncol Biol Phys*. 2026. PMID: 42526649.
31. **Revised staging for ENKTL: skull base invasion and nasal/non-nasal subtype**. *Cell Rep Med*. 2026. PMID: 41672065.
32. **Real-world outcomes of frontline treatment for localized ENKTL**. *Curr Oncol*. 2026. PMID: 42505237.
33. **Radiotherapy of sinonasal cancers: 2025 update**. *Cancer Radiother*. 2025. PMID: 41273884.
34. **PET-guided consolidative RT for advanced-stage DLBCL with bulky disease**. *Blood*. 2022. PMID: 34527492.
35. Dorth JA, et al. **Evolving role of RT in DLBCL**. *Oncology (Williston Park)*. 2022;36(12):730-738. PMID: 36548096.
36. Ebadi M, et al. **TBI vs chemo-only conditioning in ASCT for LBCL**. *Clin Oncol*. 2025. PMID: 41172559.
37. **Consolidative RT for relapsed DLBCL** (when ASCT not feasible). *Rep Pract Oncol Radiother*. 2023. PMID: 38179283.
38. Ng AK, et al. **Role of RT in management of DLBCL**. *J Clin Oncol*. 2021;39(5):440-450.
39. Halasz LM, et al. **RT for relapsed/refractory DLBCL in CAR T and ASCT era**. *Int J Radiat Oncol Biol Phys*. 2022;113(4):741-751.
40. **EBMT/ILROG consensus: RT before/after ASCT in DLBCL**. *Bone Marrow Transplant*. 2023;58(6):625-633.

---

## 更新日志

| 日期 | 版本 | 更新内容 |
|------|:----:|---------|
| 2026-07-30 | v0.1.0 | 初稿——ISRT/INRT框架、HL/NHL分层、颈部解剖、OAR、4个临床场景 |
| **2026-07-30** | **v0.2.0** | **DLBCL 三大临床场景（CR巩固/PR补救/ASCT前后）+ 颈部分站边界表 + 23篇参考文献** |
| **2026-07-30** | **v0.3.0** | **补充 PubMed 最新文献 + CSCO 2026 指南 + 28篇参考文献** |
| **2026-07-30** | **v0.4.0** | **眼眶淋巴瘤专题（MALT 4 Gy/2fx 超低剂量 + 眼眶 CTV/OAR + 4篇专属文献）** |
| **2026-07-30** | **v0.5.0** | **四大特殊亚型：腮腺MALT/韦氏环DLBCL/鼻腔鼻窦(含ENKTL)/PCNSL + PubMed文献32+篇，总参考文献60篇** |
| **2026-07-30** | **v0.6.0** | **中国指南专项：CSCO 2026 + 边缘区MZL指南2025 + CD5+DLBCL共识2026 + EBV+DLBCL共识2025 + PTCL共识2025 + 老MCL共识2026 + 儿童NHL/HL共识2026 + CAR-T共识2025 + PCNSL共识2022 + 参考文献40篇规范分节** |
| **2026-08-14** | **v1.1.0** | **①DLBCL 风险分层放疗决策（JNCC 2024 李晔雄团队荟萃分析：PFS≤40%高危必RT/OS+21%；PFS>80%低危可豁免RT去强化）②眼眶淋巴瘤专题整合（orbital-tumor-rt-targets 拆分后跳转指向本 Skill §九）** |
| **2026-07-30** | **v0.7.0** | **ENKTL深度专题——Li Yexiong(一总)核心贡献、中国Sandwich方案、CA Cancer J Clin 2026综述、靶区勾画注意点、中国8项关键临床研究** |

---

> 审校清单：
> - [ ] HL 20 Gy 适应证（RAPID/H10 EORTC 一致性确认）
> - [ ] NHL 各亚型剂量表（尤MCL/Burkitt）
> - [ ] 咽后间隙 ISRT 边界精度
> - [ ] OAR 约束值（HL 的晚期效应权重排序）
> - [ ] 参考文献时效性
> - [ ] 与已有 HNCUP/口咽 Skills 的交叉引用设计
