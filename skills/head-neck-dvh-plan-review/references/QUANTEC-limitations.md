# DVH 约束的证据基础与四个缺失维度

## QUANTEC 数据的原始来源

| OAR | 原始来源 | 可信度 |
|-----|---------|:--:|
| 脊髓 ≤45 Gy | 大鼠/豚鼠颈髓全横断位 2 Gy/fx 照射 | ⚠ 动物→人外推 |
| 脑干 ≤54 Gy | 猴/大鼠脑干局灶照射 | ⚠ |
| 视神经 ≤55 Gy | 回顾性病例汇总 | ⚠ |
| 腮腺 ≤26 Gy | IMRT 临床系列 Dmean vs 口干评分 | ✅ 人体数据 |
| 晶状体 ≤10 Gy | 白内障临床随访 | ✅ 人体数据 |

## QUANTEC 缺失的四个维度

1. **部分容积效应**：QUANTEC 基于全器官横断位 → 头颈 IMRT 仅部分容积受照 → 实际耐受更高
2. **分次效应**：低分次剂量（1.67 Gy/fx）→ BED 等效低于 2 Gy/fx 标准
3. **时间维度**：再程照射累积耐受无数据
4. **年龄/根治优先级**：年轻根治 vs 老年姑息 → 约束应不同

## BED 修正公式

BED = nd × (1 + d/(α/β))
等效 2 Gy/fx dose = BED / (1 + 2/(α/β))

示例：脊髓 Dmax 0.1cc = 47 Gy @ 1.67 Gy/fx → BED₂ = 47×(1+1.67/2)=86.2 → 等效 2 Gy/fx = 86.2/(1+2/2)=43.1 Gy → 低于 45 Gy

## 关键文献

- Kirkpatrick et al. QUANTEC Spinal Cord. IJROBP 2010. Dmax 50 Gy = 0.2% myelopathy
- Mayo et al. QUANTEC Brainstem. IJROBP 2010.
- Nieder et al. Re-RT tolerance. Cancer 2006.
- UK SABR 2022. Clin Oncol. PMID:35272913
- AAPM TG-101. Med Phys 2010.