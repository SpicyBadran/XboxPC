# MICROSOFT_RETAIL_OS_INQUIRY.md — Prepared Inquiry to Establish Authorized Retail OS Acquisition Route

**Traceability:** `INQUIRY-2026-11-22-001`  
**Branch:** `arena/00f8e176-xboxpc` @ `dc01bc1` (+ Phase 5 audit)  
**Prepared:** 2026-11-22 UTC — **DRAFT for Owner review only — DO NOT SUBMIT**  
**Author Roles:** Documentation & Evidence Agent (inquiry draft), Security Research Reviewer (legal boundary check), Verification Agent (contact-route verification)  
**Method:** Distinguishes OSU1 / Public GDK / GDKX recoveries / Complete retail OS image; contact routes are only those fetched from authoritative Microsoft domains (no invented representatives)  
**Status:** Ready for owner approval — external action blocked until owner authorizes

---

## 1. Objective (Unchanged)

Establish by **authorized, documented Microsoft response** whether a route exists to **legitimately obtain the genuine Xbox Series X retail operating system** (the HostOS + SystemOS + hypervisor + retail boot chain that runs natively on Xbox Series X — the same stack referenced in charter §2 Success Definition and Phase 5 `BOOT_CHAIN.md`) for execution on **standard x86-64 PC hardware**:

- Genuine, unmodified Microsoft OS components
- Direct boot on non-Xbox PC hardware (generic modern AMD/Intel PC — charter Tier 1 reference)
- No Windows/Linux host underneath
- No emulator or dashboard clone substituting for the retail OS
- No hardware trust bypass (preserve retail signatures)

**This inquiry does NOT request:** game SDK samples, GDK tooling, OSU1 re-explanation, Insider preview access, hardware discounts, or bypass of security controls.

---

## 2. Background Provided to Microsoft (For Context — Included in Cover Note)

To prevent misreading this as a game-publishing request, every submission will include this framing:

> **Context:** Our research organization maintains a PC compatibility investigation (“XboxPC”) under charter `CHARTER-2026-11-22-001`. We have independently audited public artifacts:
> - **OSU1 (support.xbox.com/.../offline-system-update)** is a **public update payload** (`$SystemUpdate/*.xvd` + `RM_Signature.bin` applied via Xbox Startup Troubleshooter to existing `System Update` A/B slots per community-reported layout from GBAtemp/futuretweets referencing official article; Support article existence verified at URL, body returned JS loading placeholder per Phase 6.1 — Microsoft names it Offline System Update, not factory image) — STRONGLY SUPPORTED as not a full OS nor independently bootable.
> - **Public GDK (github.com/microsoft/GDK, id 348416224)** is a **game SDK** for building Win32+GDK games that target Xbox/PC/cloud — explicitly missing Xbox console graphics driver/Shader Compiler/console environment APIs (README § “missing … only in GDKX”).
> - **Secure Xbox Downloads (aka.ms/gdkdl, learn.microsoft.com/.../access-resources)** is documented as **“Latest release of software and recoveries of the GDK, offline docs, Submission Validator”** — not a retail OS image for generic PC; personal MSAs no longer supported; Secure Downloads requires Partner Center Xbox-provisioned account + valid GDK Agreement + Entra ID tenant + MS representative enablement (`MICROSOFT_ACCESS.md`).
> - No public or authorized-secure page in our searched public sources (bounded search: support.xbox.com article shell not captured, GitHub GDK, learn.microsoft.com GDK access-resources, community storage threads) was found to advertise a retail OS image for generic PC deployment (NOT FOUND IN SEARCHED PUBLIC SOURCES; internal existence UNKNOWN).
>
> We seek only a **yes/no/qualified** answer on whether such an authorized image exists, per the six questions below, to record the official authorization boundary.

---

## 3. The Six Formal Questions (To Be Asked Verbatim)

> **Q1 — Complete retail OS image:** Does Microsoft provide, through any authorized program (public download, Partner Center Secure Downloads, managed developer program, research license, or other documented offering), a **complete Xbox Series X retail operating system image** (the HostOS + SystemOS + hypervisor + associated boot chain that executes natively on retail console hardware — the deliverable described in charter success criteria and `BOOT_CHAIN.md` §2)?
>
> **Q2 — PC-target configuration:** Is there a **Microsoft-supported, Microsoft-documented PC-target image or deployment configuration** of that retail OS for standard x86-64 PC hardware (generic modern AMD or Intel desktop with UEFI, NVMe, discrete/integrated GPU — Tier 1 family) that boots directly without a Windows/Linux host?
>
> **Q3 — GDKX recovery scope:** Are **GDKX recovery packages** available via Secure Xbox Downloads **exclusively intended for licensed Xbox development kits** (Xbox-derived SoC hardware with dev firmware), rather than as deployment artifacts for generic PC hardware?
>
> **Q4 — Authorized research access:** Is there an **authorized research or documentation program** (beyond ID@Xbox publishing) that provides access to the retail boot chain and required platform documentation (fused root-of-trust description, HSP/Pluton Xbox-instance behavior, SMU/SCP handshake outline, ACPU/SM BIOS surface expected by retail OS) sufficient to evaluate PC feasibility without bypass?
>
> **Q5 — Deployment authorization:** Does Microsoft **support or authorize** deployment or redistribution of retail Xbox OS components (signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox PC hardware — or, conversely, can Microsoft confirm that **no such deployment is supported**?
>
> **Q6 — Recorded distinction:** If no such route exists for standard PC targets, can Microsoft **confirm that distinction in writing** for the project’s feasibility record — i.e., that OSU1 is an update package, public GDK is a game SDK, GDKX recoveries are for Dev Kit, and **none of the three constitutes a PC-bootable retail OS image**?

**Deliverable expectation:** A written answer (email, Partner Center message, or linked doc page) attributable to Microsoft — not community speculation — that can be cited in `FEASIBILITY_FINAL_REVIEW.md` update with URL + date.

---

## 4. Definitions (Included as Attachment to Prevent Conflation)

| Term (our usage) | What it is | What it is not | Source that establishes distinction |
|------------------|------------|----------------|------------------------------------|
| **OSU1** | Public offline **update package** from `support.xbox.com/.../offline-system-update`: `OSU1.zip` → `$SystemUpdate/*.xvd` (host/system/systemaux/systemmisc/systemtools/updater/SettingsTemplate) + `bootanim.dat`/`empty.bin`/`RM_Signature.bin`, applied from within Xbox Startup Troubleshooter to pre-existing `System Update` A/B partitions. ~4.8–6 GB, version-gated (greyed out if past version). | Not a complete OS, not a disk image, not independently bootable, not firmware, not boot ROM, not PC-compatible. Xbox One repair `gbatemp.net/threads 496212` shows A/B copying model; TechDows documents version gate. | `fetch_page` Support page shell + `DOWNLOAD_SOURCES.md` §1 + `OSU1_ANALYSIS.md` + 5 community corroborations |
| **Public GDK** | Microsoft Game Development Kit (public, `github.com/microsoft/GDK`): common tools/libs/docs to build **games** for Xbox Game Pass for PC (Win10/11), Xbox consoles (game target), cloud. Distribution via WinGet `Microsoft.Gaming.GDK`, NuGet `Microsoft.GDK.Windows`, vcpkg `ms-gdk`. Missing Xbox console driver/Shader Compiler/console env APIs. | Not the retail OS, not hypervisor, not HostOS/SystemOS, not boot chain. README explicitly: “Xbox console gfx driver + Shader Compiler … currently only in GDKX” | GitHub API id `348416224` private false stars 1741 commit `d773744` README 17186 B + `learn.microsoft.com/.../access-resources` public vs secure split |
| **GDKX / Secure Downloads** | Controlled GDK + Xbox Extensions installer + **recoveries of the GDK** + offline docs + Submission Validator + NDA samples. Requires Partner Center Xbox-provisioned account + valid GDK Agreement + Entra tenant + **MS representative** enable of `aka.ms/gdkdl`. Personal MSAs excluded. | Not a retail OS image for generic PC. Even behind auth, listed contents are “recoveries of the **GDK**” (not “retail Xbox OS image for PC”). No line advertises PC deployment. | `fetch_page` access-resources ch 0–1 + `MICROSOFT_ACCESS.md` §3–5 + onboarding docs `devdocs.xbox.com/home/onboarding` checklist |
| **Complete retail OS image (object of inquiry)** | **Observable objective:** Genuine, unmodified, Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services without a Windows/Linux host, emulator, or dashboard clone — i.e., what “boots the Xbox” rather than what “builds games for Xbox.” **Internal architectural model (hypothesis, not Microsoft definition):** Our research hypothesizes this *may* involve a Host partition / hypervisor / System partition (e.g., `host.xvd` / `hvax64` / `system.xvd` per Xbox One-observed `BOOT_CHAIN.md` §1), but this is not asserted to be Microsoft’s package naming, a confirmed Series X specification, or an offered deliverable. **Question to Microsoft:** Whether Microsoft offers *any* complete, authorized, PC-targeted retail OS image/configuration satisfying the observable objective, regardless of internal package naming/architecture. | Not OSU1 (update of some XVDs), not GDK, not GDKX game toolchain. Would need to be a Microsoft-signed, PC-targeted image to satisfy charter. None documented as offered. | Charter §2 success table + Hot Chips 2020 pdf (360.4 mm² 15.3B transistors, 16 GB GDDR6 10+6, GPU 52 CU 12 TF, HSP SHACK MSP 4crypto/4hash/2decomp) + Xbox One Research wiki bootloaders |

*Attaching this table avoids the common misinterpretation “OSU1 contains system.xvd hence is the OS” and “GDKX recoveries are OS images for PC” — both rejected by evidence audit (`EVIDENCE_AUDIT.md` S1–S10).*

---

## 5. Official Microsoft Contact Routes — Research Results (Do Not Invent)

> Per instruction: prioritize (A) existing partner contact if available to owner, then (B) documented GDK support / developer-partner channels. No invented email/address.

### 5.1 Route A — Existing Xbox Developer-Partner Contact (Highest Priority, If Available)

| Channel | What it is | When to use | Source |
|---------|------------|-------------|--------|
| Existing **Microsoft account team / Xbox developer program representative** for your organization (if already onboarded to ID@Xbox/Partner Center) — the same `Microsoft representative` referenced in access-resources for Secure Downloads: *“You must contact your Microsoft representative to enable access to the secure download site.”* | Account-team-managed inquiry — Microsoft explicitly routes Secure Downloads enablement through this person, so they are the only party able to confirm what Secure Downloads **does not** contain. | Owner already has Partner Center Xbox-provisioned account (check `PARTNER_ORG` before using) | `fetch_page learn.microsoft.com/.../access-resources?view=gdk-2604` ch 0 § “Accessing secure resources” — important box verbatim |

> If owner has such a contact, **this is the only route that can authoritatively answer Q3/Q5/Q6** (whether Secure Downloads contains retail image for PC — the docs say “recoveries of GDK,” but a human can confirm negative in writing).

### 5.2 Route B — Documented GDK Developer Support Channels (No Prior Partnership Required for Initial Contact)

| # | Official Channel | URL / Identifier | Purpose per Microsoft | What to ask | Evidence |
|---|-----------------|------------------|-----------------------|-------------|----------|
| B1 | **Microsoft Developer Support — ID@Xbox Program** | `https://developer.microsoft.com/en-us/windows/support` → section **“ID@XBOX Program” — “Email ID@XBOX.com”**; landing page `https://developer.microsoft.com/en-us/games/partner` → “Ready to publish on XBOX? → Join ID@XBOX” | “For questions about the ID@XBOX program including game publishing, console questions, onboarding to the program and **XBOX DevKits**, contact the team directly. Email ID@XBOX.com” | Submit Q1–Q6 as **policy clarification, not onboarding**: “We are evaluating feasibility of an authorized research path to retail OS image for standard x86-64 PC (not a game publishing plan). Does such a path exist? See attached definitions.” — avoids misrouting as game pitch | `fetch_page developer.microsoft.com/en-us/windows/support` (Nov 21 2022) + `web_search GDK support ID@Xbox` result id=1 |
| B2 | **Microsoft Q&A — How can I obtain GDK hardware / Unable to access GDK download** | `https://learn.microsoft.com/en-us/answers/questions/1663748/how-can-i-obtain-the-gdk-hardware` and `https://learn.microsoft.com/en-us/answers/questions/5884771/unable-to-access-to-download-gdk-for-xbox-development` (both `learn.microsoft.com` official Q&A) | Official Microsoft-staff answers on GDK/GDKX access: requirements are organizational Entra ID tenant associated with **onboarded** Xbox Development partner in Partner Center; Secure Downloads needs **GDK Agreement + MS rep enable** | Post Q1–Q6 as **follow-up question** on one of these threads (or new question tagged `gaming-gdk`) if B1 email confirmation not yet sought — Microsoft external staff explicitly answer there and cite `GDK Agreement` terms | Both threads fetched via `web_search` “how can I obtain GDK hardware” — Microsoft external staff answers cite GDK Agreement |
| B3 | **Xbox GDK Developer Forum** | `https://aka.ms/gdkforum` (aka.ms shortlink → forum; listed on `devdocs.xbox.com/home/onboarding-access/access-resources` “GDK developer forum: Post questions and report issues to the XBOX team” + `learn.microsoft.com` GDK docs “Get help” area) | Developer Q&A with Xbox engineering team; accessible after at least limited onboarding (see below). Microsoft engineering monitors. | Ask Q3/Q5 directly after Step B4 limited exploration: “Are GDKX recoveries at `aka.ms/gdkdl` exclusively for Xbox dev kits?” — Microsoft staff routinely clarify scope there | `web_search` “Access GDK dev resources devdocs.xbox.com access-resources” result id=2 + onboarding checklist |
| B4 | **Xbox Partner Onboarding Checklist (read-only, no registration)** | `https://devdocs.xbox.com/home/onboarding` (Xbox Game Development Documentation) — full checklist: *Register as Xbox partner → Enroll to Partner Center (accept App Developer Agreement, receive Seller ID) → Apply to ID@XBOX (business info + game concept, await 10–15 business days to 3 weeks, sign Title Licensing Agreement + GDK License Agreement) → Complete onboarding via SupplierWeb + Entra ID free creation → EDS account for dev kits* | Read-only route identification — lets owner **evaluate eligibility** without creating accounts | Review prerequisites: legal entity, DUNS recommended, shipping address, NDA, ≥18, country where MS does business, Microsoft Entra capability, willingness to sign GDK Agreement — **no registration, agreement acceptance, or hardware purchase occurs now** | `fetch_page devdocs.xbox.com/home/onboarding` + `web_search ID@Xbox programSelection` |
| B5 | **Xbox Insider Program (not for this inquiry, noted to avoid misdirection)** | `https://www.xbox.com/en-us/developers/insiders` | Playtest audience expansion, not developer onboarding; community sources confirm “OSU are not an option for preview builds” — **preview OSU path is separate and also not generic PC**. | Do not use for Q1–Q6 — Insider is game-playtest, not research OS image program | `fetch_page` Insider program article + Reddit 2019 note |

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
| **ID@Xbox application** | Submit game concept for approval (10–15 business days up to 3 weeks typical), sign Title Licensing Agreement + **GDK License Agreement** | Checklist Step 3 |
| **Entra ID + MS Rep** | Association of Microsoft Entra ID tenant with Partner Center (free creation if none) + adding users + Microsoft representative enable of `aka.ms/gdkdl` Secure Downloads | `learn.microsoft.com/.../set-up-organization` + access-resources Secure note |
| **Secure Downloads** | Even then, contents = GDK software + **recoveries of GDK** + offline docs + Submission Validator + NDA samples (games-focused) — **no line lists retail OS for PC** | Access-resources § Secure resources (verified direct quote) |
| **Dev Kit hardware** | EDS account created ~1 week after GDK Agreement → order kits (separate cost, not PC hardware) | Checklist Step 4 |
| **MSA deprecation** | Personal Microsoft Accounts (MSAs) **no longer supported** for secure Xbox resources — **organizational Entra account required** | `fetch_page access-resources` Important alert box |

> The table establishes that even **full onboarding** does not demonstrably grant Q1’s retail-image-for-PC artifact — the charter’s “without requiring an Xbox console” criterion intentionally excludes Dev Kit hardware even if owner obtained it.

---

## 6. Decision Outcomes (What Each Response Means)

| Outcome code | Microsoft response | What it establishes | Technical implications (boot-chain terms) | Recommended owner decision |
|--------------|--------------------|---------------------|-------------------------------------------|----------------------------|
| **O1 COMPLETE RETAIL IMAGE AVAILABLE** | “Yes — Microsoft does provide a complete Xbox Series X retail OS image via [specific program: e.g., `aka.ms/gdkdl` category *‘Xbox OS Recovery — PC Target’* / new managed research program], and this image is authorized for standard x86-64 PC hardware.” | **Authorized acquisition path exists** — the missing feasibility piece (RISK-001) is closed; charter success criterion *Genuine OS provenance* becomes achievable. | Retail signing root (Xbox CA) would need to be accompanied by a **PC-enrollable trust/provisioning flow** (HSP/Pluton Xbox identity for PC, or single signed `hvax64`/HostOS variant built for PC firmware) — otherwise image would fail hardware-ROTL (see `BOOT_CHAIN.md` §2 #2 #3). Request MS to specify: signing variant, required PC Secure Boot enrollment (Xbox `db`), required SOC/board support list, hypervisor PC build, memory-layout config for DDR5+discrete GPU vs unified GDDR6, GPU driver for PC. | **Pause other work; document the exact authorized acquisition process + technical requirements; do not acquire image until owner authorizes new GDK Agreement/NDA scope and has recorded hash-provenance procedure (`PROVENANCE.md` + `SHA256SUMS.txt` expansion).** |
| **O2 DEV-KIT RECOVERY ONLY** | “Secure Downloads at `aka.ms/gdkdl` contains **GDK/GDKX recoveries exclusively intended for licensed Xbox development kits** (Xbox-derived SoC dev firmware). There is no Microsoft-supported retail OS image for generic PC deployment.” | Confirms **documented recoveries are Dev Kit-only** — aligns with public docs *“recoveries of the GDK”* and charter Part I §3 *Dev Kit ≠ PC* distinction. Does **not** establish PC feasibility; closes *conditional* misreading that “GDKX maybe holds PC image.” | No transfer to generic PC: Dev Kit recoveries contain Xbox SoC firmware + hypervisor tuned for Xbox SoC GDDR6/GPU/MC/SCP. No path to Tier 1 generic AMD/Intel desktop. | Record in `FEASIBILITY_FINAL_REVIEW.md` addendum: **“Microsoft confirms GDKX recoveries are Dev Kit-only; no generic PC image offered.”** — retain `NOT CURRENTLY DEMONSTRATED`; reassess only if owner later proposes custom board (scenario D) which still needs retail signing and is *not standard PC*. |
| **O3 NO PC DEPLOYMENT SUPPORT** | “Microsoft does not support or authorize deployment of retail Xbox OS components (signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox hardware. Deployment targets are limited to Xbox hardware families (retail + licensed dev kit).” | **Authoritative authorization boundary** — confirms **no Microsoft-supported path** exists for charter objective as presently defined. This response does **not** prove impossibility (see reviewer fix #2), but it does establish that *no authorized route exists*. | Hardens trust boundary: Xbox CA not in PC `db`, Xbox HSP/Pluton identity not provisionable to generic PC (PCWorld 2020 “Xbox security approach for PCs” was for Windows security, not Xbox OS portability), no PC-target hypervisor image to request. Any bypass would violate `SECURITY.md`/`ENGINEERING_RULES.md` (no key extraction/Secure Boot bypass). | **Accept as formal closure of authorized route** (not proof of no technical possibility). Record boundary; keep project alive as research per owner review §3: *preserve evidence, do not purchase hardware, do not start diagnostic probe until re-authorized as separate product*. |
| **O4 NO RESPONSE** | No reply within reasonable window (e.g., 20 business days, acknowledging ID@Xbox game-concept approval backlog of 10–15 days) or auto-generated “contact your account team” deflection | **No new evidence** — neither confirms nor denies authorized path. Retain existing verdict and documented lack of public PC image. | No change to technical blockers — all 10 dependency rows remain calibrated as before. | **Retain `NOT CURRENTLY DEMONSTRATED`**. Re-offer inquiry via alternate route (B2 Q&A post) after Owner approves; do not loop automatically. |
| **O5 AMBIGUOUS RESPONSE** | “The GDK/GDKX contains tools to build games that run on Xbox consoles and PC via Game Pass / cloud; publishing on Xbox requires ID@Xbox.” — or discussion of OSU1 / Inside previews / PlayFab — without answering Q1–Q2 | Fails to distinguish OSU1/public GDK/GDKX recovery/retail OS image (the table in §4 was attached to prevent this). Ask was misunderstood as game-publishing question. | No technical implication until clarified — ambiguity does not resolve trust block #1. | **Identify exactly what needs clarification**: resend attachment table §4 with sharper emphasis: *“We are NOT asking how to build a game that runs on Xbox OR PC. We are asking whether Microsoft distributes the Xbox Series X retail operating system itself as a PC-bootable image, distinct from those.”* — require Owner approval before follow-up. |

---

## 7. Prepared Inquiry Text (Submission-Ready, Owner-Reviewed Before Send)

> **Subject line (email route B1):** *Research inquiry — Authorized retail Xbox Series X OS image for standard x86-64 PC hardware (distinguishing OSU1 / Public GDK / GDKX recovery)*

> Dear Microsoft ID@Xbox / GDK team,
>
> We are a research group conducting an authorized-artifact feasibility study of **Xbox platform portability** under charter `XboxPC — Genuine Xbox Series X Retail OS on Standard PC Hardware`. We have completed an independent public-evidence audit (2026-11-22, branch `arena/00f8e176-xboxpc` @ `dc01bc1`) that distinguishes **OSU1 update packages, Public GDK (game SDK), and GDKX recoveries (Dev Kit-targeted)** — all verified from `support.xbox.com`, `github.com/microsoft/GDK`, `learn.microsoft.com/.../access-resources`, `devdocs.xbox.com/home/onboarding`, and Hot Chips 2020 Xbox Series X silicon presentation. **No public or documented secure artifact in our sweep constituted a complete retail OS image for generic PC.**
>
> We write only to establish the **authorized acquisition boundary** — not to request a bypass, developer hardware purchase, or agreement acceptance before your answer.
>
> **Our objective (for context):** *Genuine, unmodified, Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services — observable on retail console — to boot directly on standard x86-64 PC hardware (generic modern AMD/Intel desktop, UEFI, NVMe, discrete GPU) without a Windows/Linux host, emulator, or dashboard clone, while preserving retail signatures. Our internal research model hypothesizes this may involve Host partition / hypervisor / System partition components (e.g., `host.xvd` / `hvax64` / `system.xvd` per Xbox One-observed `BOOT_CHAIN.md` map), but we do not assert these are Microsoft-defined package names or a confirmed Series X packaging specification; we ask only whether Microsoft offers any complete, authorized PC-targeted image/configuration satisfying the observable objective, regardless of internal naming.*
>
> **Definitions attached:** A one-page table distinguishing OSU1 (`OSU1.zip` → `$SystemUpdate/*.xvd` update payload applied via Xbox Startup Troubleshooter to System Update A/B partitions), Public GDK (`github.com/microsoft/GDK` game SDK missing console driver/Shader Compiler/GDKX APIs), and GDKX/Secure Downloads (*“recoveries of the GDK” + offline docs + Submission Validator* per `learn.microsoft.com/.../access-resources`, requiring Partner Center Xbox-provisioned account + GDK Agreement + Entra ID + MS rep enable) — included to prevent conflation.
>
> **Formal questions (verbatim — requested as written record for feasibility file):**
>
> 1. Does Microsoft provide, through any authorized program, a **complete Xbox Series X retail OS image** (as defined above) as a distributable artifact?
> 2. Is there a **Microsoft-supported, Microsoft-documented PC-target image/configuration** of that retail OS for standard x86-64 PC hardware booting directly without a Windows/Linux host?
> 3. Are **GDKX recovery packages at `aka.ms/gdkdl` exclusively intended for licensed Xbox development kits** (Xbox-derived SoC hardware with dev firmware)?
> 4. Is there an **authorized research/documentation program** that grants access to the retail boot chain and required platform docs (HSP/Pluton Xbox identity, SMU/SCP handshake, ACPI/SMBIOS surface) for feasibility evaluation?
> 5. Does Microsoft **support or authorize** deployment of retail Xbox OS components (retail-signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox hardware — or can Microsoft confirm **no such deployment is supported**?
> 6. If no PC-target route exists, can Microsoft **confirm that distinction in writing** (OSU1=update, public GDK=game SDK, GDKX recoveries=Dev Kit-only, none=PC-bootable retail OS)?
>
> **What we need from you:** A short written reply (email, Partner Center message, or link to authoritative doc page) attributable to Microsoft stating, for each question, **yes/no with program name/URL, or “no such offering is provided.”** Community citations or Q&A threads are insufficient for our evidence standard — we will cite your response by URL+date in our `FEASIBILITY_FINAL_REVIEW.md` and `MICROSOFT_ACCESS.md`.
>
> **What we will not do without explicit next-step authorization from you and our owner:** register organizations, accept NDAs/GDK Agreements, submit concept applications, acquire dev kit hardware, enable Secure Downloads, download restricted materials, modify OSU1, or attempt to boot retail components — all blocked until you confirm a path exists. **This inquiry itself requires no action beyond a written answer.**
>
> Please advise whether this inquiry should be redirected to a specific team (e.g., ID@Xbox vs. Xbox Developer Program), or whether a Microsoft representative call is preferred. We can provide charter documents and audit evidence on request.
>
> Respectfully,
> Lamar — Project Owner, XboxPC (charter `CHARTER-2026-11-22-001`)
> [Organizational contact as enrolled in Microsoft directory, if any; otherwise general inquiry contact]
>
> Attachments: §4 Definitions table (1 page) + §1 context paragraph (this email)

**Variant for Microsoft Q&A post (route B2):** Same body truncated to 2000-char limit, attach table as image or gist link; tag `gaming-gdk` + `xbox-developer-program`.

---

## 8. Technical Implications Summary (For Owner Decision)

| Outcome | What we learn | What we still don’t know even with MS answer | Owner action |
|---------|---------------|---------------------------------------------|--------------|
| O1 Complete image available | Charter’s “legitimate route” piece closed; authorization boundary lifted | Exact trust provisioning still needed (Xbox CA enrollment, HSP/Pluton PC identity, GDDR6 MC config for DDR5+discrete GPU, GPU driver for PC, hypervisor PC build — per `RETAIL_OS_REQUIREMENTS.md`) — MS would need to publish those requirements alongside image | Request MS-published technical requirements document; do **not** download until Owner approves agreement scope + provenance procedure |
| O2 Dev-kit recovery only | Public docs confirmed by MS | Same blockers remain for generic PC | Record, retain verdict |
| O3 No PC deployment support (most likely per current docs) | Authoritative negative on **authorized** route — establishes boundary, **does not prove impossibility** (reviewer fix #2) | Whether an unauthorized but technically conceivable implementation exists (custom board D + retail signing would still be needed — a console SKU decision, not software workaround) | Record boundary; project stays alive as research (owner review §3); no hardware purchase |
| O4 No response | No new evidence | Unchanged | Retain `NOT CURRENTLY DEMONSTRATED`; offer alternate route after owner approval |
| O5 Ambiguous | Misrouted as publishing question | Same as O4 + need clarification | Send §3 follow-up with emphasized distinction |

---

## 9. Evidence of Applicable Requirements (Fetched, Not Assumed)

- `fetch_page https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/development-downloads/access-resources?view=gdk-2604` (chunks 0–1) — public vs secure split, personal MSAs no longer supported, Secure = *“Latest release of software and recoveries of the GDK”* (verbatim), MS rep enable.
- `fetch_page https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/set-up-organization?view=gdk-2604` — Partner Center + free Entra ID creation steps, Seller ID, user management.
- `fetch_page https://devdocs.xbox.com/home/onboarding` — full ID@Xbox onboarding checklist (Register partner → NDA → Partner Center Seller ID → ID@Xbox concept approval 10–15 days to 3 weeks → TLA + GDK License → SupplierWeb + Entra → EDS dev kits).
- `https://developer.microsoft.com/en-us/windows/support` — **ID@XBOX Program — Email ID@XBOX.com** (official GDK hardware question answers: contact representative; shipping via ID Setup).
- `https://learn.microsoft.com/en-us/answers/questions/5884771/...` — staff answer: organizational Entra ID required for Secure Downloads; personal MSA fails.
- `https://hc32.hotchips.org/.../HotChips2020_GPU_Microsoft_Jeff_Andrews_v2.pdf` slides — HSP/Pluton SHACK + MSP blocks (verified HW, not boot ladder).
- GitHub API `microsoft/GDK` — id 348416224 private false (verified).
- `developer.microsoft.com/en-us/games/partner` — Xbox Publishing guide; `aka.ms/gdkforum` — GDK developer forum.

All URLs re-verifiable; no invented inbox or representative name included.

---

## 10. Recommended Owner Decision (Per Request §5)

> **Approve this inquiry document as written; authorize Owner (Lamar) — not agent — to send it via Route B1 email `ID@XBOX.com` (or via existing account team contact if available — Route A) after confirming organizational contact identity. Do NOT authorize: Partner Center enrollment, NDA/GDK Agreement acceptance, GDKX download, dev kit purchase, Q&A posting, or registration.
>
> Upon receipt of Microsoft written answer (any of O1–O5), update `FEASIBILITY_FINAL_REVIEW.md` addendum with response citation and re-derive feasibility only on new evidence. Until then, retain `NOT CURRENTLY DEMONSTRATED`, preserve research assets, and defer diagnostic probe (Phase 6) as separate product until that boundary is settled.

---

*Prepared for Owner review — do not submit, register, accept agreements, or download restricted materials until Owner authorizes. All external actions remain blocked per `AGENTS.md` + `ENGINEERING_RULES.md` + prompt §3.*  
*Git verification for this file: `git diff` + `git status --porcelain` must show all six changed files (5 untracked + 1 modified) before staging — per reviewer fix #3.*
