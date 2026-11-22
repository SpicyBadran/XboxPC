# Roadmap — Phase Sequence & Gates

**Single source of truth:** [`architecture/roadmap.json`](architecture/roadmap.json) — 24 milestones, 8 workstreams, status/dependencies/criteria/evidence/blockers — generates [`README.md`](../README.md) dashboard via `python architecture/generate-dashboard.py`. Never edit percentages manually.

**Charter:** `PROJECT_CHARTER.md` (see §6.1 Amendment for `NOT CURRENTLY DEMONSTRATED` reconciliation)

| Phase | Name | Objective | Deliverables | Gate |
|-------|------|-----------|--------------|------|
| 0 | Foundation | Clean reproducible research environment | `INITIAL_AUDIT.md`, `PROJECT_CHARTER.md`, `REPOSITORY_ARCHITECTURE.md`, `ENGINEERING_RULES.md`, `RISK_REGISTER.md`, `ENVIRONMENT_INVENTORY.md` + `AGENTS.md`, `SECURITY.md`, `LICENSE-REVIEW.md` | **Stop and Report** — Owner approves architecture |
| 1 | Hardware Architecture | Reverse-engineer public Series X | `research/xbox-hardware/*ARCHITECTURE.md`, `research/xbox-os/*` | Stop — every subsystem sourced + confidence |
| 2 | Retail OS Availability | Can we legitimately obtain complete retail OS? | `ARTIFACT_PROVENANCE.md`, `OFFICIAL_DISTRIBUTION_ANALYSIS.md`, `RETAIL_OS_COMPLETENESS.md`, `MICROSOFT_ACCESS_REQUIREMENTS.md` | **Critical Feasibility Gate** — no assumption of availability |
| 3 | Boot & Security | Map trust chain, mark PC compatibility | `BOOT_CHAIN.md`, `BOOT_DEPENDENCY_GRAPH.md`, `SECURITY_MODEL.md`, `TRUST_REQUIREMENTS.md` | Stop — every node classified |
| 4 | PC Compatibility DB | Structured DB + research matrix | `HARDWARE_COMPATIBILITY.md`, `hardware-compatibility.json`, `CPU/GPU/FIRMWARE_COMPATIBILITY.md` | Stop — no speculative green checks |
| 5 | Feasibility Verdict | Full assessment, one verdict | `FEASIBILITY.md`, `BLOCKERS.md`, `IMPLEMENTATION_ROADMAP.md`, `FEASIBILITY_FINAL_REVIEW.md` | **Human Decision Required** — approve/reject/request evidence |
| 6 | UEFI Diagnostic Environment | Independent bootable HW probe | EFI binary, source, `BUILD_GUIDE.md`, `PHYSICAL_TEST_REPORT.md`, `KNOWN_LIMITATIONS.md` | Stop — requires Phase 5 approval |
| 7 | Genuine Execution Investigation | Authorized execution if path exists | Per-verification evidence matrix (§7) | Stop — or report blocker |
| 8 | Hardware Expansion | Certify more PCs | Per-machine profile + test report | Continuous |

**Actual state (2026-11-22, `1eac66c` merged, continuation `f59d27eb`):** See `architecture/roadmap.json` — overall 11/24 completed (45.8%), genuine readiness 0/4 (0%). Phase 0 ✅ complete (9 docs, env inventoried: GCC 12.2 + Py 3.11 present, gnu-efi/OVMF/QEMU absent, documented). Phase 1 ⚠️ partial (SoC fabric verified, board surface blocked). Phase 2 ✅ complete with calibration (OSU1/GDK/GDKX + inquiry draft, caveats preserved). Phase 3 ✅ complete (BOOT_CHAIN) + in-progress trust anchor. Phase 4 ⚠️ partial (scenarios done, DB missing). Phase 5 ✅ complete (verdict + audit). Phase 6+ 🔴 blocked until owner authorizes inquiry response / separate probe product.

**Estimates:** Audit 1–2d, Arch 3–7d, Artifacts 2–7d, Boot/Sec 5–14d, Compat 3–7d, Feasibility 2–4d, Diagnostic 2–6wks, Physical validation 1–3wks, Genuine execution Unknown/may be blocked.

**Hardware policy:** No purchases before Phase 5 verdict — preserved (no hardware provisioned, no Tier 1 selected).

**Regeneration:** `python docs/architecture/generate-dashboard.py` → updates `README.md` + `architecture/assets/*.png`; validate via `python scripts/verify-dashboard.py` (CI).

