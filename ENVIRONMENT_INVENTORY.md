# ENVIRONMENT_INVENTORY.md — Complete Build & Runtime Environment Census

**Traceability ID:** `ENV-2026-11-22-001`  
**Parent Audit:** `INITIAL_AUDIT.md` (`AUDIT-2026-11-22-001`)

---

## 1. Host Environment

```
lscpu output (2026-11-22):

Architecture:              x86_64
CPU op-mode(s):            32-bit, 64-bit
Address sizes:             46 bits physical, 48 bits virtual
Byte Order:                Little Endian
CPU(s):                    2
Vendor ID:                 GenuineIntel
Model name:                Intel(R) Xeon(R) Processor @ 2.60GHz
CPU family:                6
Model:                     106
Thread(s) per core:        2
Core(s) per socket:        1
Socket(s):                 1
Hypervisor vendor:         KVM
Virtualization type:       full
Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36
       clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc
       rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq
       ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes
       xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault
       invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1
       hle avx2 smep bmi2 erms invpcid rtm avx512f avx512dq rdseed adx smap
       avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec
       xgetbv1 xsaves arat avx512vbmi umip avx512_vbmi2 gfni vaes vpclmulqdq
       avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid fsrm md_clear arch_capabilities

MemTotal: 4034452 kB
MemFree:  3863960 kB
```

- OS: Debian 12 bookworm (`PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"`)
- E2B sandbox: `iruwctpj94q0ohdxmj6c7` — ephemeral, no persistence guarantee beyond git push
- Filesystem: container overlay, `/home/user` persisted only via git

## 2. Compiler Toolchain

| Binary | Path | Version | Notes |
|--------|------|---------|-------|
| gcc | /usr/bin/gcc | 12.2.0 | default PIE, supports x86_64 UEFI `-mno-red-zone -fno-stack-protector` |
| g++ | /usr/bin/g++ | 12.2.0 | |
| ld | /usr/bin/ld | GNU ld 2.40 | supports PE32+ via `x86_64-pe` emulation with objcopy |
| objcopy | /usr/bin/objcopy | 2.40 | required for `elf -> efi` conversion (`objcopy -j .text ... --target=efi-app-x86_64`) |
| objdump | /usr/bin/objdump | 2.40 | inspection |
| make | /usr/bin/make | GNU Make | |
| nasm | NOT FOUND | — | `apt install nasm` needed for assembly stubs |
| clang | NOT FOUND | — | `apt install clang lld` recommended for EDK2 |
| rustc/cargo | NOT FOUND | — | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| python3 | /usr/bin/python3 | 3.11.2 | evidence scripts, validators |
| pip | /usr/bin/pip | — | |
| git/gh | /usr/bin/git, /usr/local/bin/gh | 2.39.5 / 2.23.0 | |

## 3. UEFI & Firmware Build Dependencies

| Package | Installed | Purpose | Install Command |
|---------|-----------|---------|-----------------|
| gnu-efi | no | headers + crt0 for standalone EFI app | `apt install gnu-efi` |
| libgnuefi-dev | no | libgnuefi.a | `apt install gnu-efi` |
| edk2 (edk2-source) | no | Full UEFI devkit alternative | clone https://github.com/tianocore/edk2 |
| ovmf | no | UEFI firmware for QEMU | `apt install ovmf` |
| qemu-system-x86_64 | no | Emulator testing | `apt install qemu-system-x86` |
| sbsigntools | no | Secure Boot signing test | `apt install sbsigntool` (future) |

**Verified absent:** `dpkg -l | grep -i efi` and `grep -i edk` returned empty.

**Why not installed now:** Per Phase 0 acceptance criteria, no speculative bootloader has been written. Installing toolchain now is permitted but not required until Phase 6 approval. This inventory documents gap without masking it.

## 4. Reproducible Build Prerequisites (Planned)

For Phase 6, builds will be reproducible via:

- Pinned Docker image: `debian:bookworm-slim` + explicit apt package versions
- `scripts/build/build.sh` invoking `make -C platform/uefi-probe` with `SOURCE_DATE_EPOCH`
- Hash verification: `sha256sum build/*.efi > evidence/build-logs/<build-id>.sha256`
- Verification script: `tooling/build-verifier/verify.py` checking hash vs `source-register.json`

## 5. Evidence Storage

```
evidence/
  source-register/     # JSONL of every external artifact (URL, hash, date, signature)
  build-logs/          # stdout/stderr of each build, with traceable build ID
  hardware-logs/       # QEMU + physical PC diagnostic reports (JSON + human-readable)
  test-results/        # unit/integration/emulation/physical (separated per spec)
  milestone-reports/   # FEASIBILITY_FINAL_REVIEW.md etc.
```

Conventions:

- All evidence files contain header line: `Evidence ID: EVID-...` + `Generated: ISO8601` + `Generator: <tool> <version>` + `Git commit: <sha>`
- No binary blobs in Git beyond `releases/verification` signed hashes; binaries stored externally per `LICENSE-REVIEW.md`

## 6. What Can Begin Immediately (Without Additional Installs)

- ✅ Markdown research (Phase 1–5) — fully supported
- ✅ Python validators, JSON schema tooling, compatibility-database
- ✅ GH workflows (CI lint)
- ⛔ UEFI compilation — requires gnu-efi
- ⛔ QEMU boot test — requires qemu + OVMF
- ⛔ Rust evaluation — requires rustup

## 7. Next Steps

1. Owner approves Phase 1 research scope.
2. Upon Phase 5 approval for Phase 6, agent will request toolchain install authorization (or owner pre-approves here).
3. Agent will then provide `scripts/build/setup-toolchain.sh` with pinned versions for reproducibility audit.

---

**Verified by:** Verification Agent — tool output captured verbatim from `bash` audit commands.
