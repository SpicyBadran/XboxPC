# Architecture Overview — XboxPC

**Traceability:** `ARCHOV-2026-11-22-001`  
**Companion:** `REPOSITORY_ARCHITECTURE.md` (repo layout), `research/*` (detailed subsystem research Phase 1+)

---

## 1. System Context (Phase 0 Baseline)

```
[Microsoft Xbox Series X Retail Stack]        [Our Research Artifact]      [Target PC Hardware]
 ┌──────────────┐                              ┌─────────────┐             ┌─────────────────┐
 │  Retail OS   │  ← GENUINE, not ours ──?──   │ Provenance  │             │ Reference PC    │
 │  OneCore+    │   (Phase 2 proves path)      │  Analysis   │             │ Tier 1: 1 model │
 │  Host OS     │                              └─────────────┘             │ Tier 2: family  │
 │  Hypervisor  │  ← Trust anchor unavailable?  ┌─────────────┐             │ Tier 3: broad  │
 │  Security SP │   (Phase 3 graph)            │ Boot/Sec    │             │ (claims need    │
 │  Boot ROM    │                              │  Mapping    │             │  physical test) │
 └──────────────┘                              └─────────────┘             └─────────────────┘
                                                    │
                                                    ▼
                                              ┌─────────────┐
                                              │  Diagnostic │  ← OUR code, NOT Xbox OS
                                              │  UEFI Probe │    inventories PC hw/firmware
                                              │  (Phase 6)  │    produces compatibility report
                                              └─────────────┘
```

**Critical distinction:** Our UEFI diagnostic probe (Phase 6) is an *instrument* to prove whether genuine execution could exist. It is never presented as Xbox OS.

## 2. Subsystems to Research (Phase 1 Scope)

- **CPU:** AMD Zen 2 custom, 8 cores, SMT, CPUID topology — vs commodity Ryzen
- **GPU:** Custom RDNA 2, 52 CUs, hardware RT, DirectX 12 Ultimate — vs Radeon RX
- **Memory:** 16 GB GDDR6 unified, bandwidth, reserved hypervisor/framebuffer regions
- **Storage:** Custom NVMe + hardware decompression, storage virtualization, recovery
- **Firmware/Board:** Boot ROM, security processor, ACPI-equivalent config, peripheral init
- **OS:** OneCore-derived host + partitioned game OS + hypervisor + system services

Each subsystem: technical description + authoritative source + confidence + known unknowns + PC compatibility implications.

## 3. Boot Chain (To Be Mapped Phase 3)

```
Power → Boot ROM → Security Processor init → SoC Firmware → Hypervisor load
      → System loader (authenticated) → Host OS handoff → Game partition
```

Every node will be classified: Verified / Publicly documented / Authorized access required / Unknown / Not available on standard PC.

## 4. Compatibility Strategy

- Start Tier 1 one config, expand only after evidence.
- Machine-readable `hardware-compatibility.json` — not just Markdown tables.
- Every entry: identifier, manufacturer, firmware, features, test environment, date, evidence, result (`NOT TESTED`/`TESTED—PASS`/`FAIL`/`UNKNOWN`/`BLOCKED`).

## 5. Security Posture

Preserve retail signatures; no key extraction; no bypass. If trust anchor is Xbox-only, record as blocker.

---

*This is a Phase 0 placeholder — detailed subsystem docs will be created in Phase 1 under `research/xbox-hardware/` and `research/xbox-os/`.*
