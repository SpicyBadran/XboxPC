# SECURITY.md — XboxPC Security Model & Handling Policy

**Traceability:** `SEC-2026-11-22-001`

---

## 1. Purpose

This project preserves the genuine retail security model while investigating its boot chain. We do not break it.

## 2. Retail Security Properties We Preserve

- **Hardware root of trust:** On-SoC Boot ROM + fused keys establish trust anchor. We will not attempt to replicate or extract fusing.
- **Secure Boot:** Each stage authenticates next via retail signatures. We will not bypass, forge, or disable signature checks to simulate boot.
- **Security processor / Pluton heritage:** Xbox Series X contains custom security subsystem (see `research/xbox-security/`). Its services (attestation, memory encryption, device identity) are unavailable on PC — this is a documented blocker, not a bypass opportunity.
- **Memory/storage protection:** Hypervisor-reserved regions, encrypted storage virtualization — we document, not defeat.

## 3. Prohibitions

| Prohibited Action | Consequence |
|-------------------|-------------|
| Extracting Xbox signing keys (any method) | Immediate revert, charter violation |
| Glitching/faulting retail hardware to bypass auth | Out of scope, not attempted |
| Decrypting retail OS images without authorized path | Forbidden |
| Publishing proprietary binaries, decrypted images, or leaked SDKs | Legal + charter violation |
| Claiming "retail signatures verified" without tool output | Rejected by Verification Agent |

## 4. What We Do Instead

- Map each boot stage → authentication requirement → PC availability (`Not available on standard PC` where applicable).
- Record missing authorization (e.g., "Requires Microsoft cooperation: retail trust anchor not distributable").
- Use only official distribution paths (see `LICENSE-REVIEW.md`).

## 5. Sensitive Data Handling

- No secrets in Git. If test Secure Boot keys are generated for diagnostic builds, they are self-signed test keys clearly labeled `TEST-ONLY` and never presented as retail.
- `evidence/source-register/` stores hashes/signatures/Metadata, never plaintext secrets.

## 6. Review

Every security-relevant document (`BOOT_CHAIN.md`, `SECURITY_MODEL.md`, `TRUST_REQUIREMENTS.md`, `ARTIFACT_PROVENANCE.md`) requires sign-off line:

```
Reviewed by Security Research Reviewer — <name/alias> — <date> — <commit> — verdict: APPROVED/REJECTED
```

---

*This policy implements Project Definition §3 category separation and Phase 3 security requirements.*
