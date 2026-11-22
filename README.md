# XboxPC — Genuine Xbox Series X Retail OS on PC Hardware

> **Mission:** Investigate, engineer, and — only if a legitimate authorized path exists — demonstrate booting the genuine, unmodified Xbox Series X retail operating system directly on standard PC hardware from independently bootable USB/SSD.
> Not Windows with an Xbox skin. Not emulation. Not streaming.

**Charter:** [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md)  
**Audit:** [`INITIAL_AUDIT.md`](INITIAL_AUDIT.md) — Phase 0 repository & environment audit (2026-11-22)  
**Rules:** [`ENGINEERING_RULES.md`](ENGINEERING_RULES.md)  
**Security:** [`SECURITY.md`](SECURITY.md) — we preserve retail trust, we do not break it  
**Risks:** [`RISK_REGISTER.md`](RISK_REGISTER.md)  
**Architecture:** [`REPOSITORY_ARCHITECTURE.md`](REPOSITORY_ARCHITECTURE.md)

**Current Phase:** Phase 5.5 — Review HOLD (Staged 7 docs awaiting substantive review — see [`REVIEW_INDEX.md`](REVIEW_INDEX.md))  
**Branch:** `arena/00f8e176-xboxpc` @ `dc01bc1` (base `85c82f3`; Phase 2+5 staged 709+/6-)  
**Review:** Start at [`REVIEW_INDEX.md`](REVIEW_INDEX.md) → verbatim diff [`STAGED_DIFF_FOR_REVIEW.diff`](STAGED_DIFF_FOR_REVIEW.diff) (791 lines, 127881 bytes) — 7-file navigation index + evidence audit

---

## 🔍 Current Review — Phase 5.5 HOLD (You Are Here)

> **Review entry point:** [`REVIEW_INDEX.md`](REVIEW_INDEX.md) — 7-document staged work index + verdict/verified-vs-unknown/next-decision overview  
> **Verbatim staged diff:** [`STAGED_DIFF_FOR_REVIEW.diff`](STAGED_DIFF_FOR_REVIEW.diff) — 791 lines / 127881 bytes — exact `git diff --cached` output (no reconstruction)  
> *7 staged docs (A6+M1, 709+/6-) await substantive review before any commit — see REVIEW_INDEX.md §1 table for links + coverage.*

---

## Project Gates (Do Not Skip)

0. ✅ Foundation (this commit) — `INITIAL_AUDIT.md`, `PROJECT_CHARTER.md`, `ENVIRONMENT_INVENTORY.md`, `REPOSITORY_ARCHITECTURE.md`, `ENGINEERING_RULES.md`, `RISK_REGISTER.md`
1. ⏳ Public Xbox Series X Architecture — `research/xbox-hardware/*.md`
2. ⏳ Retail OS Availability — `ARTIFACT_PROVENANCE.md`
3. ⏳ Boot Chain & Security — `BOOT_CHAIN.md`, dependency graph
4. ⏳ PC Hardware Compatibility Database — `hardware-compatibility.json`
5. ⏸️ Feasibility Verdict — `FEASIBILITY_FINAL_REVIEW.md` → **Human Decision Required**
6. ⏸️ Independent UEFI Diagnostic Boot Environment (after approval)
7. ⏸️ Genuine Execution Investigation (only after prerequisites)
8. ⏸️ PC Hardware Expansion (only after Tier 1 success)

Full detail: [`docs/roadmap.md`](docs/roadmap.md)

## Repository Layout

```
XboxPC/
├── docs/                 # charter, roadmap, decisions, specifications
├── research/             # xbox-hardware/os/boot/security + pc-compatibility
├── platform/             # UEFI probe modules (Phase 6+)
├── tooling/              # hardware-report, evidence-validator, build-verifier
├── tests/                # unit / integration / emulation / physical (strictly separated)
├── evidence/             # source-register, build-logs, hardware-logs, milestone-reports
├── releases/verification # hashes/signatures (no large binaries in Git)
└── scripts/              # build / test / verify
```

See `REPOSITORY_ARCHITECTURE.md` for directory contracts and implementation rationale.

## For Agents

Read **`AGENTS.md`** before any significant change. Mandatory inspection, evidence IDs, and review roles are enforced.

## Status (Phase 0 Answers — Executive Summary)

These are detailed in the deliverables; short answers:

1. **Repo state:** Pristine `Initial commit` + 11 new Phase 0 docs on this branch; working tree clean.
2. **Toolchain:** Debian 12 + GCC 12.2 + Python 3.11 present; `gnu-efi`, QEMU/OVMF, Rust/Clang missing — documented, not blocking until Phase 6.
3. **What can begin now:** Markdown research & Python tooling (Phases 1–5) — fully supported.
4. **Official docs accessible:** See [`research/references/README.md`](research/references/README.md) bibliography (Xbox Series X HotChips 2020, Microsoft GDK docs, Xbox offline update portal).
5. **What is unavailable:** Complete retail OS artifact path, boot dependency details — to be established in Phases 2–3.
6. **Top risks:** No legitimate complete retail OS distribution, Xbox root of trust unavailable on PC, custom SoC vs commodity gap — full log in `RISK_REGISTER.md`.
7. **Demonstrable without Xbox:** UEFI diagnostic probe, hardware inventory, research synthesis.
8. **Requires Microsoft cooperation:** Genuine OS image, trust anchor, GDKX/authorized execution path.
9. **Shortest path to diagnostic boot:** Pin toolchain (`gnu-efi`+`ovmf`+`qemu`), implement `platform/uefi-probe` in C/Rust, reproducible build, QEMU smoke boot, then physical USB test — estimated 2–6 weeks after Phase 5 approval.
10. **Before genuine execution:** Provenance + authenticity verified, authorized non-Xbox execution mechanism documented, trust model satisfied, Tier 1 hardware validated.

---

*Preserve retail signatures. No bypasses. No fabrications. Evidence or it didn't happen.*
