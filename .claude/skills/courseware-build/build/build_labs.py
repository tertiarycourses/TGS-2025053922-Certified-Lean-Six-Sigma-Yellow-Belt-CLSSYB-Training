#!/usr/bin/env python3
"""Generate labs/lab-NN-*.md + labs/README.md + labs/tools.md from the same
single source (course_data + data_domainN) that drives the PPT, LP and LG, so the
labs can never drift out of alignment with the rest of the courseware.
"""
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import csv as _csv
import shutil
import course_data as C
import lab_dataset as D
import lab_files as LF
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3

ACT = sorted(DOMAIN1 + DOMAIN2 + DOMAIN3, key=lambda a: a["num"])
TOPICS = {t["num"]: t for t in C.TOPICS}


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")

TOOLS = {
    "sipoc": ("SIPOC & Process Map Builder", "https://alfredang.github.io/sipoc/"),
    "5whys": ("5 Whys", "https://alfredang.github.io/5whys/"),
    "fishbone": ("Fishbone Diagram", "https://alfredang.github.io/fishbone/"),
    "pareto": ("Pareto Chart (collaborative)", "https://alfredang.github.io/paretochart/"),
    "novaspc": ("NovaSPC", "https://alfredang.github.io/novaspc/"),
}

REGISTER_URL = ("https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html")

SCENARIO = (
    "Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long "
    "to be assigned, that they must keep chasing for status, and that agents apply different definitions "
    "of what counts as \"resolved\". You are supporting the improvement team as a Yellow Belt."
)


DATA_BRIEF = (
    f"**The data.** Two weeks of ticket data have been collected: **{D.N} tickets**, of which "
    f"**{D.DEFECTIVE} contained at least one defect**, with **{D.TOTAL_DEFECTS} defects** recorded in "
    f"total across **{D.OPP} defect opportunities per ticket**. Mean assignment time is "
    f"**{D.MEAN_MIN} minutes** against a **{D.TARGET_MIN}-minute** improvement goal. "
    "The files in this lab's `data/` folder are that extract."
)


slug = LF.slug


def dirname(a):
    return LF.dirname(a["num"], a["title"])


def lab_md(a):
    kind = "Elective" if a.get("elective") else "Core"
    title = a["title"].replace("Elective — ", "")
    tp = TOPICS[a["topic"]]
    phase = tp["phase"]
    out = []
    out.append(f"# Lab {a['num']} — {title}")
    out.append("")
    out.append(f"**DMAIC phase:** {phase}  |  **Lab type:** {kind}  |  "
               f"**Course:** {C.TITLE} ({C.COURSE_CODE})")
    out.append("")
    if a.get("elective"):
        out.append("> **Elective lab.** Complete this lab if time allows during class, or afterwards as "
                   "additional practice. It extends the same Contoso Service Desk scenario used by the "
                   "core labs.")
        out.append("")
    out.append("## Objective")
    out.append("")
    out.append(a["objective"])
    out.append("")
    out.append("## Scenario")
    out.append("")
    out.append(SCENARIO)
    out.append("")
    out.append(DATA_BRIEF)
    out.append("")
    out.append("## What you will build")
    out.append("")
    out.append(a["build"])
    out.append("")
    out.append(f"**Tools and techniques:** {a['services']}")
    out.append("")
    data, tmpl, note = LF.files_for(a["num"])
    if data or tmpl:
        out.append("## Files in this lab folder")
        out.append("")
        if data:
            out.append("**`data/` — the mock data you analyse:**")
            out.append("")
            for name in sorted(data):
                rows = data[name]
                out.append(f"- [`data/{name}`](data/{name}) — {len(rows)-1} rows · "
                           f"columns: {', '.join(str(c) for c in rows[0])}")
            out.append("")
        if tmpl:
            out.append("**`templates/` — the worksheets you fill in:**")
            out.append("")
            for name in sorted(tmpl):
                rows = tmpl[name]
                out.append(f"- [`templates/{name}`](templates/{name}) — "
                           f"columns: {', '.join(str(c) for c in rows[0])}")
            out.append("")
        out.append("Open the CSV files in Excel, LibreOffice Calc or Google Sheets. "
                   "Work on a copy so the originals stay clean for revision.")
        out.append("")
        if note:
            out.append(f"> {note}")
            out.append("")
    # any tool URLs used by this lab
    used = []
    for _, cmd in a["steps"]:
        if cmd.startswith("http"):
            for key, (name, url) in TOOLS.items():
                if url == cmd and name not in [u[0] for u in used]:
                    used.append((name, url))
    if used:
        out.append("### Online tools used in this lab")
        out.append("")
        for name, url in used:
            out.append(f"- **{name}** — {url}")
        out.append("")
    out.append("## Steps")
    out.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        out.append(f"### Step {i}")
        out.append("")
        out.append(instr)
        if cmd:
            out.append("")
            if cmd.startswith("http"):
                out.append(f"Open the tool: <{cmd}>")
            else:
                out.append("```")
                out.append(cmd)
                out.append("```")
        out.append("")
    out.append("## Check your work")
    out.append("")
    out.append(a["test"])
    out.append("")
    out.append("## Deliverable")
    out.append("")
    out.append(f"Save your output — it forms part of your Contoso improvement package and is your "
               f"revision material for the assessment.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · "
               f"© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


def readme_md():
    out = []
    out.append(f"# Labs — {C.TITLE}")
    out.append("")
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    out.append("These labs follow the DMAIC roadmap end to end. Every lab builds on the same Contoso "
               "Service Desk scenario, so your outputs accumulate into one complete improvement package.")
    out.append("")
    out.append("## How each lab is organised")
    out.append("")
    out.append("Each lab is a self-contained folder:")
    out.append("")
    out.append("```")
    out.append("lab-NN-<name>/")
    out.append("  README.md     the lab worksheet - objective, steps and the check")
    out.append("  data/         the mock data you analyse (CSV - open in Excel or Sheets)")
    out.append("  templates/    blank worksheets you fill in (CSV)")
    out.append("```")
    out.append("")
    out.append(f"All the data describes one fortnight at the Contoso Service Desk: **{D.N} tickets**, "
               f"**{D.DEFECTIVE} defective**, **{D.TOTAL_DEFECTS} defects**, "
               f"**{D.OPP} opportunities per ticket** - yield **{D.YIELD*100:.0f}%**, DPU **{D.DPU:.2f}**, "
               f"DPMO **{int(D.DPMO):,}**, sigma level **~{D.SIGMA}**. These are the same figures used by "
               "the Case Study assessment, so your lab work is direct revision.")
    out.append("")
    out.append("The headline figures are in [scenario-key-figures.csv](scenario-key-figures.csv).")
    out.append("")
    out.append("## Lab types")
    out.append("")
    out.append("- **Core** — completed by everyone; maps directly to the assessment.")
    out.append("- **Elective** — additional practice with further Lean Six Sigma tools; run when time "
               "allows or after the course.")
    out.append("")
    out.append("## Lab index")
    out.append("")
    out.append("| # | Lab | DMAIC phase | Type |")
    out.append("|---|-----|-------------|------|")
    files = {}
    for a in ACT:
        fn = f"{dirname(a)}/README.md"
        files[a["num"]] = fn
        kind = "Elective" if a.get("elective") else "Core"
        title = a["title"].replace("Elective — ", "")
        out.append(f"| {a['num']} | [{title}]({fn}) | {TOPICS[a['topic']]['phase']} | {kind} |")
    out.append("")
    out.append("## The interactive toolkit")
    out.append("")
    out.append("See [tools.md](tools.md) for the browser-based problem-solving tools used in the labs.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out), files


def tools_md():
    out = []
    out.append("# Lean Six Sigma Toolkit")
    out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE}*")
    out.append("")
    out.append("## Interactive online tools")
    out.append("")
    out.append("These browser-based tools are used during the labs. No installation or licence needed.")
    out.append("")
    out.append("| Tool | What it does | Used in |")
    out.append("|------|--------------|---------|")
    out.append("| [SIPOC & Process Map](https://alfredang.github.io/sipoc/) | Guided SIPOC that enforces the 5-7 step rule, tags pain points, and generates the swimlane and handoff table from your actor assignments | Labs 3, 12 |")
    out.append("| [5 Whys](https://alfredang.github.io/5whys/) | Build and share a 5 Whys root-cause chain | Lab 8 |")
    out.append("| [Fishbone Diagram](https://alfredang.github.io/fishbone/) | Build an Ishikawa cause-and-effect diagram | Lab 8 |")
    out.append("| [Pareto Chart](https://alfredang.github.io/paretochart/) | Collaborative session: the team brainstorms and votes, and the Pareto chart builds itself live | Lab 7 |")
    out.append("| [NovaSPC](https://alfredang.github.io/novaspc/) | Run charts, SPC charts (c, u, np, p, X-mR, X̄-R, X̄-s) and process capability from your own CSV | Labs 7, 10 |")
    out.append("")
    out.append("### Using the SIPOC builder")
    out.append("")
    out.append("1. Set the process name, start point and stop point — the grid unlocks once boundaries are agreed.")
    out.append("2. List the 5-7 process steps, then work outward: Outputs, Customers, Inputs, Suppliers.")
    out.append("3. Click a process step to tag pain points (at least three) and assign the actor who performs it.")
    out.append("4. Open the Swimlane tab — the lanes and every handoff are generated from your actor assignments.")
    out.append("5. Fill in an owner on both sides of each handoff.")
    out.append("6. Run **Check my SIPOC**, then export the PNG for your improvement package.")
    out.append("")
    out.append("### Using the collaborative Pareto tool")
    out.append("")
    out.append("1. One team member creates a session and shares the access code.")
    out.append("2. Everyone else joins the session using that code.")
    out.append("3. The team brainstorms candidate causes into the session.")
    out.append("4. Each member votes on the causes that matter most.")
    out.append("5. The live Pareto chart reveals the vital few to act on.")
    out.append("")
    out.append("## Templates you will produce")
    out.append("")
    for a in ACT:
        title = a["title"].replace("Elective — ", "")
        out.append(f"- **Lab {a['num']} — {title}:** {a['build']}")
    out.append("")
    out.append("## Formula quick reference")
    out.append("")
    out.append("| Metric | Formula |")
    out.append("|--------|---------|")
    out.append("| Yield | (Good units / Total units) × 100 |")
    out.append("| DPU | Defects / Units |")
    out.append("| DPO | Defects / (Units × Opportunities per unit) |")
    out.append("| DPMO | DPO × 1,000,000 |")
    out.append("| First Pass Yield (FPY) | Units passing with no rework / Units started |")
    out.append("| Rolled Throughput Yield (RTY) | FPY₁ × FPY₂ × … × FPYₙ |")
    out.append("| Process Cycle Efficiency | Value-added time / Total lead time |")
    out.append("| Takt time | Available working time / Customer demand |")
    out.append("")
    out.append("### Sigma level reference")
    out.append("")
    out.append("| Sigma | DPMO | Yield |")
    out.append("|-------|------|-------|")
    for s, d, y in [("1σ", "690,000", "31%"), ("2σ", "308,000", "69%"), ("3σ", "66,800", "93.3%"),
                    ("4σ", "6,210", "99.38%"), ("5σ", "233", "99.977%"), ("6σ", "3.4", "99.99966%")]:
        out.append(f"| {s} | {d} | {y} |")
    out.append("")
    out.append("## The eight wastes — DOWNTIME")
    out.append("")
    for letter, name, ex in [
        ("D", "Defects", "Wrong ticket category; work that must be redone"),
        ("O", "Overproduction", "Reports nobody reads"),
        ("W", "Waiting", "Tickets sitting in the triage queue"),
        ("N", "Non-utilised talent", "Skilled agents doing routine data entry"),
        ("T", "Transport", "Tickets bouncing between teams"),
        ("I", "Inventory", "A growing backlog of unassigned tickets"),
        ("M", "Motion", "Switching between four systems for one ticket"),
        ("E", "Extra-processing", "Approvals that add no customer value"),
    ]:
        out.append(f"- **{letter} — {name}:** {ex}")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- write
def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = _csv.writer(f)
        for r in rows:
            w.writerow(r)


os.makedirs(LABS, exist_ok=True)
# clear the previous flat layout and any stale lab folders
for old in glob.glob(os.path.join(LABS, "lab-*.md")):
    os.remove(old)
for old in glob.glob(os.path.join(LABS, "lab-*")):
    if os.path.isdir(old):
        shutil.rmtree(old)

readme, files = readme_md()
written = 0
csv_written = 0
for a in ACT:
    folder = os.path.join(LABS, dirname(a))
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(lab_md(a))
    written += 1
    data, tmpl, _ = LF.files_for(a["num"])
    if data:
        os.makedirs(os.path.join(folder, "data"), exist_ok=True)
        for name, rows in data.items():
            write_csv(os.path.join(folder, "data", name), rows)
            csv_written += 1
    if tmpl:
        os.makedirs(os.path.join(folder, "templates"), exist_ok=True)
        for name, rows in tmpl.items():
            write_csv(os.path.join(folder, "templates", name), rows)
            csv_written += 1

# shared scenario brief + the worked answer key for the metrics lab
write_csv(os.path.join(LABS, "scenario-key-figures.csv"),
          [["field", "value"],
           ["Tickets (units)", D.N],
           ["Defective tickets", D.DEFECTIVE],
           ["Total defects", D.TOTAL_DEFECTS],
           ["Opportunities per unit", D.OPP],
           ["Yield %", round(D.YIELD * 100, 1)],
           ["DPU", round(D.DPU, 2)],
           ["DPO", round(D.DPO, 4)],
           ["DPMO", int(D.DPMO)],
           ["Sigma level", D.SIGMA],
           ["Mean assignment time (min)", D.MEAN_MIN],
           ["Median assignment time (min)", D.MEDIAN_MIN],
           ["Std dev assignment time (min)", D.SD_MIN],
           ["Improvement goal (min)", D.TARGET_MIN]])
csv_written += 1

# worked answer key for the metrics lab — learners self-check after attempting it
_lab7 = [a for a in ACT if a["num"] == 7][0]
_sol = os.path.join(LABS, dirname(_lab7), "solution")
os.makedirs(_sol, exist_ok=True)
write_csv(os.path.join(_sol, "pareto-table-answers.csv"),
          [["defect_category", "count", "percent", "cumulative_percent"]] +
          [[n, c, f"{pc}%", f"{cum}%"] for n, c, pc, cum in D.pareto()])
write_csv(os.path.join(_sol, "process-metrics-answers.csv"),
          [["metric", "formula", "value"],
           ["Units", "Total tickets", D.N],
           ["Defective units", "Tickets with >= 1 defect", D.DEFECTIVE],
           ["Total defects", "Sum of all defects", D.TOTAL_DEFECTS],
           ["Opportunities per unit", "Given", D.OPP],
           ["Yield %", "(Units - Defective) / Units x 100", f"{D.YIELD*100:.0f}%"],
           ["DPU", "Defects / Units", f"{D.DPU:.2f}"],
           ["DPO", "Defects / (Units x Opportunities)", f"{D.DPO:.4f}"],
           ["DPMO", "DPO x 1,000,000", f"{int(D.DPMO):,}"],
           ["Sigma level", "DPMO conversion (1.5 sigma shift)", f"~{D.SIGMA}"],
           ["Vital few", "Top 2 categories, cumulative", "65% - Delayed assignment + Missing information"],
           ["Run chart signal", "Shift rule",
            "Mean rises from ~44 min (days 1-6) to ~72 min (days 7-10): a SHIFT (special cause) "
            "coinciding with the 9 June ITSM migration"]])
csv_written += 2

with open(os.path.join(LABS, "README.md"), "w") as f:
    f.write(readme)
with open(os.path.join(LABS, "tools.md"), "w") as f:
    f.write(tools_md())

core = sum(1 for a in ACT if not a.get("elective"))


# ---------------------------------------------------------------- repo README
def repo_readme(files):
    n = len(ACT)
    out = []
    # ---------------- centred hero ----------------
    out.append('<div align="center">')
    out.append("")
    out.append("# 🎯 Certified Lean Six Sigma Yellow Belt (CLSSYB)")
    out.append("")
    out.append(f"**{C.COURSE_CODE} · WSQ · {C.DAYS}-day hands-on Lean Six Sigma certification training**")
    out.append("")
    out.append("*Learn the DMAIC roadmap by running one real improvement project end to end.*")
    out.append("")
    reg = REGISTER_URL
    badges = [
        (f"[![Register](https://img.shields.io/badge/📝_Register_Now-tertiarycourses.com.sg-0A66C2"
         f"?style=for-the-badge)]({reg})"),
        "![WSQ Funded](https://img.shields.io/badge/WSQ-SkillsFuture_Funded-00A651?style=for-the-badge)",
        f"![Duration](https://img.shields.io/badge/Duration-{C.DAYS}_days_·_16_hours-4B5563?style=for-the-badge)",
        "![Level](https://img.shields.io/badge/Level-Beginner-7C3AED?style=for-the-badge)",
    ]
    out.append(" ".join(badges))
    out.append("")
    badges2 = [
        f"![TSC](https://img.shields.io/badge/TSC-{C.TSC_CODE.replace(chr(45), chr(45)*2)}-0F172A?style=flat-square)",
        f"![Labs](https://img.shields.io/badge/Labs-{n}_({core}_core_+_{n-core}_elective)-2563EB?style=flat-square)",
        "![Assessment](https://img.shields.io/badge/Assessment-WA_SAQ_+_Case_Study-F59E0B?style=flat-square)",
        f"![Version](https://img.shields.io/badge/Courseware-{C.VERSION}-64748B?style=flat-square)",
    ]
    out.append(" ".join(badges2))
    out.append("")
    out.append(f"**[📝 Register for this course →]({reg})**")
    out.append("")
    out.append("</div>")
    out.append("")
    out.append("---")
    out.append("")
    # ---------------- about ----------------
    out.append("## About This Course")
    out.append("")
    out.append(f"This is the official courseware repository for the WSQ **{C.TITLE}** "
               f"({C.COURSE_CODE}), delivered by "
               "[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).")
    out.append("")
    out.append(f"The course follows the **DMAIC roadmap** end to end — Define, Measure, Analyze, Improve, "
               f"Control — across **{n} hands-on labs** ({core} core and {n-core} elective). It is grounded in "
               "the Council for Six Sigma Certification (CSSC) Yellow Belt body of knowledge, so what you "
               "learn matches the recognised Yellow Belt standard.")
    out.append("")
    out.append("It is written for people who support improvement work rather than lead it — analysts, "
               "executives, engineers, supervisors and team leads who want to read process data properly, "
               "find a root cause and make a change that holds.")
    out.append("")
    # ---------------- learning outcomes ----------------
    out.append("## Learning Outcomes")
    out.append("")
    out.append("| # | On completion, you will be able to |")
    out.append("|---|------------------------------------|")
    for lo in C.LEARNING_OUTCOMES:
        code, _, text = lo.partition(": ")
        out.append(f"| **{code}** | {text} |")
    out.append("")
    # ---------------- the lab data set ----------------
    out.append("## The Lab Data Set")
    out.append("")
    out.append("Every lab works from one continuous scenario — the **Contoso Service Desk** — and one "
               "shared set of numbers, so your lab outputs accumulate into a single improvement package.")
    out.append("")
    out.append("| Measure | Baseline |")
    out.append("|---------|----------|")
    out.append(f"| Tickets analysed | {D.N} over two weeks |")
    out.append(f"| Defective tickets | {D.DEFECTIVE} ({D.DEFECTIVE/D.N*100:.0f}%) |")
    out.append(f"| Total defects | {D.TOTAL_DEFECTS} across {D.OPP} opportunities per ticket |")
    out.append(f"| Yield | {D.YIELD*100:.0f}% |")
    out.append(f"| DPU · DPMO | {D.DPU:.2f} · {int(D.DPMO):,} |")
    out.append(f"| Sigma level | ~{D.SIGMA} |")
    out.append(f"| Mean assignment time | {D.MEAN_MIN} min (median {D.MEDIAN_MIN}) vs a {D.TARGET_MIN}-min goal |")
    out.append("")
    out.append("These are the same figures as the Case Study assessment, so lab work doubles as revision. "
               "Headline values: [labs/scenario-key-figures.csv](labs/scenario-key-figures.csv).")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Courseware")
    out.append("")
    out.append("| Artifact | File |")
    out.append("|----------|------|")
    # URL-encode spaces/parens so the Markdown links work on GitHub
    def enc(p):
        return p.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    lg_md = f"LG-{C.SHORT_TITLE}.md"
    out.append(f"| **Slide deck** | `courseware/{C.SHORT_TITLE}-{C.VERSION}.pptx` (and `.pdf`) |")
    out.append(f"| **Learner Guide (Markdown)** | [{lg_md}]({enc(lg_md)}) |")
    out.append(f"| **Learner Guide (DOCX/PDF)** | `courseware/LG-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    out.append(f"| **Lesson Plan (DOCX/PDF)** | `courseware/LP-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    out.append("| **Lab Index** | [labs/README.md](labs/README.md) |")
    out.append("| **Tools and Templates** | [labs/tools.md](labs/tools.md) |")
    out.append("")
    out.append("> **Note:** assessment papers, answer keys and trainer-only materials are intentionally "
               "not published in this repository.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## How to use")
    out.append("")
    out.append("1. Read the Learner Guide first — it follows the same DMAIC order as the course.")
    out.append("2. Complete the core labs in order using the Contoso Service Desk scenario.")
    out.append("3. Complete the elective labs if time allows, or as post-course practice.")
    out.append("4. Keep every worksheet — the final lab combines them into one improvement package.")
    out.append("5. Review the 'Check your work' step at the end of each lab before moving on.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Lab catalogue")
    out.append("")
    for t in C.TOPICS:
        acts = [a for a in ACT if a["topic"] == t["num"]]
        if not acts:
            continue
        # t['title'] already leads with the phase name for the DMAIC topics, so
        # don't print it twice ("Define — Define — Scope the Problem").
        heading = t["title"] if t["title"].lower().startswith(t["phase"].lower()) \
            else f"{t['phase'].title()} — {t['title']}"
        out.append(f"### {heading}")
        out.append("")
        for a in acts:
            title = a["title"].replace("Elective — ", "")
            tag = " *(elective)*" if a.get("elective") else ""
            out.append(f"- [Lab {a['num']} - {title}](labs/{files[a['num']]}){tag}")
        out.append("")
    out.append("---")
    out.append("")
    out.append("## Repository structure")
    out.append("")
    out.append("```")
    out.append("courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan")
    out.append("  archive/           superseded deck versions")
    out.append("  assets/            diagrams and images used by the deck")
    out.append("labs/                one self-contained folder per lab:")
    out.append("  lab-NN-<name>/     README.md (worksheet) + data/ (mock CSV data)")
    out.append("                     + templates/ (worksheets to fill in)")
    out.append("  scenario-key-figures.csv   the headline metrics all labs share")
    out.append("  tools.md           the interactive toolkit")
    out.append(f"LG-{C.SHORT_TITLE}.md")
    out.append("                     Learner Guide (Markdown mirror of the DOCX)")
    out.append(".claude/skills/courseware-build/build/")
    out.append("                     single-source generators: one content module")
    out.append("                     drives the deck, LP, LG and labs")
    out.append("```")
    out.append("")
    out.append("All artifacts are generated from `course_data.py` + `data_domainN.py`, so the deck, "
               "Lesson Plan, Learner Guide and labs stay 100% aligned.")
    out.append("")
    out.append("## Interactive tools")
    out.append("")
    out.append("- [SIPOC & Process Map](https://alfredang.github.io/sipoc/) — guided SIPOC, swimlane and handoff table")
    out.append("- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder")
    out.append("- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder")
    out.append("- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative team brainstorm, vote and live chart")
    out.append("- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability")
    out.append("")
    out.append("## Reference")
    out.append("")
    out.append("- [Council for Six Sigma Certification - Lean Six Sigma Yellow Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-yellow-belt-certification/)")
    out.append("- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html)")
    out.append("- [labs/tools.md](labs/tools.md) - templates, formulas and free tools used in the labs")
    out.append("")
    out.append("## Free tools used")
    out.append("")
    out.append("- Microsoft Excel, LibreOffice Calc, or Google Sheets")
    out.append("- Draw.io / diagrams.net for SIPOC, process maps and fishbone diagrams")
    out.append("- The interactive tools listed above")
    out.append("- Whiteboard or sticky notes for facilitation activities")
    out.append("")
    out.append("---")
    out.append("")
    # ---------------- course details ----------------
    out.append("## Course Details")
    out.append("")
    out.append("| | |")
    out.append("|---|---|")
    out.append(f"| **Course title** | WSQ - {C.TITLE} |")
    out.append(f"| **Course reference** | {C.COURSE_CODE} |")
    out.append(f"| **TSC alignment** | {C.TSC_TITLE} ({C.TSC_CODE}) |")
    out.append(f"| **Duration** | {C.DAYS} days · 8 training hours per day (16 hours) |")
    out.append("| **Level** | Beginner — no prior Six Sigma knowledge required |")
    out.append(f"| **Assessment** | {C.ASSESSMENT['written']} {C.ASSESSMENT['practical']} |")
    out.append("| **Mode** | Instructor-led, hands-on labs |")
    out.append("| **Certification** | WSQ Statement of Attainment (SOA) on successful assessment |")
    out.append(f"| **Provider** | {C.ORG} ({C.UEN.replace('UEN: ', 'UEN ')}) |")
    out.append("")
    out.append("### Funding")
    out.append("")
    out.append("This is a **WSQ / SkillsFuture-funded** course. Singapore Citizens, PRs and eligible "
               "companies can claim course-fee funding, and SkillsFuture Credit may be used to offset "
               f"the fee. Current fees, funding tiers and upcoming dates are on the "
               f"[course registration page]({REGISTER_URL}).")
    out.append("")
    out.append(f"{C.ASSESSMENT['note']}")
    out.append("")
    out.append("---")
    out.append("")
    # ---------------- contact ----------------
    out.append("## Contact")
    out.append("")
    out.append("| | |")
    out.append("|---|---|")
    out.append(f"| **Course page** | [{REGISTER_URL.replace('https://', '')}]({REGISTER_URL}) |")
    out.append("| **Website** | [www.tertiarycourses.com.sg](https://www.tertiarycourses.com.sg/) |")
    out.append("| **Email** | [enquiry@tertiaryinfotech.com](mailto:enquiry@tertiaryinfotech.com) |")
    out.append("| **Tel** | +65 6255 5527 |")
    out.append("| **LMS / TMS** | [lms-tms.tertiaryinfotech.com](https://lms-tms.tertiaryinfotech.com/) |")
    out.append("")
    out.append("---")
    out.append("")
    # ---------------- closing CTA ----------------
    out.append('<div align="center">')
    out.append("")
    out.append("### Ready to start improving how your work actually runs?")
    out.append("")
    out.append(f"**[📝 Register for {C.TITLE} →]({REGISTER_URL})**")
    out.append("")
    out.append(f"*Courseware version {C.VERSION} · {C.VERSION_DATE}*")
    out.append("")
    out.append(f"© 2026 {C.ORG} · {C.UEN.replace('UEN: ', 'UEN ')}")
    out.append("")
    out.append("</div>")
    out.append("")
    return "\n".join(out)


with open(os.path.join(REPO, "README.md"), "w") as f:
    f.write(repo_readme(files))

print(f"Saved {written} lab files to {LABS}  ({core} core, {written-core} elective)")
print("Saved labs/README.md, labs/tools.md and README.md")
