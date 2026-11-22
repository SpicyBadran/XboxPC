# BOOT_CHAIN.md — Best-Supported Understanding of Xbox Series X Boot Chain & Dependencies

**Traceability:** `BOOTCHAIN-2026-11-22-001`  
**Branch:** `arena/00f8e176-xboxpc` @ `dc01bc1` (+ audited)  
**Sources:** Verified Hot Chips 2020 pdf (8/17/20, Jeff Andrews / Mark Grossman), Xbox One Research wiki *Bootloaders / Bootchain overview* (2024-03-26), Xbox One Research wiki *FAQ*, Hot Chips live-blog (AnandTech, 09:07PM–09:15PM), ITIGIC HSP/Pluton, Tom’s Hardware / PCWorld Pluton lineage, GBAtemp partition thread, Support page OSU1/Troubleshooter docs  
**Method:** For every stage: known component → available public docs → required HW/firmware → present in OSU1? → via public GDK? → via GDKX? → unknown. Unknowns explicitly labeled. No invented component names/filenames/cryptographic formats beyond sourced ones.

> This is a Phase 5 feasibility document — it **maps** the boot chain, it does not **boot** it. No bootloader code, no binary modification, no proprietary firmware dumped.

---

## 1. Overview Diagram (Publicly Supported Model)

**Caution:** Diagram assembles Xbox One Research wiki bootloaders (directly quoted) with Hot Chips 2020 Series X SoC overview (HSP/Pluton, MSP, GDDR6, SoC Fabric). Series X “might differ slightly … different primary bootmedium (SSD instead of eMMC Flash)” per wiki — so Series X deltas are noted.

```
                        ┌─────────────────────────────────────────────┐
                        │ Power-On: Southbridge → SMC (0SMCBL ROM)    │  ← Wiki: 0SMCBL ROM (factory), 1SMCBL Flash 1smcbl_*.bin, 2SMCBL SMCFW smcfw.bin
                        │           SMC.mainloop powers Security Proc │     SMC → SP Powerup SP (verified for Xbox One)
                        └──────────────────────┬──────────────────────┘
                                               │ HOTCHIPS: HSP/Pluton Root-of-Trust, SHACK exist in Series X (VERIFIED)
                        ┌──────────────────────▼──────────────────────┐
                        │ Security Processor (SP)                   │  ← Wiki: 0SP ROM factory → 1SP →2SP patched in boot.bin
                        │ SP verifies fuses, certs, decrypts 2BL   │     Critical boot.bin stage
                        │ (key = fuses + flash per Xbox One R&D)   │     HOTCHIPS: SHACK = Secure Hardware Crypto Keys (VERIFIED)
                        └──────────────────────┬──────────────────────┘
                                               │ sp->cpu: Decrypt/Load 2BL
                        ┌──────────────────────▼──────────────────────┐
                        │ x64 CPU: 2BL                              │  ← Wiki: 2BL → initializes APU/system fabric, loads SCP FW
                        │ 2BL → SCP FW → Host VBI → hvax64         │     + keytable upload, hypervisor load
                        │ (SCP = Streaming Crypto Processor)       │     Series X: PCIe8x Gen4 fabric, I/O hub, GDDR6 560GB/s (HOTCHIPS)
                        └──────────────────────┬──────────────────────┘
                                               │ cpu→hv: Load hvax64 (Hydra Hyper-V fork, ~80% rewritten)
                        ┌──────────────────────▼──────────────────────┐
                        │ Hydra Hypervisor (Host/Parent Partition) │  ← Wiki + Homebrew Retro: HostOS ~90 MB, SPLEAP anti-EoP
                        │ Isolates HostOS / SystemOS / GameOS VMs  │     Host: manager for SRA(Sys)/ERA(Game) via VBI/VBI drivers
                        │ + Security Processor handshake            │     HOTCHIPS: SPLEAP HW (verified)
                        └──────────────────────┬──────────────────────┘
                                               │ Host VBI → host.xvd (Flash/HDD/NVMe per generation)
                        ┌──────────────────────▼──────────────────────┐
                        │ HostOS (Host VBI / host.xvd)              │  ← Wiki: Load Host VBI → host.xvd (Flash for Xbox One)
                        │ Drivers ↔ hardware + hypervisor calls    │     Series X: Host XVD likely on NVMe System partition (INFERRED)
                        │ Optional: Show Recovery Menu             │     Recovery → Xbox Startup Troubleshooter (Support page)
                        └──────────────────────┬──────────────────────┘
                                               │ HostOS path: System VBI (HDD/NVMe) → system.xvd
                        ┌──────────────────────▼──────────────────────┐
                        │ SystemOS (System VBI / system.xvd)        │  ← Wiki: Load System VBI → system.xvd → Start Game
                        │ Dashboard, Guide, UWP, settings, XMA    │     GBAtemp: System Update partition 9A056AD7... with A/B slots
                        │ Mount system-related XVDs                │     OSU1 supplies system/systemaux/systemmisc/systemtools XVDs
                        └──────────────────────┬──────────────────────┘
                                               │ SystemOS → HostOS: Request VM Start (Game)
                        ┌──────────────────────▼──────────────────────┐
                        │ GameOS / TitleOS (ERA/GameCore VBI)      │  ← Wiki: ERA/GameCore VBI → era.xvd/gamecore.xvd (Game XVC)
                        │ Game execution sandbox (Code Integrity)  │     Homebrew 2026: GameCore replaced ERA
                        └─────────────────────────────────────────────┘
```

**Series X-specific addenda (from Hot Chips):** GDDR6 20 channels x16 @14Gbps →560 GB/s, GPU 52 CUs @1.825 GHz 12 TFLOPS, 2x Zen2 clusters (4C/8T 4 MB L3 each, SPLEAP per-cluster), I/O Hub x8 PCIe Gen4, Internal 1 TB NVMe x2 PCIe4 + external slot x2 PCIe4 + Blu-Ray, HSP/Pluton RoT + MSP crypto/hash/decomp @ SSD BW (>5 GB/s crypto, >6 GB/s decomp). These sit under the SOC initial blocks above SP→2BL.

---

## 2. Stage-by-Stage Table — Known Component vs Evidence vs Availability

| # | Power → Retail OS Stage | Known Component(s) (sourced) | Available Public Documentation | Required HW / Firmware | Present in public OSU1 (`$SystemUpdate/*.xvd`)? | Via public GDK? | Via authorized GDKX? | Exact Implementation Unknown |
|---|------------------------|------------------------------|-------------------------------|------------------------|-----------------------------------------------|----------------|---------------------|------------------------------|
| 1 | **Power-on & SoC init** | Southbridge SMC 0SMCBL ROM (factory) + APU fuse/voltage + GDDR6 MC training, 360.4 mm² SoC bringup | Xbox One wiki SMC 0/1/2; Hot Chips SOC Specs physical/ block diagram (verified) | Scarlett SoC fused ROM, board flash (SMC FW), GDDR6 320-bank train sequence | **No** — SMC FW / SOC init not in `$SystemUpdate`; OSU1 cannot power-on SoC generically | **No** — GDK targets games, not SoC init | **Maybe docs** — but board/ROM not distributable | Exact Series X 0SMCBL/1SMCBL filenames for Series X; voltage train table |
| 2 | **Hardware Root of Trust (HSP/Pluton)** | HSP/Pluton Root-of-Trust, SHACK, emCPUs, SPLEAP (Hot Chips slide 7) + SP 0SP ROM →1SP→2SP (wiki) | **Hot Chips verified** SHACK/HSP/MSP exist; 09:07PM live-blog “HSP/Pluton RoT” | Scarlett SoC HSP/Pluton fused keys, fuses/per-console certs | **No** — `RM_Signature.bin` is validated *against* RoT, not it; RoT is fused in SoC | **No** | NDA topics maybe describe Xbox HSP API, not retail keys | Series X per-stage SP verification key IDs / cert chain |
| 3 | **Secure-boot stages (SP→2BL→SCP)** | Wiki: SP→Decrypt/Load 2BL, CPU→SCP Decrypt/Load SCP FW + Decrypt/Upload keytable + Host VBI | Xbox One wiki diagram + SPBL `0SP ROM / 1SP+2SP in boot.bin`; Xbox One Research “keys = fuses+flight + header obfuscation” discussion | SP ROM, `boot.bin` (1SP/2SP), 2BL, SCP FW blob, keytable | **No** — boot.bin/SCP FW not in OSU1 `$SystemUpdate`; 2BL is pre-Troubleshooter | **No** | **Maybe GDKX** has console graphics driver → SCP-adjacent, but not boot-chain signing material | Series X exact 2BL name/size / SCP blob version / keytable format |
| 4 | **Platform Security Processor (attestation/anti-rollback/XMA+audio companion)** | HSP plus Logan (4 DSP), MOVAD Opus SRC, CFPU2 2×4 FP-DSP (Hot Chips slide 7), Southbridge SMC companion, XMA HW >300 rt channels | Hot Chips “Audio: Logan/MOVAD/CFPU2” + “Security and Decompression” split; Xbox One research XMA offload | HSP isolated bus cert, anti-rollback counters, HDCP/HDR + audio companion blocks | **No** | **No** (audio DSP unrelated) | GDKX NDA audio/docs maybe | Companion bus protocol / attestation call order |
| 5 | **Hypervisor (Hydra) — hvax64** | Wiki: `Load hvax64` from Host VBI; Hydra is Hyper-V fork (~80% rewritten), runs HostOS/SystemOS/GameOS VMs via VBI | Wiki Bootloaders “Load hvax64 → Load Host VBI”; FAQ “Hydra” + 09:15PM “SPLEAP: HW to prevent EoP” | Scarlett Hypervisor binary `hvax64` (signed, loaded before HostOS) | **No** — OSU1 provides `host.xvd` *content*, not verified hypervisor image itself (HostOS VBI path includes hypervisor load) | **No** | **Not confirmed** — GDKX provides *game-target* runtime, not retail hypervisor binary | Exact `hv*` binary hash / entrypoint / per-CPU SPLEAP hook for Series X |
| 6 | **Kernel & System Partition (HostOS / host.xvd → SystemOS / system.xvd)** | Wiki: Host VBI→host.xvd (Flash), optionally Recovery Menu, critical system.xvd path: HostOS→Load System VBI (HDD/NVMe)→system.xvd; GBAtemp System Update `A/`/`B/` slots (Xbox One community-observed, Series X slot count INFERRED) | Wiki Host VBI/System VBI sections + GBAtemp GPT table + `OSU1_ANALYSIS.md` §2.2 (community-reported) | HostOS binary + SystemOS + system-*.xvd set (`system/systemaux/systemmisc/systemtools/SettingsTemplate`) + updater | **Partial — reported update slices**: community-reported `$SystemUpdate` lists `host.xvd, system.xvd, systemaux.xvd, systemmisc.xvd, systemtools.xvd, SettingsTemplate.xvd, updater.xvd` as **replacement XVD slices** (secondary-source listing, not Microsoft-quoted; authoritative manifest unavailable), not full host/system flash image | **No** | **Not demonstrably** — publicly advertised Secure Downloads are GDK recoveries, not full Host/System OS (full restricted inventory UNKNOWN) | Series X exact VBI content list / slot semantics for NVMe vs eMMC layout |
| 7 | **Graphics & Display — GPU, SFS, DXR/VRS/Mesh, MSP decomp @ SSD BW** | Hot Chips: 52 CUs @1.825 GHz 12 TFLOPS, SFS Shader Feedback Streaming (64 KB mipmap), DXR/VRS/Mesh, XVA 2:1 BCPack + Opus + Zlib; SOC: Display processor HDR/WCG + HDMI 2.1 DSC, Video encoders | Hot Chips slides 2/5, Eurogamer Inside-Specs 2020-03-16 “6 GB/s hardware decompression (Zlib/BCPack) replaces 13 avg Zen2 cores”, Neogaf Hot Chips thread SFS random-access decomp | Custom GPU firmware/driver (replaced together per 09:33PM “we replace driver + firmware, significantly more efficient than PC”), display pipe, HDMI2.1 caps; MSP decompressors 2× general+texture @ >6 GB/s | **Not as boot hardware** — OSU1 has XVDs that *use* GPU once SystemOS runs, but **no GPU firmware blob** in manifest | **No** — GDK public excludes Xbox graphics driver + Shader Compiler (README “missing … only in GDKX”) | **Yes for toolchain** — GDKX grants Xbox graphics driver + compiler (NDA) — but **runtime** GPU is still Xbox SoC; toolchain does not supply PC-Radeon fallback | Exact GPU firmware blob hash / display init tables / 64 KB SFS page driver contract |
| 8 | **Storage Controller & Device** | Internal 1TB NVMe x2 PCIe4 + external slot x2 PCIe4 (Hot Chips slide 6); Velocity + MSP @ SSD BW; Xbox Storage Virtualization (GBAtemp GUIDs + XVD overlay) | Hot Chips slide 6 storage line; Reddit Storage Arch note; GBAtemp GPT GUIDs | Xbox NVMe firmware + internal System Update partition (`9A056AD7...`, Series X NVMe-observed) | **Not image** — OSU1 bytes stream into System partitions, not NVMe FW | **No** | **No** | Series X exact NVMe FW rev / external CFExpress adapter handshake |
| 9 | **Retail OS Startup — dashboard, services, GameCore/ERA VM** | SystemOS runs dashboard/Guide/UWP; HostOS starts ERA/GameCore VM for games (wiki critical Game XVC); Era → GameCore shift noted Homebrew 2026 | Wiki “Request VM Start → Load ERA/GameCore VBI → era.xvd/gamecore.xvd” + Reddit Hydra 4-VM description (HostOS light, SRA(SystemOS), ERA(GameOS), GameCore) | SystemOS services + GameCore runtime + Hypervisor Code Integrity (HVCI-like) | **Yes* but as XVDs**: OSU1 provides game-OS/System XVD replacement slices that **require** host/system already running; they are **payload, not bootstrap** | **No** — public GDK builds games *for* this stack, does not contain it | **Not demonstrably** — GDKX does not ship retail dashboard/OS for PC — it ships *game* toolchain | Exact build string / HVCI policy set for this OS build |

**Reading:** A stage is *present in OSU1* only when the reported secondary-source manifest (community listings of `$SystemUpdate`, not Microsoft-quoted) lists an artifact that directly implements that stage; “Partial” means reported XVD slices are consumed *by* that stage once it already runs, not the stage loader itself. Reported manifest absence does not independently prove boot-adjacent components are absent (authoritative manifest unavailable). `GDKX` presence indicates documentation/toolchain *about* that stage exists behind NDA, not that stage’s retail binary is supplied for PC. No Microsoft documentation was found in searched public sources describing retail OS boot deployment on standard PC hardware.

---

## 3. Dependency Graph (Text Form — Reproduces in `docs/`)

```
ROOT (fused, verified)
  SMC:0SMCBL(ROM) → 1SMCBL(flash) → 2SMCBLSMCFW
  SP: 0SP(ROM) → 1SP+2SP(boot.bin) ↘
                                   2BL ──→ SCP FW → keytable → Host VBI → hvax64 ──→ HostOS(host.xvd, Flash/NVMe) ──[Recovery Menu]──→ SystemOS(system.xvd via A/B slots, HDD/NVMe)
                                                                                              │
                                                                                              ├── MSP: crypto/hash/decomp @ NVMe BW (verified HW blocks)
                                                                                              ├── HSP/Pluton: RoT/SHACK/SPLEAP (verified HW)
                                                                                              ├── GPU: 52CU/12TF / SFS/DXR/VRS/Mesh (verified)
                                                                                              ├── CPU: 8×Zen2 @3.8/3.6 SMT (verified) / XVD: host/system*/updater/RM_Signature.bin (reported, secondary-source)
                                                                                              └── GameOS: ERA/GameCore VBI → era.xvd/gamecore.xvd (verified model, SeriesX name inferred)
                                                                                              └── GDK:PC build path (verified: public GDK does NOT contain retail OS)
                                                                                              └── GDKX: constrained recoveries/docs only (verified text: “recoveries of GDK”, not retail OS image)
```

Every node in this graph is tagged per `EVIDENCE_AUDIT.md`: power→SOC init = VERIFIED topology / INFERRED stage names; HSP/Pluton RoT & MSP = VERIFIED (Hot Chips); Boot ROM chain file names = XboxOne-observed / SeriesX-expected (downgraded per audit, INFERRED); OSU1 payload→not-OS status = VERIFIED/STRONGLY SUPPORTED; GDK/GDKX “not retail OS image for PC” = VERIFIED from docs text.

## 4. Unknowns That Block PC Path (Do Not Invent)

- Exact Series X boot ROM artifact name/content (Xbox One: `boot.bin` contains 1SP+2SP — may still but not confirmed size/hash)
- Exact SMCFW/SP FW sequencing for Series X (southbridge→SP power-up order confirmed generally; specific binary `smcfw.bin/1smcbl_*.bin` filenames are Xbox One-observed)
- Retail signing cert chain (Xbox CA thumbprint) and RM_Signature.bin algorithm (RSA/ECDSA, payload manifest format)
- Exact HostOS hvax64 hash/build and SPLEAP per-CPU hook contract
- Series X NVMe System partition GPT exact re-layout vs Xbox One eMMC (conceptual A/B verified, exact GUIDs/byte-offsets not verified for Series X)
- Xbox One→Series X GameOS rename boundary (when Era retired → GameCore + SRA labeling) — affects but does not block analysis

**Non-proprietary route remains to deepen this without MS NDA:** Hot Chips pdf public slides + Xbox One Research wiki history (2017→2026) + xbox-xmod XVD/XBFS tooling (45 payloads parsed w/ xvd_parse.py) already provide empirical GBAtemp-verified partition inventory without touching protected ROM.

---

## 5. What Is Reproducible on PC (Honest Boundary)

- **Not reproducible generically:** fused ROM RoT, fused Xbox identity, GDDR6 560 GB/s unified-pool timings, 52-CU 12 TF custom GPU, MSP @ SSD BW rates, HSP SHACK isolation — all require Xbox SoC (verified custom). Even scenarios in next section show only limited reproduction.
- **Potentially emulatable (still not retail):** Hypervisor memory window checks, ACPI OEM tables, storage GUIDs could be spoofed in a **custom board** (scenario D) or emulated hypervisor — but spoofing is simulation, not retail hardware, and would not inherit retail signing attestation.

*This document preserves the audit correction (§10 → each blocker was over-claimed as individually sufficient; reality: cumulative) while retaining the strong case that generic PC boot is not demonstrated.*
