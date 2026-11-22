# ENGINEERING_RULES.md — Non-Negotiable Engineering Norms

**Traceability:** `RULES-2026-11-22-001`  
**Authority:** `PROJECT_CHARTER.md` §7

Violation of these rules is a charter-level defect, not a style nit. Any agent (including the primary) that breaks them must be flagged by the Security Reviewer or Verification Agent and the work reverted.

---

## 1. Truthfulness & Evidence

1.1 **Never fabricate test results.** Every `PASS/FAIL` must have a log file in `evidence/test-results/` or `evidence/hardware-logs/` with timestamp, environment, and commit SHA.  
1.2 **Never claim hardware compatibility without testing.** Default state is `NOT TESTED` or `UNKNOWN`. Green check requires physical `TESTED — PASS` evidence.  
1.3 **Never combine emulator and physical results.** `tests/emulation/` and `tests/physical/` remain separate; any merged table is rejected.  
1.4 **CPU architecture ≠ platform compatibility.** The fact that Xbox Series X and PCs share x86-64 does not imply boot compatibility. Any such inference must be explicitly refuted in documentation.  
1.5 **All external claims must be cited.** Every `research/*.md` finding requires Source, Publication Date, Confidence (`Verified`/`Publicly documented`/`Inferred`/`Unknown`), and PC Compatibility Implications. Unsourced assertions are defects.  
1.6 **Independent verification is real inspection.** A reviewer must open artifacts, hashes, and logs — not rubber-stamp.

## 2. Security & Legal Boundaries

2.1 **Do not defeat retail security.** No bypassing Secure Boot, no glitching, no extracting fused keys, no forging signatures. If genuine boot requires Xbox-only trust anchor, record as blocker.  
2.2 **Do not extract or request protected signing keys.** Asking for Xbox retail signing keys (or attempting to derive them) is forbidden.  
2.3 **Do not publish proprietary binaries.** Only hashes, metadata, and provenance in Git. Binaries remain in Microsoft-controlled distribution points; local copies (if any) are gitignored and never pushed.  
2.4 **Do not seek leaked artifacts.** Game dumps, decrypted OS images, leaked GDKX — out of scope. Only official Microsoft distribution channels (OSDU recovery, documented GDK, authorized dev programs).  
2.5 **Preserve security integrity in test reports.** Any claim of "retail signatures verified" requires actual signature verification tool output, not assertion.

## 3. Repository & Change Management

3.1 **Inspect before modifying.** Before any significant change: `git status`, `git diff`, `git log -1`, baseline commit recorded in PR description.  
3.2 **Never modify unrelated repositories.** Verified scope is `/home/user/XboxPC` only. PC5 project preservation is confirmed (not present, no overwrite).  
3.3 **Isolated branches.** Implementation uses feature branches from `main` or `arena/*`; direct commits to `main` are discouraged after Phase 0.  
3.4 **Preserve evidence.** Never force-push to erase prior milestone reports, never delete `evidence/` history. `git revert` over history rewrite.  
3.5 **Reproducible builds.** `scripts/build/build.sh` must be runnable by Verification Agent to produce bit-identical EFI hash given same pinned toolchain and `SOURCE_DATE_EPOCH`.  
3.6 **No speculative bootloader in Phase 0.** Verified — none created. Future boot code requires Phase 6 authorization.

## 4. Development Conduct

4.1 **Evaluate before implementing.** Rust vs C choice for Phase 6 requires ADR with criteria (UEFI maturity, maintainability, hardware access). No custom kernel without demonstrated need.  
4.2 **Handle missing devices safely.** Diagnostic modules must tolerate absent GPU/NVMe/USB without crash or destructive write.  
4.3 **No automatic destructive actions.** Boot environment must not format disks, modify partitions, or flash firmware — enforced by code review and test.  
4.4 **No hardware purchase without owner approval.** All procurement deferred to Phase 5 gate.

## 5. Testing & Gate Discipline

5.1 **Phase gates are mandatory.** 0→1→2→3→4→5(approval)→6→7→8. Skipping is a violation.  
5.2 **Acceptance criteria are literal.** If spec says "Every node marked Verified/Publicly documented/Authorized access required/Unknown/Not available on standard PC," the graph must contain exactly those classifications.  
5.3 **Failed tests are preserved.** Do not delete red evidence; log and link to `BLOCKERS.md` / `RISK_REGISTER.md`.

## 6. Enforcement

- **Who enforces:** Security Research Reviewer (rules 2.x) and Verification Agent (rules 1.x, 3.x, 5.x).  
- **How:** PR checklist referencing this file; any PR that touches security or test claims requires reviewer sign-off with artifact inspection.  
- **Consequence:** Work violating these rules is reverted; milestone not counted.

---

*These rules derive from the Project Definition §3 category separation and Part IV §2 General Execution Policy. Amendments require ADR + owner approval.*
