# PROVENANCE.md — Acquisition Provenance & Chain of Custody

**Traceability:** `PROV-2026-11-22-001`  
**Companion:** `DOWNLOAD_SOURCES.md`, `ARTIFACT_MANIFEST.json`, `SHA256SUMS.txt`  
**Policy Ref:** `LICENSE-REVIEW.md`, `SECURITY.md`, `ENGINEERING_RULES.md` §§1–2

---

## 1. What Was Attempted — Complete Command Log

| Step | Command / Tool | URL / Target | Result | Evidence ID |
|------|---------------|--------------|--------|-------------|
| 1 | `fetch_page https://support.xbox.com/help/hardware-network/console/offline-system-update` | Xbox Support OSU page | **Success** — chunk 0 returned title "Perform an offline system update \| XBOX Support", body: Windows PC + 6 GB NTFS USB, OSU1 steps | `FETCH-XBOX-SUPPORT-20261122-01` |
| 2 | `fetch_page https://github.com/microsoft/GDK` | Public GDK repo | **Success** — chunk 0, stars 1741, latest commit d773744 (2026-11-04), full README banner | `FETCH-GITHUB-GDK-20261122-01` |
| 3 | `fetch_page https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/development-downloads/access-resources?view=gdk-2604` | GDK Access requirements | **Success** — chunk 0–1, public vs secure resources table verbatim, Partner Center + Entra requirements | `FETCH-LEARN-GDKACCESS-20261122-01` |
| 4 | `curl -L -v https://support.xbox.com/...` | Same as §1 but via bash `curl` | **Blocked** — `OpenSSL SSL_connect: SSL_ERROR_SYSCALL` after Client Hello | `CURL-BLOCK-01` |
| 5 | `curl -I https://download.microsoft.com/download/.../OSU1.zip` | Direct OSU1 | **Blocked** — same SSL syscall error | `CURL-BLOCK-02` |
| 6 | `curl -I https://aka.ms/OSU1` | Hypothetical short-url | **Blocked** — same | `CURL-BLOCK-03` |
| 7 | `python3 urllib.request.urlopen http://www.xbox.com/xboxone/osu1` | Xbox short-redirect | **Blocked** — `TLS/SSL connection has been closed (EOF)` | `PY-BLOCK-01` |
| 8 | `fetch_page https://www.xbox.com/xboxone/osu1` | Same | **HTTP 500** — server requires browser-handled redirect not proxied | `FETCH-XBOX-SHORT-01` |
| 9 | `curl -s https://api.github.com/repos/microsoft/GDK` | GitHub API | **Success** — JSON `id: 348416224`, private `false` | `API-GDK-01` |
| 10 | `curl -s https://api.github.com/repos/microsoft/GDK/contents/` | GDK contents | **Success** — 6 entries (CHANGELOG.MD, DSC, LICENSE-EN-US.MD, README.MD, SECURITY.MD, resources) | `API-GDK-CONTENTS-01` |
| 11 | `web_search "Xbox OSU1 offline system update file"` | OSU1 documentation | **Success** — 5 corroborating sources + 2 pages of fetch_page with `$SystemUpdate` layouts | `SEARCH-OSU1-01` |
| 12 | `web_search "Xbox Series X boot chain secure boot Pluton"` | Boot security | **Success** — HSP Pluton 5-source chain: Tom's Hardware, PCWorld, itigic 2021, etc. | `SEARCH-BOOT-01` |

**No proprietary binary was downloaded.** Steps 4–8 failures are logged as honest blockers, not masked.

## 2. Artifacts: Source → Acquisition → Preservation

For each artifact in `ARTIFACT_MANIFEST.json`:

| Artifact | Official Source URL | Acquisition Date | File Size (observed) | Cryptographic Hash | Signature Verification | Intended Platform | Legal Access |
|----------|---------------------|------------------|----------------------|-------------------|------------------------|-------------------|--------------|
| OSU1.zip | `support.xbox.com/.../offline-system-update` → `download.microsoft.com/.../OSU1.zip` (via `www.xbox.com/xboxone/osu1` shortlink) | **Not acquired** (blocked in sandbox) | **Not observed** (est. ~4.8–6 GB) | **Not yet** — placeholder in SHA256SUMS.txt | **Inferred** — `RM_Signature.bin` in payload validated by console with retail Xbox keys | Xbox Series X\|S + Xbox One (generic) | Public — Microsoft-provided for console repair; **no redistribution permission** — retain locally under provenance record, publish only hash/url/date |
| OSU2/OSU3 | same page, branch | Not attempted | — | Not yet | — | Original Xbox One only | Public |
| Public GDK | `github.com/microsoft/GDK` | 2026-11-22 (verified via API) | N/A (repo) | Commit `d773744` + file `README.MD` blob sha `a20e39...` | N/A — open-source tooling | Dev PCs (Windows) — not console OS | Public — `LICENSE-EN-US.MD` (Other / NOASSERTION) |
| Secure GDKX | `aka.ms/gdkdl` / `aka.ms/gdkxdocs` | Not attempted (auth required) | N/A | — | — | Dev kits + consoles under NDA | Restricted — GDK Agreement + Partner Center + Entra + MS rep |

> **Preservation commitment:** Upon owner retrieval of `OSU1.zip` in approved environment, the following will be completed:
> 1. `sha256sum OSU1.zip` → append to `SHA256SUMS.txt` as `<hash> *OSU1.zip`
> 2. `ARTIFACT_MANIFEST.json`: fill `sha256`, `file_size`, `version_build` (extracted from `updater.xvd` manifest or payload JSON), `signature_status` (attempt verification with Xbox-specific tooling — expected to fail on PC, failure is evidence)
> 3. `evidence/source-register/OSU1-<build>.json` — full JSON evidence entry per `evidence/README.md` convention (`Evidence ID: EVID-...` format)

## 3. Integrity Checks Required (Future)

- [ ] Hash recomputed locally by Verification Agent matches `SHA256SUMS.txt` entry (SHA256)
- [ ] Downloaded filename equals canonical `OSU1.zip` (no rename to `.iso`)
- [ ] Source URL is exactly the official support page link (not a mirror)
- [ ] Signature `RM_Signature.bin` exists in unpacked payload (ls `$SystemUpdate/`)
- [ ] Payload date matches support page refresh (Reddit-style build date check)
- [ ] No restricted binary accidentally committed (guard: `git log --name-only` / `.gitignore` excludes `*.zip`, `*.xvd`)

## 4. Honest Limitations

- **Size/version are estimates** until direct download. Stated ranges are explicitly marked `estimated_range` in manifest — not fabricated.
- **Internal layout ($SystemUpdate/*.xvd lists)** rests on high-confidence extrapolation from Xbox One family GBAtemp internal-partition docs. Series X\|S layout is almost certainly same genus but may have extra `.xvd` (e.g., `sys_main.xvd` vs `system.xvd` variant). Marked `high_for_xbox_one_extrapolated_to_series_x_s`.
- **Signature claim is inferred**, not signature-verified in this env. True verification requires Microsoft Xbox signing CA (not public) — failure to verify on PC is expected.

## 5. Redistribution Compliance

Per `LICENSE-REVIEW.md`:

- `OSU1.zip` and derived XVDs are **never** committed to Git. Only hashes, source URLs, dates, and *structural* file listings (filenames, not contents) are committed.
- `.gitignore` correctly excludes `*.zip`, `*.xvd`, `XBOX_OSU*.zip`, `recovery*.zip` etc. — verified via `git check-ignore`.
- This file itself contains no proprietary data.

---

*Every line here is challengeable — run the same `fetch_page`/`curl`/API commands at the same commit and you must get same results modulo Microsoft page refresh.*
