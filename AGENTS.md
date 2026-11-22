# AGENTS.md — Agent Execution Policy (XboxPC)

**Project:** XboxPC — Genuine Xbox Series X Retail OS on PC  
**Charter:** `PROJECT_CHARTER.md`  
**Rules:** `ENGINEERING_RULES.md`

---

## 1. Who This File Governs

Any coding agent (AI or human) operating on branch `arena/00f8e176-xboxpc` or any feature branch derived from it. The E2B sandbox instructions are environmental; this file is project authority.

## 2. Mandatory Pre-Work Inspection

Before any significant change:

```bash
git status
git log --oneline -5
git diff --stat HEAD
ls -la
cat INITIAL_AUDIT.md  # understand baseline
```

Record baseline commit SHA in PR description.

## 3. Role Adherence

Even a single agent must act through distinct review roles:

- **Systems Engineering Agent** — researches, implements
- **Security Research Reviewer** — independently checks trust, provenance, security claims (must open logs/artifacts)
- **Verification Agent** — reproduces builds, inspects hardware logs, enforces emulator/physical separation
- **Documentation & Evidence Agent** — maintains provenance, decisions, milestone reports

One agent wearing multiple hats must still produce separate artifacts per role (e.g., `BOOT_CHAIN.md` by Systems Eng, `SECURITY_MODEL.md` reviewed by Security Reviewer with dated sign-off).

## 4. Phase Discipline

- Do not implement Phase N+1 work while Phase N is open.
- Do not write speculative bootloader in Phase 0–5. Phase 6 implementation requires explicit owner approval after `FEASIBILITY_FINAL_REVIEW.md`.
- Each phase ends with **Stop and Report** — 15-point report per Part IV §14.

## 5. Evidence Rules

- Every external fact: Source URL + retrieval date + hash where applicable.
- Every test result: Environment tag (`unit|integration|emulation|physical`), commit SHA, timestamp, log file path.
- No `PASS` without log; no compatibility green check without physical evidence.
- Evidence directory structure from `REPOSITORY_ARCHITECTURE.md` is normative.

## 6. Security Prohibitions (Non-Negotiable)

- No bypass of Secure Boot, no key extraction, no retail image decryption attempts.
- No publishing of proprietary binaries — hashes/metadata only.
- No seeking leaked GDKX or game dumps.

Violation → immediate revert + entry in `RISK_REGISTER.md`.

## 7. Git Policy

- Work on `arena/00f8e176-xboxpc` or feature branches; never push to `main` without phase gate approval.
- `git push origin <branch>` only to current branch.
- No history rewrites that erase evidence.
- PRs via `gh pr create` / `gh pr merge --merge` only with explicit PR number.

## 8. Tooling

- Use `bash` tool with `cwd=/home/user/XboxPC` for repo operations.
- Use `start_process` only for long-running servers (dev site preview) — bind to `0.0.0.0`.
- Keep `scripts/build` reproducible; pin versions; set `SOURCE_DATE_EPOCH`.

## 8.1 Dashboard Single Source of Truth — Permanent Rule (Post-Merge 1eac66c)

**Source:** `docs/architecture/roadmap.json` — 24 milestones, 8 workstreams, status/dependencies/criteria/evidence/blockers/next-actionable.

**Regeneration (mandatory after milestone evidence changes):**
```bash
python docs/architecture/generate-dashboard.py  # updates metrics + docs/architecture/assets/*.png + README.md DASHBOARD block
python scripts/verify-dashboard.py              # CI check — fails if README/assets out-of-date vs roadmap.json
```

- Never edit milestone percentages in `README.md` manually — update `roadmap.json` status/evidenceClass, then regenerate.
- Treemap: each square = one milestone (green completed, blue in-progress, red blocked, grey planned). Genuine readiness `0/4` stays separate from overall `11/24`.
- Assets: `docs/architecture/assets/header.png`, `treemap-overall.png`, `ws-ws1.png`..`ws-ws8.png` — generated, committed.

**PR checklist (all PRs touching research/status):**
- [ ] `roadmap.json` updated if milestone evidence/status changed (not placeholders)
- [ ] `python docs/architecture/generate-dashboard.py` run — README + assets reflect new metrics
- [ ] `python scripts/verify-dashboard.py` passes locally
- [ ] `Evidence ID` + base commit SHA in PR description
- [ ] No `PASS` without log, no green check without physical evidence

**CI:** `scripts/verify-dashboard.py` is the validation script — PR CI fails if outdated. Do not bypass.

**Agent instruction:** After every successful PR merge to `main`, re-run generation to reflect newly merged state (see §8.1). Do not rely on owner remembering.

## 9. Hardware

- Do not purchase or provision physical hardware without owner approval.
- QEMU is emulation, not proof of PC boot — label correctly.

---

*Confirm reading this file by including `Evidence ID` and commit SHA in your first PR of each phase.*
