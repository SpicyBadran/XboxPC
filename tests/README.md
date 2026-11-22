# Tests — Environment-Separated

| Directory | Tag | Runs On |
|-----------|-----|---------|
| `unit/` | `unit` | Host (no firmware) |
| `integration/` | `integration` | Host |
| `emulation/` | `emulation` | QEMU + OVMF |
| `physical/` | `physical` | Real PC USB boot |

**Never merge emulator and physical results.** Each test result carries environment tag + commit SHA + timestamp + log path.

Placeholder Phase 0 — test plans live in `docs/` post-Phase 6.
