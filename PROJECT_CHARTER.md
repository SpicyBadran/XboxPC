# PROJECT CHARTER — XboxPC

**Project:** XboxPC — Genuine Xbox Series X Retail OS on Standard PC Hardware  
**Owner:** Lamar  
**Charter ID:** `CHARTER-2026-11-22-001`  
**Phase:** 0 — Engineering Foundation  
**Status:** Draft for Owner Approval  
**Branch:** `arena/00f8e176-xboxpc`

---

## 1. Mission Statement

Investigate, engineer, and — **only if a legitimate, authorized technical path exists** — demonstrate booting the **genuine, unmodified Microsoft Xbox Series X retail operating system** directly on **standard, non-Xbox PC hardware** from independently bootable USB or SSD, with no host OS, no remote console, and no security bypass.

**This project does NOT seek to:**

- Re-skin Windows or Linux as Xbox
- Stream from an Xbox
- Emulate Xbox games in a compatibility layer and call it success
- Defeat Secure Boot, extract signing keys, or bypass retail trust
- Ship a modified image falsely labeled genuine

**Diagnostic Environment Distinction:** The UEFI hardware probe we will independently build (Phase 6) is an *instrument*, NOT the Xbox OS. Phase 6 success is "we can enumerate PC hardware reproducibly," not "we run Xbox OS."

## 2. Success Definition (Formal)

The project succeeds **if and only if**:

| Criterion | Proof Required | Independent Verifier |
|-----------|----------------|---------------------|
| Genuine OS provenance | `ARTIFACT_PROVENANCE.md` showing official Microsoft source + hash + signature chain | Security Research Reviewer |
| Genuine boot | `BOOT_CHAIN.md` + recorded boot stages from power-on to OS handoff | Verification Agent |
| PC hardware | Physical non-Xbox PC inventory + `PHYSICAL_TEST_REPORT.md` | Verification Agent |
| Independent operation | No Windows/Linux host — `evidence/hardware-logs` shows bare-metal UEFI → OS | Verification Agent |
| No console dependency | Testbed has no Xbox on network; packet capture clean | Security Reviewer |
| Repeatability | Second independent reproduction with separate build log | Verification Agent |
| Security integrity | No broken signatures, no extracted keys, `SECURITY.md` attestation | Security Reviewer |

A logo on screen without these proofs is a **failure** and will be reported as such.

## 3. Tiered Hardware Scope

- **Tier 1 (Phase 7 target):** One carefully selected reference PC (e.g., AMD Zen 3/RDNA 2 desktop with UEFI 2.8+, NVMe, discrete GPU close to Series X topology). Selection deferred to Phase 4.
- **Tier 2 (Phase 8):** Family of PCs with documented common hardware (same CPU vendor + firmware class).
- **Tier 3 (Future):** Broad arbitrary PC claim — requires Tier 1 + 2 evidence first. **Not promised.**

No hardware purchased before Phase 5 Feasibility Gate.

## 4. Four Category Separation (Mandatory)

All work product must be tagged:

1. **Retail Xbox OS** — Microsoft's genuine target (not ours)
2. **Xbox Development Ecosystem** — GDK, authorized dev kits/interfaces
3. **PC Diagnostic Environment** — Our independent UEFI probe (Phase 6)
4. **Research/Emulation** — Controlled experiments, never counted as genuine execution

Mixing categories into one metric is a charter violation.

## 5. Roles & Accountability

| Role | Responsibility | Gate Authority |
|------|---------------|---------------|
| Project Owner (Lamar) | Approve architecture, hardware purchases, phase transitions | All phase gates, especially 5→6 and 6→7 |
| Systems Engineering Agent | Boot architecture research, diagnostic implementation | — |
| Security Research Reviewer | Trust assumption review, provenance validation | Veto on security claims |
| Verification Agent | Reproducible builds/logs, physical vs emulator separation | Veto on test claims |
| Documentation & Evidence Agent | Source provenance, dependency tracking, milestone reports | — |

**Independence Rule:** Different role names do not confer verification. A reviewer must inspect artifacts/logs/evidence files directly, not merely concur.

## 6. Phase Sequence & Gates

0. **Engineering Foundation** (this phase) → deliver `INITIAL_AUDIT.md`, `PROJECT_CHARTER.md`, `REPOSITORY_ARCHITECTURE.md`, `ENGINEERING_RULES.md`, `RISK_REGISTER.md` → **Stop and Report**
1. **Public Xbox Series X Architecture** → hardware/OS research with sources → Stop
2. **Retail OS Availability** → provenance analysis → Stop (Critical feasibility gate)
3. **Boot Chain & Security** → dependency graph + trust model → Stop
4. **PC Hardware Compatibility Database** → structured JSON + docs → Stop
5. **Feasibility Verdict** → `FEASIBILITY_FINAL_REVIEW.md` with one of FEASIBLE / CONDITIONALLY FEASIBLE / NOT CURRENTLY FEASIBLE / INSUFFICIENT EVIDENCE → **Human Decision Required**
6. **Independent UEFI Diagnostic Boot Environment** (only after owner approval) → EFI app + reproducible build + physical test → Stop
7. **Genuine Xbox OS Execution Investigation** (only after prerequisites demonstrated) → evidence per §2 → Stop
8. **PC Hardware Expansion** (only after genuine execution on Tier 1) → per-machine certification

Skipping a gate is a charter violation even if technical momentum suggests otherwise.

## 7. Non-Negotiable Engineering Rules (Summary; see ENGINEERING_RULES.md)

- No fabrication of test results, logs, or compatibility green checks
- No claim that x86-64 commonality implies platform compatibility
- No extraction of protected keys, no Secure Boot bypass
- No purchase/provisioning without owner approval
- No modification of unrelated repositories
- Reproducible builds with hash-verified artifacts
- Separate physical and emulator evidence; never combine
- All external artifacts recorded in `evidence/source-register/` with hash + signature status

## 8. Legal & Ethical Boundary

- Only Microsoft-distributed artifacts via official channels (OSDU portal, recovery tool, developer programs) may be acquired, and only hashes/metadata committed — never proprietary binaries.
- Game dumps, leaked SDKs, or decrypted retail images are **out of scope** and must not be sought via the agent's tools.
- `LICENSE-REVIEW.md` and `SECURITY.md` govern what may be published.

## 9. Budget & Timeline (Planning, Not Commitment)

| Workstream | Estimate | Notes |
|------------|----------|-------|
| Phase 0 audit | 1–2 days | This deliverable |
| Phase 1 architecture | 3–7 days | |
| Phase 2 artifacts | 2–7 days | |
| Phase 3 boot/security | 5–14 days | |
| Phase 4 compatibility | 3–7 days | |
| Phase 5 feasibility review | 2–4 days | |
| Phase 6 UEFI diagnostic | 2–6 weeks | After approval |
| Phase 7 genuine execution | Unknown | May be blocked indefinitely |

Research phases (1–4) may overlap technically but gates remain sequential.

## 10. Approval

| Approver | Date | Signature (commit) |
|----------|------|-------------------|
| Project Owner Lamar | — | Awaiting review of Phase 0 report |
| Systems Engineering Agent | 2026-11-22 | `INITIAL_AUDIT.md` submitted |

**Next Step:** Owner reviews `INITIAL_AUDIT.md`, `ENVIRONMENT_INVENTORY.md`, this charter, `REPOSITORY_ARCHITECTURE.md`, `ENGINEERING_RULES.md`, `RISK_REGISTER.md`, and authorizes Phase 1.

---

*This charter is the controlling document for all agent branches. Conflicts with informal branch notes are resolved in favor of the charter.*
