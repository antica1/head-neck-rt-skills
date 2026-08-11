# 头颈放疗靶区 Skill 完整索引

> 上海九院放疗中心 · 朱国培 | GitHub: antica1 | v2.3.0 | 2026-08-11
> 17 个公开 Skill · Claude Code & Hermes 双平台（shared-knowledge 已移至私有仓库，2026-08-11）

---

## 一、目录树

```
head-neck-rt-skills/
├── README.md                        # 双平台安装指南
├── CITATION.cff                     # 引用元数据
├── index.html                       # Web 入口页
├── SKILLS_INDEX.md                  # 本文件——完整索引
└── skills/
    │
    ├── neoadjuvant-deescalation/    # 化免新辅助降级（242 行）——被 11 个 Skill 引用
    │
    ├── oral-oropharynx-postop-rt-targets/  # 口腔口咽 PORT 总集（1,089 行）——含口底铁律
    │   ├── port-oral-postop/               # 口腔 PORT 子模块（574 行）
    │   └── port-oropharynx-postop/         # 口咽 PORT 子模块（207 行）
    │
    ├── oropharynx-definitive-rt/    # 口咽根治性 RT（267 行）
    │
    ├── laryngeal-hypopharyngeal-rt-targets/  # 喉/下咽索引（50 行）——仅路由
    │   ├── larynx-hypopharynx-postop/        # 喉/下咽术后 PORT（381 行）
    │   └── larynx-hypopharynx-definitive/    # 喉/下咽根治性 RT（308 行）
    │
    ├── adenoid-cystic-carcinoma-rt-targets/    # ACC 腺样囊性癌（437 行）
    ├── hncup-rt-targets/            # 原发不明转移癌（517 行）
    ├── npc-rt-target-delineation/   # NPC 鼻咽癌（78 行）
    ├── orbital-tumor-rt-targets/    # 眼眶肿瘤（1,026 行）
    ├── sinonasal-rt-targets/        # 鼻腔鼻窦癌（525 行）
    ├── salivary-gland-rt-targets/   # 唾液腺癌（806 行）
    ├── reirradiation-plan-recommend/     # 再程放疗（261 行）
    ├── head-neck-lymphoma-rt-targets/  # 头颈部淋巴瘤放疗（873 行）🆕
│
└── head-neck-dvh-plan-review/        # DVH 计划审核（257 行）
```

---

## 二、依赖关系图

```
    │
    ├── neoadjuvant-deescalation ──────────────────────────────────┐
    │   (当患者有新辅助史时加载)                                      │
    │                                                                │
    ├── oral-oropharynx-postop-rt-targets ──────────────────────────┤
    │   ├── port-oral-postop            ← neoadjuvant-deescalation ─┤
    │   └── port-oropharynx-postop      ← neoadjuvant-deescalation ─┤
    │                                                                │
    ├── oropharynx-definitive-rt        ← neoadjuvant-deescalation ─┤
    │                                                                │
    ├── laryngeal-hypopharyngeal-rt-targets ────────────────────────┤
    │   ├── larynx-hypopharynx-postop   ← neoadjuvant-deescalation ─┤
    │   └── larynx-hypopharynx-definitive ──────────────────────────┤
    │                                                                │
    ├── adenoid-cystic-carcinoma-rt-targets                                     │
    ├── hncup-rt-targets                ← npc-rt-target-delineation  │
    ├── npc-rt-target-delineation                                    │
    ├── orbital-tumor-rt-targets        ← adenoid-cystic-carcinoma-rt-targets   │
    ├── sinonasal-rt-targets                                         │
    ├── salivary-gland-rt-targets       ← adenoid-cystic-carcinoma-rt-targets   │
    ├── reirradiation-plan-recommend                                      │
    └── head-neck-dvh-plan-review                                         │
```

---

## 三、YAML Name ↔ 仓库名对照表

| 仓库名（目录） | YAML `name` | 行数 | 版本 |
|:---|---:|---:|:---:|
| neoadjuvant-deescalation | neoadjuvant-deescalation | 242 | — |
| oral-oropharynx-postop-rt-targets | oral-oropharynx-postop-rt-targets | 1,089 | 1.2.0 |
| port-oral-postop | port-oral-postop | 574 | 1.0.0 |
| port-oropharynx-postop | port-oropharynx-postop | 207 | — |
| oropharynx-definitive-rt | oropharynx-definitive-rt | 267 | — |
| laryngeal-hypopharyngeal-rt-targets | laryngeal-hypopharyngeal-rt-targets | 50 | 2.0.0 |
| larynx-hypopharynx-postop | larynx-hypopharynx-postop | 381 | — |
| larynx-hypopharynx-definitive | larynx-hypopharynx-definitive | 308 | — |
| adenoid-cystic-carcinoma-rt-targets | adenoid-cystic-carcinoma-rt-targets | 437 | 1.5.1 |
| hncup-rt-targets | hncup-rt-targets | 517 | 1.0.0 |
| npc-rt-target-delineation | npc-rt-target-delineation | 78 | 1.0.0 |
| orbital-tumor-rt-targets | orbital-tumor-rt-targets | 1,026 | 1.0.0 |
| sinonasal-rt-targets | sinonasal-rt-targets | 525 | 1.3.2 |
| salivary-gland-rt-targets | salivary-gland-rt-targets | 806 | 1.2.0 |
| reirradiation-plan-recommend | reirradiation-plan-recommend | 261 | — |
| head-neck-dvh-plan-review | head-neck-dvh-plan-review | 257 | — |

> **注意**：2026-08 已完成目录名统一——全部 Skill 的主仓库目录名与 YAML `name` 一致（`hncup-rt-targets`、`adenoid-cystic-carcinoma-rt-targets`、`head-neck-dvh-plan-review`、`reirradiation-plan-recommend`）。旧目录名（`HNCUP-rt-targets`、`head-neck-acc-rt-targets`、`head-neck-dvh-review`、`head-neck-reirradiation`）与旧 YAML name（`cervical-cup-rt-targets`）均已废弃；GitHub 独立仓库若仍用旧名，靠 301 重定向兼容。

---

## 四、跨 Skill 自动联动

| 触发场景 | 自动加载链 |
|----------|-----------|
| "眼眶 ACC" / "泪腺 ACC" | orbital-tumor-rt-targets → adenoid-cystic-carcinoma-rt-targets |
| "腮腺 ACC" / "颌下腺 ACC" | salivary-gland-rt-targets → adenoid-cystic-carcinoma-rt-targets |
| "鼻咽部 ACC" | npc-rt-target-delineation → adenoid-cystic-carcinoma-rt-targets |
| "口腔癌术后 + 化免 pCR" | port-oral-postop → neoadjuvant-deescalation |
| "口咽癌术后 + 化免 MPR" | port-oropharynx-postop → neoadjuvant-deescalation |
| "下咽癌术后 + 化免 pCR" | larynx-hypopharynx-postop → neoadjuvant-deescalation |
| "喉癌根治 + 化免 pCR" | larynx-hypopharynx-definitive → neoadjuvant-deescalation |
| "口咽根治 SIB + 化免 pCR" | oropharynx-definitive-rt → neoadjuvant-deescalation |
| "CUP 颈部转移 + 怀疑 NPC" | hncup-rt-targets → npc-rt-target-delineation |
| "再程放疗 + 需 DVH 审核" | reirradiation-plan-recommend → head-neck-dvh-plan-review |
| "任何靶区生成 + 需 DVH 审核" | any-skill → head-neck-dvh-plan-review |

---

## 五、铁律清单覆盖

| Skill | 铁律条数 | 状态 |
|------|:---:|:---:|
| neoadjuvant-deescalation | ✅ | 化免降级梯度规则 |
| oral-oropharynx-postop-rt-targets | ✅ | PORT 总集铁律 |
| port-oral-postop | ✅ 12 条 | 口腔 PORT 铁律 |
| port-oropharynx-postop | ✅ | 口咽 PORT 铁律 |
| oropharynx-definitive-rt | ✅ 14 条 | 口咽根治铁律 |
| laryngeal-hypopharyngeal-rt-targets | ❌ | 仅索引路由——无需铁律（合理） |
| larynx-hypopharynx-postop | ✅ | 喉 PORT 铁律 |
| larynx-hypopharynx-definitive | ⚠️ | 308 行完整临床 Skill——待补 |
| adenoid-cystic-carcinoma-rt-targets | ✅ | ACC 三级追踪铁律 |
| hncup-rt-targets | ✅ | CUP 铁律 |
| npc-rt-target-delineation | ❌ | 78 行纯解剖参考——无需铁律（合理） |
| orbital-tumor-rt-targets | ✅ | 眼眶铁律 |
| sinonasal-rt-targets | ⚠️ | 525 行完整临床 Skill——待补 |
| salivary-gland-rt-targets | ✅ | 唾液腺铁律 |
| reirradiation-plan-recommend | ✅ | 再程放疗铁律 |
| head-neck-dvh-plan-review | ✅ | DVH 审核铁律 |

**铁律覆盖率**：13/17（含 2 个不应有铁律的纯索引/参考文件） = 实际覆盖率 13/15 = 87%

---

## 六、双平台兼容性

| 平台 | 机制 | 状态 |
|------|------|:---:|
| Claude Code | 语义匹配 → 自动选择相关 Skill | 17/17 ✅ |
| Hermes Agent | `triggers_on` 触发词匹配 | 17/17 ✅ |
| 前端物质完整性 | `name` `description` `version` `author` `license` | 17/17 ✅ |
| `metadata.hermes` 完整性 | `tags` `triggers_on` `related_skills` | 17/17 ✅ |
| 代码块闭合 | Markdown ``` 配对 | 17/17 ✅ |

---

## 七、安装命令

**Hermes（一行全装）：**
```
```

**Claude Code（一行克隆）：**
```bash
git clone https://github.com/antica1/head-neck-rt-skills.git
```

---

> 朱国培 · 上海交通大学医学院附属第九人民医院口腔颌面-头颈肿瘤科放疗中心
> 授权：CC BY-NC-SA 4.0 | GitHub: antica1
