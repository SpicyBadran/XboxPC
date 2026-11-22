# Tooling

Independent tools that support verification:

- `hardware-report/` — Human + JSON report generator for `platform/*`
- `evidence-validator/` — Validates `evidence/source-register/*.json` against schema (hash presence, source URL, signature status)
- `build-verifier/` — Checks reproducible build hashes
- `compatibility-database/` — JSON schema + CLI queries for `hardware-compatibility.json`

Each tool has its own `README.md` + tests. No untested one-off scripts.

Placeholder Phase 0.
