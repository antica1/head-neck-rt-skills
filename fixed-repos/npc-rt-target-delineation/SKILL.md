---
name: "npc-rt-target-delineation"
description: "鼻咽癌精准靶区勾画 — 颅底孔道、海绵窦、Lancet 2025 & IG-2024 国际指南"
---

---
name: npc-rt-target-delineation
description: "Precision target volume delineation for nasopharyngeal carcinoma radiotherapy — skull base foramina, cavernous sinus, stepwise CTV construction per Lancet 2025 and IG-2024 International Guidelines."
version: 1.0.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: MIT
---

# 鼻咽癌精准靶区勾画 — 解剖参考手册

> Lancet 2025 & IG-2024 · AJCC/UICC 9th | 朱国培 · 上海九院

## 一、颅底孔道——精准边界

### 破裂孔
位于岩尖、蝶骨大翼、枕骨基底之间。Lancet：双侧覆盖。IG-2024：偏心时可仅同侧。

### 卵圆孔
蝶骨大翼，破裂孔前外侧，V3 通过。九院：双侧覆盖。

### 圆孔
蝶骨大翼前内侧，V2 通过。IG-2024：53%双侧 / 47%偏心仅同侧。

### 其他孔道
棘孔（脑膜中动脉）、眶上裂（CN III/IV/V1/VI）、视神经管（仅眶尖/视交叉受累时）、舌下神经管（仅枕骨斜坡/枕骨大孔受累时）

## 二、海绵窦——精准边界

上壁：前床突→后床突；外侧壁：CN III → IV → V1 → V2；内侧壁：蝶窦/垂体窝外侧壁；后界：Meckel 腔

覆盖规则：T4（直接侵犯）→ 70 Gy；T3（广泛颅底）→ 60 Gy 预防；T1-T2 → 不覆盖

## 三、鼻咽腔及周围

- 鼻咽黏膜（蝶窦底→软腭上缘→后鼻孔→椎前筋膜→咽隐窝）
- 咽旁间隙（咽缩肌→翼内肌→颈动脉鞘→颅底）
- 翼腭窝（V2 通颅中转站，Lancet 强调覆盖翼腭窝而非上颌窦后壁）
- T2/T4 分界：翼外肌以内→T2；以外→T4
- 后鼻腔：所有 NPC 患者必须覆盖

## 四、淋巴结站区——NPC 修正版

| 修正 | Robbins 标准 → NPC 修正 |
|------|----------------------|
| II 区前界 | 缩小以减少腮腺剂量 |
| III/IV 区前界 | 胸锁乳突肌后缘/带状肌后缘以减少甲状腺剂量 |
| Va 区上界 | 延伸至颅底（颈静脉孔） |
| RP 内侧组 | 仅受累时覆盖（Mao et al. III 期 RCT） |

颈部预防规则（Lancet）：任何 LN+ → 同侧 IV/Vb；N0 → IV/Vb 不覆盖；所有 NPC → 双侧 II/III/Va + 双侧 RP 外侧

## 五、勾画顺序——贴在 TPS 旁

```
1. GTVp：T1+C 增强区（软组织化疗后，骨质/鼻窦/海绵窦化疗前）
2. CTVp_High = GTVp + 0 mm → 70 Gy
3. CTVp_Mid  = CTVp_High + 5 mm → 60 Gy
4. CTVp_Low  = CTVp_Mid + 5 mm → 54 Gy
5. 偏心？砍对侧（破裂孔除外）
6. GTVn：化疗后残留 LN
7. CTVn_High = GTVn + 0 mm → 70 Gy
8. CTVn_Mid：仅 ENE 时 → 60 Gy
9. CTVn_Low：+3 mm → 50 Gy
10. PTV = CTV + 3 mm
```

## 六、关键 OAR 限量

脑干 ≤54 Gy、脊髓 ≤45 Gy、视交叉 ≤54 Gy、视神经 ≤54 Gy、颞叶 ≤60 Gy、晶状体 ≤10 Gy、腮腺（对侧）≤26 Gy、耳蜗 ≤45 Gy、下颌骨 ≤70 Gy

## 七、参考文献

Tang LL et al. Lancet Oncol. 2025 (PMID:40907526, 40907527); Lin SJ et al. IJROBP 2025 (PMID:40419028); AJCC/UICC 9th Edition
