# W2-M4 Inquiry Readiness Packet — Owner Decision Package

**Traceability:** `INQUIRY-READINESS-2026-11-22-001`  
**Branch:** `arena/7ff9d1c6-xboxpc` @ `f4cf313` (current head; base `8771211` on `main`) — historical provenance `dc01bc1` → `1eac66c` preserved, see §9  
**Source inquiry:** `research/xbox-os/acquisition/MICROSOFT_RETAIL_OS_INQUIRY.md` (`INQUIRY-2026-11-22-001`) — DRAFT DO NOT SUBMIT  
**Evidence baseline:** `research/xbox-os/findings/EVIDENCE_AUDIT.md` (`AUDIT-CLAIMS-2026-11-22-001`) + `research/xbox-os/documentation/OSU1_ANALYSIS.md` + `BOOT_CHAIN.md` + `MICROSOFT_ACCESS.md`  
**Status:** **Ready for owner review — NOT SENT — no Microsoft contact, no enrollment, no NDA**  
**Date:** 2026-11-22 (calibrated pass)  
**Authors:** Documentation & Evidence Agent (audit), Security Research Reviewer (contact-route verification), Verification Agent (scope check)  
**PR:** #3 draft on this branch against `main` — head `f4cf313`, base `8771211`; do not merge until owner authorizes send

> **Hard boundary:** This packet does not send, submit, or contact Microsoft. It makes the inquiry *ready* and *reviewable* so you can decide whether, where, and how to send.

---

## 1. Executive Summary — What This Packet Establishes

- **Objective:** Establish in writing whether Microsoft offers any **legitimate, complete Xbox Series X retail OS artifact** and **authorized deployment path for standard x86-64 PC hardware** — distinct from OSU1 update, public GDK, and GDKX content.
- **Current evidence (prior to inquiry):** **No** such artifact advertised in searched public sources (support.xbox.com shell + GDK 348416224 + access-resources public description + community threads) — `NOT FOUND IN SEARCHED PUBLIC SOURCES`, full restricted inventory `UNKNOWN` (public illustrative list not exhaustive). This is **not** a claim of non-existence.
- **After inquiry:** Written Microsoft reply (email, Partner Center message, or linked doc page) attributable to Microsoft can be cited in `FEASIBILITY_FINAL_REVIEW.md` addendum + `MICROSOFT_ACCESS.md`. A positive O1 answer alone does **not** automatically move feasibility to `CONDITIONALLY FEASIBLE` — that requires identifiable artifact + provenance + legitimate acquisition route + applicable agreement/authorization + explicit standard-PC deployment authorization + supported hardware/configuration and deployment documentation (see §6 O1). Until those conditions are established, retain `NOT CURRENTLY DEMONSTRATED`.
- **Next actionable:** **W2-M4 packet prepared (completed as document)** → **W7-M1 remains BLOCKED** — inquiry unsent, awaiting owner decision on **Route A (preferred internal-routing path if organization already has account relationship) or B1 `ID@XBOX.com`** after confirming contact identity. Diagnostic probe `W6` is separate product (`PC-hardware-report`), not Xbox PC evidence — does not inflate `0/4` genuine readiness.

---

## 2. Audit — Inquiry Terminology, Accuracy, Scope, Calibrated Evidence

**Method:** Compared every line of `MICROSOFT_RETAIL_OS_INQUIRY.md` against `EVIDENCE_AUDIT.md` (6 VERIFIED / 7 STRONGLY SUPPORTED / 8 INFERRED / 5 UNKNOWN / 1 CONTRADICTED) and live sources. Preserved uncertainty where evidence unavailable.

| Area | Audit result | Action taken |
|------|--------------|--------------|
| **Q1–Q6 verbatim** | All 6 questions map 1:1 to charter §2 success criteria (genuine + PC boot + no host/emulator/bypass) and to O1-O5 outcomes. No question assumes availability. | **Preserved verbatim with Q6 calibrated to neutral clarification** — no narrowing |
| **Terminology — observable objective first** | `Complete retail OS image` defined as **observable objective first** (what boots retail console to dashboard/system services — genuine, unmodified, Microsoft retail-signed Xbox Series X OS observable on retail hardware) independent of internal naming; **internal architectural model hypothesis** second (e.g., `host.xvd`/`hvax64`/`system.xvd` per Xbox One-observed `BOOT_CHAIN.md` §1) explicitly disclaimed as *not Microsoft package naming* and labeled **hypothesis where not directly established for Series X** | **Kept** — prevents inventing deliverable; HostOS/SystemOS/hypervisor labeled INFERRED for Series X |
| **Factual accuracy** | OSU1 = public update payload `$SystemUpdate/*.xvd` + `RM_Signature.bin` via Troubleshooter to `System Update` A/B slots (STRONGLY SUPPORTED via GBAtemp/futuretweets, not personally `unzip -l`); Public GDK = `348416224` `d773744` game SDK missing Xbox gfx driver (VERIFIED); Secure Downloads = GDK software and GDK recoveries + documentation + Submission Validator + restricted samples per public description (DOCUMENTED), personal MSAs excluded, GDK Agreement + Entra + MS rep enable (DOCUMENTED) — full restricted inventory beyond public description UNKNOWN | **Verified** — each claim cites `fetch_page` + API + community source in §9, no invented facts |
| **Scope** | Does not request GDK tooling, OSU1 re-explanation, Insider preview, hardware discounts, or security bypass — explicitly listed in §1 | **Preserved** — prevents misrouting as publishing/bypass request |
| **Distinctions** | Table §4 separates **retail OS** (observable objective) vs **OSU1** (update), **Public GDK** (game SDK), **GDKX / Secure Downloads** (secure Xbox downloads including GDK software/recoveries/docs/Validator/samples), **dev-kit recovery** (Xbox-derived SoC dev firmware, hypothesis where Series X specifics not public) vs **PC-target deployment** (generic Tier 1 AMD/Intel, UEFI+NVMe+discrete GPU) — charter Part I §3 categories preserved | **Kept** — avoids conflation “OSU1 contains system.xvd hence is OS” / “GDKX recoveries are PC images” (audit S10 corrected) |
| **Unsupported assumptions removed** | No claim OSU1 *is* OS; no claim GDKX *holds* PC image; no claim `each blocker independently sufficient` (S10 CONTRADICTED → cumulative, scenario D custom board can spoof interfaces, not trust); no claim Xbox CA thumbprint or Series X ACPI dump observed; do not assert all GDK recoveries exclusively Dev Kit-only unless direct authoritative source establishes | **Removed** — S1-CPUID → INFERRED/UNKNOWN, S2-ACPI/SMBIOS → UNKNOWN, S3 Secure Boot → STRONGLY SUPPORTED with QEMU caveat, S5 boot ROM names → XboxOne-observed/SeriesX-expected; GDKX scope stated exactly as public docs establish |
| **Uncertainty preserved** | Full restricted Secure inventory `UNKNOWN` beyond public description; Series X ACPI/SMBIOS dump, SMCFW, per-stage sp/certs, `hvax64` hash, memory window GVEM traps `UNKNOWN`; Xbox identity provisioning to generic PC `INFERRED impossible` (no program listed) not traced | **Preserved** — marked `UNKNOWN` in `EVIDENCE_AUDIT.md` §5 and `roadmap.json` W1-M3/W3-M2 blockers |

**Verdict:** Inquiry is **factually accurate, scoped, and calibrated** — Q6 wording neutralized per calibration task; other rewordings are calibrations, not scope changes.

---

## 3. Final Proposed Inquiry Text (Submission-Ready, Owner-Reviewed Before Send)

> **Subject (B1 email):** *Research inquiry — Authorized retail Xbox Series X OS image for standard x86-64 PC hardware (distinguishing OSU1 / Public GDK / GDKX recovery)*
>
> Dear Microsoft Xbox team,
>
> We are a research group conducting an authorized-artifact feasibility study of **Xbox platform portability** under charter `XboxPC — Genuine Xbox Series X Retail OS on Standard PC Hardware`. We have completed an independent public-evidence audit (2026-11-22, current branch `arena/7ff9d1c6-xboxpc` @ `f4cf313`, base `8771211` on `main`; historical provenance `dc01bc1` → `1eac66c`) that distinguishes **OSU1 update packages, Public GDK (game SDK), and secure Xbox downloads content** — all verified from `support.xbox.com`, `github.com/microsoft/GDK` (id 348416224), `learn.microsoft.com/.../access-resources`, `devdocs.xbox.com/home/onboarding`, and Hot Chips 2020 Series X silicon presentation (360.4mm²/15.3B/16GB GDDR6/52CU/HSP SHACK MSP). **No public artifact in our sweep constituted a complete retail OS image for generic PC.**
>
> We write only to establish the **authorized acquisition boundary** — not to request a bypass, developer hardware purchase, or agreement acceptance before your answer.
>
> **Our objective (observable behavior first, hypothesis second):** *Genuine, unmodified, Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services — observable on retail console — to boot directly on standard x86-64 PC hardware (generic modern AMD/Intel desktop, UEFI, NVMe, discrete GPU) without a Windows/Linux host, emulator, or dashboard clone, while preserving retail signatures.* Our internal research model hypothesizes this *may* involve Host partition / hypervisor / System partition components (e.g., `host.xvd` / `hvax64` / `system.xvd` per Xbox One-observed `BOOT_CHAIN.md` map) — **labeled as internal hypothesis, not asserted as Microsoft-defined package names or a confirmed Series X packaging specification**; we ask only whether Microsoft offers any complete, authorized PC-targeted image/configuration satisfying the observable objective, regardless of internal naming.
>
> **Definitions attached:** One-page table distinguishing OSU1 (`OSU1.zip` → `$SystemUpdate/*.xvd` update payload applied via Xbox Startup Troubleshooter to System Update A/B partitions), Public GDK (`github.com/microsoft/GDK` game SDK missing console driver/Shader Compiler/GDKX APIs), and secure Xbox downloads per `learn.microsoft.com/.../access-resources` (**secure Xbox downloads including GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples**, requiring Partner Center Xbox-provisioned account + GDK Agreement + Entra ID + MS rep enable) — included to prevent conflation. Full restricted inventory beyond public description is UNKNOWN and not asserted.
>
> **Formal questions (verbatim — requested as written record):**
>
> 1. Does Microsoft provide, through any authorized program, a **complete Xbox Series X retail OS image** (as defined above — observable objective, regardless of internal naming) as a distributable artifact?
> 2. Is there a **Microsoft-supported, Microsoft-documented PC-target image/configuration** of that retail OS for standard x86-64 PC hardware booting directly without a Windows/Linux host?
> 3. Are **GDKX recovery packages at `aka.ms/gdkdl` exclusively intended for licensed Xbox development kits** (Xbox-derived SoC hardware with dev firmware)?
> 4. Is there an **authorized research/documentation program** that grants access to the retail boot chain and required platform docs (HSP/Pluton Xbox identity, SMU/SCP handshake, ACPI/SMBIOS surface) for feasibility evaluation?
> 5. Does Microsoft **support or authorize** deployment of retail Xbox OS components (retail-signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox hardware — or can Microsoft confirm **no such deployment is supported**?
> 6. Can Microsoft **clarify whether any authorized PC-targeted retail OS offering exists** for standard x86-64 PC hardware, and if no such offering exists, **confirm that distinction in writing** (OSU1 is an update package, public GDK is a game SDK, secure Xbox downloads content as publicly documented does not include a PC-bootable retail OS image, and none of the three as currently offered constitutes a PC-bootable retail OS image)?
>
> **What we need:** A short written reply (email, Partner Center message, or link to authoritative doc page) attributable to Microsoft stating, for each question, **yes/no with program name/URL, or “no such offering is provided.”** Community citations or Q&A threads are insufficient for our evidence standard — we will cite your response by URL+date in `FEASIBILITY_FINAL_REVIEW.md` and `MICROSOFT_ACCESS.md`.
>
> **What we will not do without explicit next-step authorization from you and our owner:** register organizations, accept NDAs/GDK Agreements, submit concept applications, acquire dev kit hardware, enable Secure Downloads, download restricted materials, modify OSU1, or attempt to boot retail components — all blocked until you confirm a path exists. **This inquiry itself requires no action beyond a written answer.** If this inbox cannot answer Q1–Q2 (e.g., retail OS licensing/platform-engineering scope), please route the question to the appropriate Xbox platform/OS or licensing team.
>
> Please advise whether this inquiry should be redirected to a specific team (e.g., ID@Xbox vs. Xbox Developer Program), or whether a Microsoft representative call is preferred. We can provide charter documents and audit evidence on request.
>
> Respectfully,  
> Lamar — Project Owner, XboxPC (charter `CHARTER-2026-11-22-001`)  
> [Organizational contact as enrolled in Microsoft directory, if any; otherwise general inquiry contact]
>
> Attachments: §4 Definitions table (1 page) + §1 context paragraph (this email)

**Variant for Microsoft Q&A (Route B2):** Same body truncated to 2000-char limit, attach table as image or gist link; tags `gaming-gdk` + `xbox-developer-program`.

*This text is identical in substance to `MICROSOFT_RETAIL_OS_INQUIRY.md` §7, with Q6 neutralized and hypothesis labeling clarified per calibration pass.*

---

## 4. Definitions and Distinctions Table (Attachment §4)

| Term (our usage) | What it is | What it is not | Source that establishes distinction |
|------------------|------------|----------------|------------------------------------|
| **OSU1** | Public offline **update package** from `support.xbox.com/.../offline-system-update`: `OSU1.zip` → `$SystemUpdate/*.xvd` (host/system/systemaux/systemmisc/systemtools/updater/SettingsTemplate) + `bootanim.dat`/`empty.bin`/`RM_Signature.bin`, applied from within Xbox Startup Troubleshooter to pre-existing `System Update` A/B partitions. ~4.8–6 GB, version-gated (greyed out if past version). | Not a complete OS, not a disk image, not independently bootable, not firmware, not boot ROM, not PC-compatible. | `fetch_page` Support page shell + `DOWNLOAD_SOURCES.md` §1 + `OSU1_ANALYSIS.md` + 5 community corroborations (techdows/binary.ph/irepairphones/manuals.plus/futuretweets/gbatemp) |
| **Public GDK** | Microsoft Game Development Kit (public, `github.com/microsoft/GDK`): common tools/libs/docs to build **games** for Xbox Game Pass for PC (Win10/11), Xbox consoles (game target), cloud. Via WinGet `Microsoft.Gaming.GDK`, NuGet `Microsoft.GDK.Windows`, vcpkg `ms-gdk`. Missing Xbox console driver/Shader Compiler/console env APIs. | Not the retail OS, not hypervisor, not HostOS/SystemOS, not boot chain. README: “Xbox console gfx driver + Shader Compiler … currently only in GDKX” | GitHub API id `348416224` private false stars 1741 commit `d773744` README 17186 B + `learn.microsoft.com/.../access-resources` public vs secure split |
| **Secure Xbox Downloads / GDKX** | Secure Xbox downloads **including GDK software and GDK recoveries, documentation, Submission Validator, and restricted samples** per public documentation. Requires Partner Center Xbox-provisioned account + valid GDK Agreement + Entra tenant + **MS representative** enable of `aka.ms/gdkdl`. Personal MSAs excluded. Public docs describe listed contents; full restricted inventory beyond that public description is UNKNOWN and not asserted as exclusively Dev Kit-only without direct authoritative source. | Not a retail OS image for generic PC. Even behind auth, no line in public docs advertises PC deployment of retail OS. Whether any recovery is exclusively Dev Kit-only is the subject of Q3, not asserted here. | `fetch_page` `access-resources?view=gdk-2604` ch 0–1 + `MICROSOFT_ACCESS.md` §3–5 + `devdocs.xbox.com/home/onboarding` checklist |
| **Complete retail OS image (object of inquiry)** | **Observable objective first:** Genuine, unmodified, Microsoft retail-signed Xbox Series X OS that boots retail console hardware to dashboard/system services without Windows/Linux host, emulator, or dashboard clone — i.e., what “boots the Xbox.” **Internal model (hypothesis):** *May* involve Host partition / hypervisor / System partition (e.g., `host.xvd`/`hvax64`/`system.xvd` per Xbox One-observed `BOOT_CHAIN.md` §1) — **labeled as hypothesis, not Microsoft naming or confirmed Series X spec**. **Question:** Whether Microsoft offers *any* complete, authorized, PC-targeted image satisfying observable objective, regardless of naming. | Not OSU1 (update of some XVDs), not GDK, not GDKX game toolchain. Would need to be Microsoft-signed, PC-targeted image. None documented as offered. | Charter §2 success table + Hot Chips 2020 (360.4mm²/15.3B/16GB GDDR6/52CU/HSP SHACK) + Xbox One Research wiki bootloaders (XboxOne-observed, SeriesX-expected) |

---

## 5. Recipient-Route Evidence and Recommendation

**Method:** For each route: exact source URL, what it establishes, what it does not, uncertainty. No invented contacts. Fetched via `fetch_page` + `web_search` 2026-11-22, calibration pass 2026-11-22.

### Route A — Preferred Internal-Routing Path If Organization Already Has Account Relationship

| Field | Detail |
|-------|--------|
| **Channel** | Existing **Microsoft account team / Xbox developer program representative** for your organization (if already onboarded to ID@Xbox/Partner Center) — the `Microsoft representative` referenced in access-resources for Secure Downloads |
| **URL / Source** | `fetch_page https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/development-downloads/access-resources?view=gdk-2604` ch 0 § “Accessing secure resources” Important box verbatim: *“You must contact your Microsoft representative to enable access to the secure download site.”* |
| **What it establishes** | Microsoft explicitly routes **Secure Downloads enablement** through this representative — therefore they are a **preferred internal-routing path** for enabling download access if the organization already has an account relationship. |
| **What it does not establish** | Official documentation establishes that this representative **enables download access**; it **does not establish exclusive authority over product inventory or retail OS policy** (e.g., whether a PC-targeted retail OS offering exists — that is beyond Secure Downloads enablement and requires routing to the appropriate platform/OS or licensing team). Do not present this person as the only authority who can confirm Secure Downloads contents or retail OS policy. |
| **Uncertainty** | If owner has no prior onboarding, contact identity is `UNKNOWN` — check `PARTNER_ORG` before using. Do not invent a rep name. Should be described as preferred internal routing if available, not as exclusive gatekeeper. |

### Route B — Documented GDK Developer Support Channels (No Prior Partnership Required for Initial Contact)

#### B1 — Microsoft Developer Support — ID@Xbox Program (Documented Initial Contact for Console/DevKit Questions)

| Field | Detail |
|-------|--------|
| **Channel** | **Microsoft Developer Support — ID@Xbox Program — Email `ID@XBOX.com`** |
| **URL / Identifier** | `https://developer.microsoft.com/en-us/windows/support` → section **“ID@XBOX Program” — “Email ID@XBOX.com”**; landing page `https://developer.microsoft.com/en-us/games/partner` → “Ready to publish on XBOX? → Join ID@XBOX” |
| **What it establishes** | `fetch_page developer.microsoft.com/en-us/windows/support` (Nov 21 2022) states: *“For questions about the ID@XBOX program including game publishing, console questions, onboarding to the program and XBOX DevKits, contact the team directly. Email ID@XBOX.com”* — this is a **documented, public inbox for ID@Xbox, console, and DevKit questions** (onboarding and console questions). `web_search GDK support ID@Xbox` result id=1 corroborates. |
| **What it does not establish** | Does **not** establish this inbox as a confirmed retail OS licensing or platform-engineering authority. It is a documented initial contact that can route console/DevKit questions; for Q1–Q2 retail OS licensing/platform-engineering scope, ask it to **route the question to the appropriate Xbox platform/OS or licensing team** if it cannot answer directly. Do not describe it as authoritative for retail OS licensing. |
| **Uncertainty** | Response time **UNKNOWN** — do not transfer game-concept review timelines to support correspondence; no response-time promise is made. Routing accuracy depends on framing as **policy clarification, not game pitch**, and on requesting referral if out of scope. Suitable as initial contact for Q1–Q6 with explicit routing request. |

**Recommendation:** If owner has **no existing Route A account relationship**, **B1 `ID@XBOX.com` is the documented primary initial contact** — the only documented public inbox explicitly for Xbox developer program console/onboarding questions. Frame as policy clarification and include: *“If this inbox cannot answer Q1–Q2, please route to the appropriate Xbox platform/OS or licensing team.”*

#### B2 — Microsoft Q&A — GDK Hardware / Download Access (Fallback, Not Equivalent Authority)

| Field | Detail |
|-------|--------|
| **Channel** | **Microsoft Q&A** — `https://learn.microsoft.com/en-us/answers/questions/1663748/how-can-i-obtain-the-gdk-hardware` and `https://learn.microsoft.com/en-us/answers/questions/5884771/unable-to-access-to-download-gdk-for-xbox-development` (both `learn.microsoft.com` official Q&A) |
| **What it establishes** | `fetch_page` + `web_search` show Microsoft external staff answers cite **organizational Entra ID tenant + onboarded Xbox Development partner + GDK Agreement + MS rep enable** as Secure Downloads prerequisites; personal MSA fails. Establishes that Q&A staff do answer GDK/GDKX access questions and cite GDK Agreement terms. |
| **What it does not establish** | Not equivalent authoritative channel for retail OS image confirmation — Q&A answers GDK access mechanics, not authorization boundary. Treating Q&A as equal to B1 would overstate authority (packet distinguishes fallback vs primary). |
| **Uncertainty** | Thread 1663748/5884771 may be archived; new question tagged `gaming-gdk` may be needed. Response quality varies — not citable as written Microsoft confirmation of no PC image unless answer explicitly states it. |

#### B3 — Xbox GDK Developer Forum (Conditional, Requires Limited Onboarding)

| Field | Detail |
|-------|--------|
| **Channel** | `https://aka.ms/gdkforum` → Xbox GDK developer forum (shortlink listed on `devdocs.xbox.com/home/onboarding-access/access-resources` “GDK developer forum: Post questions and report issues to the XBOX team”) |
| **What it establishes** | Developer Q&A with Xbox engineering team, Microsoft engineering monitors — documented on `devdocs.xbox.com/home/onboarding` and `learn.microsoft.com` GDK docs “Get help” area. |
| **What it does not establish** | Accessible only after at least limited onboarding (see B4). Not usable as first contact without account. |
| **Uncertainty** | Access requires Partner Center + Entra setup — not usable until owner chooses to evaluate B4 checklist. |

#### B4 — Xbox Partner Onboarding Checklist (Read-Only, No Registration)

| Field | Detail |
|-------|--------|
| **Channel** | `https://devdocs.xbox.com/home/onboarding` — full checklist: Register as Xbox partner → Enroll to Partner Center (accept App Developer Agreement, receive Seller ID) → Apply to ID@XBOX (business info + game concept → sign Title Licensing Agreement + GDK License Agreement) → Complete onboarding via SupplierWeb + Entra ID → EDS account for dev kits |
| **What it establishes** | `fetch_page devdocs.xbox.com/home/onboarding` establishes prerequisites (legal entity, DUNS recommended, shipping address, NDA, ≥18, country where MS does business, Entra capability, willingness to sign GDK Agreement). Establishes that **even full onboarding** publicly documented contents are GDK software + GDK recoveries + documentation + Submission Validator + restricted samples — **no line in public docs lists retail OS for PC**. |
| **What it does not establish** | Does not provide a contact for unsolicited inquiry — it is a **read-only evaluation tool** to let owner assess eligibility without creating accounts. No registration, agreement acceptance, or hardware purchase occurs now. |
| **Uncertainty** | Not relevant until after inquiry response. |

#### B5 — Xbox Insider Program (Explicitly Not for This Inquiry)

| Field | Detail |
|-------|--------|
| **Channel** | `https://www.xbox.com/en-us/developers/insiders` |
| **What it establishes** | `fetch_page` Insider program article + Reddit 2019 note: playtest audience expansion, not developer onboarding; community sources confirm “OSU are not an option for preview builds” — preview OSU path separate and not generic PC. |
| **What it does not establish** | Any retail OS image for PC — listed only to avoid misdirection. |
| **Uncertainty** | None — correctly excluded. |

### Route C — Community / Non-Authoritative (Informational Only)

| Channel | Why listed | Action |
|---------|------------|--------|
| GitHub Discussions at `github.com/microsoft/GDK` | Public GDK repo has Discussions enabled — community can explain GDK vs GDKX README distinction | Do not use for Q1–Q6; read-only |

### Route Requirements Evidence (If Owner Chose to Onboard — Not Requested Now)

| Requirement | Detail | Source |
|-------------|--------|--------|
| Legal entity | Must be legal business (studio/publisher), DUNS recommended, shipping address, legal name/DBA | `devdocs.xbox.com/home/onboarding` checklist prerequisites |
| Partner Dashboard + NDA | Register via `developer.microsoft.com/en-us/games/partner` → NDA | Checklist Step 1 |
| Partner Center | Enroll, accept App Developer Agreement, receive Seller ID | Checklist Step 2 + `learn.microsoft.com/.../access-resources` public vs secure |
| ID@Xbox application | Submit game concept → sign Title Licensing + GDK License Agreement | Checklist Step 3 |
| Entra ID + MS Rep | Associate Entra ID tenant with Partner Center (free creation) + MS rep enable of `aka.ms/gdkdl` | `learn.microsoft.com/.../set-up-organization` + access-resources Secure note |
| Secure Downloads | Even then, publicly documented contents = GDK software + **GDK recoveries** + documentation + Submission Validator + restricted samples — **no line lists retail OS for PC** | Access-resources § Secure resources (verified public description) |
| Dev Kit hardware | EDS account after GDK Agreement → order kits (separate cost, not PC hardware) | Checklist Step 4 |
| MSA deprecation | Personal Microsoft Accounts **no longer supported** for secure Xbox resources — **organizational Entra account required** | `fetch_page access-resources` Important alert box |

### Recommendation Summary

- **If owner has existing Microsoft account team / Xbox program rep (Route A):** Use **Route A as preferred internal-routing path** — it enables Secure Downloads and can route internally to the appropriate platform/OS or licensing team for Q1–Q2; do not describe it as exclusive authority over product inventory or retail OS policy.
- **Otherwise:** **Route B1 `ID@XBOX.com` is the documented primary initial contact** for ID@Xbox, console, and DevKit questions — suitable for policy clarification with explicit routing request: *“If this inbox cannot answer retail OS licensing scope, please route to the appropriate Xbox platform/OS or licensing team.”* Response time UNKNOWN — no promise made.
- **Fallback not equivalent:** **Route B2 Q&A** — suitable for follow-up clarification if B1 deflects, not as initial authoritative channel. Do not treat as endorsement. Do not transfer game-concept review timelines to support correspondence.
- **No invented contacts:** All emails/URLs from fetched Microsoft domains; `ID@XBOX.com` is verbatim from `developer.microsoft.com/en-us/windows/support` § ID@Xbox Program, not guessed.

---

## 6. O1–O5 Response/Outcome Matrix — What Each Response Establishes and Next Action

| Code | Microsoft response | What it establishes | Technical implications (boot-chain terms) | Next action (owner + agent) |
|------|------------------|---------------------|-------------------------------------------|-----------------------------|
| **O1 COMPLETE RETAIL IMAGE AVAILABLE (conditional, not automatic feasibility)** | “Yes — Microsoft does provide a complete Xbox Series X retail OS image via [specific program: e.g., `aka.ms/gdkdl` category *‘Xbox OS Recovery — PC Target’* / new managed research program], and this image is authorized for standard x86-64 PC hardware.” | Establishes that Microsoft **states** an image exists — does **not** automatically set feasibility to `CONDITIONALLY FEASIBLE`. Feasibility moves only when **all** of the following are established: (1) **identifiable artifact and provenance** (exact image name/version/hash, signing identity — Xbox CA variant if any, distribution URL or program name); (2) **legitimate acquisition route and applicable agreement/authorization** (Partner Center program, GDK Agreement/NDA scope, Entra/MS rep enablement); (3) **explicit standard-PC deployment authorization** (written confirmation that deployment to generic Tier 1 PC hardware is supported, not merely Dev Kit); (4) **supported hardware/configuration and deployment documentation** (SOC/board/GPU/memory support list, hypervisor PC build if any, Secure Boot `db` enrollment, deployment guide). Until those four conditions are established, retain `NOT CURRENTLY DEMONSTRATED`. | If O1 verified, retail signing root (Xbox CA) would need to be accompanied by **PC-enrollable trust/provisioning flow** (HSP/Pluton Xbox identity for PC, or single signed `hvax64`/HostOS variant for PC firmware) — otherwise image would fail hardware-RoT (see `BOOT_CHAIN.md` §2 rows 2–3). Request MS to specify: signing variant, required PC Secure Boot enrollment (Xbox `db`), SOC/board support list, hypervisor PC build, memory-layout config for DDR5+discrete GPU vs unified GDDR6, GPU driver for PC. All **hypothesis where not directly established for Series X**. | **Pause other work; document exact authorized acquisition process + technical requirements; do NOT acquire image until owner authorizes new GDK Agreement/NDA scope and records hash-provenance procedure (`PROVENANCE.md` + `SHA256SUMS.txt` expansion). Update `roadmap.json` W7-M1 only when four conditions above are fully established — do not set `CONDITIONALLY FEASIBLE` on a bare “yes” without artifact/provenance/authorization/configuration.** |
| **O2 DEV-KIT RECOVERY ONLY** | “Secure Downloads at `aka.ms/gdkdl` contains recovery packages exclusively intended for licensed Xbox development kits (Xbox-derived SoC dev firmware). There is no Microsoft-supported retail OS image for generic PC deployment.” | Establishes, if Microsoft states it in writing, that **recoveries as offered are Dev Kit-only** — this confirms scope **only to the extent Microsoft explicitly states it**; public docs alone describe contents as “GDK software and GDK recoveries” without a public line asserting exclusive Dev Kit-only scope for all recoveries. Does **not** establish PC feasibility; closes conditional misreading that GDKX maybe holds PC image. | No transfer to generic PC: Dev Kit recoveries contain Xbox SoC firmware + hypervisor tuned for Xbox SoC GDDR6/GPU/MC/SCP (hypothesis for Series X specifics where not directly established). No path to Tier 1 generic AMD/Intel desktop. | Record in `FEASIBILITY_FINAL_REVIEW.md` addendum with citation: **“Microsoft confirms GDKX recoveries as offered are Dev Kit-only; no generic PC image offered.”** — retain `NOT CURRENTLY DEMONSTRATED`; reassess only if owner later proposes custom board (scenario D) which still needs retail signing and is *not standard PC*. |
| **O3 NO PC DEPLOYMENT SUPPORT** | “Microsoft does not support or authorize deployment of retail Xbox OS components (signed hypervisor, HostOS/SystemOS XVDs, retail signing root) onto non-Xbox hardware. Deployment targets are limited to Xbox hardware families (retail + licensed dev kit).” | **Authoritative authorization boundary** — confirms **no Microsoft-supported path** exists for charter objective as presently defined. This response does **not** prove impossibility (reviewer fix #2), but it does establish *no authorized route*. | Hardens trust boundary: Xbox CA not in PC `db`, Xbox HSP/Pluton identity not provisionable to generic PC (PCWorld 2020 “Xbox security approach for PCs” was for Windows security, not Xbox OS portability), no PC-target hypervisor image. Any bypass would violate `SECURITY.md`/`ENGINEERING_RULES.md` (no key extraction/Secure Boot bypass). | **Accept as formal closure of authorized route** (not proof of no technical possibility). Record boundary; keep project alive as research per owner review: *preserve evidence, do not purchase hardware, do not start diagnostic probe until re-authorized as separate product*. Update `roadmap.json` O3 blocker noted, but readiness stays 0%. |
| **O4 NO RESPONSE** | No reply within reasonable window or auto-generated “contact your account team” deflection | **No new evidence** — neither confirms nor denies authorized path. Retain existing verdict and documented lack of public PC image. | No change to technical blockers — all 10 dependency rows remain calibrated as before. | **Retain `NOT CURRENTLY DEMONSTRATED`**. Re-offer inquiry via alternate route (B2 Q&A post) after Owner approves; do not loop automatically. |
| **O5 AMBIGUOUS RESPONSE** | “The GDK/GDKX contains tools to build games that run on Xbox consoles and PC via Game Pass / cloud; publishing on Xbox requires ID@Xbox.” — or discussion of OSU1 / Inside previews / PlayFab — without answering Q1–Q2 | Fails to distinguish OSU1/public GDK/defined secure-downloads content/retail OS image (definitions table §4 was attached to prevent this). Ask was misunderstood as game-publishing question. | No technical implication until clarified — ambiguity does not resolve trust block #1. | **Identify exactly what needs clarification**: resend attachment table §4 with sharper emphasis: *“We are NOT asking how to build a game that runs on Xbox OR PC. We are asking whether Microsoft distributes the Xbox Series X retail operating system itself as a PC-bootable image, distinct from those — observable objective as defined.”* — require Owner approval before follow-up. |

**Destination remains:** Genuine, unmodified retail OS on standard PC — no host OS/emulator/bypass. O1 would move toward `CONDITIONALLY FEASIBLE` only **after** four conditions above (artifact/provenance/route+agreement/PC-authorization/configuration) are established — not automatically on a “yes.”

---

## 7. Send-Readiness Checklist — All Must Be ✅ Before Send

- [ ] **Definitions table §4 attached** (1 page) — prevents conflation OSU1/GDK/secure-downloads/retail OS
- [ ] **Context paragraph §3 included** — frames as policy clarification, not game pitch; requests routing if out of scope
- [ ] **Six questions verbatim Q1–Q6** — Q6 neutral clarification whether any authorized PC-targeted offering exists
- [ ] **Observable objective first + hypothesis disclaimer** — observable objective (boots retail console to dashboard) defined independently; *may* involve `host.xvd`/`hvax64`/`system.xvd` per Xbox One-observed `BOOT_CHAIN.md`, **labeled as hypothesis not Microsoft naming, not Series X spec**
- [ ] **No bypass/NDA/hardware request** — explicitly states inquiry itself requires no action beyond written answer; no enrollment, GDKX download, or OSU1 modification until owner authorizes
- [ ] **Route confirmed** — owner checked: Route A exists? If yes, use A as preferred internal-routing path; if not, B1 `ID@XBOX.com` with routing request to platform/OS or licensing team if needed
- [ ] **Organizational contact identity confirmed** — sender is Lamar — Project Owner (charter `CHARTER-2026-11-22-001`) with correct enrolled directory contact if any
- [ ] **Subject line** — *Research inquiry — Authorized retail Xbox Series X OS image for standard x86-64 PC hardware (distinguishing OSU1 / Public GDK / GDKX recovery)*
- [ ] **Attachments** — §4 table + §1 context paragraph — for Q&A variant, truncated to 2000-char limit with table as image/gist, tags `gaming-gdk` + `xbox-developer-program`
- [ ] **Evidence packet ready** — can provide charter + audit (`EVIDENCE_AUDIT.md`, `BOOT_CHAIN.md`, Hot Chips pdf reference) on Microsoft request
- [ ] **Hard boundaries acknowledged** — no Partner Center enrollment, no GDK Agreement/NDA acceptance, no Q&A posting, no registration until this inquiry answered

**Any “no” → do not send. Fix checklist, then re-review.**

---

## 8. Explicit Owner Authorization Section — Sign to Authorize External Contact

> **Authorization is required for ANY external contact. Agent (AI) is never authorized to send, register, or accept agreements.**

**Option A — If existing Microsoft account relationship (preferred internal routing):**

- [ ] **I, Lamar — Project Owner, authorize ME (not agent) to send this inquiry via Route A existing Microsoft account team / Xbox developer program representative** (the MS rep referenced in `access-resources` Important box — enables download access; I understand this is a **preferred internal-routing path**, not an exclusive product-inventory authority). I have confirmed `PARTNER_ORG` account exists.

**Option B — Primary initial contact (if no existing account relationship):**

- [ ] **I, Lamar — Project Owner, authorize ME (not agent) to send this inquiry via Route B1 email `ID@XBOX.com`** as documented initial contact for ID@Xbox/console/DevKit questions, with request to route to appropriate Xbox platform/OS or licensing team if out of scope.

**Explicitly DO NOT authorize (check to confirm understanding):**

- [ ] Partner Center enrollment, NDA/GDK Agreement acceptance, GDKX download, dev kit purchase, Q&A posting, registration — **NOT authorized** in this packet. Separate authorization required after inquiry response.

**Upon Microsoft response (any O1–O5):**

- [ ] Update `FEASIBILITY_FINAL_REVIEW.md` addendum with response citation (URL + date) and re-derive feasibility **only** when O1 four conditions (artifact/provenance/route+agreement/PC-authorization/configuration) are fully established; otherwise retain `NOT CURRENTLY DEMONSTRATED`
- [ ] Update `docs/architecture/roadmap.json` (W2-M4→W7-M1) and regenerate dashboard via `python docs/architecture/generate-dashboard.py` + `python scripts/verify-dashboard.py`
- [ ] Until then, retain `NOT CURRENTLY DEMONSTRATED`, preserve research assets, defer diagnostic probe (W6) as separate `PC-hardware-report` product until that boundary settled

**Owner signature:**

- Name: _________________________
- Date: _________________________
- Chosen route: ☐ Route A (account team: _________________) ☐ Route B1 `ID@XBOX.com` ☐ Defer/Deny
- Notes: _________________________

**Agent sign-off:**

- Documentation & Evidence Agent (inquiry audit): 2026-11-22 — no fabricated routes, no endorsement claims; Route A not presented as exclusive authority
- Security Research Reviewer (contact verification): 2026-11-22 — all URLs from fetched Microsoft domains, no invented inbox; response times marked UNKNOWN
- Verification Agent (scope check): 2026-11-22 — distinctions preserved, GDKX scope stated exactly as public docs establish, uncertainty marked UNKNOWN

---

*Prepared for owner review — do not submit, register, accept agreements, or download restricted materials until owner authorizes. All external actions remain blocked per `AGENTS.md` + `ENGINEERING_RULES.md` + charter §8.*  
*This packet reflects reconciliation pass on `f4cf313` (base `8771211`); prior history `dc01bc1` → `1eac66c` → `8771211` preserved in prior commits and `MICROSOFT_RETAIL_OS_INQUIRY.md` provenance.*  
*Next packet on response: `FEASIBILITY_FINAL_REVIEW.md` addendum + `roadmap.json` W7 status update (W7-M1 not complete until four O1 conditions met).*

