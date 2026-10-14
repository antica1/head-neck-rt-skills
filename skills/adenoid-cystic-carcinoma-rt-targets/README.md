# ACC RT Target Delineation Skill — Deployment Guide

## File Overview

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill file (compatible with both Hermes Agent and Claude Code) |
| `README.md` | This guide |

---

## 一、Install on Hermes Agent

### Method 1 — One-line install via URL (recommended)

```bash
hermes skills install https://raw.githubusercontent.com/antica1/head-neck-acc-rt-targets/master/SKILL.md
```

### Method 2 — Tap the GitHub repo as skill source

```bash
hermes skills tap add https://github.com/antica1/head-neck-acc-rt-targets
hermes skills install adenoid-cystic-carcinoma-rt-targets
```

### Method 3 — Manual copy

```bash
mkdir -p ~/.hermes/skills/research/adenoid-cystic-carcinoma-rt-targets
curl -o ~/.hermes/skills/research/adenoid-cystic-carcinoma-rt-targets/SKILL.md \
  https://raw.githubusercontent.com/antica1/head-neck-acc-rt-targets/master/SKILL.md
```

### Verify installation

```bash
hermes skills list | grep adenoid
```

---

## 二、Search & Trigger Keywords

Once installed, the skill activates automatically when these terms appear in conversation:

| Language | Trigger Keywords |
|----------|-----------------|
| English | `adenoid cystic carcinoma`, `ACC target delineation`, `ACC radiotherapy`, `trigeminal nerve pathway`, `perineural invasion RT`, `cavernous sinus ACC` |
| Chinese | `腺样囊性癌`, `ACC 靶区`, `三叉神经通路`, `神经侵犯放疗`, `海绵窦照射` |

**Manual load**: `/skill adenoid-cystic-carcinoma-rt-targets`

---

## 三、Install on Claude Code (Claude Desktop)

Copy the `SKILL.md` into Claude Code's skills-plugin directory:

```bash
# Locate Claude's skills directory (varies by installation)
# Typical path on Windows:
cp SKILL.md %LOCALAPPDATA%/Claude-3p/local-agent-mode-sessions/skills-plugin/<user-uuid>/skills/adenoid-cystic-carcinoma-rt-targets/

# On macOS/Linux:
cp SKILL.md ~/.claude/skills/adenoid-cystic-carcinoma-rt-targets/
```

The same trigger keywords apply.

---

## 四、For Developers

### Skill Metadata

```yaml
name: adenoid-cystic-carcinoma-rt-targets
version: 1.0.0
author: Zhu Guopei / Shanghai Ninth People's Hospital
license: MIT
```

### To contribute

1. Fork this repository
2. Edit `SKILL.md`
3. Submit a pull request

### Contact

Zhu Guopei, MD — antica@gmail.com  
Department of Radiation Oncology, Shanghai Ninth People's Hospital  
Shanghai Jiao Tong University School of Medicine

## Related Skills — Shanghai Ninth People's Hospital Head & Neck RT Series

| Skill | Description |
|-------|-------------|
| [NPC Target Delineation](https://github.com/antica1/npc-rt-target-delineation) | Lancet 2025 + IG-2024, skull base millimeter-level |
| [HNCUP Target Delineation](https://github.com/antica1/HNCUP-rt-targets) | Occult primary, selective mucosal RT |
| [**ACC Post-op RT**](https://github.com/antica1/head-neck-acc-rt-targets) | Sensory nerve pathway, facial nerve management |
| [Orbital Tumor RT](https://github.com/antica1/orbital-tumor-rt-targets) | Compartment irradiation, VIII/IX/IIa cascade |
| [DVH Plan Review](https://github.com/antica1/head-neck-dvh-review) | One-glance pass/fail, dual-track physicist/physician reports |
| [Re-Irradiation Planning](https://github.com/antica1/head-neck-reirradiation) | Quad-Shot + SBRT + IO/ADC, cumulative BED |
| [All Skills](https://github.com/antica1) | Six skills from Shanghai Ninth People's Hospital |
