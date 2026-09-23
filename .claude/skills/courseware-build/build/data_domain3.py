"""
Domain 3 — Improve and Control the Process.

Activities 9-10 (assessed core) plus optional stretch activities imported from the
original v20 trainer deck so no activity from the original course is lost:
Affinity Diagram, Kano Analysis, Project Charter, VSM, Takt Time, Descriptive
Statistics, Benchmarking, Solution Selection Matrix, FMEA and Implementation Plan.
"""

DOMAIN3 = [
    dict(
        num=9, topic=4,
        title="Countermeasures, 5S, Mistake Proofing, Standard Work, and Kaizen",
        objective="Recommend improvement actions that address the proven root cause (A5).",
        desc="Generate and select countermeasures that attack the root cause you proved — not "
             "the symptom. Apply the core Lean improvement tools: 5S, poka-yoke, visual "
             "management, standard work and Kaizen.",
        build="A prioritised countermeasure set with a 5S plan, a poka-yoke design and standard work.",
        services="Brainstorming, 5S, poka-yoke, visual management, standard work, Kaizen",
        steps=[
            ("Generate countermeasures for each proven root cause — quantity before quality.", ""),
            ("Prioritise using an impact vs effort matrix to find the quick wins.", ""),
            ("Apply 5S thinking — Sort, Set in order, Shine, Standardise, Sustain — including to digital work.", ""),
            ("Design one poka-yoke that makes the error difficult or impossible to make.", ""),
            ("Draft standard work so the improved method is repeatable by anyone.", ""),
            ("Plan a Kaizen event or pilot to test the countermeasure at small scale first.", ""),
            ("Distinguish a containment countermeasure from a permanent solution.", ""),
        ],
        test="Every countermeasure traces back to a proven root cause, and your poka-yoke prevents rather than detects the error.",
    ),
    dict(
        num=10, topic=5,
        title="Control Plan, A3 Summary, Handover, and Certification Readiness",
        objective="Recommend control actions to sustain process performance (A5).",
        desc="Hold the gain. Build a control plan that names the metric, the target, the "
             "monitoring frequency, the owner and the reaction plan — then tell the whole "
             "improvement story on a single A3 page and hand it over.",
        build="A control plan, an A3 one-page summary, a handover checklist and a readiness plan.",
        services="Control plan, SPC thinking, visual management, A3 report, handover",
        steps=[
            ("Create the control plan: metric, target, monitoring method, frequency, owner, reaction plan.", ""),
            ("Define the visual management approach — board, dashboard or huddle — that keeps it visible.", ""),
            ("Specify the reaction plan: exactly what happens when a metric falls outside target.", ""),
            ("Write the A3 summary: background, current state, goal, analysis, countermeasures, results, follow-up.", ""),
            ("Prepare the handover checklist so the process owner can sustain it without you.", ""),
            ("Complete your personal certification readiness plan — which topics need most review.", ""),
        ],
        test="Every control plan row has a named owner and a reaction plan, and your A3 fits on one page.",
    ),
    # ---------------- optional stretch activities (from the original v20 deck) ----------------
    dict(
        num=11, topic=1, elective=True,
        title="Elective — Affinity Diagram and Kano Analysis",
        objective="Organise customer requirements and classify them by satisfaction impact (K2).",
        desc="Two Define-phase tools from the original course. Use an Affinity Diagram to "
             "cluster unstructured VOC input into themes, then apply Kano Analysis to classify "
             "requirements as Must-Be, One-Dimensional or Delighter.",
        build="An Affinity Diagram of clustered VOC themes and a Kano classification table.",
        services="Affinity Diagram, Kano Analysis, VOC clustering",
        steps=[
            ("Write each VOC statement on a separate note — one idea per note.", ""),
            ("Cluster related notes into natural groups without talking, then name each group.", ""),
            ("Classify each requirement as Must-Be, One-Dimensional or Delighter.", ""),
            ("Plot the requirements on the Kano diagram and identify where to invest first.", ""),
        ],
        test="Every VOC note sits in exactly one named affinity group and carries a Kano classification.",
    ),
    dict(
        num=12, topic=2, elective=True,
        title="Elective — Value Stream Map and Takt Time",
        objective="Quantify flow, lead time and takt time across the value stream (A3, A4).",
        desc="Extend process mapping into Lean metrics. Map the value stream with process and "
             "wait times, calculate process cycle efficiency, then compute takt time to see "
             "whether the process can meet customer demand.",
        build="A value stream map with lead time, process time and a calculated takt time.",
        services="SIPOC & Process Map Builder, value stream mapping, lead time, WIP, takt time",
        steps=[
            ("Map the value stream: each step with its process time and the wait time between steps. Start from your Activity 3 process map.",
             "https://alfredang.github.io/sipoc/"),
            ("Total the value-added time and the lead time, then compute process cycle efficiency.", ""),
            ("Calculate takt time = available working time / customer demand.", ""),
            ("Compare cycle time against takt time to identify the bottleneck step.", ""),
        ],
        test="Your lead time equals the sum of all process and wait times, and takt time is expressed per unit.",
    ),
    dict(
        num=13, topic=4, elective=True,
        title="Elective — Solution Selection Matrix, Benchmarking, and FMEA",
        objective="Evaluate and de-risk candidate solutions before implementation (A5, K2).",
        desc="Three Improve-phase tools from the original course. Score solutions against "
             "weighted criteria, benchmark against outstanding practice, and use FMEA to find "
             "how a proposed change could fail before it does.",
        build="A scored solution selection matrix, a benchmarking summary and an FMEA with RPN.",
        services="Solution selection matrix, benchmarking, FMEA, RPN scoring",
        steps=[
            ("Agree the selection criteria and weight each by importance.", ""),
            ("Score every candidate solution against the weighted criteria and rank the results.", ""),
            ("Benchmark your process against an internal or external reference and note the gap.", ""),
            ("Build an FMEA: failure mode, effect, cause, then score Severity, Occurrence and Detection.", ""),
            ("Calculate RPN = S x O x D and address the highest-RPN failure modes first.", ""),
        ],
        test="Your matrix ranks solutions by weighted score, and every FMEA row has an RPN and an action for the highest scores.",
    ),
    dict(
        num=14, topic=5, elective=True,
        title="Elective — Descriptive Statistics and Implementation Planning",
        objective="Summarise data numerically and plan the rollout (A4, A5).",
        desc="Close the loop. Compute the measures of central tendency and dispersion that "
             "describe your data, then convert the selected countermeasures into a dated "
             "implementation plan with owners and barriers identified.",
        build="A descriptive statistics summary and a dated implementation plan.",
        services="Mean, median, range, standard deviation, implementation planning",
        steps=[
            ("Compute the mean and median for your assignment-time data and compare them.", ""),
            ("Compute the range and standard deviation to describe the spread.", ""),
            ("Explain what the mean-versus-median difference reveals about outliers and skew.", ""),
            ("Write the implementation plan: action, owner, date, barriers and mitigation.", ""),
        ],
        test="You can explain why the mean and median differ in your data, and every implementation action has an owner and a date.",
    ),
]
