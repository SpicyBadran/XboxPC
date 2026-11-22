# XboxPC — Review Index (Phase 5.5 — Staged Documentation)

> **For owners/reviewers:** This index makes the current staged work easy to navigate without relying on chat output or temporary viewers. All substantive work is the **7-file staged diff** — this file and `STAGED_DIFF_FOR_REVIEW.diff` are navigation aids only.

**Branch:** `arena/00f8e176-xboxpc` @ `dc01bc1` (base `85c82f3` per current session)  
**Status:** **7 files staged, not committed, not pushed** — awaiting substantive review  
**Verbatim diff:** [`STAGED_DIFF_FOR_REVIEW.diff`](STAGED_DIFF_FOR_REVIEW.diff) — 791 lines / 127,881 bytes — exact output of `git diff --cached --no-ext-diff --unified=3`  
**README:** [`README.md`](README.md) → links here

---

## 1. Quick Review Links — The Seven Changed Documents

| # | Document (staged) | Size in diff | What it covers |
|---|-------------------|--------------|----------------|
| 1 | [`research/xbox-os/acquisition/MICROSOFT_RETAIL_OS_INQUIRY.md`](research/xbox-os/acquisition/MICROSOFT_RETAIL_OS_INQUIRY.md) | +203 | **Traceability `INQUIRY-2026-11-22-001`** — DRAFT inquiry to Microsoft (owner-only, DO NOT SUBMIT). Six verbatim questions (complete retail image / PC-target / GDKX scope / research access / deployment authorization / written confirmation) + definitions table (OSU1 vs Public GDK vs GDKX vs hypothetical complete image) + Routes A/B (existing account team vs documented `ID@XBOX.com` / Q&A / GDK forum) + 5 outcome codes O1–O5. Blocks external action until owner authorizes. |
| 2 | [`research/xbox-os/documentation/BOOT_CHAIN.md`](research/xbox-os/documentation/BOOT_CHAIN.md) | +117 | **Traceability `BOOTCHAIN-2026-11-22-001`** — Best-supported boot chain map: overview diagram (SMC→SP→2BL→SCP→hvax64→HostOS→SystemOS→GameOS) with Hot Chips verified HW blocks (360.4 mm² / 16 GB GDDR6 560 GB/s / 52 CU 12 TF / HSP-SHACK-MSP) + stage-by-stage table (9 stages: known component / public docs / required HW / OSU1? / GDK? / GDKX? / unknown) + dependency graph + unknowns list + generic-PC reproducibility boundary. No code/bypass. |
| 3 | [`research/xbox-os/documentation/OSU1_ANALYSIS.md`](research/xbox-os/documentation/OSU1_ANALYSIS.md) | 7+/6- (M) | **Traceability `OSU1-ANALYSIS-2026-11-22-001`** — Modified to add top banner: “no local OSU1.zip downloaded; internal structure = secondary-source reporting via GBAtemp+futuretweets, not `unzip -l`; confidence STRONGLY SUPPORTED.” Distribution/placement downgraded from Confirmed→Strongly Supported, generic-PC boot absence → “not found in reported secondary-source manifest; authoritative manifest UNKNOWN.” References updated. |
| 4 | [`research/xbox-os/documentation/RETAIL_OS_REQUIREMENTS-CORRECTIONS.md`](research/xbox-os/documentation/RETAIL_OS_REQUIREMENTS-CORRECTIONS.md) | +21 | **Traceability `RETAIL-REQ-CORR-2026-11-22-001`** — Corrections appendix to `RETAIL_OS_REQUIREMENTS.md` (original retained). 10-row table: old classification → corrected (`VERIFIED`/`STRONGLY SUPPORTED`/`INFERRED`/`UNKNOWN`/`CONTRADICTED`) + why corrected + corrected statement. Authoritative confidence set per `EVIDENCE_AUDIT.md`. |
| 5 | [`research/xbox-os/findings/EVIDENCE_AUDIT.md`](research/xbox-os/findings/EVIDENCE_AUDIT.md) | +95 | **Traceability `AUDIT-CLAIMS-2026-11-22-001`** — Independent auditor (separate from Systems Engineering Agent). Full claim matrix: OSU1 A1–A7 + platform S1–S10, each with exact old wording → source → direct? → corroboration → verdict → corrected wording → evidence to resolve. Counts: VERIFIED 6 / STRONGLY SUPPORTED 7 / INFERRED 8 / UNKNOWN 5 / CONTRADICTED 0. Secondary-source re-grading + §4 VERIFIED facts + §5 UNKNOWNS. |
| 6 | [`research/xbox-os/findings/FEASIBILITY_FINAL_REVIEW.md`](research/xbox-os/findings/FEASIBILITY_FINAL_REVIEW.md) | +164 | **Traceability `FEAS-2026-11-22-001`** — Phase 5 gate decision. Executive summary (directional truth preserved) + 6 required answers (Q1 obtain via public? Q2 via GDKX? Q3 PC-image documented? Q4 PC boot demonstrated? Q5 what would change verdict? Q6 further engineering justified?) + verdict table (`NOT CURRENTLY DEMONSTRATED` selected) + audit corrections since dc01bc1 + evidence references + next-engineering-decision (Microsoft inquiry). |
| 7 | [`research/xbox-os/findings/PC_COMPATIBILITY_SCENARIOS.md`](research/xbox-os/findings/PC_COMPATIBILITY_SCENARIOS.md) | +102 | **Traceability `COMPAT-SCENARIOS-2026-11-22-001`** — 6 scenarios (A Generic AMD / B Generic Intel / C AMD Pluton+Secure Boot / D Custom board reproducing Xbox characteristics / E Licensed Dev Kit / F Actual Xbox Series X control). Each: known / missing / reproducible / requires MS auth / demonstrated? + ground-rules (don’t conflate GDK games with retail OS; Dev Kit ≠ generic PC; custom ≠ generic). Summary comparison table; no scenario shows generic-PC boot. |

**Supporting context (not in staged diff, but referenced):** `research/xbox-os/documentation/RETAIL_OS_REQUIREMENTS.md` (original, retained for provenance), `DOWNLOAD_SOURCES.md`, `MICROSOFT_ACCESS.md`, `ARTIFACT_COMPLETENESS.md`, `PROVENANCE.md`, `research/references/README.md`.

---

## 2. Project Status at a Glance

- **Objective (unchanged):** Genuine, unmodified Xbox Series X retail OS (HostOS+SystemOS+hypervisor+retail boot chain) booting directly on standard x86-64 PC hardware — no Windows/Linux host, no emulator, no dashboard clone, no trust bypass.
- **Phase:** Phase 2 acquisition investigation complete @ `dc01bc1` → Phase 5 audit/gate complete → **Phase 5.5 review HOLD** (this index).
- **Gates 0–4 complete, Gate 5 `FEASIBILITY_FINAL_REVIEW.md` awaiting owner approval.** No bootloader, disk image, or hardware work authorized until approval.
- **Evidence hygiene:** No `OSU1.zip`/XVD binary/ROM/GDKX NDA material acquired or committed; no hash fabricated; no bypass attempted; no hardware purchased.
- **What’s staged now:** `7 files changed, 709 insertions(+), 6 deletions(-)` — `git status --short` shows `A6+M1` + this review aid `?? STAGED_DIFF_FOR_REVIEW.diff` (untracked, not staged).

---

## 3. Feasibility Verdict

> **`NOT CURRENTLY DEMONSTRATED`** — *not* `NOT FEASIBLE UNDER CURRENTLY KNOWN CONSTRAINTS` and *not* `CONDITIONALLY FEASIBLE`.

**Why this wording:** Public OSU1 is an update payload, not a full OS; public GDK is a game SDK; Secure Xbox Downloads is publicly listed as “recoveries of the GDK” (full restricted inventory `UNKNOWN` beyond illustrative public list, not `including:` exhaustive) — so no genuine authorized PC boot path is demonstrated. But the audit downgraded ten blockers from *Confirmed* to `INFERRED`/`UNKNOWN` where the binding to retail OS code wasn’t witnessed (e.g., CPUID allowlist, ACPI OEM gating), and showed a custom board could spoof interfaces (not trust). Therefore cumulative block is strong but does not prove exhaustive impossibility — the stronger negative would be an overclaim (audit S10 `CONTRADICTED`).

**Charter mapping:** Prompt `NOT CURRENTLY DEMONSTRATED` ≈ charter `NOT CURRENTLY FEASIBLE` / `INSUFFICIENT EVIDENCE` — treated equivalently here.

---

## 4. What’s Verified vs. Still Unknown

**Verified (another engineer can reproduce):**
- V1 OSU1 distribution exists (`support.xbox.com/.../offline-system-update` shell + 5+ community corroborations) → `OSU1.zip` → `$SystemUpdate/` (ZIP, not ISO).
- V2 OSU1 is update, not full OS/disk image (consumed inside Xbox Startup Troubleshooter onto `System Update` A/B slots; greyed-out-version gate).
- V3 Public GDK = game SDK, not retail OS; Secure Downloads = GDK/GDKX recoveries + docs + Submission Validator (personal MSAs excluded, MS rep required) — directly quoted.
- V4 Scarlett SoC custom: 360.4 mm² / 15.3B transistors / 16 GB GDDR6 10+6 560 GB/s 320 banks / 8× Zen2 3.8/3.6 SMT + SPLEAP / GPU 52 CU 12 TF 3328 SP SFS/DXR/VRS/Mesh / HSP/Pluton SHACK + MSP 4crypto/4hash/2decomp @ SSD BW — Hot Chips 2020 pdf slides 2–7 + AnandTech live-blog 09:07PM–09:15PM.
- V5 Bootloaders follow fused-ROM→SP chain generally (Xbox One wiki 2024-03-26 + Hot Chips HSP/Pluton); Hydra hypervisor HostOS/SystemOS/GameOS via VBIs — strongly supported for Xbox One, Series X-expected.
- V6 Generic PCs present different CPU family/model, memory pools, storage topology, driver/GPU firmware coupling — sufficient to defeat drop-in.

**Strongly Supported / Inferred / Unknown (calibrated, not hidden):**
- OSU1 internal file list, A/B slot behavior → STRONGLY SUPPORTED via ≥2 independent secondary sources (not personally `unzip -l`); Xbox One GPT GUIDs extrapolated to Series X → INFERRED; exact retail boot ROM filenames (`smcfw.bin`/`boot.bin`) → XboxOne-observed/SeriesX-expected; Secure Boot CA mismatch (Xbox CA not in PC `db`) → STRONGLY SUPPORTED with QEMU-enrolled-Xbox-CA caveat; ACPI/SMBIOS gating, CPUID allowlist, per-stage SP verification → INFERRED→UNKNOWN.
- Full restricted Secure Downloads inventory beyond public “recoveries of the GDK” description → UNKNOWN (illustrative `including:` list, not exhaustive).

See `EVIDENCE_AUDIT.md` §2–5 + `RETAIL_OS_REQUIREMENTS-CORRECTIONS.md` table for per-claim calibration.

---

## 5. Next Decision (Owner)

| Decision | Options | Until then |
|----------|---------|------------|
| Accept `FEASIBILITY_FINAL_REVIEW.md` as final Phase 5 evidence and record `NOT CURRENTLY DEMONSTRATED` | **Approve** / Request revision (cite claim/tag) | Keep research assets, preserve audit docs |
| Authorize single next request: Microsoft inquiry (`MICROSOFT_RETAIL_OS_INQUIRY.md` Q1–Q6 via Route A account team or B1 `ID@XBOX.com`) | **Authorize** / Defer | Do not enroll Partner Center / accept NDA/GDK Agreement / download GDKX / purchase Dev Kit / post Q&A |
| Authorize generic PC UEFI diagnostic probe as independent `PC-hardware-report` product (not “Xbox PC” evidence) — charter Phase 6 | **Authorize separately** / Defer to after inquiry | No bootloader/XVD work |
| Hardware purchase | **Do not authorize** | RISK-005, charter §3 |

Any Microsoft written answer (O1 complete image / O2 Dev Kit-only / O3 no PC deployment / O4 no response / O5 ambiguous) → update `FEASIBILITY_FINAL_REVIEW.md` addendum with citation + re-derive feasibility only on new evidence.

---

## 6. How to Review

1. Start here (this index) → pick a document in §1 table.
2. For full staged changes verbatim, open [`STAGED_DIFF_FOR_REVIEW.diff`](STAGED_DIFF_FOR_REVIEW.diff) (exact `git diff --cached` output; no reconstruction).
3. Cross-check with live docs in `research/xbox-os/{acquisition,documentation,findings}/`.
4. When ready, give verdict per §5 — no additional engineering until explicit approval.

*Review aids (`REVIEW_INDEX.md`, `STAGED_DIFF_FOR_REVIEW.diff`) are not staged — they are untracked navigation material and will remain out of the eventual documentation commit unless owner requests inclusion.*
