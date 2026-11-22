# References — Bibliography & Source Register Index

**Traceability:** `REF-2026-11-22-001`

This directory tracks *about* sources; actual hash+signature entries live in `evidence/source-register/`.

## Authoritative Sources (To Verify Phase 1)

| Source | URL / Document | Relevance | Retrieval Plan |
|--------|---------------|-----------|----------------|
| Microsoft Xbox Series X tech reveal (Wired, Eurogamer/DF, HotChips 2020) | HotChips 2020 slides / AnandTech/DF summary | Official SoC architecture | Phase 1 web_search + fetch_page |
| AMD Zen 2 microarchitecture | AMD docs + HotChips talks | CPU core topology | Phase 1 |
| AMD RDNA 2 architecture | AMD RDNA 2 whitepaper | GPU CU/RT | Phase 1 |
| Microsoft GDK documentation | https://learn.microsoft.com/en-us/gaming/gdk/ | Dev interfaces, what GDK exposes vs GDKX | Phase 2 |
| Xbox Offline System Update portal | https://support.xbox.com/help/hardware-network/offline-system-update | Recovery image distribution | Phase 2 artifact provenance |
| UEFI Specification 2.10 | https://uefi.org/specifications | Phase 6 diagnostic build | Phase 6 |
| ACPI 6.5, PCI Express, NVMe 2.0 specs | uefi.org / pcisig.com / nvmexpress.org | Platform inventories | Phase 6 |

## Evidence Protocol

For every acquired artifact:

```json
{
  "evidence_id": "EVID-2026-11-22-001",
  "source_url": "https://...",
  "retrieval_date": "2026-11-22",
  "file_name": "XBOX_OSU1_...zip",
  "sha256": "...",
  "signature_verified": false,
  "version": "...",
  "license_or_access": "public / requires_dev_account",
  "notes": ""
}
```

*Placeholder Phase 0 — populated as research proceeds.*
