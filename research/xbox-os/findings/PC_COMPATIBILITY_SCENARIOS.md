# PC_COMPATIBILITY_SCENARIOS.md — Scenario-Separate Assessment (Audit-Required)

**Traceability:** `COMPAT-SCENARIOS-2026-11-22-001`  
**Depends on:** `BOOT_CHAIN.md`, `EVIDENCE_AUDIT.md`, `RETAIL_OS_REQUIREMENTS-CORRECTIONS.md`, `DOWNLOAD_SOURCES.md`  
**Method:** Each scenario evaluated against 10 dependency areas (§5 of RETAIL_OS_REQUIREMENTS) with explicit *known / missing / reproducible / requires authorization / demonstrated?* — never conflating “runs Xbox-developed games” with “runs retail Xbox OS”; never treating dev kit as proof of generic PC capability.

---

## Ground Rules

| Rule | Rationale |
|------|-----------|
| Don’t confuse “runs games built with GDK” with “runs retail HostOS/SystemOS/GameOS” | Public GDK builds Win32+GDK games that *target* Xbox consoles/xCloud via Win32 abstraction; they do not invoke Xbox HostOS Hypervisor or SystemOS dashboard — verified by GDK README missing Xbox driver |
| Don’t treat Dev Kit as generic PC proof | A licensed Xbox Dev Kit **is Xbox hardware** with dev firmware — boot succeeds *because* it is Xbox-trusted, not because path works on generic PC |
| Custom board ≠ generic PC | Scenario D is intentionally included to separate “engineered to mimic selected Xbox characteristics” from “bought at retail for $800” |

---

## A. Generic modern AMD desktop PC (e.g., Ryzen 7000/8000 on AM5, DDR5, Radeon RX 7600–7900, UEFI 2.8+, Secure Boot with Windows CA)

| Sub-question | Answer |
|--------------|--------|
| **What is technically known** | PC is x86-64 ISA compatible (verified). CPU is Zen 4/5 Family 19h/26h (not Fam 17h model 71/132), memory is split DDR5 5200–6000 on 2×64-bit channels (not 20×16 GDDR6 560 GB/s with 320 banks — verified Hot Chips), GPU is discrete RDNA 3/3.5 with PC Adrenalin driver (not Xbox embedded 52 CU 12 TF non-HAL GPU — verified custom), storage is standard NVMe (not Xbox GPT GUIDs or MSP offload), UEFI exports `DB/Kek/PK` Windows CA (not Xbox CA — inferred, not thumbprint-verified), HSP/Pluton may exist on Ryzen 6000+ AM5 but is PC-flavored (verified port lineage 2021, not Xbox identity) |
| **What is missing** | Fused ROM RoT / Scarlett Boot ROM image, Xbox-fused retail keys validating `RM_Signature.bin`/XVDs, GDDR6 unified-pool 10+6 interleave timings, custom ACPI/SMBIOS OEM scope, HVax64 + HostOS host.xvd that *targets* PC firmware, GameCore image that addresses PC BARs |
| **What could theoretically be reproduced** | CPU mode (still Zen-family), NVMe 4.0 throughput approaching Xbox raw (2.4 GB/s), display via UEFI GOP up to 4K120 — none reproduces Xbox platform config, only generic PC config |
| **What requires MS authorization / proprietary HW** | Retail signing cert chain, Xbox HSP/Pluton identity, GDDR6 controller firmware, MSP decompressor schedule/BCPack dictionary, Xbox driver+GPU firmware coupling, GPT GUID enforcement |
| **Genuine retail OS execution demonstrated?** | **No — not demonstrated. Cumulative divergence makes drop-in boot implausible; no independent test has booted retail `system.xvd` on any generic AMD desktop and passed attestation** |

*Classification: `NOT CURRENTLY DEMONSTRATED`; strong negative but not proven exhaustive impossibility because scenario D remains theoretically conceivable (so stronger negative would exceed evidence).*

## B. Generic modern Intel desktop PC (e.g., Core 13th/14th or Arrow Lake, DDR5/DDR4, GeForce RTX 40/50, UEFI + TPM 2.0 discrete)

| Sub-question | Answer |
|--------------|--------|
| **Known** | x86-64 still, Intel CPUID Family 6 model ~0xB5/0xC5/0xA7 vs AMD 17h — even further from Cardinal/Project X; integrated security processor is Intel BootGuard/Titan-derivative (not AMD ASP/HSP); GPU is NVIDIA, entirely different driver ABI (not Xbox 52-CU RDNA2); same storage/UEFI divergences as A |
| **Missing** | Same as A plus *greater* CPU-topology distance; Intel SMU/power/thermal tables unrelated to Scarlett; Intel I/O fabric not AMD Scalable Data Fabric |
| **Reproducible** | Only generic x86-64 + NVMe speed; no Xbox platform characteristic reproduced more than A |
| **Requires authorization** | Same as A; even custom x86-64 board using Intel would need to spoof AMD-specific Fabric/coherence and GPU |
| **Demonstrated?** | **No — strictly weaker case than A** |

## C. AMD PC with integrated Security Processor (Ryzen 6000+/7000 with Pluton) + modern UEFI Secure Boot (TPM 2.0 / discrete / fTPM, SHACK-capable)

| Sub-question | Answer |
|--------------|--------|
| **Known** | PC Pluton *does* descend from Xbox HSP program — verified lineage: Xbox ASP (2013 Cortex-A5) → Azure Sphere → AMD Security Processor (+Pluton) 2020→ Ryzen Mobile 6000 (PCWorld/Tom’s 2020). So PC now has HSP-class hardware — **but** firmware is PC-provisioned (AMDs PSP + Pluton 2.0 SHACK-like), bound to PC manufacturer EK and Windows/BitLocker policy, not Xbox Live |
| **Missing** | Xbox-fused identity (Xbox per-console certs, Live attestation, anti-rollback fused counters), Xbox SMU/HSP→SCP handshake expecting Scarlett fuse set, Xbox storage GUID expectation, GPU, GDDR6, ACPU/SoC fabric |
| **Reproducible** | Hardware crypto/hash/decomp blocks conceptually overlapping with MSP blocks, but *instance* is PC-bound; QEMU/OEM Secure Boot could enroll custom Xbox CA and still not supply hardware root-of-trust — emulated, not hardware-rooted |
| **Requires authorization** | Xbox identity provisioning service (no public program; MS rep enable for GDKX does not grant Xbox CA); Xbox GPU firmware/GDDR6 init |
| **Demonstrated?** | **No — Pluton-on-PC does not make PC into Xbox-trusted platform. Microsoft explicitly migrated *technology* from Xbox to PC for Windows security (PCWorld 2020: “Xbox security approach for PCs” + “chip-to-cloud” via Windows Update), not for porting Xbox retail OS to PC** |

*Note: Treating “Pluton on PC proves Xbox OS should now boot” conflates lineage with provisioning — audit downgrades this from alleged blocker #3 to correctly understood distinction between hardware-class vs instance.*

## D. Custom x86-64 motherboard designed to reproduce selected Xbox platform characteristics (bespoke board, not generic PC)

| Sub-question | Answer |
|--------------|--------|
| **Known** | Hypothetical — *could* implement subset: 20-channel GDDR6 interleaving emulation (costly, still not same bank count), spoof ACPI `MSFT` OEM + `\_SB.XBOX_` scope + `XBOX` SMBIOS string, expose Xbox GPT GUIDs via custom SPI NVMe shim that re-exports `9A056AD7…` System Update layout, mimic BAR map of embedded GPU via FPGA-attached RDNA2, expose Security Processor MMIO shim that ignores checks |  
| **Missing** | Fused Xbox retail keys/cert chain (cannot self-provision retail trust — would need Microsoft signing), genuine HSP/Pluton Xbox identity, exact GPU driver blob *signed by Microsoft for retail OS to accept*, Hypervisor `hvax64` binary authorized for this board (MS would need to sign it), exact SMU/SoC init sequence (NDA), NVMe MSP/BCPack hardware scheduler |
| **Reproducible in principle** | Selected **observable** platform characteristics (ACPI names, GUIDs, memory map windows, BAR sizes) are spoofable by an engineer with SoC datasheet access; they are *interfaces*, not *trust* |
| **Requires authorization** | Retail signing for every stage (boot.bin→hypervisor→XVDs) by Microsoft Xbox CA; without signature, spoof fails attestation → retail OS intentional E-code halt (expected per community E-code repair reports, not Microsoft-quoted Series X log; not bypassed) — would require MS to sign custom board as Xbox hardware (a console hardware SKU decision, not a software project) |
| **Demonstrated?** | **No demonstration exists; theoretically it is the *only* non-Xbox path that could even approximate retail checks — but it defeats “standard PC hardware” objective and still needs MS retail signatures, so even this path is `NOT CURRENTLY DEMONSTRATED` for the charter’s “standard PC hardware” goal** |

*This scenario corrects old claim #10 (“each listed blocker independently prevents all possible PC boot paths”) — for generic PC, cumulative block is dispositive; for a custom board, some *interface* blockers are defeatable, but the *trust* blocker remains.*

## E. Licensed Xbox Development Kit (GDKX-target, Xbox hardware with dev firmware)

| Sub-question | Answer |
|--------------|--------|
| **Known** | Dev Kit **is** Xbox-derived SoC (same Scarlett family, dev-fused identity) with dev hypervisor that can launch both ERA/GameCore and UWP/SystemOS sandboxes; GDKX toolchain (Xbox graphics driver + Shader Compiler + NDA APIs) targets it; GDK recoveries target it |
| **Missing relative to charter goal** | It is **not** generic PC — it is proprietary Xbox hardware sold/leasable only to managed program members under NDA; using it would violate success criterion “Does not require a physical Xbox” → “standard PC hardware, no console dependency” (charter §1 table) |
| **Reproducible** | Irrelevant — success is on Xbox-silicon |
| **Requires authorization** | Partner Center + GDK Agreement + MS rep + dev-kit hardware provisioning (exactly the program described in `MICROSOFT_ACCESS.md`) |
| **Genuine retail OS execution demonstrated?** | **Trivially on Xbox-derived hardware, non-trivially on PC; charter treats this as `CONTROLLED EXPERIMENTS that cannot be represented as genuine execution` (Part I §3 category Research/emulation), not as Phase 7 acceptance** — so **No** for the charter objective, **Yes** for obvious trivial Xbox-hardware case that this project is not claiming |

*This distinction was missing in early drafts that could be misread as “GDKX proves PC should now boot” — EVIDENCE_AUDIT §2/S10 correction clarifies.*

## F. Actual Xbox Series X hardware (retail console — the control)

| Sub-question | Answer |
|--------------|--------|
| **Known** | Entire verified chain executes: power SMC→SP ROM→2BL→SCP→Host VBI→hvax64→HostOS(host.xvd)→SystemOS(system.xvd via A/B)→GameOS/GameCore(era.xvd/gamecore.xvd), with OSU1 update payload consumed via Troubleshooter onto System Update partitions; MSP/HSP/MSP offload verified; storage/GPU/memory exact as Hot Chips |
| **Missing** | Nothing for its own execution — this is the **reference truth**; still not inspectable inside sandbox (no proprietary binary dumped) |
| **Reproducible** | Xbox boots Xbox — not evidence of PC boot |
| **Requires authorization** | Ownership of retail hardware only (public) |
| **Genuine retail OS execution demonstrated?** | **Yes — on its native hardware. This is the baseline; the project’s charter asks whether *the same* OS boots on generic PC hardware without host OS/Linux, without emulation, without dashboard clone — which remains undemonstrated** |

*F corrects earlier overconfident extrapolation: because F boots, G generic PC boot was assumed to be blocked by same factors that F relies on — but audit shows some factors (CPUID allowlist, ACPI OEM gating) are **inferred**, not witnessed in F’s logs either.*

---

## Summary comparison

| Scenario | Generic HW → Xbox RoT gap | Verdict on genuine retail OS boot (charter sense) |
|---------|------------------------|---------------------------------------------------|
| **A Generic AMD PC** | Multiple (CPU family, GDDR6 topology, GPU custom, storage GUIDs, PC Secure Boot CA) — some VERIFIED, some STRONGLY SUPPORTED/INFERRED | **NOT CURRENTLY DEMONSTRATED** (strong engineering case against, not exhaustive impossibility proof) |
| B Generic Intel PC | Strictly larger gap (plus Intel vs AMD fabric) | **NOT CURRENTLY DEMONSTRATED — even weaker** |
| C AMD Pluton PC | Pluton lineage verified but PC-instance not Xbox-identity — narrows one HW class gap, still missing Xbox provisioning | **NOT CURRENTLY DEMONSTRATED** |
| **D Custom board** | Interface gaps spoofable; trust gap (retail signatures) still requires MS authorization | **NOT CURRENTLY DEMONSTRATED on “standard PC hardware” charter terms; theoretically nearest to hypothetical if MS cooperated — but then it wouldn’t be standard PC** |
| E Dev Kit | Xbox silicon — trivial Xbox-side boot, but charter categories it as dev-ecosystem, not PC proof | **No (per charter) / Yes (trivially on Xbox hardware)** |
| F Xbox Series X | Reference truth | **Yes — on native hardware, not in scope** |

**No scenario shows genuine retail OS executing on generic PC hardware.** The corrected blocker set therefore does **not** need to claim “each independently proves impossibility”; it suffices to claim “cumulative, independently audited block demonstrates generic PC path is not currently established”.
