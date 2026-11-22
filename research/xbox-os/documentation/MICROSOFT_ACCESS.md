# MICROSOFT_ACCESS.md — Legitimate Paths to Authorized Xbox Developer Resources

**Traceability:** `ACCESS-2026-11-22-001`  
**Source of Truth:** `https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/development-downloads/access-resources?view=gdk-2604` (verified via `fetch_page`, 2026-11-22, chunks 0–1) + `https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/set-up-organization`  
**Classification:** Public vs Secure resource split — exact steps to *attempt* secure access; no bypass attempted

---

## 1. Overview

Microsoft partitions GDK/Xbox development resources into **Public** (no auth, suffices for building PC games) and **Secure** (requires full Xbox development partner onboarding). The retail console OS boot chain is **not** listed among public resources and is **not demonstrably** included even in secure resources.

## 2. Public Resources (No Authorization)

| Resource | URL / ID | What It Gives |
|----------|----------|---------------|
| Public gaming documentation | `https://learn.microsoft.com/en-us/gaming/` | Landing page — all public GDK docs: app model, Store publishing, gaming overview |
| Public GDK on GitHub | `https://aka.ms/gdk` → `https://github.com/microsoft/GDK` | Common tools, libs, docs for Xbox Game Pass for PC (Win10/11), Xbox consoles (game building), cloud gaming; does **not** include console hypervisor/OS/boot chain |
| Public GDK samples | `https://github.com/microsoft/Xbox-GDK-Samples/` | Sample code demonstrating GDK features (Win32+ GDK, Store submission flow) |

> These are sufficient for this project's **research phases** (understanding app model, store flow, public GPU/CPU info). They are insufficient to obtain or boot retail Xbox OS.

## 3. Secure Resources (Authorization Required)

| Resource | URL / ID | Purpose | Who Needs It |
|----------|----------|---------|--------------|
| **Secure Xbox Downloads** | `https://aka.ms/gdkdl` (high-speed download service) | "Latest release of software and recoveries of the GDK", offline docs, Submission Validator, NDA samples, event materials | Developers targeting Xbox consoles |
| **Xbox Developer Forums** | `https://forums.xboxlive.com/` | Direct MS support | On-boarded partners |
| **Microsoft GDK NDA Topics** | `https://learn.microsoft.com/en-us/gaming/xbox-nda-docs/` | Graphics APIs specific to Xbox consoles (e.g., Xbox graphics driver, shader compiler) | On-boarded partners |

**Crucially — what is *not* listed:**

> Secure Downloads description from docs: *"Latest release of software and **recoveries** of the GDK. Offline versions of GDK documentation. **Submission Validator**..."*

No mention of "Xbox Series X retail OS image for generic PC", "retail boot chain image", "PC-deployable hypervisor", or "Xbox System Update ISO". Recoveries are GDK *development* recoveries (for Dev Kit), not retail console re-flash for non-Xbox hardware. Conflating them would be misrepresentation.

## 4. Exact Access Steps (Documented — Do Not Bypass)

### 4.1 Prerequisites

1. **Be part of an organization** that has been **onboarded as an Xbox development partner** in Microsoft's managed Xbox program (e.g., ID@Xbox). Personal enrollment is insufficient.
2. Organization must hold a **Microsoft Partner Center account** that was **provisioned during initial onboarding as an Xbox Development partner** (not a generic MPN account).
3. Organization must have a **valid Microsoft Game Development Kit (GDK) Agreement**.

### 4.2 Entra Tenant Association

Permissions are managed by the **owner of the Partner Center account** via a **Microsoft Entra ID tenant** (formerly Azure AD):

1. Owner navigates to Partner Center → associates Entra tenant (steps at `learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/set-up-organization`).
2. Individual members are added to that Entra tenant; owner grants Xbox-access roles.
3. If organization lacks Entra tenant: follow `Associate Microsoft Entra ID with your Partner Center account` (link in Access Resources page: `learn.microsoft.com/en-us/windows/uwp/publish/associate-azure-ad-with-partner-center`).

> **Alert from docs:** *"Personal Microsoft accounts (MSAs) are no longer supported for access at this time. If you do not have a Microsoft Entra tenant associated with your partner center account, you can add one..."*

### 4.3 Secure Xbox Downloads — Separate Authorization

```
Important: Access to Secure Xbox Downloads is not managed through Partner Center.
You must contact your Microsoft representative to enable access to the secure download site.
```

- Even with Partner Center + Entra set up, the download site (`aka.ms/gdkdl`) requires explicit enablement by a **Microsoft representative** (account manager for the managed program).
- Troubleshooting checklist from docs:
  - Verify signed into correct account (account vs correct Entra tenant)
  - Use "Switch directory" to select tenant linked to Partner Center
  - Verify added to company's Partner Center account

### 4.4 Developer Program Entry (If Not Yet Onboarded)

If company lacks Partner Center account:

1. Follow `Set up your organization in Partner Center` (`learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/get-started/overviews/set-up-organization?view=gdk-2604`).
2. Apply to managed program (ID@Xbox: `https://developer.microsoft.com/en-us/games/publish/program-selection` — link in GDK README "Licence and login required: GDKX (confidential program downloads): https://aka.ms/gdkdl").
3. Await Microsoft review/approval — **not automatic; Microsoft curates managed program membership**.
4. Only then proceed to §4.2–4.3.

## 5. What Authorization Does **Not** Guarantee (Honest Boundaries)

| Assumption to Avoid | Reality |
|---------------------|---------|
| "Once I have GDKX I'll have retail OS for PC" | GDKX provides Xbox-target toolchain and console graphics driver. It does **not** ship a PC-bootable retail OS. Retail hypervisor/OS remains console-fused. |
| "Secure Downloads likely contains OSU1 equivalent for PC" | OSU1 is public via Xbox Support; its PC-bootable equivalent is not listed among secure resources. |
| "I can redistribute whatever I download after onboarding" | GDK/GDKX are under NDA and proprietary licenses; redistribution of retail OS bits would violate terms. Our repo policy is hash-only (see `LICENSE-REVIEW.md`). |
| "Microsoft will provision Xbox identity for generic PC" | No public program advertises provisioning Xbox console identity (hardware root of trust) onto non-Xbox PC. Pluton for PC is for Windows security, not Xbox Live identity. |

## 6. Alternative Authorized Paths Evaluated (Out-of-Scope or Nonexistent)

| Path | Evaluated | Result |
|------|-----------|--------|
| Xbox Developer Mode (Dev Mode Activation app) | Publicly documented: turning retail Xbox into dev kit for side-loaded UWP/Win32 games | Does not give retail OS image; runs game/app in sandbox above retail OS. Irrelevant to PC boot. |
| Xbox System Update — Online | Console downloads direct from Xbox Live, not distributed as offline image | Not obtainable as standalone image without capture; console-bound. |
| Microsoft Store "OS recovery image" for PC | Some OEMs provide Windows recovery images; Xbox does not publish analogous generic image | Not existent per Xbox Support page; only OSU1 for console. |
| Insider Preview OSU | Community note: "OSU are not an option for preview builds" (Reddit 2019) | Insider builds are even less redistributable. |

## 7. Next Concrete Actions for Project Owner (Lamar) — Ordered

1. **(Immediate, no MS involvement):** Retrieve `OSU1.zip` in approved environment (Windows PC, unrestricted network) by expanding Step 1 on `support.xbox.com/.../offline-system-update`; record `sha256sum` → `SHA256SUMS.txt` and detailed inner-file hashes → `ARTIFACT_MANIFEST.json`. Even without PC boot, this satisfies acquisition provenance.
2. **(If Xbox console access available):** Document current console OS version (`Settings → System → Console info`) and compare to OSU1 applied version — confirms update-not-OS nature.
3. **(If exploring dev access):** Evaluate whether organization qualifies for ID@Xbox / Partner Center onboarding (requires company entity, Entra tenant readiness). Do **not** start onboarding speculatively before Feasibility Gate (Phase 5) concludes — onboarding is lengthy and does not demonstrably include retail OS for PC.
4. **(Alternative research):** Focus Phase 3 boot dependency graph on publicly accessible HotChips + Pluton + ACPI analysis rather than gated NDA material — higher yield with no approval overhead.

## 8. Verification Checklist

- [ ] All URLs verified via `fetch_page`/`curl -I` to GitHub API (success) vs Xbox.com (blocked → noted)
- [ ] No bypass of auth attempted (no login spoof, no leaked credentials)
- [ ] No assumption that GDK access → retail OS access (explicitly refuted with evidence)
- [ ] Steps quoted verbatim from docs with page URL and retrieval date

---

*This file is the authoritative description of legitimate Microsoft access for this project. Updates must re-verify the source page; do not copy community hearsay into the steps.*
