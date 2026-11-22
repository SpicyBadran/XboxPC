# RISK_REGISTER.md — Live Risk Log

**Traceability:** `RISKREG-2026-11-22-001`  
**Update cadence:** Every phase "Stop and Report"

---

## Risk Scoring

- **Likelihood:** Low / Medium / High
- **Impact:** Low (schedule) / Medium (phase rework) / High (project infeasibility) / Critical (legal/safety)
- **Status:** Open / Mitigated / Accepted / Blocked (requires external cooperation)

---

## Active Risks

### RISK-001 — No legitimate complete retail OS distribution path

- **Category:** Artifact Provenance (Phase 2)
- **Description:** Microsoft may not publicly distribute a complete, independently bootable retail Xbox Series X OS image. Recovery packages (OSU1) for Xbox One/Series exist but are console-bound and not a full offline OS; system updates are delta/Cab-type with encrypted/signed components. If no complete artifact is legitimately obtainable, Phase 7 is blocked.
- **Likelihood:** High — public documentation suggests retail OS is not offered as standalone image outside console recovery flow.
- **Impact:** Critical — undermines core charter success criterion (genuine OS provenance).
- **Mitigation:** Phase 2 must exhaust official channels: Xbox Support recovery portal (https://support.xbox.com/help/hardware-network/offline-system-update), OSDU documentation, GDK/GDKX program terms, Xbox Insider recovery options. Document each channel's output type, encryption, and hardware binding. Record failure to obtain as legitimate blocker rather than speculate.
- **Owner:** Systems Engineering Agent
- **Status:** Open
- **Evidence:** To be collected in `ARTIFACT_PROVENANCE.md` / `OFFICIAL_DISTRIBUTION_ANALYSIS.md`

### RISK-002 — Hardware root of trust unavailable on PC

- **Category:** Security / Boot Chain (Phase 3)
- **Description:** Xbox Series X boots from on-SoC Boot ROM + security processor (System on Chip custom trust anchor, possibly with Pluton-derived or legacy Xbox Security Processor). PC UEFI + TPM 2.0 + Secure Boot is not equivalent. If any stage requires Xbox-fused keys or XSP services, genuine retail boot cannot be reproduced on PC without violating security rules.
- **Likelihood:** High
- **Impact:** Critical — even if OS image were obtained, it would fail authentication on non-Xbox hardware.
- **Mitigation:** Phase 3 must map each boot stage's authentication requirement and mark PC compatibility as `Not available on standard PC` where unverified. Do not attempt bypass.
- **Status:** Open
- **Owner:** Security Research Reviewer

### RISK-003 — Custom SoC ≠ commodity AMD hardware

- **Category:** Hardware Architecture (Phase 1/4)
- **Description:** Xbox Series X SoC "Project Scarlett" is a custom AMD Zen 2 + RDNA 2 with unified memory, custom I/O, hardware decompression, custom bus, and firmware. Desktop Ryzen/Radeon sharing ISA family does not imply initialization, memory map, or device-enumeration compatibility. Assuming compatibility is a known-antipattern the charter explicitly forbids.
- **Likelihood:** High
- **Impact:** High — even Tier 1 reference PC may be uncertifiable.
- **Mitigation:** Phase 1 must distinguish publicly documented ISA features from undocumented Xbox platform behavior. Phase 4 must mark all PC entries UNKNOWN until physical-tested.
- **Status:** Open
- **Owner:** Systems Engineering Agent

### RISK-004 — Legal / distribution boundary misstep

- **Category:** Legal (All phases)
- **Description:** Agent could inadvertently seek, hash, or publish proprietary Microsoft binaries, game dumps, or leaked GDKX, violating license and project security commitment.
- **Likelihood:** Medium (agent has web search + code generation; temptation to scrape)
- **Impact:** Critical — legal exposure, repository takedown.
- **Mitigation:** `LICENSE-REVIEW.md` + `SECURITY.md` enforce hash/metadata-only storage. Tooling/Evidence Validator rejects commits containing binaries >threshold or known proprietary paths. Verification Agent audits `evidence/source-register`.
- **Status:** Mitigated (controls defined this phase)
- **Owner:** Documentation Agent + Verification Agent

### RISK-005 — Premature hardware purchase or Tier 3 compatibility promise

- **Category:** Scope / Schedule (Phase 5)
- **Description:** Pressure to "show progress" may lead to buying Tier 1 hardware before feasibility verdict or promising arbitrary PC compatibility without evidence.
- **Likelihood:** Medium
- **Impact:** Medium — wasted budget, false compatibility claims.
- **Mitigation:** Charter explicitly defers purchase to post-Phase 5. RISK_REGISTER is reviewed at Phase 5 gate. Tier claims require per-machine physical evidence.
- **Status:** Mitigated (governance in place)
- **Owner:** Project Owner

### RISK-006 — Physical-vs-emulator test conflation

- **Category:** Verification (Phase 6+)
- **Description:** Demonstrating boot in QEMU+OVMF is useful but not proof of physical PC boot. Mixing results would falsely satisfy "PC hardware" criterion.
- **Likelihood:** Medium
- **Impact:** Medium — invalidates compatibility claims.
- **Mitigation:** `tests/emulation/` vs `tests/physical/` separation is structural; reports must tag environment; Verification Agent rejects merged results.
- **Status:** Mitigated (structural separation defined)
- **Owner:** Verification Agent

### RISK-007 — Toolchain reproducibility failure (sandbox ephemerality)

- **Category:** Build Integrity (Phase 6)
- **Description:** E2B sandbox is ephemeral; local EFI builds could be lost or irreproducible if toolchain is not pinned (gcc version drift, gnu-efi version mismatch).
- **Likelihood:** Medium
- **Impact:** Medium — breaks reproducibility proof required by success criteria.
- **Mitigation:** Pinned Docker/toolchain (`scripts/build/setup-toolchain.sh`), `SOURCE_DATE_EPOCH`, hash attestation in `releases/verification/`. Audit captures current versions.
- **Status:** Open
- **Owner:** Verification Agent

### RISK-008 — Insufficient evidence for verdict (INCOMPLETE research)

- **Category:** Research Completeness (Phases 1–4)
- **Description:** Agent may declare FEASIBLE or NOT FEASIBLE on partial data, rather than correct verdict INSUFFICIENT EVIDENCE.
- **Likelihood:** Medium
- **Impact:** High — incorrect gate decision leads to wasted implementation or premature abandonment.
- **Mitigation:** Phase 5 requires answering 10 explicit feasibility questions with evidence references; verdict taxonomy includes INSUFFICIENT EVIDENCE; owner must approve.
- **Status:** Open
- **Owner:** Documentation Agent

---

## Closed / Retired Risks

*(none in Phase 0)*

---

## Review History

| Date | Phase | Reviewer | Action |
|------|-------|----------|--------|
| 2026-11-22 | 0 | Systems Engineering Agent | Initial register created (8 risks) |
| — | 5 | Project Owner + all agents | Scheduled full review at Feasibility Gate |

---

*Next update: After Phase 1 research — expected new risks around GPU initialization specifics and storage virtualization unknowns.*
