"""
Domain 2 — Measure and Analyse Process Performance.

Activities 5-8. DMAIC Define/Measure/Analyze depth: data collection, process metrics,
Pareto, run charts and root cause analysis.
"""

DOMAIN2 = [
    dict(
        num=5, topic=1,
        title="DMAIC Overview, Problem Statement, Scope, and Stakeholders",
        objective="Support the Define phase of a DMAIC project (A1, A2).",
        desc="Step up from PDCA to the full DMAIC roadmap. Clarify what each phase delivers, "
             "where a Yellow Belt contributes most, and prepare defensible Define-phase "
             "information for the project leader.",
        build="A DMAIC phase table, refined problem statement, stakeholder map and benefit estimate.",
        services="DMAIC roadmap, project charter, stakeholder analysis, CTQ linkage",
        steps=[
            ("Summarise all five DMAIC phases: purpose, key deliverable and Yellow Belt support role.", ""),
            ("Refine the problem statement so it is specific, measurable and solution-free.", ""),
            ("Identify stakeholders and classify each by influence and interest.", ""),
            ("Define the project scope and state the expected benefit in business terms.", ""),
            ("Link the problem back to the CTQ requirements captured in Activity 2.", ""),
            ("Confirm which DMAIC phases a Yellow Belt can support most strongly.", ""),
        ],
        test="Your problem statement passes the 'no solution named' test and every stakeholder has a defined engagement approach.",
    ),
    dict(
        num=6, topic=2,
        title="Data Collection, KPIs, Check Sheets, and Basic Metrics",
        objective="Plan and execute data collection against defined quality standards (A4).",
        desc="Replace anecdote with evidence. Define KPIs with unambiguous operational "
             "definitions, design a check sheet, plan the sampling approach, and understand "
             "which data type you are collecting — because the data type drives the tool.",
        build="A data collection plan, an operational definition set and a working check sheet.",
        services="KPI definition, operational definitions, check sheets, sampling, data types",
        steps=[
            ("Classify your data: continuous vs discrete, nominal vs ordinal — and why it matters.", ""),
            ("Define KPIs with operational definitions, data source and collection frequency.", ""),
            ("Design a check sheet capturing date, ticket ID, type, assignment time and defect category.", ""),
            ("Define mutually exclusive defect categories so every observation lands in exactly one.", ""),
            ("Plan sampling: how many, how often, by whom — and identify possible bias.", ""),
            ("State which KPI best reflects the customer pain point from your VOC work.", ""),
        ],
        test="Two different people reading your operational definition would record the same value for the same event.",
    ),
    dict(
        num=7, topic=3,
        title="Pareto, Run Charts, Variation, Yield, DPU, and DPMO",
        objective="Analyse process performance data to quantify and prioritise (A3, A4).",
        desc="Turn collected data into decisions. Apply the Pareto principle to find the vital "
             "few categories, use a run chart to see behaviour over time, and calculate the "
             "standard Six Sigma process metrics.",
        build="A Pareto chart, a run chart and calculated yield, DPU, DPO, DPMO and sigma level.",
        services="Pareto Chart tool (collaborative), NovaSPC, yield/DPU/DPO/DPMO, sigma level, variation",
        steps=[
            ("Build the Pareto table: category, count, percentage and cumulative percentage.", ""),
            ("In your group, open the collaborative Pareto tool — one member creates the session and shares the code, then everyone joins, brainstorms and votes to produce the live Pareto chart.",
             "https://alfredang.github.io/paretochart/"),
            ("Identify the vital few categories driving about 80% of the problem.", ""),
            ("Export your assignment-time data as CSV and plot a run chart in NovaSPC.",
             "https://alfredang.github.io/novaspc/"),
            ("Interpret the run chart for trend, shift, cluster and oscillation patterns.", ""),
            ("Calculate yield, DPU, DPO and DPMO from your defect data.", ""),
            ("Convert DPMO to a sigma level and interpret what it says about the process.", ""),
            ("Distinguish common-cause from special-cause variation and why the response differs.", ""),
        ],
        test="Your cumulative percentage column reaches 100%, and you can state the sigma level with the DPMO it came from.",
    ),
    dict(
        num=8, topic=3,
        title="Root Cause Analysis with 5 Whys, Fishbone, and Evidence",
        objective="Identify root causes of variation using structured analysis (A3).",
        desc="Move from symptom to cause. Apply the 5 Whys to drill past the obvious, organise "
             "candidate causes on a Fishbone diagram, then test each candidate against the "
             "evidence you actually collected.",
        build="A completed 5 Whys chain, a Fishbone diagram and an evidence-tested cause shortlist.",
        services="5 Whys tool, Fishbone tool, 5M categories, brainstorming, multi-voting",
        steps=[
            ("Write the problem statement precisely — the effect you are explaining.", ""),
            ("Complete a 5 Whys chain with the online 5 Whys tool, continuing until you reach an actionable cause.",
             "https://alfredang.github.io/5whys/"),
            ("Build a Fishbone diagram with the online Fishbone tool using the 5M categories: Manpower, Method, Machine, Material, Measurement.",
             "https://alfredang.github.io/fishbone/"),
            ("Brainstorm candidate causes into each category — no evaluation during generation.", ""),
            ("Use multi-voting to shortlist the most likely causes as a team.", ""),
            ("Test each shortlisted cause against your Activity 7 data — does the evidence support it?", ""),
            ("State why the team must not jump straight to solutions.", ""),
        ],
        test="Each shortlisted root cause is supported by named evidence, and your 5 Whys chain ends at something you can act on.",
    ),
]
