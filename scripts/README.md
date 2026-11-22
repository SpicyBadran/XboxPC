# Scripts — Reproducible Build & Verify

| Script | Purpose |
|--------|---------|
| `build/setup-toolchain.sh` | Pin toolchain versions, install gnu-efi/ovmf/qemu |
| `build/build.sh` | Reproducible EFI build (`SOURCE_DATE_EPOCH`) |
| `build/verify.sh` | Check build output hashes |
| `test/run-unit.sh` | Host unit tests |
| `test/run-emulation.sh` | QEMU+OVMF smoke boot |
| `verify/verify-evidence.sh` | Validate `evidence/source-register` + hashes |

All scripts are non-destructive, no partition edits. Placeholder Phase 0 — implemented Phase 6.
