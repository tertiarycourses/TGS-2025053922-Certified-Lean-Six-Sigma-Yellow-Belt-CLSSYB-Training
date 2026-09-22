"""
SINGLE SOURCE OF TRUTH — Certified Lean Six Sigma Yellow Belt (CLSSYB) Training.

Content is grounded in two references (see reference/):
  * "SG - Dr. Alfred Ang - Certified Lean Six Sigma Yellow Belt (CLSSYB) - v20.pptx"
    (the original 387-slide trainer deck — concepts, diagrams and activities)
  * "Six Sigma: A Complete Step-by-Step Guide" — The Council for Six Sigma
    Certification (CSSC), July 2018 edition — the body-of-knowledge that defines
    the Yellow Belt standard, so the certification is credible.

Every artifact (PPT, LP, LG, LG.md, labs index) is generated from this module +
data_domainN.py so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Certified Lean Six Sigma Yellow Belt (CLSSYB) Training"
SHORT_TITLE  = "Certified Lean Six Sigma Yellow Belt (CLSSYB) Training"
COURSE_CODE  = "TGS-2025053922"
VERSION      = "v8"
VERSION_DATE = "23 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2

# ------------------------------------------------------------------ TSC alignment (WSQ)
TSC_TITLE = "Quality Process Control"
TSC_CODE  = "ELE-QUA-5006-1.1"
TSC_ABILITIES = [
    "A1: Define project to meet process performance.",
    "A2: Establish project scope of work and the number of hours based on organisational requirements.",
    "A3: Analyse process performance data to identify root causes of variation.",
    "A4: Measure process performance against defined quality standards.",
    "A5: Recommend improvement and control actions to sustain process performance.",
]
TSC_KNOWLEDGE = [
    "K1: Lean and Six Sigma concepts, wastes, value and variation.",
    "K2: Quality tools and techniques for process improvement.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Define a project and establish the scope of work using Six Sigma's Define, Measure and Analyse phases.",
    "LO2: Apply Lean and Six Sigma concepts — value, waste, defects and variation — to a work process.",
    "LO3: Map a process using SIPOC, process maps and value stream maps to expose handoffs and waste.",
    "LO4: Collect and analyse process data using check sheets, Pareto charts, run charts and basic metrics.",
    "LO5: Identify root causes using 5 Whys, Fishbone analysis and evidence-based prioritisation.",
    "LO6: Recommend improvement and control actions to sustain gains, and prepare for certification.",
]

# ------------------------------------------------------------------ topics
# The course follows the DMAIC roadmap end to end: Foundations establish the
# language, then one topic per DMAIC phase. Every lab lands inside the phase it
# belongs to, so the slides, LG, LP and labs all tell one coherent story.
TOPICS = [
    dict(num=0, code="00", phase="FOUNDATIONS",
         title="Six Sigma Foundations",
         subtitle="Quality · Lean · Six Sigma · Lean Six Sigma · Belt roles · The DMAIC roadmap",
         weighting="15%",
         concepts=[
            ("What is Quality", "Quality is conformance to customer requirements — not merely defect-free output."),
            ("What is Lean", "A method to maximise customer value by systematically removing waste and improving flow."),
            ("What is Six Sigma", "A data-driven method to reduce variation and defects — targeting 3.4 defects per million."),
            ("Lean Six Sigma", "The combined method: faster flow AND fewer defects, driven by data."),
            ("Belt roles", "White, Yellow, Green, Black and Master Black Belt — who does what on a project."),
            ("The DMAIC roadmap", "Define, Measure, Analyze, Improve, Control — the disciplined improvement path."),
         ]),
    dict(num=1, code="D", phase="DEFINE",
         title="Define — Scope the Problem",
         subtitle="VOC · CTQ · Project charter · Problem statement · Scope · SIPOC · Process mapping",
         weighting="25%",
         concepts=[
            ("Voice of the Customer", "Capture customer needs in their own words before deciding anything."),
            ("Critical to Quality", "Translate each VOC need into a specific, measurable CTQ requirement."),
            ("Project charter", "Problem statement, goal, scope, team and benefit — the project's contract."),
            ("Problem statement", "Process, time period, measurable issue and impact — and never a solution."),
            ("SIPOC", "The macro as-is map: Suppliers, Inputs, Process, Outputs, Customers."),
            ("Process mapping", "Flowcharts and swimlanes expose the handoffs where delay and defects are born."),
         ]),
    dict(num=2, code="M", phase="MEASURE",
         title="Measure — Quantify Performance",
         subtitle="The 8 wastes · Data types · Data collection plan · Check sheets · Yield · DPMO · Sigma level",
         weighting="25%",
         concepts=[
            ("The 8 wastes", "DOWNTIME — Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
            ("Types of data", "Continuous vs discrete; nominal vs ordinal — the data type drives the tool choice."),
            ("Data collection plan", "What, who, when and how — with operational definitions to remove ambiguity."),
            ("Check sheets", "A simple structured form is the most reliable way to capture process data."),
            ("Process metrics", "Yield, DPU, DPO and DPMO quantify how well the process actually performs."),
            ("Sigma level", "Convert DPMO into a sigma level to benchmark the process against Six Sigma."),
         ]),
    dict(num=3, code="A", phase="ANALYZE",
         title="Analyze — Find the Root Cause",
         subtitle="Variation · Pareto · Run charts · 5 Whys · Fishbone · Multi-voting · Evidence",
         weighting="20%",
         concepts=[
            ("Variation", "Common cause is built into the process; special cause is an external, assignable signal."),
            ("Pareto analysis", "The 80/20 rule separates the vital few causes from the trivial many."),
            ("Run charts", "Plot the metric over time to reveal trend, shift, cluster and oscillation."),
            ("5 Whys", "Ask why repeatedly to drill from the symptom down to an actionable cause."),
            ("Fishbone diagram", "Organise candidate causes by category — Manpower, Method, Machine, Material, Measurement."),
            ("Evidence testing", "A cause is only a root cause when the data you collected supports it."),
         ]),
    dict(num=4, code="I", phase="IMPROVE",
         title="Improve — Fix the Cause",
         subtitle="Countermeasures · 5S · Poka-Yoke · Standard work · Kaizen · Solution selection · Piloting",
         weighting="10%",
         concepts=[
            ("Generating solutions", "Brainstorm widely against the proven root cause before evaluating anything."),
            ("Solution selection", "Score candidate solutions against weighted criteria before committing."),
            ("5S", "Sort, Set in order, Shine, Standardise, Sustain — for physical and digital work."),
            ("Poka-Yoke", "Mistake proofing makes the error difficult or impossible to make in the first place."),
            ("Standard work", "Document the improved method so anyone can repeat it the same way."),
            ("Piloting", "Test the change at small scale to expose issues before full rollout."),
         ]),
    dict(num=5, code="C", phase="CONTROL",
         title="Control — Hold the Gain",
         subtitle="Control plan · Visual management · SOPs · Huddles · A3 · Handover · Certification",
         weighting="5%",
         concepts=[
            ("Control plan", "Metric, target, monitoring method, frequency, owner and reaction plan."),
            ("Process control", "A process is in control when it varies consistently within expected limits."),
            ("Visual management", "Boards and dashboards keep the improved performance visible to everyone."),
            ("Standard operating procedures", "Written instructions that lock in the improved method."),
            ("Team huddles", "Short, regular stand-ups that surface problems while they are still small."),
            ("A3 and handover", "One-page storytelling to summarise, hand over and sustain the improvement."),
         ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Six Sigma foundations, Define phase and process mapping",
    2: "Measure, Analyse, Improve, Control and assessment",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 60 minutes, open book.",
    practical="Case Study (CS) — applied Lean Six Sigma tasks, 90 minutes, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)
