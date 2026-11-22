# Technical Foundation Assessment — 2026-11-22 (Post-Merge 1eac66c)

**Branch:** `arena/f59d27eb-xboxpc` @ `1eac66c` continuation  
**Source of truth:** `roadmap.json` — 24 milestones, 8 workstreams

---

## 1. What we have actually accomplished (evidence-linked)

- **Foundation (Phase 0):** 9 docs present and reviewed: `INITIAL_AUDIT.md`, `PROJECT_CHARTER.md`, `REPOSITORY_ARCHITECTURE.md`, `ENGINEERING_RULES.md`, `RISK_REGISTER.md`, `ENVIRONMENT_INVENTORY.md` (`ENV-2026-11-22-001` — Debian 12 + GCC 12.2.0 + Python 3.11.2 present; gnu-efi/ovmf/qemu/clang/nasm absent, documented), plus `AGENTS.md`, `SECURITY.md`, `LICENSE-REVIEW.md`. No placeholders counted as complete — these are real.

- **Hardware architecture (WS1):** SoC core + fabric verified from Hot Chips 2020 (W1-M1/M2) — `EVIDENCE_AUDIT.md` V4 (360.4mm²/15.3B/16GB GDDR6/52CU/MSP). Board/firmware surface blocked (W1-M3) — honestly marked UNKNOWN, not hidden.

- **Acquisition & provenance (WS2):** OSU1 secondary-source layout (GBAtemp/futuretweets, STRONGLY SUPPORTED) + GDK verified (348416224) + GDKX public scope documented (recoveries of the GDK) + inquiry draft `INQUIRY-2026-11-22-001` ready (6 questions, definitions, routes, O1-O5) — all blocked from external action until owner send.

- **Boot chain & security (WS3):** `BOOT_CHAIN.md` diagram + 9-stage table + dependency graph (W3-M1 completed), trust anchor in-progress (W3-M2 INFERRED), security prohibitions documented (W3-M3).

- **Requirements & audit (WS4):** 10-row requirements + 21-line corrections appendix + 95-line audit matrix (VERIFIED 6/STRONGLY 7/INFERRED 8/UNKNOWN 5/CONTRADICTED 0) — every claim regraded with source/direct?/corroboration.

- **Compatibility (WS5):** 6 scenarios A–F documented (no generic-PC boot, D custom board distinction) — structured DB missing (planned, not marked done).

- **Repository navigability:** `REVIEW_INDEX.md` + exact `STAGED_DIFF_FOR_REVIEW.diff` merged to `main` via PR #1; now `roadmap.json` + generated dashboard + assets.

**What we have NOT accomplished (honest):** No EFI binary, no tooling CLI, no tests/physical logs, no hardware-database JSON, no Tier 1 PC, no custom board — `platform/`, `tooling/`, `scripts/`, `tests/` remain README placeholders (see below).

---

## 2. What genuinely exists vs planned — platform/tooling/scripts/tests/ build env

**Inspected 2026-11-22 on `arena/f59d27eb-xboxpc`:**

| Directory | What’s there | Genuine? | Phase 6 ready? |
|-----------|--------------|----------|----------------|
| `platform/` | `README.md` only — modular design spec (uefi-probe, cpu/memory/pci/gpu/storage/firmware) | No code — **planned** | No — requires owner approval + toolchain install |
| `tooling/` | `README.md` only — hardware-report/validator/build-verifier/compatibility-database specs | No CLI — **planned** | No |
| `scripts/` | `README.md` only + `verify-dashboard.py` (this branch) | Scripts placeholder — **partial** (dashboard validation added now) | No build scripts |
| `tests/` | `README.md` only — unit/integration/emulation/physical placeholders | No tests — **planned** | No |
| `evidence/` | Source-register + build-logs + hardware-logs skeletons | No real logs — **planned** | No |
| `releases/verification/` | README + hashes placeholder | No binaries — **by design** | N/A |

**Current build environment (re-checked, not blind copy of original inventory):**

```
gcc 12.2.0 (Debian 12.2.0-14+deb12u1) — present
g++ 12.2.0 — present
ld GNU 2.40, objcopy 2.40 — present
make GNU Make — present
python3 3.11.2 — present
git 2.39.5 / gh 2.23.0 — present
gnu-efi / libgnuefi-dev — absent (dpkg -l empty)
ovmf — absent
qemu-system-x86_64 — absent
sbsigntools — absent
edk2 — absent
nasm — absent
clang/lld — absent
rustc/cargo — absent
```

**Why absent is not a bug:** Per charter Phase 0 acceptance, no speculative bootloader is written before approval. Inventory documents gap without masking it; install is `apt install gnu-efi ovmf qemu-system-x86` — gated until Phase 6.

**No test results invented:** No `PASS` without log; no compatibility green check without physical evidence — `ENGINEERING_RULES.md` enforced.

---

## 3. What remains technically unknown (explicit, not hidden)

See `EVIDENCE_AUDIT.md` §5 + `BOOT_CHAIN.md` §4 + `roadmap.json` W1-M3/W3-M2 blockers:

- CPUID allowlist branch (if any) — inferred, not witnessed
- ACPI `MSFT` / `\_SB.XBOX_` OEM strings, SMBIOS Xbox string, SMC registers
- Retail signing cert chain (Xbox CA thumbprint) vs PC `db`/`KEK`/`PK`
- Per-stage Series X Boot ROM filenames/sizes + SCP keytable upload for Series X (Xbox One `smcfw.bin`/`boot.bin` known, Series X may rename, SSD vs eMMC)
- Hypervisor handshake (SMU+SCP), reserved memory window GVEM traps
- Whether custom board reproducing selected Xbox characteristics could satisfy checks if authorized (requires Microsoft retail signing — SKU decision, not workaround)
- Full restricted Secure Downloads inventory beyond public illustrative `including:` list

*Do not fill with assumptions — marked UNKNOWN in `roadmap.json`.*

---

## 4. What blocks genuine Xbox OS execution on a PC

**Primary (authorization):** No legitimate retail OS artifact for generic PC in searched public sources — `W7-M1` blocked. OSU1 is update payload, public GDK is game SDK, Secure Downloads publicly lists *recoveries of the GDK* (full restricted inventory `UNKNOWN`). Requires Microsoft written response (inquiry Q1-Q2).

**Secondary (cumulative SoC/trust, not independent):** Fused ROM RoT, GDDR6 560GB/s unified pool, 52CU non-HAL GPU, MSP @ SSD BW, HSP SHACK isolation, GPT 9A056AD7 A/B slots, `hvax64` Hydra — all Xbox SoC-bound. Generic PC deltas verified (W1-V6: different CPU family, DDR split vs unified GDDR6, standard NVMe without Xbox GUIDs/MSP, PC Windows CA in `db` not Xbox CA). Audit S10 corrected: blockers cumulative, scenario D custom board could spoof interfaces but not retail signatures.

**Tertiary (engineering):** No toolchain/hardware — `platform/` not implemented, no Tier 1 reference PC selected (RISK-005, charter §3).

**Destination remains:** Genuine, unmodified retail OS booting directly on non-Xbox x86-64 PC, no host OS/emulator/bypass — requires W7-M1→W7-M2 + W6-M4 + W5-M2, all blocked. Research 45.8% ≠ readiness 0%.

---

## 5. Next engineering milestones (practical roadmap)

**Independent of Microsoft response (can proceed if owner re-approves separately):**
- `W6-M1` architecture review → `W6-M2` `apt install gnu-efi ovmf qemu-system-x86` → `W6-M3` EFI implementation + QEMU smoke → `W6-M4` physical USB test on Tier 1

**Dependent on Microsoft response (do not start until O1/O2/O3 in writing):**
- `W7-M1` authorized execution path (needs `W2-M4` O1) → `W7-M2` repeatable demo → `W8-M1/M2` physical validation

**Recommended order (from `roadmap.json` nextActions):**
1. **NA-1:** Owner sends inquiry via Route A (existing account team MS rep) or **B1 `ID@XBOX.com`** — documented GDK program contact (`developer.microsoft.com/en-us/windows/support` ID@Xbox section, `learn.microsoft.com/answers` official Q&A). Do NOT enroll Partner Center / accept NDA.
2. **NA-2:** Separately decide if UEFI probe proceeds as independent `PC-hardware-report` product (not Xbox PC evidence) — only then install toolchain.
3. **NA-3:** Maintain dashboard — update `roadmap.json` when evidence changes + regenerate.

---

## 6. Microsoft Inquiry — Ready for Owner Review (Primary Next Step)

**File:** `research/xbox-os/acquisition/MICROSOFT_RETAIL_OS_INQUIRY.md` (`INQUIRY-2026-11-22-001`, 203 lines) — **DRAFT DO NOT SUBMIT, unsent**

- **Six verbatim questions:** Q1 complete retail image via any program? Q2 PC-target configuration for standard x86-64? Q3 GDKX recoveries exclusively for Dev Kit? Q4 authorized research program for boot chain docs? Q5 deployment authorization? Q6 written confirmation that none constitute PC-bootable retail OS?
- **Definitions attachment (§4):** OSU1 (public update package $SystemUpdate/*.xvd + RM_Signature.bin via Troubleshooter) vs Public GDK (game SDK, missing console driver/Shader Compiler) vs GDKX/Secure Downloads (recoveries of the GDK + docs + Validator, MS rep enable) — prevents conflation.
- **Contact routes (§5):** Prioritized A (existing Microsoft account team / Xbox program rep if owner already onboarded — the only party to confirm Secure Downloads negative per access-resources Important box) → B1 **Email `ID@XBOX.com`** (developer.microsoft.com/en-us/windows/support ID@Xbox Program section: “For questions about ID@Xbox program including game publishing, console questions, onboarding to DevKits, contact Email ID@XBOX.com”) → B2 Microsoft Q&A threads (learn.microsoft.com/answers 1663748/5884771, organizational Entra required, MS rep enable) → B3 `aka.ms/gdkforum` → B4 onboarding checklist (read-only, no registration).
- **Most appropriate documented route (no prior partnership):** **B1 `ID@XBOX.com`** — Microsoft explicitly routes GDKX Secure Downloads enablement through MS rep, so account team (A) is authoritative if exists; otherwise B1 is the documented program inbox for console onboarding questions. B2 Q&A is fallback for follow-up clarification.
- **Outcomes O1-O5:** O1 complete image available → CONDITIONALLY FEASIBLE; O2 Dev Kit-only → confirms boundary; O3 no PC deployment → authoritative negative (not impossibility); O4 no response → retain verdict; O5 ambiguous → resend with table emphasis.
- **Status:** All external actions remain blocked per `AGENTS.md` + `ENGINEERING_RULES.md` prompt §3 — requires owner authorization before any email, NDA, Partner Center enrollment, or GDKX download.

---

## 7. UEFI Diagnostic Probe — What It Would Deliver, Cost, and What It Would NOT Prove

**Deliver (if owner approves as separate `PC-hardware-report` product):**
- Modular EFI app inventories: CPU (CPUID family/model/topology), memory (UEFI map + reserved ranges), PCI BDF, GPU (PCI IDs + GOP), storage (NVMe Block I/O, read-only), firmware (UEFI rev, ACPI/SMBIOS, Secure Boot `db`/`KEK`/`PK` state)
- Human + JSON report (per `tooling/hardware-report` spec), reproducible build log with hashes, `BUILD_GUIDE.md`, `KNOWN_LIMITATIONS.md`, `PHYSICAL_TEST_REPORT.md` (environment tag unit/emulation/physical, commit SHA, timestamp, log path)
- QEMU+OVMF smoke boot + optional Tier 1 physical USB boot — strictly separated evidence

**Cost (from `ENVIRONMENT_INVENTORY.md` + charter §9):**
- Engineering: 2–6 weeks after Phase 6 approval (pin toolchain `gnu-efi`+`ovmf`+`qemu`, implement `platform/uefi-probe` in C/Rust, reproducible build, emulator test, physical USB)
- Hardware: none until Tier 1 approved (RISK-005); install is `apt install gnu-efi ovmf qemu-system-x86` — no purchase for emulator phase
- Maintenance: keep probe as instrument, not Xbox PC evidence (charter Part III Phase 6 distinction)

**Would NOT prove:**
- That Xbox OS *can* boot on PC (probe enumerates deltas; feasibility verdict stays `NOT CURRENTLY DEMONSTRATED` until Microsoft artifact)
- Any compatibility `PASS` without physical log — no speculative green checks in `hardware-compatibility.json`
- That emulator results equal physical proof — labels remain strict

*Probe is valuable regardless of Xbox verdict as independent hardware diagnostic — but only after owner re-approves it separately from Xbox feasibility.*

---

*This assessment is generated from `roadmap.json` + live repo inspection, not placeholders. Update roadmap.json when evidence changes; regenerate dashboard before PR.*
