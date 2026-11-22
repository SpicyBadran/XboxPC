# UEFI Diagnostic Probe — Bounded Specification (Smallest Useful, Separate Product)

**Traceability:** `PROBE-SPEC-2026-11-22-001`  
**Branch:** `arena/7ff9d1c6-xboxpc` @ `8771211` (continuation from merged `1eac66c`)  
**Status:** **Specification only — NOT IMPLEMENTED — owner must re-authorize as separate product `PC-hardware-report`**  
**Depends on:** `docs/architecture/roadmap.json` W6-M1..M4, `PLATFORM/README.md`, `ENVIRONMENT_INVENTORY.md` (ENV-2026-11-22-001), `FEASIBILITY_FINAL_REVIEW.md` Phase 5 verdict  
**Hard boundary:** This spec does **not** increase genuine Xbox OS execution readiness (stays `0/4`). It is an *instrument* to enumerate PC hardware reproducibly, not Xbox OS compatibility proof.

> **Do not implement in this phase** — this is the bounded spec requested for W6 decision. Implementation requires owner approval per `PROJECT_CHARTER.md` Phase 6 gate and `AGENTS.md` §4.

---

## 1. Purpose — What It Is and Is Not

**Is:** Independent, bootable UEFI application (EFI binary + source) that inventories a **standard x86-64 PC's** CPU, memory map, PCI, GPU, storage, firmware — producing a reproducible human + JSON report. It runs **without** Windows/Linux host, directly from USB via UEFI boot.

**Is NOT:** Xbox OS, bootloader for retail OS, XVD extraction, Secure Boot bypass, compatibility `PASS` claim, or emulator/physical conflated proof.

**Success criterion (W6-M4):** `we can enumerate PC hardware reproducibly` — not `we run Xbox OS`.

---

## 2. Platform Module Boundaries — `platform/` (No Monolithic `main.c`)

Each module owns one concern, exports `efi_status_t inventory_<module>(report_context *ctx)` — unit-testable, per `PLATFORM/README.md` contracts.

| Module | Responsibility | Key UEFI Services / Data | Output Fields (see §4 JSON) | Phase |
|--------|----------------|--------------------------|-----------------------------|-------|
| `uefi-probe/` | EFI entry `efi_main`, boot services init, console, exit/reboot, error handling | `EFI_SYSTEM_TABLE`, `BootServices`, `ConOut`, `GetMemoryMap` | `probe.version`, `probe.timestamp`, `probe.uefi_revision`, `probe.build_hash` | W6-M1 |
| `cpu-inventory/` | CPUID, vendor, brand, family/model/stepping, topology (APIC), ISA (x86-64, SSE/AVX), virtualization | `EFI_MP_SERVICES_PROTOCOL` (if present) + `asm cpuid`, `EFI_CPU_ARCH_PROTOCOL` | `cpu.vendor`, `cpu.family/model/stepping`, `cpu.topology.cores/threads`, `cpu.isa`, `cpu.virtualization` | W6-M3 |
| `memory-inventory/` | UEFI memory map descriptors, reserved ranges, hypervisor/framebuffer hints | `GetMemoryMap` + `EFI_MEMORY_DESCRIPTOR` types | `memory.map[]`, `memory.total_kb`, `memory.reserved_regions`, `memory.hypervisor_windows` (observed, not claimed compatible) | W6-M3 |
| `pci-inventory/` | PCI BDF enumeration, vendor/device/class, topology, BARs (read-only) | `EFI_PCI_ROOT_BRIDGE_IO_PROTOCOL`, `EFI_PCI_IO_PROTOCOL` | `pci.devices[]` (BDF, vid:did, class, BARs, topology tree) | W6-M3 |
| `gpu-inventory/` | GPU PCI IDs, Graphics Output Protocol (GOP) modes, no full driver claim | `EFI_PCI_IO_PROTOCOL` + `EFI_GRAPHICS_OUTPUT_PROTOCOL` | `gpu.pci_ids[]`, `gpu.gop.modes[]`, `gpu.display.current`, `gpu.driver_note` (e.g., no Radeon fallback) | W6-M3 |
| `storage-inventory/` | NVMe/SATA/USB via Block I/O, read-only (no write, no Xbox GUID enforcement) | `EFI_BLOCK_IO_PROTOCOL`, `EFI_DISK_INFO_PROTOCOL` | `storage.devices[]` (type NVMe/SATA/USB, size, block_size, GPT presence — no Xbox GUID check) | W6-M3 |
| `firmware-inventory/` | UEFI revision, ACPI/SMBIOS tables, Secure Boot state (`PK/KEK/db/dbx`), firmware vendor | `EFI_ACPI_TABLE_PROTOCOL`, `SMBIOS`, `EFI_VARIABLE_SERVICES` (`SecureBoot`, `PK` etc) | `firmware.uefi_revision`, `firmware.vendor`, `firmware.acpi.oem_id`, `firmware.smbios`, `firmware.secure_boot` (enabled/disabled + db state) | W6-M3 |

**Design rules:**
- Read-only enumeration — no writes, no bypass, no key extraction.
- No claim `x86-64 commonality implies compatibility` — report enumerates deltas, decision is separate.
- Each module fails gracefully (e.g., `AGP` not present) — logs `NOT FOUND` not `FAIL` without evidence.

---

## 3. Tooling — `tooling/hardware-report` JSON Schema and Human Report

**JSON schema (machine-readable, per `roadmap.json` W5-M2 expectations):**

```json
{
  "$schema": "https://xboxpc.example.com/schemas/hardware-report-v1.json",
  "probe": {
    "version": "0.1.0",
    "timestamp": "2026-11-22T08:00:00Z",
    "build_hash": "sha256:abc...",
    "uefi_revision": "2.8",
    "platform": "qemu-ovmf | physical-tier1"
  },
  "environment": {
    "tag": "emulation | physical",
    "commit_sha": "1e5d6ff",
    "timestamp": "2026-11-22T08:00:00Z",
    "log_path": "evidence/hardware-logs/2026-11-22-qemu-smoke.log"
  },
  "cpu": { "vendor": "GenuineIntel", "family": 6, "model": 106, "stepping": 0, "brand": "Intel Xeon @2.6GHz", "topology": { "sockets":1, "cores":1, "threads":2 }, "isa": ["sse2","avx2"], "virtualization": "KVM" },
  "memory": { "total_kb": 4034452, "map": [{"type":"EfiConventionalMemory","phys_start":"0x100000","pages": 256}], "reserved": [] },
  "pci": { "devices": [{"bdf":"00:01.0","vid":8086,"did":1234,"class":"Display","bars":[ ]}] },
  "gpu": { "pci_ids": [{"vid":1002, "did": 73bf}], "gop": {"modes": [{"width":1024,"height":768}]}, "driver_note": "No Radeon fallback — Xbox 52CU non-HAL coupling not satisfied" },
  "storage": { "devices": [{"type":"NVMe","size_gb":512,"block_size":512,"gpt":true}] },
  "firmware": { "vendor": "EDK2 OVMF", "uefi_revision":"2.8", "acpi": {"oem_id":"BOCHS"}, "smbios": {"manufacturer":"QEMU"}, "secure_boot": {"enabled": false, "db": "Windows Production CA not Xbox CA"} },
  "result": "NOT_TESTED | TESTED—PASS | TESTED—FAIL | UNKNOWN | BLOCKED",
  "notes": "No compatibility green check without physical evidence — see ENGINEERING_RULES.md"
}
```

**Human-readable report (`hardware-report` CLI):**
- Markdown table per subsystem (CPU, memory map, PCI list, GPU GOP, storage, firmware) + JSON path reference.
- Status per subsystem: `INVENTORIED` / `NOT FOUND` / `ERROR <code>` — never `COMPATIBLE` with Xbox without Microsoft authorization.
- Links to log file (hash-verified, `evidence/hardware-logs/`).

**Validation (per `tooling/evidence-validator` spec):**
- Every field: source (UEFI service), retrieval timestamp, commit SHA, environment tag (`unit|integration|emulation|physical`).
- No `PASS` without log; no green check without physical evidence — enforced by `ENGINEERING_RULES.md`.

---

## 4. Hardware and Firmware Fields to Collect — Checklist (Not Xbox Compatibility Claim)

**CPU:**
- [ ] `CPUID` leaf 0x0–0x16, `0x80000000` — vendor (`GenuineIntel`/`AuthenticAMD`), family/model/stepping (vs Xbox Fam17h m71/132), brand string
- [ ] Topology: APIC IDs, sockets/cores/threads, SMT, ISA (x86-64, SSE/AVX/AVX2/AVX512), virtualization (KVM/VMware/Hyper-V)

**Memory:**
- [ ] UEFI `GetMemoryMap` — descriptors (type, phys start, pages, attrs), total, conventional vs reserved, hypervisor windows (observed)
- [ ] No claim GDDR6 unified pool — report DDR5 split vs Xbox GDDR6 (W1-M4 divergence table)

**PCI:**
- [ ] BDF enumeration, vendor/device/class/subclass, BARs (type, size), topology tree — read-only

**GPU:**
- [ ] PCI IDs (e.g., 1002:73bf Radeon RX), GOP current mode + mode list, display topology — **no full driver claim**

**Storage:**
- [ ] Block I/O devices (NVMe/SATA/USB), size, block size, GPT GUIDs (observed, not enforced) — no Xbox 9A056AD7 A/B enforcement

**Firmware:**
- [ ] UEFI revision, firmware vendor (EDK2/AMI/Phoenix), ACPI `OEM ID`/`OEM Table ID` (e.g., `BOCHS` vs Xbox `MSFT`), SMBIOS manufacturer/product
- [ ] Secure Boot state: `SecureBoot` var, `PK`/`KEK`/`db`/`dbx` — contents (Windows Prod CA not Xbox CA — inferred, not thumbprint-verified)

---

## 5. Build/Test Environment Prerequisites

**Prerequisites (from `ENVIRONMENT_INVENTORY.md` ENV-2026-11-22-001 — re-checked):**

| Package | Installed? | Install (gated until Phase 6 approval) | Purpose |
|---------|------------|----------------------------------------|---------|
| `gcc` 12.2.0, `ld` 2.40, `objcopy` 2.40, `make`, `python3` 3.11.2, `git`/`gh` | ✅ present | — | Base toolchain, `elf→efi` via `objcopy -j .text --target=efi-app-x86_64` |
| `gnu-efi` (headers + crt0 `crt0-efi-x86_64.o`) | ❌ absent | `apt install gnu-efi` | EFI entry, `efi.h` |
| `libgnuefi-dev` | ❌ absent | `apt install gnu-efi` | `libgnuefi.a` |
| `ovmf` (UEFI firmware for QEMU) | ❌ absent | `apt install ovmf` | QEMU boot firmware |
| `qemu-system-x86_64` | ❌ absent | `apt install qemu-system-x86` | Emulation testing |
| `edk2` | ❌ absent | `git clone https://github.com/tianocore/edk2` | Alternative EDK2 toolchain |
| `clang`/`lld`, `nasm`, `rustc` | ❌ absent | `apt install clang lld nasm` / `rustup` | Future EDK2/Rust options |
| `sbsigntools` | ❌ absent | `apt install sbsigntool` | Secure Boot signing test (future) |

**Reproducible build (planned, per `ENVIRONMENT_INVENTORY.md` §4):**
- Pin versions (`gcc 12.2.0` etc), set `SOURCE_DATE_EPOCH`, use `scripts/build` wrapper, hash log `releases/verification/build-hashes.txt` — no large binaries in Git.

---

## 6. QEMU Smoke-Test Scope and Limitations

**Scope (emulation):**
- Boot probe via `qemu-system-x86_64 -bios /usr/share/OVMF/OVMF.fd -drive file=fat:rw:platform/build/ -boot n` — expect `EFI binary → inventories → JSON + human report → reboot`.
- Environment tag `emulation`, commit SHA, timestamp, log `evidence/hardware-logs/2026-11-22-qemu-smoke.log` — hash-verified, committed log.

**Limitations (honest):**
- QEMU is **not** proof of PC boot — labels strictly `emulation` per `AGENTS.md` §9 / `ENGINEERING_RULES.md`; OVMF firmware vendor `BOCHS` vs Xbox `MSFT` not Xbox trust.
- Emulation does not validate physical DDR/GPU/storage divergence (W1-V6 deltas remain).
- No Secure Boot enforcement test — Windows Production CA in `db` not Xbox CA (INFERRED mismatch, not thumbprint-verified).

---

## 7. Physical USB Test Scope, Safety, and Acceptance Criteria

**Scope (physical — requires owner approval + Tier 1 reference PC):**
- Build USB FAT32 with `EFI/BOOT/BOOTX64.EFI` (probe) + `startup.nsh` fallback — boot Tier 1 PC via UEFI boot menu (no host OS installed, no disk write).
- Collect same inventories as QEMU, tag `physical`, log `evidence/hardware-logs/2026-11-22-physical-tier1.log`.

**Safety considerations:**
- **Read-only:** No disk writes, no NVRAM variable writes, no firmware updates — `Block I/O` read-only, no `SetVariable` except diagnostic log if needed (ask owner).
- **Reversible:** Reboot to original firmware boot order after test — no persistent change.
- **No hardware purchase until Tier 1 approved** (RISK-005, charter §3) — use existing lab PC or owner-provided reference, not agent-provisioned.
- **Isolation:** No network, no Xbox OS attempt, no key extraction — per `SECURITY.md`.

**Acceptance criteria (per `roadmap.json` W6-M4):**
- Physical test report with environment `physical`, commit SHA, timestamp, `log_path` — hash-verified, committed.
- Emulation vs physical comparison table (e.g., CPUID Fam 6 m106 vs Fam 17h m71/132, DDR5 vs GDDR6) — no `PASS` without log, no green check without physical evidence.
- `KNOWN_LIMITATIONS.md` documents QEMU vs physical deltas — not inflated to `COMPATIBLE`.

---

## 8. Estimated Effort with Assumptions and Dependencies

| Milestone | Effort | Assumptions | Dependencies | Does it prove Xbox boot? |
|-----------|--------|-------------|--------------|--------------------------|
| **W6-M1** architecture review | ✅ Done (this spec) | Module contracts frozen, AGENTS.md Phase 6 gate noted — no code yet | W4-M2 | **No** — design only |
| **W6-M2** toolchain | 0.5 day | `apt install gnu-efi ovmf qemu-system-x86` — owner approves Phase 6 as separate product | W6-M1 | **No** — tooling only |
| **W6-M3** probe impl + QEMU smoke | 2–4 weeks (C/Rust, `platform/uefi-probe` + 6 modules, `tooling/hardware-report`, reproducible build, QEMU log) | Engineer familiar with UEFI boot services; `gnu-efi` crt0 + `objcopy` flow; `hardware-report` JSON schema frozen | W6-M2 | **No** — enumerates PC, not Xbox compatibility |
| **W6-M4** physical USB validation | 1–2 weeks (Tier 1 PC provision, USB build, 2–3 physical runs, comparison + `KNOWN_LIMITATIONS.md`) | Tier 1 reference PC selected per `W5-M2` (deferred to Phase 4), owner approves hardware (no purchase without approval) | W6-M3 + W5-M2 | **No** — instrument, not Xbox OS proof |

**Total Phase 6 (if approved separately):** 2–6 weeks + 1–3 weeks physical — per charter §9 estimates; genuine execution `W7` still blocked (requires Microsoft artifact W7-M1).

**Dependencies:** `W6-M2` → `W6-M3` → `W6-M4`; `W6-M4` also needs `W5-M2` Tier 1 profile. All blocked until owner authorizes probe as independent `PC-hardware-report` product (not Xbox PC evidence) — per `FEASIBILITY_FINAL_REVIEW.md` §2.6.

---

## 9. What It Must NOT Increase

- **Genuine readiness stays `0/4`** — `roadmap.json` WS7+WS8 independent metric, not inflated by `W6` progress.
- **No `hardware-compatibility.json` green check** without physical log — per `ENGINEERING_RULES.md` and `roadmap.json` W5-M2 criteria.
- **No claim of PC-target Xbox OS image** — probe enumerates PC that *differs* from Xbox (W1-V6 deltas: CPU family, DDR split, GPU custom, storage GUIDs, PC CA).
- **No bypass** — read-only, no Secure Boot bypass, no key extraction, no Xbox GUID spoofing beyond probe's optional *observation* of custom-board interfaces (W8-D distinction).

---

*This spec is code-free and hardware-free — it defines the smallest useful instrument to decide next engineering, not to claim Xbox PC feasibility. Update `roadmap.json` W6-M1..M4 when evidence changes; regenerate dashboard via `python docs/architecture/generate-dashboard.py`.*

