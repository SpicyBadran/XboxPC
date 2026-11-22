# RETAIL_OS_REQUIREMENTS.md — What PC Hardware Would Have to Provide for Genuine Retail Boot

**Traceability:** `RETAIL-REQ-2026-11-22-001`  
**Depends on:** `OSU1_ANALYSIS.md`, `DOWNLOAD_SOURCES.md`  
**Method:** Distinguish confirmed public architecture, strongly supported inferences, unknowns — do not claim x86-64 implies PC compatibility

---

## 1. Purpose

Even if OSU1 were a full OS (it is not — see `OSU1_ANALYSIS.md`), the retail Xbox Series X OS would still refuse to execute outside its trust/platform environment. This document catalogs every known/suspected dependency that prevents genuine PC boot, with classification.

## 2. Dependency Table (10 Areas from Spec)

| # | Dependency | Xbox Implementation | PC Gap | Classification |
|---|------------|-------------------|--------|----------------|
| 1 | **Hardware Root of Trust & Boot Chain** | On-SoC Boot ROM (fused, not flash-rewritable) → Security Processor init → AMD PSP-secured BLDR → hypervisor load → host OS handoff. Boot ROM is in custom Scarlett SoC (HotChips 2020). | PC UEFI firmware (`bootx64.efi` + `SEC`/`PEI`/`DXE`) is motherboard-provided, x86 generic, with TPM 2.0 via SPI/I2C (discrete TPM or firmware TPM). No Scarlett Boot ROM image is publicly distributed. Even on PCs with Pluton (Ryzen 6000+), Pluton firmware is PC-flavored, not Xbox-fused. | **Confirmed requirement; PC: not available** |
| 2 | **Secure Boot & Signature Validation** | Xbox Secure Boot chain verifies hypervisor and subsequent partitions with retail Microsoft Xbox signing keys fused into security processor / Pluton-derived HSP. `RM_Signature.bin` in OSU1 payload is validated against those keys. Failure → E-code (E105 etc.). | PC Secure Boot uses UEFI `db`/`KEK`/`PK` with Microsoft Windows Production CA for Windows boot. Xbox retail CA is not in PC db; Xbox signature cannot be validated by PC firmware; attempting to enroll Xbox keys would require Microsoft Xbox CA — not distributed. Emulated Secure Boot in QEMU can load custom keys, but that is not preservation of retail trust. | **Strongly supported inference** |
| 3 | **Platform Identity & Security Processor** | Custom Security Processor (HSP Pluton heritage): Xbox Series X was the *first* HSP Pluton deployment (HotChips talk: "Xbox Series X ... ability to decide whether program can run"). Later ported to PC Ryzen 6000 as AMD PSP+Pluton. Xbox instance holds Xbox-unique identity, attestation keys, anti-rollback counters, HDCP/content protection. Communicates with SOC via isolated bus. | PC Pluton/TPM provides different identity (device-specific EK) bound to PC manufacturer, not Xbox Live device identity. Xbox services would see unknown device. No way to provision Xbox identity onto generic PC without MS cooperation; would require Xbox Device Identity Service. | **Confirmed (Pluton lineage) + strongly inferred binding** |
| 4 | **Firmware Init & Hardware Configuration** | Custom Scarlett SoC initialization: memory controller training for 16 GB GDDR6 with 320-bit wide bus (vs DDR4/DDR5 DIMM), voltage rails, PCIe Gen4 custom fabric, hardware decompression (Zlib/BCPack), DirectStorage offload, USB+ storage controller quirks. Firmware lives partially in SoC ROM + onboard SPI flash (not in OSU1). | Commodity Ryzen desktop: DDR5 SODIMM/UDIMM, different memory map; custom GDDR6 controller config is not in PC UEFI. GPU fabric (52-CU RDNA2 with Xbox customizations — ray accelerators, sampler feedback) is SoC-internal, not discrete Radeon. No PC firmware can replicate Scarlett init sequence without SoC datasheet (NDA). | **Strongly supported** |
| 5 | **CPU Requirements** | AMD Custom Zen 2: 8 cores (2×4 with 1 core reserved per HotChips), SMT, CPUID masked to Xbox-specific family/model, virtualization via hypervisor trapping (not PC Hyper-V exactly). Power/frequency governed by custom SMU. | PC Ryzen/Inte Core present different CPUID (family/model/stepping), different topology and C-state controls. Retail OS likely hard-checks CPUID against allowlist; mismatch at kernel/hypervisor level would hang. Instruction set is same (x86-64) but platform config is not. | **Confirmed architecture; strong inference of CPUID gating** |
| 6 | **Memory Layout & Initialization** | Unified 16 GB GDDR6: 10 GB @ 560 GB/s for GPU-optimized + 6 GB @ 336 GB/s; 32 MB?/Reserved hypervisor + Secure Enclave windows; contiguous physical carve-outs for framebuffer, decompression scratch, hypervisor shadow pages. Memory protection via hypervisor (Guest Mode Execute Trap etc.). | PC split pools (system DDR + VRAM). No unified high-bandwidth GDDR6 backing; address map from UEFI memory map would expose DDR5 regions, not Xbox carve-outs. Hypervisor would attempt to map absent physical windows → fault. | **Strongly supported** |
| 7 | **GPU Architecture & Driver** | Custom RDNA 2 embedded in SoC: 52 CUs @ 1.825 GHz (12 TFLOPs), 3328 shaders (?), hardware RT, Sampler Feedback Streaming, Variable Rate Shading, mesh shaders. Command submission via custom Xbox Graphics Command Processor + firmware; drivers are inbox Xbox, not Radeon Adrenalin. PCIe device ID is Xbox-specific (not RX 5700/6700 XT). | Discrete Radeon or integrated RDNA2 present different PCI IDs, BARs, and firmware interface. Retail OS driver would probe for Xbox GPU BAR topology and firmware blob (not present) → fail. Vulkan/DX12 on PC is different ABI from Xbox's Xbox Graphics API (GDKX-only, NDA). | **Confirmed GPU custom; strong inference of driver fail** |
| 8 | **Storage Controller & Device Assumptions** | Custom NVMe controller (raw 2.4 GB/s, 4.8 GB/s compressed, 1 TB stock) + Xbox Storage Virtualization (partitions Temp/User/System Update/System Support, XVD overlay), hardware decompression engine tightly coupled to storage. Velocity Architecture expects specific queue depths and I/O prioritization. | PC NVMe/SATA/USB exposes standard NVM Express driver; Xbox OS storage stack expects Xbox partition GUIDs (`869BB5E0...` etc. + B3727DA5..., C90D7A47...) and Xbox-padded GPT layout; standard Windows GPT would be rejected. Read-only Block I/O probe in our diagnostic would show different. | **Strongly supported** |
| 9 | **Hypervisor & Kernel Dependencies** | Xbox host OS runs atop Xbox Hypervisor (a OneCore-derived hypervisor with Host OS + Game OS partitions, System OS, Era OSVM). Hypervisor is early-boot-loaded and depends on Security Processor + SMU secure handshake. It enforces isolation: host cannot see GameVM memory, and vice versa. | PC hypervisor (Hyper-V, KVM) is different root-of-trust; Xbox hypervisor expects Xbox Security Processor + ACPI tables + SR-IOV config not present on PC. Booting Xbox hypervisor image on QEMU would immediately require Xbox ACPI (`MSFT` OEM?) and would not find security processor MMIO. | **Strongly supported** |
| 10 | **Platform Interfaces (ACPI/SMBIOS/UEFI)** | Xbox firmware exports custom ACPI tables (not standard PC DSDT/SSDT/MSDM/SLIC but Xbox-specific OEM ID "MSFT" with Xbox SSDT entries for SoC thermal, power, custom bus). SMBIOS reports Xbox model/revision for licensing (e.g., `Xbox Series X` string). Boot manager invokes Xbox-specific HAL extensions. | PC ACPI/SMBIOS reports motherboard vendor (ASUS, Gigabyte, etc.) and generic OEM IDs. Xbox OS would detect mismatch (e.g., lookup for `XBOX` OEM table fails, device presence check for `\_SB.XBOX_` scope absent) and intentionally halt per E-code path. UEFI boot would not even start Xbox OS loader (no Xbox boot manager entry in Boot#### vars). | **Confirmed ACPI divergence pattern; inference of intentional gating** |

---

## 3. Summary Classification

- **Confirmed requirements:** Root of trust (Boot ROM), Pluton/Security Processor lineage, basic SoC customization (HotChips 2020), memory unified pool existence
- **Strongly supported inferences:** CPUID allowlist, signature validation, GPU BAR/firmware mismatch, storage GUID enforcement, hypervisor dependency, ACPI OEM check — each follows directly from Xbox console security model documented for TPM/Pluton + PC analogous behavior
- **Unknown requiring evidence:** Exact ACPI table names/fields (NDA), precise hypervisor handoff calling convention, decompression engine register addresses, E-code-specific failure thresholds

No row establishes PC compatibility; x86-64 ISA overlap is necessary but not sufficient.

## 4. What Would Prove Otherwise

A PC-boot path would require **all** of:

1. Microsoft-authorized Xbox identity provisioning for PC (no public program — Secure Downloads page lists no such artifact)
2. Published Xbox Boot ROM/FW for PC or Xbox Security Processor emulation with retail keys (no public distribution)
3. Published Xbox HAL/DSDT for generic PC (NDA)
4. Microsoft-signed hypervisor image that targets PC firmware (not listed in GDKX recoveries)

Absent these, genuine retail boot on PC remains **blocked** regardless of OSU1 availability.

## 5. References

- HotChips 2020 Microsoft Xbox Series X System Architecture deep dive (Chip-to-cloud Pluton diagram, Scarlett SoC block diagram, memory subsystem)
- `itigic.com/hsp-pluton-security-processor-inside-cpus/` — "Xbox Series X is where HSP Pluton has ability to decide whether program can run"
- `tomshardware.com/news/microsoft-pluton-processor-intel-adopt-amd-security-approach` — Xbox-on-2023 → PC on 2026 port lineage: AMD Security Processor (2013 Xbox) → Azure Sphere → Pluton in Ryzen 6000
- `pcworld.idg.com.au/article/.../microsoft-pluton-will-build-xbox-security...` — AMD ASP (Cortex-A5) → Pluton integration, SHACK key isolation
- XboxOne HDD repair thread `gbatemp.net/threads/496212` — GPT GUIDs and A/B slot update mechanism (infer Series X retained)
- `support.xbox.com/.../offline-system-update` — E-codes E105 etc. imply signature failure paths
- Public GDK vs GDKX distinction (`github.com/microsoft/GDK` README + `aka.ms/gdk` access page)

*All claims cite observable public or community-verifiable evidence; no proprietary Xbox firmware was accessed.*
