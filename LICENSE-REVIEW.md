# LICENSE-REVIEW.md — Distribution & Artifact Handling

**Traceability:** `LIC-2026-11-22-001`

---

## 1. What This Repository Contains (and Does Not)

- **Contains:** Markdown research, JSON schemas, source code we write (UEFI diagnostic probe under MIT — to be declared in Phase 6), tooling, build scripts, evidence logs (hashes, URLs, test outputs).
- **Does NOT contain:** Microsoft-proprietary binaries, decrypted Xbox OS images, GDKX content, game dumps, dashboard assets as binaries. Only provenance metadata (hash, source URL, signature status) may appear in `evidence/source-register/`.

## 2. Artifact Classes (per Project Definition Phase 2)

| Artifact | Distribution Status | Git Storage |
|----------|---------------------|-------------|
| Official system update (from Microsoft) | Verify authenticity, document hash | Hash + URL only |
| Recovery package (OSU/OSU1) | Recovery-only, not full OS | Hash + URL only |
| Public GDK | Available under Microsoft license | May reference publicly documented APIs |
| Restricted GDKX | Requires authorization | Not acquired; document requirement only |
| Game package | Not OS | Do not acquire |
| Retail OS components | Provenance must be established | Hash + provenance only |

## 3. Legal Access Conditions

We acquire artifacts only via:

- Microsoft Xbox Support offline update portal (https://support.xbox.com/help/hardware-network/offline-system-update)
- Official Microsoft Download / Xbox Insider channels
- Xbox Developer Program documentation (https://learn.microsoft.com/en-us/gaming/gdk/)
- Authorized hardware purchase (console recovery via owned hardware — recovery image for repair, not redistribution)

We do **not** scrape, torrent, or use unauthorized mirrors.

## 4. License of Our Code

Our independently developed diagnostic environment (Phase 6) — UEFI probe, inventory modules, report generator — will be licensed **MIT** (to be added as `LICENSE` in Phase 6). This covers only code we author. It does not grant rights to Microsoft components.

Until Phase 6, this file is the governing license notice; no code is yet licensed.

## 5. Evidence Retention Policy

- Evidence binaries (OS images, large firmware) are **not** committed. Store externally with access log; commit only SHA256 + source entry.
- Retention: per milestone; GC only by owner approval.
- Size cap: cumulative turn-end patchset <128 MB / 10k files.

## 6. Questions

Contact Project Owner before adding any third-party code or artifact reference.

---

*Last reviewed: 2026-11-22 — placeholder until Phase 2 artifact analysis completes.*
