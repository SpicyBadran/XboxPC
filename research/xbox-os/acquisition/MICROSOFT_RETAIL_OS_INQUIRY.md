# MICROSOFT_RETAIL_OS_INQUIRY.md — Prepared Inquiry to Establish Authorized Retail OS Acquisition Route

**Traceability:** `INQUIRY-2026-11-22-001`  
**Branch:** `arena/7ff9d1c6-xboxpc` @ `86cccdb` (base `8771211` on `main`; historical provenance `dc01bc1` → `1eac66c` preserved)  
**Prepared:** 2026-11-22 UTC — **DRAFT for Owner review only — DO NOT SUBMIT**  
**Author Roles:** Documentation & Evidence Agent (inquiry draft), Security Research Reviewer (legal boundary check), Verification Agent (contact-route verification)  
**Method:** Distinguishes OSU1 / Public GDK / secure Xbox downloads content / Complete retail OS image; contact routes are only those fetched from authoritative Microsoft domains (no invented representatives)  
**Status:** Ready for owner approval — external action blocked until owner authorizes — **inquiry UNSENT, no Microsoft contact, W7-M1 BLOCKED**

---

## 1. Objective (Unchanged — observable behavior first)

Establish by **authorized, documented Microsoft response** whether a route exists to **legitimately obtain the genuine Xbox Series X retail operating system** — defined first by **observable behavior**: genuine, unmodified Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services without a Windows/Linux host, emulator, or dashboard clone — for execution on **standard x86-64 PC hardware** (generic modern AMD/Intel desktop, UEFI, NVMe, discrete GPU — Tier 1 reference):

- Genuine, unmodified Microsoft OS components (retail-signed, observable on retail console)
- Direct boot on non-Xbox PC hardware (generic modern AMD/Intel PC — charter Tier 1 reference)
- No Windows/Linux host underneath
- No emulator or dashboard clone substituting for the retail OS
- No hardware trust bypass (preserve retail signatures)

HostOS/SystemOS/hypervisor package structure (e.g., `host.xvd`/`hvax64`/`system.xvd`) is **labeled as internal hypothesis where not directly established for Series X** (Xbox One-observed, Series X expected — see `BOOT_CHAIN.md` §1). We do **not** assert this is Microsoft-defined package naming or a confirmed Series X specification.

**This inquiry does NOT request:** game SDK samples, GDK tooling, OSU1 re-explanation, Insider preview access, hardware discounts, or bypass of security controls.

---

## 2. Background Provided to Microsoft (For Context — Included in Cover Note)

To prevent misreading this as a game-publishing request, every submission will include this framing:

> **Context:** Our research organization maintains a PC compatibility investigation (“XboxPC”) under charter `CHARTER-2026-11-22-001`. We have independently audited public artifacts:
> - **OSU1 (support.xbox.com/.../offline-system-update)** is a **public update payload** (`$SystemUpdate/*.xvd` + `RM_Signature.bin` applied via Xbox Startup Troubleshooter to existing `System Update` A/B slots per community-reported layout from GBAtemp/futuretweets referencing official article; Support article existence verified at URL, body returned JS loading placeholder per Phase 6.1 — Microsoft names it Offline System Update, not factory image) — STRONGLY SUPPORTED as not a full OS nor independently bootable.
> - **Public GDK (github.com/microsoft/GDK, id 348416224)** is a **game SDK** for building Win32+GDK games that target Xbox/PC/cloud — explicitly missing Xbox console graphics driver/Shader Compiler/console environment APIs (README § “missing … only in GDKX”).
> - **Secure Xbox Downloads (aka.ms/gdkdl, learn.microsoft.com/.../access-resources)** is documented as **secure Xbox downloads including GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples** — not a retail OS image for generic PC; personal MSAs no longer supported; Secure Downloads requires Partner Center Xbox-provisioned account + valid GDK Agreement + Entra ID tenant + MS representative enablement (`MICROSOFT_ACCESS.md`). Public documentation establishes the listed contents (GDK software and GDK recoveries, documentation, Submission Validator, restricted samples); **do not claim this is exhaustive — full restricted inventory beyond that public description is UNKNOWN**.
> - Whether GDKX recoveries are exclusively intended for licensed Xbox development kits remains **Q3 — an open question**, not an asserted fact until direct authoritative source establishes it.
> - No public or authorized-secure page in our searched public sources (bounded search: support.xbox.com article shell not captured, GitHub GDK, learn.microsoft.com GDK access-resources, community storage threads) was found to advertise a retail OS image for generic PC deployment (NOT FOUND IN SEARCHED PUBLIC SOURCES; internal existence UNKNOWN).
>
> We seek only a **yes/no/qualified** answer on whether such an authorized image exists, per the six questions below, to record the official authorization boundary.

---

## 3. The Six Formal Questions (To Be Asked Verbatim — aligned with decision packet)

> **Q1 — Complete retail OS image:** Does Microsoft provide, through any authorized program (public download, Partner Center Secure Downloads, managed developer program, research license, or other documented offering), a **complete Xbox Series X retail operating system image** (genuine, unmodified retail-signed Xbox Series X OS observable on retail console booting to dashboard/system services — regardless of internal package naming; internal model *may* involve HostOS/SystemOS/hypervisor components per Xbox One-observed map, labeled as hypothesis where not established for Series X)?
>
> **Q2 — PC-target configuration:** Is there a **Microsoft-supported, Microsoft-documented PC-target image or deployment configuration** of that retail OS for standard x86-64 PC hardware (generic modern AMD or Intel desktop with UEFI, NVMe, discrete/integrated GPU — Tier 1 family) that boots directly without a Windows/Linux host?
>
> **Q3 — GDKX recovery scope:** Are **GDKX recovery packages** available via Secure Xbox Downloads **exclusively intended for licensed Xbox development kits** (Xbox-derived SoC hardware with dev firmware), rather than as deployment artifacts for generic PC hardware?
>
> **Q4 — Authorized research access:** Is there an **authorized research or documentation program** (beyond ID@Xbox publishing) that provides access to the retail boot chain and required platform documentation (fused root-of-trust description, HSP/Pluton Xbox-instance behavior, SMU/SCP handshake outline, ACPI/SMBIOS surface expected by retail OS) sufficient to evaluate PC feasibility without bypass?
>
> **Q5 — Deployment authorization:** Does Microsoft **support or authorize** deployment or redistribution of retail Xbox OS components (signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox PC hardware — or, conversely, can Microsoft confirm that **no such deployment is supported**?
>
> **Q6 — Recorded distinction:** Can Microsoft **clarify whether any authorized PC-targeted retail OS offering exists** for standard x86-64 PC hardware, and if no such offering exists, **confirm that distinction in writing** for the project’s feasibility record — i.e., that OSU1 is an update package, public GDK is a game SDK, secure Xbox downloads content as publicly documented does not include a PC-bootable retail OS image, and **none of the three as currently offered constitutes a PC-bootable retail OS image**?

**Deliverable expectation:** A written answer (email, Partner Center message, or linked doc page) attributable to Microsoft — not community speculation — that can be cited in `FEASIBILITY_FINAL_REVIEW.md` update with URL + date. **A positive O1 answer alone does not change feasibility; all four O1 conditions (identifiable artifact/provenance, legitimate route+agreement, explicit PC deployment authorization, supported hardware/configuration + deployment docs) must be evidenced before `NOT CURRENTLY DEMONSTRATED` can move.**

---

## 4. Definitions (Included as Attachment to Prevent Conflation)

| Term (our usage) | What it is | What it is not | Source that establishes distinction |
|------------------|------------|----------------|------------------------------------|
| **OSU1** | Public offline **update package** from `support.xbox.com/.../offline-system-update`: `OSU1.zip` → `$SystemUpdate/*.xvd` (host/system/systemaux/systemmisc/systemtools/updater/SettingsTemplate) + `bootanim.dat`/`empty.bin`/`RM_Signature.bin`, applied from within Xbox Startup Troubleshooter to pre-existing `System Update` A/B partitions. ~4.8–6 GB, version-gated (greyed out if past version). | Not a complete OS, not a disk image, not independently bootable, not firmware, not boot ROM, not PC-compatible. Xbox One repair `gbatemp.net/threads 496212` shows A/B copying model; TechDows documents version gate. | `fetch_page` Support page shell + `DOWNLOAD_SOURCES.md` §1 + `OSU1_ANALYSIS.md` + 5 community corroborations |
| **Public GDK** | Microsoft Game Development Kit (public, `github.com/microsoft/GDK`): common tools/libs/docs to build **games** for Xbox Game Pass for PC (Win10/11), Xbox consoles (game target), cloud. Distribution via WinGet `Microsoft.Gaming.GDK`, NuGet `Microsoft.GDK.Windows`, vcpkg `ms-gdk`. Missing Xbox console driver/Shader Compiler/console env APIs. | Not the retail OS, not hypervisor, not HostOS/SystemOS, not boot chain. README explicitly: “Xbox console gfx driver + Shader Compiler … currently only in GDKX” | GitHub API id `348416224` private false stars 1741 commit `d773744` README 17186 B + `learn.microsoft.com/.../access-resources` public vs secure split |
| **Secure Xbox Downloads / GDKX** | Secure Xbox downloads **including GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples** per public documentation (`learn.microsoft.com/.../access-resources`). Requires Partner Center Xbox-provisioned account + valid GDK Agreement + Entra tenant + **MS representative** enable of `aka.ms/gdkdl`. Personal MSAs excluded. Public docs establish listed contents; **full restricted inventory beyond that public description is UNKNOWN — do not claim exhaustive**. Whether recoveries are exclusively Dev Kit-only remains Q3, not asserted here. | Not a retail OS image for generic PC. Even behind auth, no line in public docs advertises PC deployment of retail OS. Whether any recovery is exclusively Dev Kit-only is the subject of Q3, not asserted here. | `fetch_page` access-resources ch 0–1 + `MICROSOFT_ACCESS.md` §3–5 + onboarding docs `devdocs.xbox.com/home/onboarding` checklist |
| **Complete retail OS image (object of inquiry)** | **Observable objective first:** Genuine, unmodified, Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services without a Windows/Linux host, emulator, or dashboard clone — i.e., what “boots the Xbox” rather than what “builds games for Xbox.” **Internal architectural model (hypothesis, not Microsoft definition):** Our research hypothesizes this *may* involve a Host partition / hypervisor / System partition (e.g., `host.xvd` / `hvax64` / `system.xvd` per Xbox One-observed `BOOT_CHAIN.md` §1), but this is **labeled as internal hypothesis where not directly established for Series X**, not asserted to be Microsoft’s package naming, a confirmed Series X specification, or an offered deliverable. **Question to Microsoft:** Whether Microsoft offers *any* complete, authorized, PC-targeted retail OS image/configuration satisfying the observable objective, regardless of internal package naming/architecture. | Not OSU1 (update of some XVDs), not GDK, not GDKX game toolchain. Would need to be a Microsoft-signed, PC-targeted image to satisfy charter. None documented as offered. | Charter §2 success table + Hot Chips 2020 pdf (360.4 mm² 15.3B transistors, 16 GB GDDR6 10+6, GPU 52 CU 12 TF, HSP SHACK MSP 4crypto/4hash/2decomp) + Xbox One Research wiki bootloaders (XboxOne-observed, SeriesX-expected) |

*Attaching this table avoids the common misinterpretation “OSU1 contains system.xvd hence is the OS” and “GDKX recoveries are OS images for PC” — both rejected by evidence audit (`EVIDENCE_AUDIT.md` S1–S10).*

---

## 5. Official Microsoft Contact Routes — Research Results (Do Not Invent)

> Per instruction: prioritize (A) existing partner contact if available to owner, then (B) documented GDK support / developer-partner channels. No invented email/address.

### 5.1 Route A — Preferred Internal-Routing Path If Organizational Microsoft Account Relationship Exists

| Channel | What it is | When to use | Source |
|---------|------------|-------------|--------|
| Existing **Microsoft account team / Xbox developer program representative** for your organization (if already onboarded to ID@Xbox/Partner Center) — the same `Microsoft representative` referenced in access-resources for Secure Downloads: *“You must contact your Microsoft representative to enable access to the secure download site.”* | **Preferred internal-routing path** if organization already has Microsoft account relationship — Microsoft explicitly routes **Secure Downloads enablement** through this representative (Important box). It **is not exclusive authority on product inventory or retail OS policy** — for Q1–Q2 retail OS licensing/platform-engineering scope, ask to route to appropriate Xbox platform/OS or licensing team if out of scope. | Owner already has Partner Center Xbox-provisioned account (check `PARTNER_ORG` before using) | `fetch_page learn.microsoft.com/.../access-resources?view=gdk-2604` ch 0 § “Accessing secure resources” — Important box verbatim |

> If owner has such a contact, **this is a preferred internal-routing path** (not exclusive authority) for Q3/Q5/Q6 and can route Q1–Q2 to the appropriate team. **Response SLA UNKNOWN — do not promise a response time.**

### 5.2 Route B — Documented GDK Developer Support Channels (No Prior Partnership Required for Initial Contact)

| # | Official Channel | URL / Identifier | Purpose per Microsoft | What to ask | Evidence |
|---|-----------------|------------------|-----------------------|-------------|----------|
| B1 | **Microsoft Developer Support — ID@Xbox Program** | `https://developer.microsoft.com/en-us/windows/support` → section **“ID@XBOX Program” — “Email ID@XBOX.com”**; landing page `https://developer.microsoft.com/en-us/games/partner` → “Ready to publish on XBOX? → Join ID@XBOX” | “For questions about the ID@XBOX program including game publishing, console questions, onboarding to the program and **XBOX DevKits**, contact the team directly. Email ID@XBOX.com” — **documented initial contact for ID@Xbox, console, onboarding, and DevKit questions** | Submit Q1–Q6 as **policy clarification, not onboarding**: “We are evaluating feasibility of an authorized research path to retail OS image for standard x86-64 PC (not a game publishing plan). Does such a path exist? See attached definitions. **If this inbox cannot answer retail OS licensing/platform-engineering scope (Q1–Q2), please route to the appropriate Xbox platform/OS or licensing team.**” — avoids misrouting as game pitch | `fetch_page developer.microsoft.com/en-us/windows/support` (Nov 21 2022) + `web_search GDK support ID@Xbox` result id=1 |
| B2 | **Microsoft Q&A — How can I obtain GDK hardware / Unable to access GDK download** | `https://learn.microsoft.com/en-us/answers/questions/1663748/how-can-i-obtain-the-gdk-hardware` and `https://learn.microsoft.com/en-us/answers/questions/5884771/unable-to-access-to-download-gdk-for-xbox-development` (both `learn.microsoft.com` official Q&A) | Official Microsoft-staff answers on GDK/GDKX access: requirements are organizational Entra ID tenant associated with **onboarded** Xbox Development partner in Partner Center; Secure Downloads needs **GDK Agreement + MS rep enable** | Post Q1–Q6 as **follow-up question** on one of these threads (or new question tagged `gaming-gdk`) if B1 email confirmation not yet sought — Microsoft external staff explicitly answer there and cite `GDK Agreement` terms | Both threads fetched via `web_search` “how can I obtain GDK hardware” — Microsoft external staff answers cite GDK Agreement |
| B3 | **Xbox GDK Developer Forum** | `https://aka.ms/gdkforum` (aka.ms shortlink → forum; listed on `devdocs.xbox.com/home/onboarding-access/access-resources` “GDK developer forum: Post questions and report issues to the XBOX team” + `learn.microsoft.com` GDK docs “Get help” area) | Developer Q&A with Xbox engineering team; accessible after at least limited onboarding (see below). Microsoft engineering monitors. | Ask Q3/Q5 directly after Step B4 limited exploration: “Are GDKX recoveries at `aka.ms/gdkdl` exclusively for Xbox dev kits?” — Microsoft staff routinely clarify scope there | `web_search` “Access GDK dev resources devdocs.xbox.com access-resources” result id=2 + onboarding checklist |
| B4 | **Xbox Partner Onboarding Checklist (read-only, no registration)** | `https://devdocs.xbox.com/home/onboarding` (Xbox Game Development Documentation) — full checklist: *Register as Xbox partner → Enroll to Partner Center (accept App Developer Agreement, receive Seller ID) → Apply to ID@XBOX (business info + game concept, sign Title Licensing Agreement + GDK License Agreement) → Complete onboarding via SupplierWeb + Entra ID free creation → EDS account for dev kits* | Read-only route identification — lets owner **evaluate eligibility** without creating accounts | Review prerequisites: legal entity, DUNS recommended, shipping address, NDA, ≥18, country where MS does business, Microsoft Entra capability, willingness to sign GDK Agreement — **no registration, agreement acceptance, or hardware purchase occurs now** | `fetch_page devdocs.xbox.com/home/onboarding` + `web_search ID@Xbox programSelection` |
| B5 | **Xbox Insider Program (not for this inquiry, noted to avoid misdirection)** | `https://www.xbox.com/en-us/developers/insiders` | Playtest audience expansion, not developer onboarding; community sources confirm “OSU are not an option for preview builds” — **preview OSU path is separate and also not generic PC**. | Do not use for Q1–Q6 — Insider is game-playtest, not research OS image program | `fetch_page` Insider program article + Reddit 2019 note |

**Response time for all routes: UNKNOWN — do not promise a response SLA. Do not transfer game-concept review timelines (e.g., 10–15 days to 3 weeks for ID@Xbox concept approval) to support correspondence.**

### 5.3 Route C — Community / Non-Authoritative (Informational Only, Not Asking)

| Channel | Why listed | Action |
|---------|------------|--------|
| GitHub Discussions at `github.com/microsoft/GDK` | Public GDK repo has Discussions enabled — community can explain GDK vs GDKX README distinction but **cannot provide retail OS image or authorization answer** | Do not use for Q1–Q6; read-only |

### 5.4 Program Requirements Evidence (What Would Be Required If Owner Chose to Onboard — Not Requested Now)

| Requirement | Detail | Source |
|-------------|--------|--------|
| **Legal entity** | Must be legal business (studio/publisher), obtain DUNS recommended, provide shipping address, legal name/DBA | `devdocs.xbox.com/home/onboarding` checklist prerequisites |
| **Partner Dashboard + NDA** | Register as Xbox partner via Xbox Partner Dashboard at `developer.microsoft.com/en-us/games/partner` → NDA (usually ~20 min–3 days) | Same checklist Step 1 |
| **Partner Center** | Enroll to Partner Center, accept App Developer Agreement, receive Seller ID | Checklist Step 2 + `learn.microsoft.com/.../access-resources` public vs secure |
| **ID@Xbox application** | Submit game concept for approval, sign Title Licensing Agreement + **GDK License Agreement** | Checklist Step 3 |
| **Entra ID + MS Rep** | Association of Microsoft Entra ID tenant with Partner Center (free creation if none) + adding users + Microsoft representative enable of `aka.ms/gdkdl` Secure Downloads | `learn.microsoft.com/.../set-up-organization` + access-resources Secure note |
| **Secure Downloads** | Even then, publicly documented contents = **GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples** — **no line lists retail OS for PC**; full restricted inventory beyond public description UNKNOWN, not exhaustive | Access-resources § Secure resources (verified public description) |
| **Dev Kit hardware** | EDS account created ~1 week after GDK Agreement → order kits (separate cost, not PC hardware) | Checklist Step 4 |
| **MSA deprecation** | Personal Microsoft Accounts (MSAs) **no longer supported** for secure Xbox resources — **organizational Entra account required** | `fetch_page access-resources` Important alert box |

> The table establishes that even **full onboarding** does not demonstrably grant Q1’s retail-image-for-PC artifact — the charter’s “without requiring an Xbox console” criterion intentionally excludes Dev Kit hardware even if owner obtained it.

---

## 6. Decision Outcomes (What Each Response Means)

| Outcome code | Microsoft response | What it establishes | Technical implications (boot-chain terms) | Recommended owner decision |
|--------------|--------------------|---------------------|-------------------------------------------|----------------------------|
| **O1 COMPLETE RETAIL IMAGE AVAILABLE (conditional — does not alone change feasibility)** | “Yes — Microsoft does provide a complete Xbox Series X retail OS image via [specific program: e.g., `aka.ms/gdkdl` category *‘Xbox OS Recovery — PC Target’* / new managed research program], and this image is authorized for standard x86-64 PC hardware.” | Establishes Microsoft **states** an image exists — **does not automatically set feasibility to `CONDITIONALLY FEASIBLE`**. Feasibility moves only when **all four conditions are evidenced**: (1) **identifiable artifact and provenance** (exact image name/version/hash, signing identity, distribution URL/program name); (2) **legitimate acquisition route and applicable agreement** (Partner Center program, GDK Agreement/NDA scope, Entra/MS rep enablement); (3) **explicit authorization for deployment on standard PC hardware** (written confirmation for generic Tier 1 PC, not merely Dev Kit); (4) **supported hardware/configuration and deployment documentation** (SOC/board/GPU/memory support list, hypervisor PC build if any, Secure Boot `db` enrollment, deployment guide). **Until all four evidenced, retain `NOT CURRENTLY DEMONSTRATED` — do not turn a bare yes, ambiguous response, or GDKX access into feasibility.** | Retail signing root (Xbox CA) would need to be accompanied by a **PC-enrollable trust/provisioning flow** (HSP/Pluton Xbox identity for PC, or single signed `hvax64`/HostOS variant built for PC firmware) — otherwise image would fail hardware-RoT (see `BOOT_CHAIN.md` §2 #2 #3). Request MS to specify: signing variant, required PC Secure Boot enrollment (Xbox `db`), required SOC/board support list, hypervisor PC build, memory-layout config for DDR5+discrete GPU vs unified GDDR6, GPU driver for PC. Labeled as hypothesis where not directly established for Series X. | **Pause other work; document the exact authorized acquisition process + technical requirements; do not acquire image until owner authorizes new GDK Agreement/NDA scope and has recorded hash-provenance procedure (`PROVENANCE.md` + `SHA256SUMS.txt` expansion). Update `roadmap.json` W7-M1 only when four conditions fully evidenced — not on a bare yes.** |
| **O2 DEV-KIT RECOVERY ONLY** | “Secure Downloads at `aka.ms/gdkdl` contains **GDK/GDKX recoveries exclusively intended for licensed Xbox development kits** (Xbox-derived SoC dev firmware). There is no Microsoft-supported retail OS image for generic PC deployment.” | Establishes, **only to the extent Microsoft explicitly states in writing**, that recoveries as offered are Dev Kit-only. **Public docs alone describe contents as “GDK software and GDK recoveries” without a public line asserting exclusive Dev Kit-only scope for all recoveries — do not rely on public docs alone; Q3 remains the question.** Does **not** establish PC feasibility; closes conditional misreading that “GDKX maybe holds PC image.” | No transfer to generic PC: Dev Kit recoveries contain Xbox SoC firmware + hypervisor tuned for Xbox SoC GDDR6/GPU/MC/SCP. No path to Tier 1 generic AMD/Intel desktop. | Record in `FEASIBILITY_FINAL_REVIEW.md` addendum: **“Microsoft confirms GDKX recoveries as offered are Dev Kit-only; no generic PC image offered.”** — retain `NOT CURRENTLY DEMONSTRATED`; reassess only if owner later proposes custom board (scenario D) which still needs retail signing and is *not standard PC*. |
| **O3 NO PC DEPLOYMENT SUPPORT** | “Microsoft does not support or authorize deployment of retail Xbox OS components (signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox hardware. Deployment targets are limited to Xbox hardware families (retail + licensed dev kit).” | **Authoritative authorization boundary** — confirms **no Microsoft-supported path** exists for charter objective as presently defined. This response does **not** prove impossibility (see reviewer fix #2), but it does establish that *no authorized route exists*. | Hardens trust boundary: Xbox CA not in PC `db`, Xbox HSP/Pluton identity not provisionable to generic PC (PCWorld 2020 “Xbox security approach for PCs” was for Windows security, not Xbox OS portability), no PC-target hypervisor image to request. Any bypass would violate `SECURITY.md`/`ENGINEERING_RULES.md` (no key extraction/Secure Boot bypass). | **Accept as formal closure of authorized route** (not proof of no technical possibility). Record boundary; keep project alive as research per owner review §3: *preserve evidence, do not purchase hardware, do not start diagnostic probe until re-authorized as separate product*. |
| **O4 NO RESPONSE** | No reply within reasonable window (UNKNOWN SLA — do not assume 10–15 day timeline) or auto-generated “contact your account team” deflection | **No new evidence** — neither confirms nor denies authorized path. Retain existing verdict and documented lack of public PC image. | No change to technical blockers — all 10 dependency rows remain calibrated as before. | **Retain `NOT CURRENTLY DEMONSTRATED`**. Re-offer inquiry via alternate route (B2 Q&A post) after Owner approves; do not loop automatically. |
| **O5 AMBIGUOUS RESPONSE** | “The GDK/GDKX contains tools to build games that run on Xbox consoles and PC via Game Pass / cloud; publishing on Xbox requires ID@Xbox.” — or discussion of OSU1 / Inside previews / PlayFab — without answering Q1–Q2 | Fails to distinguish OSU1/public GDK/defined secure-downloads content/retail OS image (the table in §4 was attached to prevent this). Ask was misunderstood as game-publishing question. | No technical implication until clarified — ambiguity does not resolve trust block #1. | **Identify exactly what needs clarification**: resend attachment table §4 with sharper emphasis: *“We are NOT asking how to build a game that runs on Xbox OR PC. We are asking whether Microsoft distributes the Xbox Series X retail operating system itself as a PC-bootable image, distinct from those — observable objective as defined.”* — require Owner approval before follow-up. |

**Destination remains:** Genuine, unmodified retail OS on standard PC — no host OS/emulator/bypass. O1 would move toward `CONDITIONALLY FEASIBLE` only **after** four conditions (artifact/provenance, route+agreement, PC-authorization, configuration/docs) are evidenced — not automatically on a “yes.” **Do not turn ambiguous, bare yes, or GDKX access into feasibility.**

---

## 7. Prepared Inquiry Text (Submission-Ready, Owner-Reviewed Before Send)

> **Subject line (email route B1):** *Research inquiry — Authorized retail Xbox Series X OS image for standard x86-64 PC hardware (distinguishing OSU1 / Public GDK / secure Xbox downloads)*
>
> Dear Microsoft Xbox team,
>
> We are a research group conducting an authorized-artifact feasibility study of **Xbox platform portability** under charter `XboxPC — Genuine Xbox Series X Retail OS on Standard PC Hardware`. We have completed an independent public-evidence audit (2026-11-22, branch `arena/7ff9d1c6-xboxpc` @ `86cccdb`, base `8771211` on `main`; historical provenance `dc01bc1` → `1eac66c` preserved) that distinguishes **OSU1 update packages, Public GDK (game SDK), and secure Xbox downloads content (GDK software and GDK recoveries, documentation, Submission Validator, restricted samples per `learn.microsoft.com/.../access-resources`)** — all verified from `support.xbox.com`, `github.com/microsoft/GDK`, `learn.microsoft.com/.../access-resources`, `devdocs.xbox.com/home/onboarding`, and Hot Chips 2020 Xbox Series X silicon presentation. **No public or documented secure artifact in our sweep constituted a complete retail OS image for generic PC.**
>
> We write only to establish the **authorized acquisition boundary** — not to request a bypass, developer hardware purchase, or agreement acceptance before your answer.
>
> **Our objective (observable behavior first, hypothesis second):** *Genuine, unmodified, Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services — observable on retail console — to boot directly on standard x86-64 PC hardware (generic modern AMD/Intel desktop, UEFI, NVMe, discrete GPU) without a Windows/Linux host, emulator, or dashboard clone, while preserving retail signatures.* Our internal research model hypothesizes this *may* involve Host partition / hypervisor / System partition components (e.g., `host.xvd` / `hvax64` / `system.xvd` per Xbox One-observed `BOOT_CHAIN.md` map) — **labeled as internal hypothesis, not asserted as Microsoft-defined package names or a confirmed Series X packaging specification**; we ask only whether Microsoft offers any complete, authorized PC-targeted image/configuration satisfying the observable objective, regardless of internal naming.
>
> **Definitions attached:** A one-page table distinguishing OSU1 (`OSU1.zip` → `$SystemUpdate/*.xvd` update payload applied via Xbox Startup Troubleshooter to System Update A/B partitions), Public GDK (`github.com/microsoft/GDK` game SDK missing console driver/Shader Compiler/GDKX APIs), and secure Xbox downloads per `learn.microsoft.com/.../access-resources` (**secure Xbox downloads including GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples** — public docs establish listed contents, full restricted inventory beyond that public description is UNKNOWN and not claimed exhaustive; whether recoveries are exclusively Dev Kit-only remains Q3) — included to prevent conflation.
>
> **Formal questions (verbatim — requested as written record for feasibility file):**
>
> 1. Does Microsoft provide, through any authorized program, a **complete Xbox Series X retail OS image** (as defined above — observable objective, regardless of internal naming) as a distributable artifact?
> 2. Is there a **Microsoft-supported, Microsoft-documented PC-target image/configuration** of that retail OS for standard x86-64 PC hardware booting directly without a Windows/Linux host?
> 3. Are **GDKX recovery packages at `aka.ms/gdkdl` exclusively intended for licensed Xbox development kits** (Xbox-derived SoC hardware with dev firmware)?
> 4. Is there an **authorized research/documentation program** that grants access to the retail boot chain and required platform docs (HSP/Pluton Xbox identity, SMU/SCP handshake, ACPI/SMBIOS surface) for feasibility evaluation?
> 5. Does Microsoft **support or authorize** deployment of retail Xbox OS components (retail-signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox hardware — or can Microsoft confirm **no such deployment is supported**?
> 6. Can Microsoft **clarify whether any authorized PC-targeted retail OS offering exists** for standard x86-64 PC hardware, and if no such offering exists, **confirm that distinction in writing** (OSU1 is an update package, public GDK is a game SDK, secure Xbox downloads content as publicly documented does not include a PC-bootable retail OS image, and none of the three as currently offered constitutes a PC-bootable retail OS image)?
>
> **What we need from you:** A short written reply (email, Partner Center message, or link to authoritative doc page) attributable to Microsoft stating, for each question, **yes/no with program name/URL, or “no such offering is provided.”** Community citations or Q&A threads are insufficient for our evidence standard — we will cite your response by URL+date in our `FEASIBILITY_FINAL_REVIEW.md` and `MICROSOFT_ACCESS.md`.
>
> **What we will not do without explicit next-step authorization from you and our owner:** register organizations, accept NDAs/GDK Agreements, submit concept applications, acquire dev kit hardware, enable Secure Downloads, download restricted materials, modify OSU1, or attempt to boot retail components — all blocked until you confirm a path exists. **This inquiry itself requires no action beyond a written answer. If this inbox cannot answer retail OS licensing/platform-engineering scope (Q1–Q2), please route the question to the appropriate Xbox platform/OS or licensing team.**
>
> Please advise whether this inquiry should be redirected to a specific team (e.g., ID@Xbox vs. Xbox Developer Program), or whether a Microsoft representative call is preferred. We can provide charter documents and audit evidence on request.
>
> Respectfully,
> Lamar — Project Owner, XboxPC (charter `CHARTER-2026-11-22-001`)
> [Organizational contact as enrolled in Microsoft directory, if any; otherwise general inquiry contact]
>
> Attachments: §4 Definitions table (1 page) + §1 context paragraph (this email)

**Variant for Microsoft Q&A post (route B2):** Same body truncated to 2000-char limit, attach table as image or gist link; tag `gaming-gdk` + `xbox-developer-program`.

**Note:** Six questions remain aligned with decision packet — **no silent scope broadening**. Q3 remains open question; public secure-downloads listing is not claimed exhaustive. **Feasibility guidance:** a positive O1 answer alone does not change status; all four O1 conditions must be evidenced.

---

## 8. Technical Implications Summary (For Owner Decision)

| Outcome | What we learn | What we still don’t know even with MS answer | Owner action |
|---------|---------------|---------------------------------------------|--------------|
| O1 Complete image available | Microsoft states image exists — **does not alone close legitimate route**; four conditions still required (artifact/provenance, route+agreement, explicit PC authorization, hardware/config docs) | Exact trust provisioning still needed (Xbox CA enrollment, HSP/Pluton PC identity, GDDR6 MC config for DDR5+discrete GPU, GPU driver for PC, hypervisor PC build — per `RETAIL_OS_REQUIREMENTS.md`) — MS would need to publish those requirements alongside image | Request MS-published technical requirements document; **do not change feasibility until four conditions evidenced**; do not download until Owner approves agreement scope + provenance procedure |
| O2 Dev-kit recovery only | Public docs scope clarified only to extent MS explicitly states; public listing alone does not assert exclusive Dev Kit-only for all recoveries | Same blockers remain for generic PC | Record, retain `NOT CURRENTLY DEMONSTRATED` |
| O3 No PC deployment support | Authoritative negative on **authorized** route — establishes boundary, **does not prove impossibility** | Whether an unauthorized but technically conceivable implementation exists (custom board D + retail signing would still be needed — a console SKU decision, not software workaround) | Record boundary; project stays alive as research (owner review §3); no hardware purchase |
| O4 No response | No new evidence | Unchanged | Retain `NOT CURRENTLY DEMONSTRATED`; offer alternate route after owner approval |
| O5 Ambiguous | Misrouted as publishing question | Same as O4 + need clarification | Send §3 follow-up with emphasized distinction |

**Until all four O1 conditions evidenced, retain `NOT CURRENTLY DEMONSTRATED` — do not turn ambiguous/yes/access into feasibility.**

---

## 9. Evidence of Applicable Requirements (Fetched, Not Assumed)

- `fetch_page https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/development-downloads/access-resources?view=gdk-2604` (chunks 0–1) — public vs secure split, personal MSAs no longer supported, Secure = *“Latest release of software and recoveries of the GDK”* per page section, but **public description is secure Xbox downloads including GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples — not exhaustive, full inventory UNKNOWN**, MS rep enable.
- `fetch_page https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/set-up-organization?view=gdk-2604` — Partner Center + free Entra ID creation steps, Seller ID, user management.
- `fetch_page https://devdocs.xbox.com/home/onboarding` — full ID@Xbox onboarding checklist (Register partner → NDA → Partner Center Seller ID → ID@Xbox concept approval → TLA + GDK License → SupplierWeb + Entra → EDS dev kits) — concept-approval time is for game publishing, **not a support SLA, SLA remains UNKNOWN**.
- `https://developer.microsoft.com/en-us/windows/support` — **ID@XBOX Program — Email ID@XBOX.com** (official GDK hardware question answers: contact representative; shipping via ID Setup) — **documented initial contact for ID@Xbox/console/onboarding/DevKit questions, not confirmed retail OS licensing authority — request escalation if out of scope**.
- `https://learn.microsoft.com/en-us/answers/questions/5884771/...` — staff answer: organizational Entra ID required for Secure Downloads; personal MSA fails.
- `https://hc32.hotchips.org/.../HotChips2020_GPU_Microsoft_Jeff_Andrews_v2.pdf` slides — HSP/Pluton SHACK + MSP blocks (verified HW, not boot ladder).
- GitHub API `microsoft/GDK` — id 348416224 private false (verified).
- `developer.microsoft.com/en-us/games/partner` — Xbox Publishing guide; `aka.ms/gdkforum` — GDK developer forum.

All URLs re-verifiable; no invented inbox or representative name included. **Response SLA UNKNOWN for all routes — no promise.**

---

## 10. Recommended Owner Decision (Per Request §5)

> **Approve this inquiry document as written; authorize Owner (Lamar) — not agent — to send it via Route A (preferred internal-routing path if organizational Microsoft account relationship exists) or Route B1 email `ID@XBOX.com` (documented initial contact, request escalation to platform/OS or licensing team if out of scope) after confirming organizational contact identity. Do NOT authorize: Partner Center enrollment, NDA/GDK Agreement acceptance, GDKX download, dev kit purchase, Q&A posting, or registration.
>
> Upon receipt of Microsoft written answer (any of O1–O5), update `FEASIBILITY_FINAL_REVIEW.md` addendum with response citation and re-derive feasibility **only when all four O1 conditions (identifiable artifact/provenance, legitimate route+agreement, explicit PC authorization, supported hardware/configuration docs) are evidenced**; otherwise retain `NOT CURRENTLY DEMONSTRATED`. Until then, preserve research assets, and defer diagnostic probe (Phase 6) as specification-only separate product until that boundary is settled.

---

*Prepared for Owner review — **INQUIRY UNSENT, NO MICROSOFT CONTACT** — do not submit, register, accept agreements, or download restricted materials until Owner authorizes. All external actions remain blocked per `AGENTS.md` + `ENGINEERING_RULES.md` + prompt §3. **W7-M1 remains BLOCKED (inquiry UNSENT, not complete) — a positive O1 alone does not change feasibility; probe is specification-only (no implementation). Research progress (12/24 50.0%) and genuine execution readiness (0/4 0.0% NOT CURRENTLY DEMONSTRATED) remain separate.***  
*Git: this file at `86cccdb` (base `8771211`); prior `dc01bc1` → `1eac66c` historical provenance preserved — do not label historical SHAs as current head.*
