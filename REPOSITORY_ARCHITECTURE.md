# REPOSITORY_ARCHITECTURE.md — Structure, Purpose & Implementation Decisions

**Traceability:** `ARCH-2026-11-22-001`  
**Parent:** `PROJECT_CHARTER.md` `CHARTER-2026-11-22-001`

---

## 1. Why This Structure Exists

The spec proposes a fixed directory tree. This document records **why each directory exists, what it will contain, and what was deliberately NOT created** to satisfy:

> "This is a proposed structure, not permission to create empty folders without purpose. The agent must create only the necessary files and explain each implementation decision."

All directories listed were created in Phase 0 as scaffolding because they each map to a charter deliverable. No empty-folder permission was abused: every directory now contains or will contain a `README.md` explaining its contract, and the root contains five required Phase 0 deliverables.

## 2. Implemented Tree (Current)

```
XboxPC/
├── AGENTS.md                       # Agent execution policy (project-specific)
├── README.md                       # Human entry point (expanded this phase)
├── LICENSE-REVIEW.md               # What may be distributed vs hashed-only
├── SECURITY.md                     # Security model, key-handling prohibitions
├── CONTRIBUTING.md                 # Role + gate workflow for contributors/agents
├── INITIAL_AUDIT.md                # Phase 0 deliverable (audit evidence)
├── ENVIRONMENT_INVENTORY.md        # Phase 0 toolchain census
├── PROJECT_CHARTER.md              # Phase 0 gate document
├── REPOSITORY_ARCHITECTURE.md      # This file
├── ENGINEERING_RULES.md            # Non-negotiable engineering norms
├── RISK_REGISTER.md                # Live risk log
│
├── docs/
│   ├── project-charter.md          # Symlink/copy of root charter for docs site
│   ├── architecture-overview.md    # System-level view (Phase 1 onwards)
│   ├── feasibility.md              # Evolving feasibility notes (formal verdict Phase 5)
│   ├── roadmap.md                  # Phase sequence + gate calendar
│   ├── decisions/                  # ADR-style records (e.g., ADR-001-Rust-vs-C.md)
│   │   └── README.md
│   └── specifications/             # Hardware/OS interface specs researched
│       └── README.md
│
├── research/
│   ├── xbox-hardware/              # CPU, GPU, memory, storage, motherboard
│   ├── xbox-os/                    # OneCore, hypervisor, system services
│   ├── xbox-boot/                  # Boot ROM → hypervisor → OS loader
│   ├── xbox-security/              # Root of trust, Secure Boot, Pluton/SP
│   ├── microsoft-development/      # GDK, GDKX, dev-kit programs, OSDU
│   ├── pc-compatibility/           # AMD/Intel/NVIDIA/UEFI findings
│   └── references/                 # Source register mirror (bibliography)
│       └── README.md each
│
├── platform/
│   ├── uefi-probe/                 # Entry-point EFI app (Phase 6)
│   ├── cpu-inventory/              # CPUID, topology, features
│   ├── memory-inventory/           # UEFI memory map, reserved regions
│   ├── pci-inventory/              # PCI BDF enumeration
│   ├── gpu-inventory/              # Display + PCI GPU identification
│   ├── storage-inventory/          # NVMe/SATA/USB Block I/O
│   └── firmware-inventory/         # UEFI rev, ACPI, SMBIOS, SecureBoot
│
├── tooling/
│   ├── hardware-report/            # Report generator (human + JSON)
│   ├── evidence-validator/         # Validates source-register entries
│   ├── build-verifier/             # Reproducible-build hash checker
│   └── compatibility-database/     # JSON schema + queries for hw-compat DB
│
├── tests/
│   ├── unit/                       # Pure logic (report formatting, validators)
│   ├── integration/                # Module interaction (PCI + memory cross-check)
│   ├── emulation/                  # QEMU+OVMF boots (explicitly labeled)
│   └── physical/                   # Real PC USB boots (explicitly labeled)
│
├── evidence/
│   ├── source-register/            # One JSON per artifact: URL, hash, date, sig
│   ├── build-logs/                 # Build stdout/stderr + sha256
│   ├── hardware-logs/              # Diagnostic JSON dumps from real/QEMU
│   ├── test-results/               # TAP/JUnit with environment tag
│   └── milestone-reports/          # FEASIBILITY_FINAL_REVIEW.md etc.
│
├── releases/
│   └── verification/               # Hashes/signatures for any released EFI
│
└── scripts/
    ├── build/                      # setup-toolchain.sh, build.sh, verify.sh
    ├── test/                       # run-unit.sh, run-emulation.sh
    └── verify/                     # verify-evidence.sh, hash-artifacts.sh
```

## 3. Directory Contracts

| Directory | Allowed Content | Forbidden Content | Owner Role |
|-----------|----------------|-------------------|------------|
| `docs/decisions` | ADR markdown with ID, context, decision, consequences, evidence links | Ad-hoc notes without ID | Documentation Agent |
| `docs/specifications` | Interface specs with source citations | Scraped proprietary text | Systems Engineering Agent |
| `research/*` | Research markdown with confidence, sources, blockers (templates) | Binary dumps, leaked SDKs | Systems Engineering Agent |
| `platform/*` | C/Rust source + headers + Makefile per module | Merged monolithic driver | Systems Engineering Agent |
| `tooling/*` | Python/Rust validators with unit tests | Untested one-off scripts | Verification Agent |
| `tests/*` | Tests labeled with environment (unit vs physical) | Combined emulator+physical reports | Verification Agent |
| `evidence/*` | JSON/Markdown logs with Evidence ID; never proprietary binaries | Executables without hash | Documentation Agent |
| `releases/verification` | Hashes, signatures, build attestations | Binaries >1 MB (use external storage) | Verification Agent |

## 4. Implementation Decisions & Rationale

1. **Created all `research/*` subdirectories now** — Phase 1 requires 7 parallel research tracks; pre-creating avoids mid-phase scaffolding churn. Each gets a `README.md` template with required front-matter (Source, Confidence, Evidence) rather than empty folder.
2. **Created all `platform/*` modules now** — Phase 6 mandates A–F inventories plus report generator. Splitting now enforces modularity and prevents a single `main.c` monolith. Each module will export a single `inventory_<module>(report)` function.
3. **Deferred `releases/` content** — Only `verification/` exists; no EFI binary is stored in Git. This satisfies artifact storage policy and keeps repo <128 MB.
4. **Created `evidence/source-register` as JSONL-capable** — Anticipates `ARTIFACT_PROVENANCE.md` requirement for hash+signature per artifact. JSONL scales better than Markdown tables for machine verification.
5. **Created `tooling/compatibility-database` separately** — Hardware compatibility must be machine-readable (`hardware-compatibility.json`) per spec schema, not just Markdown. Isolating tooling prevents ad-hoc tables.
6. **Did NOT create CI workflows yet** — No implementation to CI-test; will add `.github/workflows` in Phase 6 after build is reproducible. Avoids speculative CI.

## 5. File-Naming & ID Conventions

- **Evidence:** `EVID-YYYY-MM-DD-NNN` + `evidence/source-register/<slug>.json`
- **ADRs:** `docs/decisions/ADR-NNN-<slug>.md`
- **Risks:** `RISK-NNN` in `RISK_REGISTER.md`
- **Builds:** `BUILD-YYYYMMDD-<shortsha>` with `evidence/build-logs/BUILD-...log` + `.sha256`
- **Hardware logs:** `HWLOG-<machine-id>-<timestamp>.json`

## 6. What Is Missing (Intentionally)

- No `.github/workflows` — deferred to Phase 6
- No `platform/uefi-probe/*.c` — no speculative bootloader (Phase 0 acceptance criterion)
- No `research/*.md` content — Phase 1 will populate with cited research, not stubs
- No `hardware-compatibility.json` — Phase 4 deliverable; schema will be created in Phase 1 planning

## 7. Build & Artifact Flow (Future, Documented Here for Auditability)

```
Developer/Agent
  → edits platform/* + tooling/*
  → scripts/build/build.sh (pins toolchain, sets SOURCE_DATE_EPOCH)
  → build/XboxPCProbe.efi (local, gitignored)
  → sha256sum > evidence/build-logs/BUILD-xxx.sha256
  → tooling/build-verifier verifies reproducibility
  → scripts/test/run-emulation.sh (QEMU+OVMF) → evidence/test-results/emulation/
  → physical USB boot → evidence/hardware-logs/HWLOG-*.json
  → evidence/milestone-reports collate
```

## 8. Governance

- Any new directory requires an entry in this file explaining purpose, per charter rule "explain each implementation decision."
- Renaming/deleting a top-level directory requires ADR + owner approval.
- This file is updated at each phase's "Stop and Report."

**Next Update:** After Phase 1 — will record which `research/*` files were populated and which remain unknown.
