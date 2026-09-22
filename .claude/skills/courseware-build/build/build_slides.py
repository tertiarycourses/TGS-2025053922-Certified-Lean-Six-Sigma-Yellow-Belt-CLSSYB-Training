#!/usr/bin/env python3
"""Build the CLSSYB slide deck — all-white Tertiary house style, DMAIC order.

Structure:
  Cover → Admin (TRAQOM, trainers x2, ground rules, LMS, lesson plan, TSC,
  outcomes, course outline, briefing, assessment, assessment flow)
  → Foundations → D → M → A → I → C  (each phase: concept slides then its labs)
  → Wrap-up → Assessment → Assessment Flow → Digital Attendance → TRAQOM → Thank You

Content comes entirely from course_data.py + data_domainN.py + concepts.py so the
PPT, LP, LG and labs stay 100% aligned.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import course_data as C
import lab_dataset as DS
import lab_files as LF
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from components import (Deck, BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT,
                        WHITE, LINE, DMAIC_COLORS)
import concepts

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3


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
ASSETS = os.path.join(REPO, "courseware", "assets")


def asset(name):
    p = os.path.join(ASSETS, name)
    return p if os.path.exists(p) else None


d = Deck(C)

# ============================================================ COVER
d.cover(logo=asset("tertiary-logo.png"))

# ============================================================ ADMIN
d.section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

d.flow_h("Digital Attendance (Mandatory)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Repeat for AM, PM and the assessment",
    "Keep 75% attendance to stay eligible for funding",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

# --- two trainer profile cards (house hard rule) ---
d.trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
                "General Trainer template —\nto be completed by the trainer",
                [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
                 ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
                initials="?", accent=GREY)   # no photo: the two PNGs are 16:9 slide captures, not portraits
d.trainer_slide("YOUR TRAINER", C.TRAINER,
                "Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
                [("Role", "Principal Trainer, Tertiary Infotech Academy Pte. Ltd."),
                 ("Qualifications", "PhD; Certified Lean Six Sigma practitioner and trainer."),
                 ("Delivers", "WSQ courses on Lean Six Sigma, quality management and data analytics."),
                 ("Experience", "Process improvement across manufacturing, service and technology sectors."),
                 ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
                initials="AA", accent=BLUE)  # initials avatar until a real portrait asset is supplied

d.content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Your experience with process improvement or quality work (if any).",
    "One process at work that frustrates you — we may use it as your course scenario.",
], kicker="ICE-BREAKER")

d.tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for certification.",
], kicker="HOUSEKEEPING", cols=2, size=15)

# --- Download course material (visual step flow, not a bullet wall) ---
lms = asset("lms_download.png")
if lms:
    d.image_slide("Download Your Course Material", lms,
                  kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com",
                  caption="Log in to lms-tms.tertiaryinfotech.com to download the slides, Learner Guide and lab files.")
else:
    d.flow_h("Download Your Course Material", [
        "Go to lms-tms.tertiaryinfotech.com",
        "Sign in with the account details given in class",
        "Open this course from your dashboard",
        "Download the slides, Learner Guide and lab files",
        "Keep them open — the assessment is open book",
    ], kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com", color=TEAL)

# --- Lesson plan ---
d.two_col("Lesson Plan — 2 Days, 8 Hours per Day",
          [("Day 1 — " + C.DAY_THEMES[1], 0),
           ("Digital attendance (AM) · Introductions", 1),
           ("Foundations: Quality, Lean, Six Sigma, belts, DMAIC", 1),
           ("Lab 1 — Yellow Belt role and scenario", 1),
           ("DEFINE: VOC, CTQ, charter, SIPOC, process mapping", 1),
           ("Labs 2-5 — VOC/waste, SIPOC, PDCA charter, DMAIC Define", 1)],
          [("Day 2 — " + C.DAY_THEMES[2], 0),
           ("Digital attendance (AM)", 1),
           ("MEASURE: wastes, data types, check sheets, DPMO", 1),
           ("Lab 6 — Data collection and KPIs", 1),
           ("ANALYZE: Pareto, run charts, 5 Whys, Fishbone", 1),
           ("Labs 7-8 — Data analysis and root cause", 1),
           ("IMPROVE & CONTROL: 5S, poka-yoke, control plan, A3", 1),
           ("Labs 9-10 · Revision · Final Assessment", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Day 1", rhead="Day 2")

# --- WSQ TSC alignment ---
d.content(f"Skills Framework — TSC: {C.TSC_TITLE}", [
    f"TSC Code: {C.TSC_CODE}",
] + C.TSC_ABILITIES + C.TSC_KNOWLEDGE, kicker="WSQ SKILLS FRAMEWORK", size=16)

d.tile_grid("Learning Outcomes", [
    ("LO1 — Define & scope", "Define a project and establish scope using Define, Measure and Analyse."),
    ("LO2 — Lean & Six Sigma concepts", "Apply value, waste, defects and variation to a work process."),
    ("LO3 — Map the process", "Use SIPOC, process maps and value stream maps to expose handoffs."),
    ("LO4 — Measure & analyse", "Use check sheets, Pareto, run charts and process metrics."),
    ("LO5 — Root cause", "Identify root causes with 5 Whys, Fishbone and evidence."),
    ("LO6 — Improve & control", "Recommend improvement and control actions that sustain the gain."),
], kicker="WHAT YOU'LL ACHIEVE", cols=2, size=14)

d.dmaic_wheel("Course Outline — We Follow DMAIC End to End", [
    ("D", "Define", ["Foundations + Define", "VOC, CTQ, charter", "SIPOC, process maps", "Labs 1-5"]),
    ("M", "Measure", ["8 wastes, data types", "Collection plan", "Yield, DPMO, sigma", "Lab 6"]),
    ("A", "Analyze", ["Variation", "Pareto, run charts", "5 Whys, Fishbone", "Labs 7-8"]),
    ("I", "Improve", ["Solution selection", "5S, poka-yoke", "Standard work", "Lab 9"]),
    ("C", "Control", ["Control plan", "Visual management", "A3 and handover", "Lab 10"]),
], kicker="COURSE ROADMAP")

# --- Briefing BEFORE assessment (house hard rule) ---
d.content("Briefing for Assessment", [
    "Place phones and other materials under the table or on the floor.",
    "No photos or recording of assessment scripts.",
    "No discussion during the assessment.",
    "Use a black/blue pen for hard-copy assessments.",
    "No liquid paper / correction tape.",
    "Scripts are collected when time is up.",
], kicker="BEFORE YOU SIT THE ASSESSMENT")

d.content("Assessment", [
    C.ASSESSMENT["written"],
    C.ASSESSMENT["practical"],
    "Format: Open Book — slides, Learner Guide and approved materials only.",
    C.ASSESSMENT["note"],
    "An appeal process is available if required.",
], kicker="FINAL ASSESSMENT")

d.flow_h("Assessment Flow", [
    "TRAQOM survey — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ), then the Case Study — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
], kicker="ON ASSESSMENT DAY", color=VIOLET)

# NOTE: no Practice Exam slide — there is no CLSSYB practice exam available.
# (The bundled courseware/assets/practice_exam.png belongs to a DIFFERENT course
# — CompTIA CySA+, TGS-2024049211 — and must never be used in this deck.)

# ============================================================ FOUNDATIONS
concepts.foundations(d)

# ---------------- the shared lab data set (one scenario, one set of numbers) ----
d.tile_grid("The Contoso Service Desk Data Set", [
    ("One scenario, one data set",
     f"Every lab works from the same two weeks of service desk activity: {DS.N} tickets, "
     f"{DS.DEFECTIVE} of them defective, {DS.TOTAL_DEFECTS} defects in total."),
    ("Defect opportunities",
     f"Each ticket carries {DS.OPP} defect opportunities — the basis for DPO and DPMO."),
    ("Baseline performance",
     f"Yield {DS.YIELD*100:.0f}% · DPU {DS.DPU:.2f} · DPMO {int(DS.DPMO):,} · sigma level ~{DS.SIGMA}."),
    ("Speed of assignment",
     f"Mean {DS.MEAN_MIN} min, median {DS.MEDIAN_MIN} min, against a {DS.TARGET_MIN}-minute goal — "
     "the gap between mean and median is the story."),
    ("Where the files are",
     "Each lab folder holds data/ (the mock data you analyse) and templates/ "
     "(the blank worksheets you complete)."),
    ("Why it matters",
     "These are the same figures as the Case Study assessment — your lab work is your revision."),
], kicker="LAB DATA · labs/", cols=2, size=13)

d.tile_grid("What the Baseline Data Already Tells You", [
    ("Delayed assignment · 48", "40% of all defects — the single largest category."),
    ("Missing information · 30", "25% — together with delays this is the vital few: 65%."),
    ("Wrong queue · 18", "15% — tickets bouncing between teams."),
    ("Reopened ticket · 12", "10% — the fix did not hold the first time."),
    ("Duplicate ticket · 8", "6.7% — the same issue logged twice."),
    ("Unclear status · 4", "3.3% — the trivial many, by count."),
], kicker="PARETO PREVIEW · ANALYSED IN LAB 7", cols=3, size=12)

# ============================================================ DMAIC PHASES + LABS
PHASE_FN = {
    1: concepts.define_phase,
    2: concepts.measure_phase,
    3: concepts.analyze_phase,
    4: concepts.improve_phase,
    5: concepts.control_phase,
}
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}


def render_labs(acts, phase_label):
    for a in acts:
        opt = a.get("elective", False)
        tag = f"LAB {a['num']}"
        d.activity_overview(tag, a["title"], a["desc"], a["build"], a["services"],
                            kicker=f"{phase_label} · HANDS-ON", elective=opt)
        steps = a["steps"]
        total = len(steps)
        short = a["title"][:38]
        for i, (instr, cmd) in enumerate(steps, 1):
            d.step_slide(f"LAB {a['num']} · {short}", a["title"], i, total, instr, cmd)
        data_f, tmpl_f, _ = LF.files_for(a["num"])
        if data_f or tmpl_f:
            def cols(header, budget):
                """Join column names, dropping whole columns that do not fit (never mid-word)."""
                out, used = [], 0
                for c in (str(x) for x in header):
                    if used + len(c) + 2 > budget:
                        out.append(f"+{len(header)-len(out)} more")
                        break
                    out.append(c)
                    used += len(c) + 2
                return ", ".join(out)

            tiles = []
            for name in sorted(data_f):
                rows = data_f[name]
                tiles.append((f"data/{name}",
                              f"{len(rows)-1} rows · {cols(rows[0], 62)}"))
            for name in sorted(tmpl_f):
                tiles.append((f"templates/{name}",
                              "Worksheet to complete · " + cols(tmpl_f[name][0], 52)))
            d.tile_grid(f"Lab {a['num']} — Your Data Files", tiles,
                        kicker=f"LAB {a['num']} · labs/{LF.dirname(a['num'], a['title'])}/",
                        cols=1, size=13)
        d.test_slide(a["title"], a["test"], kicker=f"LAB {a['num']} · VERIFY")


# Foundations labs (topic 0) come right after the foundations concepts
render_labs(TOPIC_ACTS.get(0, []), "FOUNDATIONS")

for t in C.TOPICS:
    if t["num"] == 0:
        continue
    idx = t["num"] - 1
    col = DMAIC_COLORS[idx % len(DMAIC_COLORS)]
    d.section(f"DMAIC · {t['phase']}", t["title"], t["code"], t["subtitle"])
    d.tile_grid(f"Key Concepts — {t['phase'].title()}", t["concepts"],
                kicker=f"{t['phase']} · {t['weighting']} OF THE COURSE", cols=2, size=14, accent=col)
    # teaching content for this phase
    PHASE_FN[t["num"]](d)
    # labs that belong to this phase
    acts = TOPIC_ACTS.get(t["num"], [])
    if acts:
        core = [a for a in acts if not a.get("elective")]
        opts = [a for a in acts if a.get("elective")]
        rows = []
        for a in core:
            rows.append((f"Lab {a['num']} — {a['title'][:46]}", a["build"][:70]))
        for a in opts:
            rows.append((f"Lab {a['num']} (elective) — {a['title'].replace('Elective — ', '')[:40]}",
                         a["build"][:70]))
        d.tile_grid(f"Hands-On Labs — {t['phase'].title()}", rows,
                    kicker="WHAT YOU'LL DO", cols=1, size=14, accent=col)
        render_labs(acts, f"DMAIC · {t['phase']}")
    # phase recap
    d.content(f"Recap — {t['phase'].title()}",
              [c[0] + " — " + c[1] for c in t["concepts"]],
              kicker="PHASE RECAP", size=15)

# ============================================================ WRAP-UP
d.section("WRAP-UP", "Course Summary & Next Steps", "")
d.dmaic_wheel("What You Achieved — The Full DMAIC Journey", [
    ("D", "Define", ["Captured VOC and CTQ", "Wrote the charter", "Built the SIPOC", "Mapped the process"]),
    ("M", "Measure", ["Found the 8 wastes", "Built the data plan", "Collected the baseline", "Calculated DPMO"]),
    ("A", "Analyze", ["Built the Pareto", "Read the run chart", "Ran 5 Whys and Fishbone", "Proved the cause"]),
    ("I", "Improve", ["Selected solutions", "Applied 5S and poka-yoke", "Wrote standard work", "Piloted the change"]),
    ("C", "Control", ["Built the control plan", "Set visual management", "Wrote the A3", "Handed over"]),
], kicker="YOUR IMPROVEMENT PACKAGE")

d.tile_grid("Your Integrated Improvement Package", [
    ("Role and scenario", "Yellow Belt responsibility table and a selected improvement scenario."),
    ("VOC, CTQ and waste", "Customer requirements translated to CTQs, plus a waste walk log."),
    ("SIPOC and process map", "Macro and detailed maps with pain points and handoffs marked."),
    ("Charter and Define pack", "PDCA charter, problem statement, scope and stakeholder map."),
    ("Measurement and analysis", "Data collection plan, check sheet, Pareto, run chart and metrics."),
    ("Root cause and countermeasures", "5 Whys, Fishbone, evidence tests and prioritised countermeasures."),
    ("Control plan and A3", "Control plan, visual management approach, A3 summary and handover."),
    ("Certification readiness", "Your personal review plan for the assessment."),
], kicker="WHAT YOU BUILT", cols=2, size=13)

d.tile_grid("Final Readiness Checklist", [
    "Can you explain the Yellow Belt role and where it stops?",
    "Can you define Lean, Six Sigma and Lean Six Sigma in your own words?",
    "Can you trace a VOC statement through to a CTQ and a metric?",
    "Can you name the eight wastes and give a service example of each?",
    "Can you explain each DMAIC phase and what it delivers?",
    "Can you calculate yield, DPU, DPO and DPMO from raw data?",
    "Can you interpret a Pareto chart and a run chart?",
    "Can you explain your root cause with the evidence behind it?",
    "Can you describe how the control plan sustains the gain?",
], kicker="BEFORE THE ASSESSMENT", cols=1, size=14, accent=TEAL)

d.tile_grid("Continuing Your Lean Six Sigma Journey", [
    ("Apply it at work", "Run one small PDCA improvement in your own area within 30 days."),
    ("Green Belt", "The next step — leads smaller DMAIC projects and handles the statistics."),
    ("Keep the templates", "Your lab outputs are reusable templates for real projects."),
    ("Join the community", "Share improvements with colleagues; Kaizen spreads by example."),
], kicker="NEXT STEPS", cols=2, size=15, accent=AMBER)

# ============================================================ CLOSE (house order)
# Assessment → Assessment Flow → Digital Attendance → TRAQOM → Thank You
d.big_statement("Final Assessment",
                "Written Assessment (SAQ, 60 minutes) followed by the Case Study (90 minutes). Both are open book.",
                "ASSESSMENT", color=VIOLET)

d.flow_h("Assessment Flow", [
    "TRAQOM survey — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ), then the Case Study — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
], kicker="ON ASSESSMENT DAY", color=VIOLET)

d.flow_h("Digital Attendance (Assessment)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Attendance must be recorded before you begin the papers",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

d.flow_h("TRAQOM Survey", [
    "Open the TRAQOM survey link on the LMS",
    "Key in the last four characters of your NRIC/FIN",
    "Key in the six-digit course run ID",
    "Complete and submit — your feedback shapes this course",
], kicker="YOUR FEEDBACK", color=TEAL)

d.content("Certificate & Support", [
    "Two e-certificates are awarded on demonstrating competency and achieving at least 75% attendance.",
    "A SkillsFuture Statement of Attainment (SOA) is issued for the WSQ assessment.",
    "Email: enquiry@tertiaryinfotech.com",
    "Tel / WhatsApp: +65 6100 0613",
], kicker="AFTER THE COURSE")

d.big_statement("Thank You!",
                "Go and improve one process this month — that is what a Yellow Belt is for.",
                "END OF COURSE", color=BLUE)

# ============================================================ TRANSITIONS + SAVE
d.apply_transitions(kind="fade", dur_ms=700)

out = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
d.prs.save(out)
print(f"✅ {out}")
print(f"   {len(d.prs.slides._sldIdLst)} slides")
