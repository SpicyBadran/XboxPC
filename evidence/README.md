# Evidence — Traceable Artifact Store

| Subdir | Content | Convention |
|--------|---------|------------|
| `source-register/` | One JSON per external artifact (URL, hash, date, signature) | `EVID-YYYY-MM-DD-NNN.json` |
| `build-logs/` | Build stdout/stderr + sha256 | `BUILD-YYYYMMDD-<sha>.log` + `.sha256` |
| `hardware-logs/` | Diagnostic dumps (JSON+hreadable) | `HWLOG-<machine>-<ts>.json` |
| `test-results/` | TAP/JUnit per environment | `test-<env>-<ts>.xml` |
| `milestone-reports/` | Phase gate reports | `FEASIBILITY_FINAL_REVIEW.md` etc. |

**Every file header must contain:** `Evidence ID` + `Generated` + `Generator` + `Git commit`.

No proprietary binaries in Git — hashes/metadata only (see `LICENSE-REVIEW.md`).
