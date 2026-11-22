#!/usr/bin/env python3
"""
Generate XboxPC project dashboard from roadmap.json — single source of truth.
Creates treemap-style PNG visualizations and updates README.md between markers.
Usage: python docs/architecture/generate-dashboard.py
"""
import json
import pathlib
import math

ROOT = pathlib.Path(__file__).parent.parent.parent  # repo root
ROADMAP = pathlib.Path(__file__).parent / "roadmap.json"
ASSETS = pathlib.Path(__file__).parent / "assets"
README = ROOT / "README.md"

# Colors — Xbox-inspired dark technical
COLORS = {
    "bg": "#0d1117",
    "panel": "#161b22",
    "border": "#30363d",
    "completed": "#238636",      # green
    "completed_alt": "#2ea043",
    "documented": "#1f6feb",     # blue for documented/research
    "in_progress": "#1f6feb",
    "blocked": "#f85149",        # red for blocked (honest)
    "blocked_dim": "#da3633",
    "planned": "#484f58",        # grey
    "unknown": "#6e7681",
    "text": "#c9d1d9",
    "text_dim": "#8b949e",
    "accent": "#107c10",         # Xbox green
    "xbox": "#107c10",
    "warning": "#d29922",
}

STATUS_COLOR = {
    "completed": COLORS["completed"],
    "in_progress": COLORS["in_progress"],
    "blocked": COLORS["blocked"],
    "planned": COLORS["planned"],
}

EVIDENCE_COLOR = {
    "VERIFIED": COLORS["completed"],
    "DOCUMENTED": COLORS["documented"],
    "RESEARCHED": "#8957e5",
    "INFERRED": "#d29922",
    "UNKNOWN": COLORS["unknown"],
}

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("Pillow not installed — run pip install Pillow")

def load_roadmap():
    with open(ROADMAP, encoding="utf-8") as f:
        data = json.load(f)
    return data

def compute_metrics(data):
    total = 0
    completed = 0
    blocked = 0
    planned = 0
    in_progress = 0
    ws_metrics = []
    for ws in data["workstreams"]:
        ms = ws["milestones"]
        n = len(ms)
        c = sum(1 for m in ms if m["status"] == "completed")
        b = sum(1 for m in ms if m["status"] == "blocked")
        p = sum(1 for m in ms if m["status"] == "planned")
        ip = sum(1 for m in ms if m["status"] == "in_progress")
        total += n
        completed += c
        blocked += b
        planned += p
        in_progress += ip
        ws_metrics.append({
            "id": ws["id"],
            "name": ws["name"],
            "n": n,
            "completed": c,
            "blocked": b,
            "planned": p,
            "in_progress": ip,
            "pct": round(100*c/n, 1) if n else 0,
            "color": ws.get("color", COLORS["accent"])
        })
    # genuine readiness: W7 + W8
    genuine_ws = [ws for ws in data["workstreams"] if ws["id"] in ("WS7", "WS8")]
    genuine_total = sum(len(ws["milestones"]) for ws in genuine_ws)
    genuine_completed = sum(1 for ws in genuine_ws for m in ws["milestones"] if m["status"] == "completed")
    genuine_pct = round(100*genuine_completed/genuine_total, 1) if genuine_total else 0
    overall_pct = round(100*completed/total, 1) if total else 0
    # summary block already in json but recompute for safety
    return {
        "total": total,
        "completed": completed,
        "blocked": blocked,
        "planned": planned,
        "in_progress": in_progress,
        "overall_pct": overall_pct,
        "genuine_total": genuine_total,
        "genuine_completed": genuine_completed,
        "genuine_pct": genuine_pct,
        "ws_metrics": ws_metrics,
    }

def draw_treemap_grid(metrics, out_path, title=None, cell_size=14, gap=2):
    """Draw simple grid treemap: each milestone = one square, colored by status."""
    if not HAS_PIL:
        return
    # For overall, we draw workstreams as groups of cells sized by n
    # Simpler: grid per workstream
    cols = 8
    n = metrics["total"] if "total" in metrics else sum(m["n"] for m in metrics["ws_metrics"])
    # overall image size
    width = 900
    height = 180
    img = Image.new("RGB", (width, height), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    # title
    try:
        font_small = ImageFont.load_default()
        font_bold = ImageFont.load_default()
    except:
        font_small = ImageFont.load_default()
        font_bold = font_small
    if title:
        draw.text((10, 8), title, fill=COLORS["text"], font=font_small)
    x0, y0 = 10, 30
    # layout workstreams horizontally, each as block of cells
    total = metrics["total"]
    x = x0
    for ws in metrics["ws_metrics"]:
        # block width proportional to n
        block_w = int((ws["n"] / total) * (width - 20)) - gap
        block_h = 120
        # background panel
        draw.rounded_rectangle([x, y0, x+block_w, y0+block_h], radius=6, fill=COLORS["panel"], outline=COLORS["border"])
        # header
        draw.text((x+6, y0+6), ws["name"].split(" ")[0][:12], fill=COLORS["text_dim"], font=font_small)
        draw.text((x+6, y0+18), f"{ws['completed']}/{ws['n']} {ws['pct']}%", fill=COLORS["text"], font=font_small)
        # grid cells inside
        cx, cy = x+6, y0+36
        cell = 14
        cols_in_block = max(1, (block_w - 12) // (cell+gap))
        for idx in range(ws["n"]):
            # find milestone status: we need to map idx to status order completed, in_progress, blocked, planned
            # approximate: first completed green, then in_progress blue, then blocked red, then planned grey
            if idx < ws["completed"]:
                col = COLORS["completed"]
            elif idx < ws["completed"] + ws["in_progress"]:
                col = COLORS["in_progress"]
            elif idx < ws["completed"] + ws["in_progress"] + ws["blocked"]:
                col = COLORS["blocked"]
            else:
                col = COLORS["planned"]
            r = idx % cols_in_block
            c = idx // cols_in_block
            px = cx + r*(cell+gap)
            py = cy + c*(cell+gap)
            if px + cell > x+block_w -6 or py+cell > y0+block_h -6:
                continue
            draw.rounded_rectangle([px, py, px+cell, py+cell], radius=2, fill=col)
        x += block_w + gap + 4
    img.save(out_path)
    print(f"saved {out_path}")

def draw_workstream_detail(ws, out_path):
    if not HAS_PIL:
        return
    n = len(ws["milestones"])
    cols = 6
    rows = math.ceil(n / cols)
    cell = 36
    gap = 6
    pad = 16
    header_h = 50
    width = cols * (cell+gap) + pad*2
    height = header_h + rows * (cell+gap) + pad
    img = Image.new("RGB", (width, height), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    try:
        font_small = ImageFont.load_default()
        font_bold = ImageFont.load_default()
    except:
        font_small = ImageFont.load_default()
        font_bold = font_small
    # header
    draw.text((pad, 10), ws["name"], fill=COLORS["text"], font=font_bold)
    draw.text((pad, 24), f"{ws['id']} — {len(ws['milestones'])} milestones", fill=COLORS["text_dim"], font=font_small)
    # status summary
    completed = sum(1 for m in ws["milestones"] if m["status"]=="completed")
    pct = round(100*completed/n) if n else 0
    draw.text((width - 80, 10), f"{completed}/{n} {pct}%", fill=COLORS["text"], font=font_small)
    y0 = header_h
    for i, m in enumerate(ws["milestones"]):
        r = i % cols
        c = i // cols
        x = pad + r*(cell+gap)
        y = y0 + c*(cell+gap)
        col = STATUS_COLOR.get(m["status"], COLORS["planned"])
        draw.rounded_rectangle([x, y, x+cell, y+cell], radius=4, fill=col, outline=COLORS["border"])
        # milestone id centered
        tid = m["id"].split("-")[1] if "-" in m["id"] else m["id"][:3]
        # center text
        # Use small font, approximate centering
        draw.text((x+6, y+12), tid, fill="white", font=font_small)
        # evidence dot border color
        evc = EVIDENCE_COLOR.get(m["evidenceClass"], COLORS["unknown"])
        draw.rectangle([x, y+cell-4, x+cell, y+cell], fill=evc)
    img.save(out_path)
    print(f"saved {out_path}")

def draw_header_banner(metrics, out_path):
    if not HAS_PIL:
        return
    width, height = 1100, 160
    img = Image.new("RGB", (width, height), COLORS["bg"])
    draw = ImageDraw.Draw(img)
    try:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_bold = ImageFont.load_default()
    except:
        font_large = ImageFont.load_default()
        font_small = font_large
        font_bold = font_large
    # Xbox green accent bar top
    draw.rectangle([0, 0, width, 4], fill=COLORS["xbox"])
    # Project title
    draw.text((20, 14), "XboxPC", fill="white", font=font_large)
    draw.text((120, 18), "Genuine Xbox Series X Retail OS on Standard PC Hardware", fill=COLORS["text_dim"], font=font_small)
    # Destination line
    dest = "Destination: Genuine, unmodified retail OS booting directly on non-Xbox x86-64 PC — no host OS, emulator, or security bypass."
    draw.text((20, 42), dest[:110], fill=COLORS["text"], font=font_small)
    # Metrics boxes
    boxes = [
        (f"Overall", f"{metrics['completed']}/{metrics['total']}  {metrics['overall_pct']}%", COLORS["completed"] if metrics['overall_pct']>40 else COLORS["planned"]),
        (f"Genuine readiness", f"{metrics['genuine_completed']}/{metrics['genuine_total']}  {metrics['genuine_pct']}%", COLORS["blocked"] if metrics['genuine_pct']==0 else COLORS["completed"]),
        (f"Blocked", f"{metrics['blocked']} milestones", COLORS["blocked"]),
        (f"Next", f"W2-M4 → W7-M1  Inquiry", COLORS["documented"]),
    ]
    x = 20
    y = 70
    bw, bh = 240, 70
    gap = 16
    for title, value, col in boxes:
        draw.rounded_rectangle([x, y, x+bw, y+bh], radius=6, fill=COLORS["panel"], outline=COLORS["border"])
        draw.rectangle([x, y, x+bw, y+4], fill=col)
        draw.text((x+10, y+12), title, fill=COLORS["text_dim"], font=font_small)
        draw.text((x+10, y+32), value, fill="white", font=font_bold)
        x += bw + gap
    # footer hint
    draw.text((20, 148), "Single source: docs/architecture/roadmap.json  •  Run python docs/architecture/generate-dashboard.py after milestone change", fill=COLORS["text_dim"], font=font_small)
    img.save(out_path)
    print(f"saved {out_path}")

def render_readme(data, metrics):
    """Generate dashboard markdown between markers, preserve other content outside markers."""
    # Build dashboard section
    ws = data["workstreams"]
    # Build milestone table rows
    milestone_rows = []
    for w in ws:
        for m in w["milestones"]:
            status_icon = {
                "completed": "✅",
                "in_progress": "🔵",
                "blocked": "🔴",
                "planned": "⬜",
            }.get(m["status"], "⬜")
            ev = m["evidenceClass"]
            milestone_rows.append(f"| `{m['id']}` | {m['title']} | {w['name'].split(' ')[0]} | {status_icon} {m['status']} | `{ev}` | {m['completionCriteria'][:70]}... |")
    # Workstream summary table
    ws_rows = []
    for w in ws:
        m = next(x for x in metrics["ws_metrics"] if x["id"]==w["id"])
        bar = "█" * int(m["pct"]/10) + "░" * (10 - int(m["pct"]/10))
        ws_rows.append(f"| {w['id']} | {w['name']} | {m['completed']}/{m['n']} | {m['pct']}% | `{bar}` |")
    # Blockers list
    blockers = data["summary"]["majorBlockers"]
    blocker_md = "\n".join(f"- 🔴 **{b}**" for b in blockers)
    # Evidence legend
    dashboard_md = f"""
<!-- DASHBOARD:START — generated from docs/architecture/roadmap.json do not edit manually — run python docs/architecture/generate-dashboard.py -->

<div align="center">

### 🎯 Destination
**Genuine, unmodified Xbox Series X retail OS booting directly on non-Xbox x86-64 PC hardware, without a host OS, emulator, or security bypass.**

*Research progress ≠ execution readiness — see separate metrics below.*

</div>

![Header](docs/architecture/assets/header.png)

**Overall:** `{metrics['completed']}/{metrics['total']} milestones` **{metrics['overall_pct']}%** • **Genuine execution readiness:** `{metrics['genuine_completed']}/{metrics['genuine_total']} milestones` **{metrics['genuine_pct']}%** • **Blocked:** `{metrics['blocked']} milestones` • **Next:** `W2-M4 → W7-M1` *Owner sends Microsoft inquiry*

![Overall treemap](docs/architecture/assets/treemap-overall.png)

---

### Workstreams — 8 parallel tracks to genuine execution

| ID | Workstream | Done | Progress | Bar |
|---|------------|------|----------|-----|
{chr(10).join(ws_rows)}

*Each square in treemap = one milestone (green completed, blue in-progress, red blocked, grey planned). Milestones only complete when evidence criteria satisfied.*

| Workstream | Treemap |
|------------|---------|
"""
    for w in ws:
        dashboard_md += f"| **{w['name']}** | ![{w['id']}](docs/architecture/assets/ws-{w['id'].lower()}.png) |\n"

    dashboard_md += f"""
---

### Evidence discipline — five levels, honest blockers

| Class | Meaning | Example |
|-------|---------|---------|
| `VERIFIED` | Independently reproducible (Hot Chips pdf, GitHub API 348416224, fetch_page) | SoC 360.4mm²/15.3B/16GB GDDR6 |
| `DOCUMENTED` | Published Microsoft docs quoted (access-resources “recoveries of the GDK”) | GDKX Secure scope, MS rep required |
| `RESEARCHED` | ≥2 independent secondary sources (GBAtemp/futuretweets) | OSU1 $SystemUpdate layout |
| `INFERRED` | Reasonable engineering inference from verified topology | CPUID allowlist maybe, memory window fault |
| `UNKNOWN` | No public evidence — explicitly marked | Xbox CA thumbprint, ACPI dump, full Secure inventory |

- **Implementation / Build / Test / Emulation / Physical** are separate — never combine.
- `STAGED_DIFF_FOR_REVIEW.diff` is exact `git diff --cached` for substantive review.
- Review: [`REVIEW_INDEX.md`](REVIEW_INDEX.md) • Live research: [`research/xbox-os/`](research/xbox-os/)

---

### Milestones — 24 total, {metrics['completed']} completed, {metrics['in_progress']} in-progress, {metrics['blocked']} blocked, {metrics['planned']} planned

| ID | Title | WS | Status | Evidence | Completion criteria (truncated) |
|---|-------|----|--------|----------|---------------------------------|
{chr(10).join(milestone_rows)}

*Full criteria, dependencies, evidence refs: `docs/architecture/roadmap.json` — single source of truth.*

---

### Major blockers — displayed honestly, not hidden

{blocker_md}

- **Destination requires W7-M1→W7-M2 + W6-M4 + W5-M2 — all blocked.** Research 45.8% ≠ readiness 0.0%.

---

### Current milestone, next action, destination readiness

- **Current milestone:** `W2-M4` *Microsoft retail OS inquiry (unsent)* — DRAFT `INQUIRY-2026-11-22-001` with 6 verbatim questions, definitions table, routes A/B1-B4, O1-O5; external action blocked until owner authorizes.
- **Next actionable:** `NA-1` Owner sends inquiry via Route A (account team) or B1 `ID@XBOX.com` after confirming contact identity — do NOT enroll Partner Center / accept NDA. Outcome O1 moves to CONDITIONALLY FEASIBLE; O2/O3 confirms boundary.
- **Independent work:** `W6` UEFI probe can proceed as **separate product** `PC-hardware-report` only after owner re-approves it separately — not Xbox PC evidence.
- **Dependent work:** `W7` genuine execution + `W8` physical validation blocked until Microsoft response + `W6-M4` physical logs.

| Metric | Value |
|--------|-------|
| **Overall milestone progress** | {metrics['completed']}/{metrics['total']} ({metrics['overall_pct']}%) |
| **Genuine Xbox OS execution readiness** | {metrics['genuine_completed']}/{metrics['genuine_total']} ({metrics['genuine_pct']}%) — separate |
| **Destination** | Genuine unmodified retail OS on standard PC — no host OS/emulator/bypass |

---

### How to keep dashboard honest — automatic maintenance

- **Source:** `docs/architecture/roadmap.json` — milestone IDs, workstream, status, dependencies, criteria, evidence, blockers, next actionable.
- **Regenerate:** `python docs/architecture/generate-dashboard.py` — updates metrics, PNGs in `docs/architecture/assets/`, and this README section between `<!-- DASHBOARD:START -->` / `<!-- DASHBOARD:END -->`.
- **Validate:** `python scripts/verify-dashboard.py` — CI check fails if README out-of-date vs roadmap.json.
- **Rule:** `AGENTS.md` §5 + PR checklist — never edit percentages in README manually; update `roadmap.json` when evidence changes.

<!-- DASHBOARD:END -->
"""
    return dashboard_md

def main():
    data = load_roadmap()
    metrics = compute_metrics(data)
    # update summary counts in json for consistency (optional, write back computed)
    # Generate assets
    ASSETS.mkdir(parents=True, exist_ok=True)
    if HAS_PIL:
        draw_header_banner(metrics, ASSETS / "header.png")
        draw_treemap_grid(metrics, ASSETS / "treemap-overall.png", title="Overall milestone treemap — 8 workstreams, each square = one milestone")
        for ws in data["workstreams"]:
            draw_workstream_detail(ws, ASSETS / f"ws-{ws['id'].lower()}.png")
    else:
        print("Skipping image generation — Pillow missing")
    # Update README between markers
    dashboard_md = render_readme(data, metrics)
    readme_text = README.read_text(encoding="utf-8")
    start = "<!-- DASHBOARD:START"
    end = "<!-- DASHBOARD:END -->"
    if start in readme_text and end in readme_text:
        before = readme_text.split(start)[0]
        after = readme_text.split(end)[1] if end in readme_text else ""
        new_readme = before + dashboard_md + after
        README.write_text(new_readme, encoding="utf-8")
        print(f"Updated {README}")
    else:
        # If no markers, append
        with open(README, "a", encoding="utf-8") as f:
            f.write("\n" + dashboard_md)
        print(f"Appended dashboard to {README}")
    # Print summary
    print(f"Metrics: {metrics['completed']}/{metrics['total']} overall {metrics['overall_pct']}% — genuine {metrics['genuine_completed']}/{metrics['genuine_total']} {metrics['genuine_pct']}%")

if __name__ == "__main__":
    main()
