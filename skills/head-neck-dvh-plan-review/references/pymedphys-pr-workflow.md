# pymedphys PR Contribution Workflow

## Fork → Code → Test → PR → Iterate

Tested 2026-07-12 with `head_neck_dvh.py` contribution to `pymedphys/pymedphys`.

### Steps

1. **Fork** the target repo on GitHub → your account
2. **Clone** your fork: `git clone git@github.com:antica1/pymedphys.git`
3. **Add code** under `lib/pymedphys/_constraints/` with tests under `lib/pymedphys/tests/constraints/`
4. **Run tests** with ad-hoc Python script (not pytest — environment may not have it):
   `python -c "import sys; sys.path.insert(0,'lib'); from pymedphys._constraints.head_neck_dvh import *; ..."`
5. **Commit + push**: `git add ... && git commit -m "..." && git push origin main`
6. **Open PR** on GitHub.com from your fork's main branch
7. **Respond to reviews**: make changes, verify, commit, push — PR auto-updates
8. **Merging blocked** = normal — only maintainers with write access can merge. Just wait.

### Pitfalls

- **Branch name**: pymedphys uses `main` not `master`
- **Test runner**: don't assume `pytest` is installed — use plain Python assert scripts
- **check_constraint signature**: `(oar_name: str, modality: Modality, metrics: dict)` returns dict with `"overall"` key, NOT an object with `.level`
- **Modality fallback**: when SBRT limits are missing for an OAR (e.g. lens), `check_constraint` falls back to conventional limits via `constraint.get(modality.value, constraint.get("conventional", {}))`
- **Reviewer may ask for tests** that don't match your API shape — adapt to match your actual signatures, explain in comment
