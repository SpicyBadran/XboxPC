#!/usr/bin/env python3
"""
Verify README dashboard matches docs/architecture/roadmap.json single source of truth.
CI check: fails if README out-of-date vs roadmap.json or assets missing/stale.
Usage: python scripts/verify-dashboard.py [--fix]
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent.parent
ROADMAP = ROOT / "docs/architecture/roadmap.json"
README = ROOT / "README.md"
ASSETS = ROOT / "docs/architecture/assets"

def load_roadmap():
    with open(ROADMAP, encoding="utf-8") as f:
        return json.load(f)

def compute_metrics(data):
    total = sum(len(ws["milestones"]) for ws in data["workstreams"])
    completed = sum(1 for ws in data["workstreams"] for m in ws["milestones"] if m["status"] == "completed")
    blocked = sum(1 for ws in data["workstreams"] for m in ws["milestones"] if m["status"] == "blocked")
    genuine_ws = [ws for ws in data["workstreams"] if ws["id"] in ("WS7", "WS8")]
    genuine_total = sum(len(ws["milestones"]) for ws in genuine_ws)
    genuine_completed = sum(1 for ws in genuine_ws for m in ws["milestones"] if m["status"] == "completed")
    overall_pct = round(100*completed/total, 1) if total else 0
    genuine_pct = round(100*genuine_completed/genuine_total, 1) if genuine_total else 0
    return {
        "total": total,
        "completed": completed,
        "blocked": blocked,
        "overall_pct": overall_pct,
        "genuine_total": genuine_total,
        "genuine_completed": genuine_completed,
        "genuine_pct": genuine_pct,
    }

def check_readme(metrics):
    text = README.read_text(encoding="utf-8")
    errors = []
    # Check dashboard markers exist
    if "<!-- DASHBOARD:START" not in text:
        errors.append("README missing <!-- DASHBOARD:START --> marker")
    if "<!-- DASHBOARD:END -->" not in text:
        errors.append("README missing <!-- DASHBOARD:END --> marker")
    # Check key metrics appear
    checks = [
        (f"{metrics['completed']}/{metrics['total']}", "overall milestone count"),
        (f"{metrics['genuine_completed']}/{metrics['genuine_total']}", "genuine readiness count"),
        (str(metrics['overall_pct']), "overall percentage"),
    ]
    for needle, desc in checks:
        if needle not in text:
            errors.append(f"README missing {desc} '{needle}' — run python docs/architecture/generate-dashboard.py")
    # Check assets exist
    required = ["header.png", "treemap-overall.png"] + [f"ws-{ws.lower()}.png" for ws in ["WS1","WS2","WS3","WS4","WS5","WS6","WS7","WS8"]]
    for asset in required:
        p = ASSETS / asset
        if not p.exists():
            errors.append(f"Missing asset {p} — run python docs/architecture/generate-dashboard.py")
        elif p.stat().st_mtime < ROADMAP.stat().st_mtime:
            errors.append(f"Stale asset {p} (older than roadmap.json) — regenerate")
    # Check roadmap links
    if "docs/architecture/roadmap.json" not in text:
        errors.append("README should link to docs/architecture/roadmap.json single source")
    if "REVIEW_INDEX.md" not in text:
        errors.append("README should link to REVIEW_INDEX.md")
    return errors

def main():
    if not ROADMAP.exists():
        print(f"❌ {ROADMAP} not found", file=sys.stderr)
        sys.exit(2)
    if not README.exists():
        print(f"❌ {README} not found", file=sys.stderr)
        sys.exit(2)
    data = load_roadmap()
    metrics = compute_metrics(data)
    print(f"Roadmap: {metrics['completed']}/{metrics['total']} ({metrics['overall_pct']}%) overall, genuine {metrics['genuine_completed']}/{metrics['genuine_total']} ({metrics['genuine_pct']}%)")
    errors = check_readme(metrics)
    if errors:
        print("❌ Dashboard verification FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print("\nFix: python docs/architecture/generate-dashboard.py", file=sys.stderr)
        sys.exit(1)
    print("✅ Dashboard verified — README matches roadmap.json and assets present")
    sys.exit(0)

if __name__ == "__main__":
    main()
