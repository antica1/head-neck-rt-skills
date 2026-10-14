# NPC RT Target Delineation — Precision Skull Base Skill

Radiotherapy target volume delineation for nasopharyngeal carcinoma at millimeter-level anatomical precision, based on Lancet Oncology 2025 and Red Journal IG-2024 International Guidelines.

## What This Skill Does

NPC target delineation requires extreme anatomical precision — individual skull base foramina, cavernous sinus walls, perineural pathways. This skill provides:

1. **Skull base foramen boundaries** — foramen lacerum, ovale, rotundum, superior orbital fissure, optic canal (each with mm-level CT landmarks)
2. **Cavernous sinus anatomy** — four walls, Meckel's cave, stepwise coverage rules
3. **Three-tier CTV construction** — 0 → 70 Gy, +5 → 60 Gy, +5 → 54 Gy (Lancet standard)
4. **NPC-modified lymph node levels** — with explicit boundary differences from standard Robbins
5. **AJCC 9th Edition staging** — ENE → N3b, lateral pterygoid as T2/T4 cutpoint

## Quick Install

### Hermes Agent
```bash
hermes skills install https://raw.githubusercontent.com/antica1/npc-rt-target-delineation/master/SKILL.md
```

## Trigger Keywords

`NPC target` `nasopharyngeal carcinoma` `skull base foramen` `cavernous sinus` `Rosenmuller fossa` `鼻咽癌靶区`

## Key References

- Tang LL et al. *Lancet Oncol*. 2025. PMID:40907526 (Primary)
- Tang LL et al. *Lancet Oncol*. 2025. PMID:40907527 (Neck)
- Lin SJ et al. *Int J Radiat Oncol Biol Phys*. 2025. PMID:40419028 (IG-2024)
- AJCC/UICC 9th Edition. 2025.

## Author

Zhu Guopei, MD — Shanghai Ninth People's Hospital. Contact: antica@gmail.com

## License

MIT

## Related Skills — Shanghai Ninth People's Hospital Head & Neck RT Series

| Skill | Description |
|-------|-------------|
| [**NPC Target Delineation**](https://github.com/antica1/npc-rt-target-delineation) | Lancet 2025 + IG-2024, skull base millimeter-level |
| [HNCUP Target Delineation](https://github.com/antica1/HNCUP-rt-targets) | Occult primary, selective mucosal RT |
| [ACC Post-op RT](https://github.com/antica1/head-neck-acc-rt-targets) | Sensory nerve pathway, facial nerve management |
| [Orbital Tumor RT](https://github.com/antica1/orbital-tumor-rt-targets) | Compartment irradiation, VIII/IX/IIa cascade |
| [DVH Plan Review](https://github.com/antica1/head-neck-dvh-review) | One-glance pass/fail, dual-track physicist/physician reports |
| [Re-Irradiation Planning](https://github.com/antica1/head-neck-reirradiation) | Quad-Shot + SBRT + IO/ADC, cumulative BED |
| [All Skills](https://github.com/antica1) | Six skills from Shanghai Ninth People's Hospital |
