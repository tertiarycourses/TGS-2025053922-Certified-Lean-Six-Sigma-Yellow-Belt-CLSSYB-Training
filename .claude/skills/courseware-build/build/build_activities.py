#!/usr/bin/env python3
"""Generate the activities/ folder — ONE FOLDER PER ACTIVITY, each holding the
house artefact set as DOCX **and** PDF, plus the activity's own mock data:

    activities/
      README.md
      tools.md
      scenario-key-figures.csv
      07 - Pareto, Run Charts, Variation, Yield, DPU, and DPMO/
        A07-Facilitator-Guide-Pareto-Run-Charts-....docx | .pdf
        A07-Learner-Worksheet-Pareto-Run-Charts-....docx | .pdf
        A07-Checklist-Pareto-Run-Charts-....docx         | .pdf
        data/         the mock CSV data the learner analyses
        templates/    blank CSV worksheets the learner completes
        solution/     worked answers (Activity 7 only — trainer releases after the attempt)

House format (matching the Tertiary Infotech reference activity packs):
  * blue banner table (org name + course title · course code)
  * a 4-chip meta row: TYPE / DURATION / MAPS TO / TOPIC
  * Name+Date table on learner-facing sheets
  * Heading 2 sections, Arial 11pt body
  * Facilitator Guide carries the numbered run-sheet as a 3-column table
    (# | Instruction to learners | Facilitator note)
  * Checklist carries a criteria table (# | Criterion | Evidences | ✓)

Content is driven by course_data.py + data_domain1..3.py + data_activity_meta.py
+ lab_files.py, so the packs stay aligned with the slide deck, Lesson Plan,
Learner Guide and the Case Study assessment.
"""
import csv as _csv
import os, re, sys, shutil, subprocess, tempfile

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
import lab_dataset as D
import lab_files as LF
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_activity_meta import META
ACT=sorted(DOMAIN1+DOMAIN2+DOMAIN3, key=lambda a: a["num"])


def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and (os.path.isdir(os.path.join(d,"activities")) or os.path.isdir(os.path.join(d,"labs"))):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO=_find_repo(HERE)
ACTIVITIES=os.path.join(REPO,"activities")

REGISTER_URL=("https://www.tertiarycourses.com.sg/"
              "wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html")

SCENARIO=("Contoso Service Desk handles employee IT requests. Employees complain that tickets take "
          "too long to be assigned, that they must keep chasing for status, and that agents apply "
          "different definitions of what counts as \"resolved\". Handoffs between the front line and "
          "the specialist queues are unclear, and although ticket data exists it is inconsistent. "
          "You are supporting the improvement team as a Yellow Belt — you do not lead the project.")

DATA_BRIEF=(f"Two weeks of data have been collected: {D.N} tickets, of which {D.DEFECTIVE} contained "
            f"at least one defect, with {D.TOTAL_DEFECTS} defects recorded in total across {D.OPP} "
            f"defect opportunities per ticket. Mean assignment time is {D.MEAN_MIN} minutes "
            f"(median {D.MEDIAN_MIN}) against a {D.TARGET_MIN}-minute improvement goal. The CSV files "
            f"in this activity's data/ folder are that extract.")

BRAND="1F6FEB"; INK="111827"; GREEN="10B981"; LIGHT="F5F8FC"; LINE="E2E8F0"
BRAND_RGB=RGBColor(0x1F,0x6F,0xEB); INK_RGB=RGBColor(0x11,0x18,0x27)
GREY_RGB=RGBColor(0x55,0x5B,0x66)
RULE="_"*95

def slug(t): return re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")
def title_slug(t): return re.sub(r"[^A-Za-z0-9]+","-",t).strip("-")

TOPIC_BY_NUM={t["num"]:t for t in C.TOPICS}
TYPE_LABEL={True:"Elective Activity", False:"Core Activity"}

def clean_title(a): return a["title"].replace("Elective — ", "")
def folder_for(a): return f"{a['num']:02d} - {clean_title(a)}"

# ------------------------------------------------------------------ docx bits
def shade(cell,hexfill):
    tcPr=cell._tc.get_or_add_tcPr()
    shd=OxmlElement("w:shd"); shd.set(qn("w:val"),"clear")
    shd.set(qn("w:color"),"auto"); shd.set(qn("w:fill"),hexfill)
    tcPr.append(shd)

def no_borders(table):
    tbl=table._tbl; tblPr=tbl.tblPr
    borders=OxmlElement("w:tblBorders")
    for edge in ("top","left","bottom","right","insideH","insideV"):
        el=OxmlElement(f"w:{edge}"); el.set(qn("w:val"),"none"); el.set(qn("w:sz"),"0")
        borders.append(el)
    tblPr.append(borders)

def new_doc():
    doc=Document()
    n=doc.styles["Normal"]; n.font.name="Arial"; n.font.size=Pt(11)
    for st,sz,col in (("Heading 1",16,BRAND),("Heading 2",13,INK)):
        s=doc.styles[st]; s.font.name="Arial"; s.font.size=Pt(sz); s.font.bold=True
        s.font.color.rgb=RGBColor.from_string(col)
    for s in doc.sections:
        s.left_margin=s.right_margin=Cm(2.26)
        s.top_margin=s.bottom_margin=Cm(2.0)
    return doc

def banner(doc):
    """Blue org/course banner across the top."""
    t=doc.add_table(rows=1,cols=1); t.alignment=WD_TABLE_ALIGNMENT.CENTER
    c=t.rows[0].cells[0]; shade(c,BRAND); no_borders(t)
    p=c.paragraphs[0]; p.space_after=Pt(0)
    r=p.add_run(C.ORG); r.bold=True; r.font.size=Pt(10); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
    p2=c.add_paragraph(); p2.space_before=Pt(0)
    r2=p2.add_run(f"{C.TITLE}  ·  {C.COURSE_CODE}")
    r2.font.size=Pt(8.5); r2.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
    return t

def meta_chips(doc,a):
    """TYPE / DURATION / MAPS TO / TOPIC chip row."""
    t=TOPIC_BY_NUM[a["topic"]]; m=META[a["num"]]
    chips=[("TYPE",TYPE_LABEL[bool(a.get("elective"))]),
           ("DURATION",m["duration"]),
           ("DMAIC PHASE",t["phase"]),
           ("MAPS TO",a["objective"].split("(")[-1].rstrip(").") if "(" in a["objective"] else t["phase"])]
    tbl=doc.add_table(rows=1,cols=4); no_borders(tbl)
    for cell,(k,v) in zip(tbl.rows[0].cells,chips):
        shade(cell,LIGHT)
        p=cell.paragraphs[0]; p.space_after=Pt(0)
        r=p.add_run(k); r.bold=True; r.font.size=Pt(7.5); r.font.color.rgb=BRAND_RGB
        p2=cell.add_paragraph(); p2.space_before=Pt(0)
        r2=p2.add_run(v); r2.font.size=Pt(9); r2.font.color.rgb=INK_RGB
    doc.add_paragraph()
    return tbl

def name_date(doc):
    t=doc.add_table(rows=2,cols=2); t.style="Table Grid"
    for i,label in enumerate(("Name","Date")):
        c=t.rows[i].cells[0]; c.text=""
        r=c.paragraphs[0].add_run(label); r.bold=True; r.font.size=Pt(9.5)
        shade(c,LIGHT)
        t.rows[i].cells[1].text=""
    doc.add_paragraph()

def head(doc,a,kind):
    p=doc.add_paragraph(); p.space_after=Pt(2)
    r=p.add_run(f"ACTIVITY {a['num']} — {kind}")
    r.bold=True; r.font.size=Pt(12); r.font.color.rgb=BRAND_RGB
    p2=doc.add_paragraph(); p2.space_after=Pt(8)
    r2=p2.add_run(clean_title(a)); r2.bold=True; r2.font.size=Pt(15); r2.font.color.rgb=INK_RGB

def blanks(doc,n=1):
    for _ in range(n):
        p=doc.add_paragraph(); p.space_after=Pt(2)
        r=p.add_run(RULE); r.font.size=Pt(10); r.font.color.rgb=RGBColor(0xAA,0xB2,0xBF)

def footer_note(doc):
    p=doc.add_paragraph(); p.space_before=Pt(14)
    r=p.add_run(f"{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · "
                f"© 2026 {C.ORG}")
    r.font.size=Pt(8); r.font.color.rgb=GREY_RGB; r.italic=True

# ------------------------------------------------------------------ documents
def _files_block(doc, a, learner=True):
    """List the activity's own data / template CSV files."""
    data_f, tmpl_f, note = LF.files_for(a["num"])
    if not (data_f or tmpl_f): return
    doc.add_heading("Files in this activity folder", level=2)
    if data_f:
        p=doc.add_paragraph(); r=p.add_run("data/ — the mock data you analyse:"); r.bold=True
        for name in sorted(data_f):
            rows=data_f[name]
            doc.add_paragraph(f"{name} — {len(rows)-1} rows ({', '.join(str(c) for c in rows[0])})",
                              style="List Bullet")
    if tmpl_f:
        p=doc.add_paragraph(); r=p.add_run("templates/ — the worksheets you complete:"); r.bold=True
        for name in sorted(tmpl_f):
            doc.add_paragraph(f"{name} ({', '.join(str(c) for c in tmpl_f[name][0])})",
                              style="List Bullet")
    doc.add_paragraph("Open these in Excel, Google Sheets or LibreOffice Calc. Work on a copy so the "
                      "originals stay clean for revision.")
    if note:
        doc.add_paragraph(note)


def facilitator_guide(a):
    m=META[a["num"]]; t=TOPIC_BY_NUM[a["topic"]]
    doc=new_doc(); banner(doc); head(doc,a,"FACILITATOR GUIDE"); meta_chips(doc,a)

    doc.add_heading("Purpose of this activity",level=2)
    doc.add_paragraph(a["objective"])
    doc.add_paragraph(a["desc"])

    doc.add_heading("What learners produce",level=2)
    doc.add_paragraph(m["artefact"])

    doc.add_heading("Materials required",level=2)
    for x in ["Learner Worksheet (one per learner)",
              "Checklist (one per group)",
              "A laptop with Excel, Google Sheets or LibreOffice Calc",
              "The CSV files in this activity's data/ and templates/ folders",
              "Flipchart or A3 sheet and markers",
              "The course slides for the scenario and the framework"]:
        doc.add_paragraph(x,style="List Bullet")
    if any(cmd.startswith("http") for _,cmd in a["steps"]):
        doc.add_paragraph("A browser — this activity uses an online tool (URL in the run-sheet).",
                          style="List Bullet")

    doc.add_heading("Set-up",level=2)
    doc.add_paragraph("Groups of 3-5. Distribute one worksheet per learner and one checklist per "
                      "group. Every activity runs on the same continuous Contoso Service Desk "
                      "scenario, so remind learners where this one sits in that story before starting.")

    doc.add_heading("Scenario / briefing material",level=2)
    doc.add_paragraph(SCENARIO)
    doc.add_paragraph(DATA_BRIEF)

    _files_block(doc,a,learner=False)

    doc.add_heading("How to run it — step by step",level=2)
    tbl=doc.add_table(rows=1,cols=3); tbl.style="Table Grid"
    hdr=tbl.rows[0].cells
    for i,h in enumerate(["#","Instruction to learners","Facilitator note"]):
        hdr[i].text=""; r=hdr[i].paragraphs[0].add_run(h)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(hdr[i],BRAND)
    tips=m.get("tips",[])
    for i,(instr,cmd) in enumerate(a["steps"],1):
        cells=tbl.add_row().cells
        cells[0].text=""; cells[0].paragraphs[0].add_run(str(i)).font.size=Pt(9.5)
        cells[1].text=""
        pp=cells[1].paragraphs[0]
        pp.add_run(instr).font.size=Pt(9.5)
        if cmd:
            p2=cells[1].add_paragraph()
            r2=p2.add_run(f"Tool: {cmd}" if cmd.startswith("http") else cmd)
            r2.font.size=Pt(8.5); r2.font.color.rgb=BRAND_RGB
        cells[2].text=""
        note=tips[i-1] if i-1 < len(tips) else ""
        cells[2].paragraphs[0].add_run(note).font.size=Pt(9)
        if i%2==0:
            for c in cells: shade(c,LIGHT)

    doc.add_heading("Suggested timing",level=2)
    tt=doc.add_table(rows=1,cols=2); tt.style="Table Grid"
    h=tt.rows[0].cells
    for i,x in enumerate(["Minutes","Phase"]):
        h[i].text=""; r=h[i].paragraphs[0].add_run(x)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(h[i],BRAND)
    for mins,phase in m["timing"]:
        c=tt.add_row().cells
        c[0].text=""; c[0].paragraphs[0].add_run(f"{mins} min").font.size=Pt(9.5)
        c[1].text=""; c[1].paragraphs[0].add_run(phase).font.size=Pt(9.5)
    pt=doc.add_paragraph()
    r=pt.add_run(f"Total: {sum(x for x,_ in m['timing'])} minutes"); r.bold=True; r.font.size=Pt(9.5)

    doc.add_heading("Discussion & decision prompts",level=2)
    for prompt in m["prompts"]:
        doc.add_paragraph(prompt,style="List Number")

    doc.add_heading("Debrief",level=2)
    doc.add_paragraph("Bring the class back together and draw out the learning:")
    for b in ["Ask two or three groups to show what they produced, not just what they concluded.",
              "Ask what surprised them — the gap between what they assumed and what the data showed.",
              f"Link the activity explicitly back to the {t['phase']} phase of DMAIC.",
              "Remind learners this activity rehearses what the Case Study assessment will require."]:
        doc.add_paragraph(b,style="List Bullet")
    doc.add_paragraph("Reflection questions:")
    for point in m["reflect"]:
        doc.add_paragraph(point,style="List Bullet")

    if m.get("tips"):
        doc.add_heading("Facilitator notes — what to watch for",level=2)
        for tip in m["tips"]:
            doc.add_paragraph(tip,style="List Bullet")

    doc.add_heading("Success criterion",level=2)
    doc.add_paragraph(a["test"])

    doc.add_heading("Assessment link",level=2)
    doc.add_paragraph(
        f"This activity builds the {t['phase']} phase of DMAIC. All activities are in-class "
        f"activities assessed indirectly through the open-book Case Study (CS), which reuses the "
        f"same techniques on the same Contoso Service Desk scenario and the same figures "
        f"({D.N} tickets, yield {D.YIELD*100:.0f}%, DPMO {int(D.DPMO):,}). Knowledge is assessed in "
        f"the Written Assessment (WA-SAQ). Nothing is assessed that is not practised here or "
        f"taught in the slides.")
    footer_note(doc)
    return doc


def learner_worksheet(a):
    m=META[a["num"]]; t=TOPIC_BY_NUM[a["topic"]]
    doc=new_doc(); banner(doc); head(doc,a,"LEARNER WORKSHEET"); meta_chips(doc,a); name_date(doc)

    doc.add_heading("What you are doing",level=2)
    doc.add_paragraph(a["desc"])
    p=doc.add_paragraph()
    r=p.add_run("What you will produce: "); r.bold=True
    p.add_run(m["artefact"])
    p=doc.add_paragraph()
    r=p.add_run("Tools and techniques: "); r.bold=True
    p.add_run(a["services"])

    doc.add_heading("The scenario",level=2)
    doc.add_paragraph(SCENARIO)
    doc.add_paragraph(DATA_BRIEF)

    _files_block(doc,a,learner=True)

    doc.add_heading("Your steps",level=2)
    for instr,cmd in a["steps"]:
        p=doc.add_paragraph(style="List Number")
        p.add_run(instr)
        if cmd:
            p2=doc.add_paragraph()
            r2=p2.add_run(f"    Tool: {cmd}" if cmd.startswith("http") else f"    {cmd}")
            r2.font.size=Pt(9); r2.font.color.rgb=BRAND_RGB

    doc.add_heading("Your working space",level=2)
    doc.add_paragraph("Complete every field. You may keep this worksheet and refer to it during "
                      "the open-book assessment.")
    for i,(instr,_) in enumerate(a["steps"],1):
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        short=instr if len(instr)<=88 else instr[:85].rstrip()+"..."
        r=p.add_run(f"Step {i} — {short}"); r.bold=True; r.font.size=Pt(10)
        r.font.color.rgb=BRAND_RGB
        blanks(doc,2)

    doc.add_heading("Answers to the discussion prompts",level=2)
    for i,prompt in enumerate(m["prompts"],1):
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(f"{i}. {prompt}"); r.bold=True; r.font.size=Pt(10)
        blanks(doc,2)

    doc.add_heading("Reflect & discuss",level=2)
    for point in m["reflect"]:
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(point); r.bold=True; r.font.size=Pt(10)
        blanks(doc,2)

    doc.add_heading("Check your work",level=2)
    doc.add_paragraph(a["test"])
    footer_note(doc)
    return doc


def checklist(a):
    m=META[a["num"]]; t=TOPIC_BY_NUM[a["topic"]]
    doc=new_doc(); banner(doc); head(doc,a,"CHECKLIST"); meta_chips(doc,a); name_date(doc)

    doc.add_heading(f"Self-check — {clean_title(a)}",level=2)
    doc.add_paragraph("Tick each item you have completed. Any blank is a gap to close before "
                      "your group presents at the debrief.")
    tbl=doc.add_table(rows=1,cols=4); tbl.style="Table Grid"
    h=tbl.rows[0].cells
    for i,x in enumerate(["#","Criterion","Evidences","✓"]):
        h[i].text=""; r=h[i].paragraphs[0].add_run(x)
        r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor(0xFF,0xFF,0xFF)
        shade(h[i],BRAND)
    for i,item in enumerate(m["checklist"],1):
        c=tbl.add_row().cells
        c[0].text=""; c[0].paragraphs[0].add_run(str(i)).font.size=Pt(9.5)
        c[1].text=""; c[1].paragraphs[0].add_run(item).font.size=Pt(9.5)
        c[2].text=""; c[2].paragraphs[0].add_run(t["phase"]).font.size=Pt(9.5)
        c[3].text=""
        if i%2==0:
            for cc in c: shade(cc,LIGHT)
    doc.add_paragraph()

    doc.add_heading("Debrief check",level=2)
    p=doc.add_paragraph(); r=p.add_run(a["test"]); r.font.size=Pt(10.5)

    doc.add_heading("Feedback",level=2)
    for q in ["What did you find hardest in this activity?",
              "What is the ONE thing you will do differently at work?"]:
        p=doc.add_paragraph(); p.space_after=Pt(2); p.space_before=Pt(8)
        r=p.add_run(q); r.bold=True; r.font.size=Pt(10)
        blanks(doc,2)
    footer_note(doc)
    return doc


# ------------------------------------------------------------------ pdf
_SOFFICE=shutil.which("soffice") or shutil.which("libreoffice")

def to_pdf(docx_path):
    """Convert a DOCX to PDF beside it. Returns True on success."""
    if not _SOFFICE: return False
    outdir=os.path.dirname(docx_path)
    # A stale PDF/DOCX left in place makes LibreOffice emit "<name> 2.pdf" instead of
    # overwriting, so clear the target first and give every call its own profile.
    stale=os.path.splitext(docx_path)[0]+".pdf"
    if os.path.exists(stale):
        try: os.remove(stale)
        except OSError: pass
    with tempfile.TemporaryDirectory() as tmp:
        profile=os.path.join(tmp,"lo")
        try:
            subprocess.run([_SOFFICE,"--headless",
                            f"-env:UserInstallation=file://{profile}",
                            "--convert-to","pdf","--outdir",outdir,docx_path],
                           check=True,capture_output=True,timeout=240)
        except Exception:
            return False
    return os.path.exists(os.path.splitext(docx_path)[0]+".pdf")

# ------------------------------------------------------------------ indexes
def readme_md():
    core=[a for a in ACT if not a.get("elective")]
    L=[f"# {C.TITLE} — Activities",""]
    L.append(f"**{C.COURSE_CODE}**  ·  **Version {C.VERSION} · {C.VERSION_DATE}**")
    L.append("")
    L.append(f"{len(ACT)} in-class activities ({len(core)} core, {len(ACT)-len(core)} elective) "
             "following the DMAIC roadmap end to end. Every activity runs on one continuous "
             "scenario — the **Contoso Service Desk** — so the outputs accumulate into a single "
             "improvement package and rehearse the open-book Case Study assessment.")
    L.append("")
    L.append("## What each activity folder contains")
    L.append("")
    L.append("| Artefact | What it is | Who uses it |")
    L.append("|---|---|---|")
    L.append("| `ANN-Facilitator-Guide-*.docx` / `.pdf` | Purpose, materials, set-up, scenario, the "
             "numbered run-sheet with facilitator notes, timing, debrief and success criterion | Trainer |")
    L.append("| `ANN-Learner-Worksheet-*.docx` / `.pdf` | The scenario, the steps and a working space "
             "to capture the artefact and prompt answers | Learner |")
    L.append("| `ANN-Checklist-*.docx` / `.pdf` | Criteria table to tick before the debrief, plus feedback | Learner group |")
    L.append("| `data/*.csv` | The mock data the activity analyses | Learner |")
    L.append("| `templates/*.csv` | Blank worksheets to complete in a spreadsheet | Learner |")
    L.append("| `solution/*.csv` | Worked answers (Activity 7 only) | Trainer — release after the attempt |")
    L.append("")
    L.append("## The shared data set")
    L.append("")
    L.append(f"All activities work from one fortnight of Contoso Service Desk activity: "
             f"**{D.N} tickets**, **{D.DEFECTIVE} defective**, **{D.TOTAL_DEFECTS} defects** across "
             f"**{D.OPP} opportunities per ticket**.")
    L.append("")
    L.append("| Measure | Baseline |")
    L.append("|---------|----------|")
    L.append(f"| Yield | {D.YIELD*100:.0f}% |")
    L.append(f"| DPU · DPO | {D.DPU:.2f} · {D.DPO:.4f} |")
    L.append(f"| DPMO | {int(D.DPMO):,} |")
    L.append(f"| Sigma level | ~{D.SIGMA} |")
    L.append(f"| Mean assignment time | {D.MEAN_MIN} min (median {D.MEDIAN_MIN}, sd {D.SD_MIN}) |")
    L.append(f"| Improvement goal | {D.TARGET_MIN} min |")
    L.append("")
    L.append("These are the same figures as the Case Study assessment, so activity work is direct "
             "revision. Headline values: [scenario-key-figures.csv](scenario-key-figures.csv).")
    L.append("")
    L.append("## Activities")
    L.append("")
    L.append("| # | DMAIC phase | Activity | Type | Duration | Folder |")
    L.append("|---|---|---|---|---|---|")
    for a in ACT:
        t=TOPIC_BY_NUM[a["topic"]]
        L.append(f"| {a['num']} | {t['phase']} | {clean_title(a)} | "
                 f"{TYPE_LABEL[bool(a.get('elective'))]} | {META[a['num']]['duration']} | "
                 f"`{folder_for(a)}/` |")
    L.append("")
    L.append("See [tools.md](tools.md) for the interactive tools and formula reference.")
    L.append("")
    L.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    L.append("")
    return "\n".join(L)


def tools_md():
    L=["# Lean Six Sigma Toolkit","",f"*{C.TITLE} · {C.COURSE_CODE}*",""]
    L.append("## Interactive online tools")
    L.append("")
    L.append("Browser-based, no installation or licence needed.")
    L.append("")
    L.append("| Tool | What it does | Used in |")
    L.append("|------|--------------|---------|")
    L.append("| [SIPOC & Process Map](https://alfredang.github.io/sipoc/) | Guided SIPOC that enforces the 5-7 step rule, tags pain points and generates the swimlane and handoff table | Activities 3, 12 |")
    L.append("| [5 Whys](https://alfredang.github.io/5whys/) | Build and share a 5 Whys root-cause chain | Activity 8 |")
    L.append("| [Fishbone Diagram](https://alfredang.github.io/fishbone/) | Build an Ishikawa cause-and-effect diagram | Activity 8 |")
    L.append("| [Pareto Chart](https://alfredang.github.io/paretochart/) | Collaborative session: the team brainstorms and votes, and the chart builds itself live | Activity 7 |")
    L.append("| [NovaSPC](https://alfredang.github.io/novaspc/) | Run charts, SPC charts and process capability from your own CSV | Activities 7, 10 |")
    L.append("")
    L.append("## Formula quick reference")
    L.append("")
    L.append("| Metric | Formula |")
    L.append("|--------|---------|")
    for k,v in [("Yield","(Good units / Total units) × 100"),("DPU","Defects / Units"),
                ("DPO","Defects / (Units × Opportunities per unit)"),("DPMO","DPO × 1,000,000"),
                ("First Pass Yield (FPY)","Units passing with no rework / Units started"),
                ("Rolled Throughput Yield","FPY₁ × FPY₂ × … × FPYₙ"),
                ("Process Cycle Efficiency","Value-added time / Total lead time"),
                ("Takt time","Available working time / Customer demand"),
                ("RPN","Severity × Occurrence × Detection")]:
        L.append(f"| {k} | {v} |")
    L.append("")
    L.append("### Sigma level reference")
    L.append("")
    L.append("| Sigma | DPMO | Yield |")
    L.append("|-------|------|-------|")
    for a_,b_,c_ in [("1σ","690,000","31%"),("2σ","308,000","69%"),("3σ","66,800","93.3%"),
                     ("4σ","6,210","99.38%"),("5σ","233","99.977%"),("6σ","3.4","99.99966%")]:
        L.append(f"| {a_} | {b_} | {c_} |")
    L.append("")
    L.append("## The eight wastes — DOWNTIME")
    L.append("")
    for letter,name,ex in [
        ("D","Defects","Wrong ticket category; work that must be redone"),
        ("O","Overproduction","Reports nobody reads"),
        ("W","Waiting","Tickets sitting in the triage queue"),
        ("N","Non-utilised talent","Skilled agents doing routine data entry"),
        ("T","Transport","Tickets bouncing between teams"),
        ("I","Inventory","A growing backlog of unassigned tickets"),
        ("M","Motion","Switching between four systems for one ticket"),
        ("E","Extra-processing","Approvals that add no customer value")]:
        L.append(f"- **{letter} — {name}:** {ex}")
    L.append("")
    L.append(f"*{C.TITLE} · {C.COURSE_CODE} · © 2026 {C.ORG}*")
    L.append("")
    return "\n".join(L)


def write_csv(path, rows):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=_csv.writer(f)
        for r in rows: w.writerow(r)


def repo_readme():
    n = len(ACT)
    core = len([a for a in ACT if not a.get("elective")])
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
        f"![Activities](https://img.shields.io/badge/Activities-{n}_({core}_core_+_{n-core}_elective)-2563EB?style=flat-square)",
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
    out.append("## The Activity Data Set")
    out.append("")
    out.append("Every activity works from one continuous scenario — the **Contoso Service Desk** — and one "
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
    out.append("These are the same figures as the Case Study assessment, so activity work doubles as revision. "
               "Headline values: [activities/scenario-key-figures.csv](activities/scenario-key-figures.csv).")
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
    out.append("| **Activity Index** | [activities/README.md](activities/README.md) |")
    out.append("| **Tools and Templates** | [activities/tools.md](activities/tools.md) |")
    out.append("")
    out.append("> **Note:** assessment papers, answer keys and trainer-only materials are intentionally "
               "not published in this repository.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## How to use")
    out.append("")
    out.append("1. Read the Learner Guide first — it follows the same DMAIC order as the course.")
    out.append("2. Work the core activities in order using the Contoso Service Desk scenario.")
    out.append("3. Complete the elective activities if time allows, or as post-course practice.")
    out.append("4. Keep every worksheet — the final activity combines them into one improvement package.")
    out.append("5. Review the Checklist at the end of each activity before moving on.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Activity catalogue")
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
            out.append(f"- **Activity {a['num']} - {title}**{tag} — `activities/{folder_for(a)}/`")
        out.append("")
    out.append("---")
    out.append("")
    out.append("## Repository structure")
    out.append("")
    out.append("```")
    out.append("courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan")
    out.append("  archive/           superseded deck versions")
    out.append("  assets/            diagrams and images used by the deck")
    out.append("activities/          one self-contained folder per activity:")
    out.append("  NN - <Name>/       ANN-Facilitator-Guide-*.docx|pdf")
    out.append("                     ANN-Learner-Worksheet-*.docx|pdf")
    out.append("                     ANN-Checklist-*.docx|pdf")
    out.append("                     data/      the mock CSV data to analyse")
    out.append("                     templates/ blank CSV worksheets to complete")
    out.append("  scenario-key-figures.csv   the headline metrics all activities share")
    out.append("  tools.md           the interactive toolkit")
    out.append("archive/             superseded material (the previous labs/ layout)")
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
    out.append("- [activities/tools.md](activities/tools.md) - frameworks, formulas and free tools")
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




# ------------------------------------------------------------------ main
if __name__=="__main__":
    # rebuild the tree from scratch so renamed folders never linger
    if os.path.isdir(ACTIVITIES):
        for old in sorted(os.listdir(ACTIVITIES)):
            q=os.path.join(ACTIVITIES,old)
            if os.path.isdir(q) and re.match(r"^\d{2} - ", old): shutil.rmtree(q)
    os.makedirs(ACTIVITIES,exist_ok=True)

    with open(os.path.join(REPO,"README.md"),"w",encoding="utf-8") as f:
        f.write(repo_readme())
    print("Wrote repo README.md")

    for name,text in (("README.md",readme_md()),("tools.md",tools_md())):
        with open(os.path.join(ACTIVITIES,name),"w",encoding="utf-8") as f: f.write(text)
        print("Wrote",name)

    write_csv(os.path.join(ACTIVITIES,"scenario-key-figures.csv"),
              [["field","value"],
               ["Tickets (units)",D.N],["Defective tickets",D.DEFECTIVE],
               ["Total defects",D.TOTAL_DEFECTS],["Opportunities per unit",D.OPP],
               ["Yield %",round(D.YIELD*100,1)],["DPU",round(D.DPU,2)],
               ["DPO",round(D.DPO,4)],["DPMO",int(D.DPMO)],["Sigma level",D.SIGMA],
               ["Mean assignment time (min)",D.MEAN_MIN],
               ["Median assignment time (min)",D.MEDIAN_MIN],
               ["Std dev assignment time (min)",D.SD_MIN],
               ["Improvement goal (min)",D.TARGET_MIN]])
    print("Wrote scenario-key-figures.csv")

    pdf_ok=pdf_skip=0; csv_n=1
    for a in ACT:
        d=os.path.join(ACTIVITIES,folder_for(a)); os.makedirs(d,exist_ok=True)
        ts=title_slug(clean_title(a)); n=f"A{a['num']:02d}"
        for kind,builder in (("Facilitator-Guide",facilitator_guide),
                             ("Learner-Worksheet",learner_worksheet),
                             ("Checklist",checklist)):
            path=os.path.join(d,f"{n}-{kind}-{ts}.docx")
            builder(a).save(path)
            if to_pdf(path): pdf_ok+=1
            else: pdf_skip+=1
        # the activity's own mock data + blank worksheets
        data_f,tmpl_f,_=LF.files_for(a["num"])
        for sub,files in (("data",data_f),("templates",tmpl_f)):
            if not files: continue
            os.makedirs(os.path.join(d,sub),exist_ok=True)
            for name,rows in files.items():
                write_csv(os.path.join(d,sub,name),rows); csv_n+=1
        if a["num"]==7:
            sol=os.path.join(d,"solution"); os.makedirs(sol,exist_ok=True)
            write_csv(os.path.join(sol,"pareto-table-answers.csv"),
                      [["defect_category","count","percent","cumulative_percent"]]+
                      [[x,c,f"{pc}%",f"{cum}%"] for x,c,pc,cum in D.pareto()])
            write_csv(os.path.join(sol,"process-metrics-answers.csv"),
                      [["metric","formula","value"],
                       ["Units","Total tickets",D.N],
                       ["Defective units","Tickets with >= 1 defect",D.DEFECTIVE],
                       ["Total defects","Sum of all defects",D.TOTAL_DEFECTS],
                       ["Opportunities per unit","Given",D.OPP],
                       ["Yield %","(Units - Defective) / Units x 100",f"{D.YIELD*100:.0f}%"],
                       ["DPU","Defects / Units",f"{D.DPU:.2f}"],
                       ["DPO","Defects / (Units x Opportunities)",f"{D.DPO:.4f}"],
                       ["DPMO","DPO x 1,000,000",f"{int(D.DPMO):,}"],
                       ["Sigma level","DPMO conversion (1.5 sigma shift)",f"~{D.SIGMA}"],
                       ["Vital few","Top 2 categories, cumulative",
                        "65% - Delayed assignment + Missing information"],
                       ["Run chart signal","Shift rule",
                        "Mean rises from ~44 min (days 1-6) to ~72 min (days 7-10): a SHIFT "
                        "(special cause) coinciding with the 9 June ITSM migration"]])
            csv_n+=2
        print(f"Wrote {folder_for(a)}/")

    strays=[os.path.join(r,f) for r,_,fs in os.walk(ACTIVITIES) for f in fs
            if re.search(r" \d+\.(docx|pdf)$", f)]
    if strays:
        junk=os.path.join(REPO,"archive","stray-duplicate-renders")
        for f in strays:
            d=os.path.join(junk,os.path.relpath(os.path.dirname(f),ACTIVITIES))
            os.makedirs(d,exist_ok=True); shutil.move(f,os.path.join(d,os.path.basename(f)))
        print(f"Moved {len(strays)} stray duplicate render(s) to archive/stray-duplicate-renders/")

    print(f"\n{len(ACT)} activity folders · {csv_n} CSV files · "
          f"PDFs rendered: {pdf_ok}, failed/skipped: {pdf_skip}")
    if pdf_skip and not _SOFFICE:
        print("NOTE: soffice/libreoffice not found — PDFs were not rendered.")
