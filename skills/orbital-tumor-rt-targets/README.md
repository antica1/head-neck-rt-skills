# Orbital Tumor RT — Target Delineation Skill

Radiotherapy target volume delineation and dose constraints for orbital tumors — lymphoma, solid malignancies, and benign entities.

## What This Skill Does

The orbit is the most OAR-dense region in radiation oncology. This skill provides a standardized decision chain:

1. **Three-compartment localization** — intraocular vs orbital vs extraorbital
2. **Extraorbital lymphatic cascade** — VIII→IX→IIa (often missed by ophthalmologists)
3. **Compartment-based irradiation** — not distance-based margins
4. **Door and next room** — orbital apex (the door) + cavernous sinus (the next room)
5. **Anterior segment co-management** — cornea, lacrimal gland, nasolacrimal duct

## Quick Install

### Hermes Agent
```bash
hermes skills install https://raw.githubusercontent.com/antica1/orbital-tumor-rt-targets/master/SKILL.md
```

### Claude Code
Copy `SKILL.md` into your Claude skills directory.

## Trigger Keywords

`orbital tumor` `eye tumor` `ocular lymphoma` `lacrimal gland` `sebaceous carcinoma` `retinoblastoma` `uveal melanoma` `orbital radiotherapy`

## Key References

- 中国眼及附属器肿瘤放射治疗指南（2021版）. 中国医师协会放疗专委会.
- Pinnix CC et al. *JAMA Oncol* 2024 (PMID:38990564) — Ultralow-dose orbital RT
- ILROG Guidelines. *IJROBP* 2021
- QUANTEC / AAPM TG-101

## Author

Zhu Guopei, MD — Department of Radiation Oncology, Shanghai Ninth People's Hospital, Shanghai Jiao Tong University School of Medicine.  
Contact: antica@gmail.com

## License

MIT

## Related Skills — Shanghai Ninth People's Hospital Head & Neck RT Series

| Skill | Description |
|-------|-------------|
| [NPC Target Delineation](https://github.com/antica1/npc-rt-target-delineation) | Lancet 2025 + IG-2024, skull base millimeter-level |
| [HNCUP Target Delineation](https://github.com/antica1/HNCUP-rt-targets) | Occult primary, selective mucosal RT |
| [ACC Post-op RT](https://github.com/antica1/head-neck-acc-rt-targets) | Sensory nerve pathway, facial nerve management |
| [**Orbital Tumor RT**](https://github.com/antica1/orbital-tumor-rt-targets) | Compartment irradiation, VIII/IX/IIa cascade |
| [DVH Plan Review](https://github.com/antica1/head-neck-dvh-review) | One-glance pass/fail, dual-track physicist/physician reports |
| [Re-Irradiation Planning](https://github.com/antica1/head-neck-reirradiation) | Quad-Shot + SBRT + IO/ADC, cumulative BED |
| [All Skills](https://github.com/antica1) | Six skills from Shanghai Ninth People's Hospital |
