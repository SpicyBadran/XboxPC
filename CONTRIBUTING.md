# CONTRIBUTING.md — How to Contribute (Humans & Agents)

## Workflow

1. Inspect baseline (`git status`, `INITIAL_AUDIT.md`).
2. Create feature branch: `git checkout -b arena/<phase>-<slug>`.
3. Implement with traceable evidence IDs.
4. Run applicable tests (`scripts/test/run-unit.sh`); capture logs.
5. Open PR: `gh pr create --title "..." --body "Baseline: <sha>"`.
6. Require review from appropriate role (Security Reviewer for security claims, Verification for test claims).
7. Owner merges via `gh pr merge <number> --merge` as last command in chain.

## Phase Gates

See `PROJECT_CHARTER.md` §6 — do not skip. Each phase PR must include 15-point report.

## Evidence

All new facts need source + date + confidence. See `ENGINEERING_RULES.md`.

## No-Go

- No proprietary binaries in Git.
- No hardware purchase without owner.
- No emulator→physical conflation.

