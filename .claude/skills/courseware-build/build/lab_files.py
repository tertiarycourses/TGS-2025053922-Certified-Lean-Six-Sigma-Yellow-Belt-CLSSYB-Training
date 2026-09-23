"""Per-lab data files and worksheet templates — the single source for labs/<lab>/data
and labs/<lab>/templates.

Each entry maps a GLOBAL lab number to the files that lab ships:
  data      — populated mock data the learner analyses (CSV)
  templates — blank/partially-blank worksheets the learner fills in (CSV)

Every populated figure derives from lab_dataset.py, so the labs, the slides, the
Learner Guide and the Case Study assessment can never disagree.
"""
import re

import lab_dataset as D


def slug(title):
    t = title.replace("Elective — ", "")
    t = re.sub(r"[^a-zA-Z0-9 ]", "", t).lower()
    return "-".join(t.split())[:60]


def dirname(num, title):
    """Folder name for a lab — lab-NN-slug. The one definition used by every builder."""
    return f"lab-{num:02d}-{slug(title)}"

TICKET_HEADER = ["ticket_id", "date", "ticket_type", "channel", "assigned_queue", "agent",
                 "assignment_time_min", "met_30min_goal", "defect_count",
                 "defect_categories", "reopened"]


def _tickets():
    return [TICKET_HEADER] + [[r[k] for k in TICKET_HEADER] for r in D.ROWS]


def _daily():
    hdr = ["date", "tickets", "mean_assignment_min", "median_assignment_min",
           "defects", "missed_30min_goal"]
    return [hdr] + [[d[k] for k in hdr] for d in D.DAILY]


def _pareto_counts():
    return [["defect_category", "count"]] + [[n, c] for n, c in D.DEFECTS]


def _voc():
    return [
        ["id", "customer_statement", "source", "date"],
        ["VOC-01", "I raised a ticket yesterday morning and nobody has picked it up.", "Employee survey", "2026-06-02"],
        ["VOC-02", "I have to keep emailing the service desk just to find out what is happening.", "Employee survey", "2026-06-02"],
        ["VOC-03", "One agent told me it was resolved but the laptop still will not connect.", "Complaint log", "2026-06-03"],
        ["VOC-04", "I had to explain the same problem three times to three different people.", "Focus group", "2026-06-04"],
        ["VOC-05", "I do not know who owns my ticket once it leaves the service desk.", "Focus group", "2026-06-04"],
        ["VOC-06", "When it is urgent I just walk over to the IT room — that is faster.", "Interview", "2026-06-05"],
        ["VOC-07", "Please just tell me realistically when it will be fixed.", "Employee survey", "2026-06-05"],
        ["VOC-08", "My ticket was closed without anyone telling me what was done.", "Complaint log", "2026-06-08"],
        ["VOC-09", "The portal asks for information you cannot possibly know.", "Interview", "2026-06-09"],
        ["VOC-10", "It gets bounced between teams and restarts each time.", "Focus group", "2026-06-10"],
    ]


def _waste_walk():
    return [
        ["obs_id", "observation", "process_step", "time_lost_min", "waste_type"],
        ["W-01", "Ticket sits in the unassigned queue overnight", "Triage", 480, ""],
        ["W-02", "Agent re-keys the ticket details into the asset system", "Assignment", 6, ""],
        ["W-03", "Ticket sent to Network, returned, then sent to Desktop Support", "Routing", 95, ""],
        ["W-04", "Employee called twice to chase status", "Status update", 12, ""],
        ["W-05", "Senior engineer resets passwords that the portal could self-serve", "Resolution", 20, ""],
        ["W-06", "38 tickets waiting in the backlog at the start of the shift", "Triage", 0, ""],
        ["W-07", "Agent switches between four systems to complete one ticket", "Resolution", 9, ""],
        ["W-08", "Approval collected for a standard software install", "Approval", 240, ""],
        ["W-09", "Ticket reopened because the fix did not hold", "Closure", 150, ""],
        ["W-10", "Weekly report produced that nobody opens", "Reporting", 60, ""],
    ]


def _process_steps():
    return [
        ["step_no", "activity", "actor", "system", "process_time_min", "wait_time_min", "handoff_to"],
        [1, "Employee logs the ticket", "Employee", "Self-service portal", 5, 0, "Service Desk"],
        [2, "Ticket lands in the unassigned queue", "System", "ITSM", 0, 38, "Triage agent"],
        [3, "Triage agent reviews and categorises", "Triage agent", "ITSM", 6, 4, "Triage agent"],
        [4, "Agent decides the specialist queue", "Triage agent", "ITSM", 4, 7, "Specialist queue"],
        [5, "Specialist queue accepts the ticket", "Specialist", "ITSM", 3, 52, "Specialist"],
        [6, "Specialist resolves the issue", "Specialist", "ITSM + asset tools", 34, 0, "Employee"],
        [7, "Ticket closed and employee notified", "Specialist", "ITSM", 2, 0, ""],
    ]


def _fivewhys_template():
    return [
        ["why_level", "question", "answer", "evidence_needed", "evidence_found"],
        [1, "Why is ticket assignment delayed?", "", "", ""],
        [2, "Why?", "", "", ""],
        [3, "Why?", "", "", ""],
        [4, "Why?", "", "", ""],
        [5, "Why?", "", "", ""],
        ["", "Root cause (actionable):", "", "", ""],
    ]


def _fishbone_template():
    rows = [["category", "possible_cause", "supported_by_evidence"]]
    for cat in ["Manpower", "Method", "Machine", "Material", "Measurement"]:
        for _ in range(3):
            rows.append([cat, "", ""])
    return rows


def _rc_evidence():
    """Evidence the team gathered while investigating delayed assignment."""
    return [
        ["evidence_id", "observation", "source", "supports_cause"],
        ["E-01", "Mean assignment time rose from 44 min (days 1-6) to 72 min (days 7-10)", "daily-summary.csv", ""],
        ["E-02", "The ITSM server migration went live on 9 June 2026", "Change log", ""],
        ["E-03", "Only 2 of 5 triage agents were rostered on 10-12 June", "Duty roster", ""],
        ["E-04", "No documented rule states how quickly a ticket must be assigned", "Process audit", ""],
        ["E-05", "18 tickets were routed to the wrong specialist queue and came back", "defect-counts.csv", ""],
        ["E-06", "The portal does not make the asset tag a required field", "System inspection", ""],
        ["E-07", "30 tickets were logged with missing information", "defect-counts.csv", ""],
        ["E-08", "Triage is not assigned to a named owner at peak times", "Interview", ""],
    ]


def _candidates():
    return [
        ["solution_id", "candidate_solution", "est_cost", "est_effort_days"],
        ["S-1", "Mandatory triage checklist before a ticket can be assigned", "Low", 3],
        ["S-2", "Make asset tag and impact required fields in the portal", "Low", 5],
        ["S-3", "Named triage owner on every shift", "Low", 1],
        ["S-4", "Auto-routing rules based on ticket type", "Medium", 15],
        ["S-5", "Replace the ITSM platform", "High", 120],
    ]


def _control_plan_template():
    return [
        ["process_step", "metric", "target", "owner", "check_frequency", "response_plan"],
        ["Triage", "Mean assignment time", "< 30 min", "", "Daily", ""],
        ["Triage", "Tickets unassigned > 60 min", "0", "", "Daily", ""],
        ["Routing", "Wrong-queue defects", "< 2 per week", "", "Weekly", ""],
        ["Closure", "Reopened tickets", "< 1%", "", "Weekly", ""],
        ["", "", "", "", "", ""],
    ]


# --------------------------------------------------------------- per-lab map
LAB_FILES = {
    1: dict(
        templates={
            "yellow-belt-responsibilities.csv": [
                ["responsibility", "your_contribution", "belt_that_leads_it"],
                ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]],
            "belt-pathway-comparison.csv": [
                ["belt", "typical_role", "training_days", "leads_or_supports", "typical_project_scope"],
                ["White", "", "", "", ""], ["Yellow", "", "", "", ""], ["Green", "", "", "", ""],
                ["Black", "", "", "", ""], ["Master Black Belt", "", "", "", ""]],
            "project-selection-criteria.csv": [
                ["criterion", "does_the_scenario_meet_it", "evidence"],
                ["Part of day-to-day work", "", ""],
                ["Small and manageable", "", ""],
                ["Aligned to business goals", "", ""],
                ["Data is available", "", ""]],
        },
        note="The scenario brief and the two weeks of ticket data are in data/."),
    2: dict(
        data={"voice-of-customer.csv": _voc, "waste-walk-observations.csv": _waste_walk},
        templates={
            "voc-to-ctq.csv": [["voc_id", "customer_statement", "need", "ctq_requirement", "measure", "target"],
                               ["VOC-01", "", "", "", "", ""], ["VOC-02", "", "", "", "", ""],
                               ["VOC-03", "", "", "", "", ""], ["VOC-04", "", "", "", "", ""],
                               ["VOC-05", "", "", "", "", ""]],
            "value-added-analysis.csv": [["step_no", "activity", "VA_BVA_NVA", "justification"],
                                         [1, "", "", ""], [2, "", "", ""], [3, "", "", ""],
                                         [4, "", "", ""], [5, "", "", ""], [6, "", "", ""], [7, "", "", ""]],
        },
        note="Tag every waste-walk observation with one of the eight DOWNTIME waste types."),
    3: dict(
        data={"process-steps.csv": _process_steps},
        templates={
            "sipoc.csv": [["suppliers", "inputs", "process_step", "outputs", "customers"],
                          ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
                          ["", "", "", "", ""], ["", "", "", "", ""]],
            "handoff-register.csv": [["handoff_no", "from_actor", "to_actor", "trigger", "owner_both_sides", "pain_point"],
                                     [1, "", "", "", "", ""], [2, "", "", "", "", ""], [3, "", "", "", "", ""]],
        },
        note="data/process-steps.csv holds the as-is step, actor, system and timing data."),
    4: dict(
        templates={"pdca-charter.csv": [
            ["section", "content"],
            ["Problem statement (process, period, measurable issue, impact — no solution)", ""],
            ["Goal statement (metric, baseline, target, date)", ""],
            ["In scope", ""], ["Out of scope", ""],
            ["Stakeholders and their interest", ""],
            ["Plan", ""], ["Do", ""], ["Check", ""], ["Act — decision rule (adopt/adapt/abandon)", ""]]},
        note="Baseline figures for the goal statement come from data/daily-summary.csv."),
    5: dict(
        templates={
            "dmaic-phase-table.csv": [["phase", "purpose", "key_deliverable", "yellow_belt_support_role"],
                                      ["Define", "", "", ""], ["Measure", "", "", ""], ["Analyze", "", "", ""],
                                      ["Improve", "", "", ""], ["Control", "", "", ""]],
            "stakeholder-map.csv": [["stakeholder", "interest", "influence_H_M_L", "interest_H_M_L", "engagement_approach"],
                                    ["Service desk manager", "", "", "", ""], ["Triage agents", "", "", "", ""],
                                    ["Specialist queues", "", "", "", ""], ["Employees (customers)", "", "", "", ""],
                                    ["Green Belt project lead", "", "", "", ""]],
        }),
    6: dict(
        data={"daily-summary.csv": _daily},
        templates={
            "data-collection-plan.csv": [["kpi", "operational_definition", "data_type", "data_source", "frequency", "who_collects", "bias_risk"],
                                         ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]],
            "check-sheet.csv": [["date", "ticket_id", "ticket_type", "assignment_time_min", "defect_category", "rework_required", "notes"],
                                ["", "", "", "", "", "", ""]],
        },
        note="data/service-desk-tickets.csv is the full two-week extract (400 tickets)."),
    7: dict(
        data={"defect-counts.csv": _pareto_counts, "daily-summary.csv": _daily},
        templates={
            "pareto-table.csv": [["defect_category", "count", "percent", "cumulative_percent"],
                                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""],
                                 ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
            "process-metrics.csv": [["metric", "formula", "your_calculation"],
                                    ["Units", "Total tickets", ""],
                                    ["Defective units", "Tickets with >= 1 defect", ""],
                                    ["Total defects", "Sum of all defects", ""],
                                    ["Opportunities per unit", "Given", "6"],
                                    ["Yield %", "(Units - Defective) / Units x 100", ""],
                                    ["DPU", "Defects / Units", ""],
                                    ["DPO", "Defects / (Units x Opportunities)", ""],
                                    ["DPMO", "DPO x 1,000,000", ""],
                                    ["Sigma level", "From the DPMO conversion table", ""]],
        },
        note="Upload data/assignment-times.csv to NovaSPC for the run chart. Worked answers are in "
             "solution/pareto-table-answers.csv and solution/process-metrics-answers.csv — "
             "attempt the lab before opening them."),
    8: dict(
        data={"defect-counts.csv": _pareto_counts, "daily-summary.csv": _daily,
              "root-cause-evidence.csv": _rc_evidence},
        templates={"five-whys.csv": _fivewhys_template(), "fishbone-causes.csv": _fishbone_template(),
                   "cause-evidence-test.csv": [["candidate_cause", "evidence_that_supports_it", "evidence_that_contradicts_it", "verdict"],
                                               ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]},
        note="Test every candidate cause against the Activity 7 data before shortlisting it."),
    9: dict(
        templates={
            "countermeasures.csv": [["root_cause", "countermeasure", "type_5S_pokayoke_standardwork", "impact_H_M_L", "effort_H_M_L", "expected_effect"],
                                    ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]],
            "5s-plan.csv": [["S", "what_it_means_here", "action", "owner"],
                            ["Sort", "", "", ""], ["Set in order", "", "", ""], ["Shine", "", "", ""],
                            ["Standardise", "", "", ""], ["Sustain", "", "", ""]],
        }),
    10: dict(
        templates={"control-plan.csv": _control_plan_template(),
                   "a3-summary.csv": [["a3_section", "content"],
                                      ["Background", ""], ["Current state", ""], ["Goal", ""],
                                      ["Root cause analysis", ""], ["Countermeasures", ""],
                                      ["Results", ""], ["Follow-up and handover", ""]],
                   "handover-checklist.csv": [["handover_item", "accepted_by", "date", "notes"],
                                              ["Control plan", "", "", ""], ["Standard work", "", "", ""],
                                              ["Visual management board", "", "", ""], ["A3 summary", "", "", ""]]},
        note="Re-plot data/assignment-times.csv in NovaSPC to show the post-improvement position."),
    11: dict(
        data={"voice-of-customer.csv": _voc},
        templates={"affinity-groups.csv": [["voc_id", "statement", "affinity_group"], ["", "", ""]],
                   "kano-classification.csv": [["requirement", "kano_class_MustBe_OneDim_Delighter", "why", "invest_first"],
                                               ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]}),
    12: dict(
        data={"process-steps.csv": _process_steps},
        templates={"value-stream-map.csv": [["step_no", "activity", "process_time_min", "wait_time_min", "VA_or_NVA"],
                                            [1, "", "", "", ""], [2, "", "", "", ""], [3, "", "", "", ""],
                                            [4, "", "", "", ""], [5, "", "", "", ""], [6, "", "", "", ""], [7, "", "", "", ""]],
                   "takt-time.csv": [["input", "value"],
                                     ["Available working time per day (min)", "450"],
                                     ["Customer demand per day (tickets)", "40"],
                                     ["Takt time (min per ticket)", ""],
                                     ["Total process time (min)", ""], ["Total lead time (min)", ""],
                                     ["Process cycle efficiency %", ""]]}),
    13: dict(
        data={"candidate-solutions.csv": _candidates},
        templates={"solution-selection-matrix.csv": [["solution", "impact_w5", "cost_w3", "ease_w2", "weighted_score", "rank"],
                                                     ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]],
                   "fmea.csv": [["process_step", "failure_mode", "effect", "cause", "severity_1_10", "occurrence_1_10", "detection_1_10", "RPN", "action"],
                                ["", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""]]}),
    14: dict(
        data={"daily-summary.csv": _daily},
        templates={"descriptive-statistics.csv": [["statistic", "formula_or_function", "your_value"],
                                                  ["Mean", "AVERAGE(range)", ""], ["Median", "MEDIAN(range)", ""],
                                                  ["Mode", "MODE(range)", ""], ["Range", "MAX - MIN", ""],
                                                  ["Standard deviation", "STDEV.S(range)", ""],
                                                  ["What the mean-vs-median gap tells you", "", ""]],
                   "implementation-plan.csv": [["action", "owner", "start_date", "due_date", "barrier", "mitigation"],
                                               ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]},
        note="data/assignment-times.csv is the raw column for the statistics."),
}

# Labs that analyse the full ticket extract / raw assignment-time column
FULL_EXTRACT_LABS = [1, 6, 7, 14]
ASSIGNMENT_COLUMN_LABS = [7, 10, 14]


def files_for(num):
    """Return (data_files, template_files, note) for a lab number."""
    spec = LAB_FILES.get(num, {})
    data = {}
    for name, fn in (spec.get("data") or {}).items():
        data[name] = fn() if callable(fn) else fn
    if num in FULL_EXTRACT_LABS:
        data["service-desk-tickets.csv"] = _tickets()
    if num in ASSIGNMENT_COLUMN_LABS:
        data["assignment-times.csv"] = [["date", "ticket_id", "assignment_time_min"]] + \
            [[r["date"], r["ticket_id"], r["assignment_time_min"]] for r in D.ROWS]
    return data, (spec.get("templates") or {}), spec.get("note", "")
