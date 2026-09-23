#!/usr/bin/env python3
"""Lean Six Sigma teaching content — the concept slides, in DMAIC order.

Each function renders the concept slides for one part of the course. Every key
concept is explained VISUALLY (diagram, chart, matrix, timeline) rather than as a
wall of bullets, per the house design standard. Content is grounded in the CSSC
"Six Sigma: A Complete Step-by-Step Guide" and the original v20 trainer deck.
"""
from pptx.util import Inches, Pt
from components import (BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT, WHITE,
                        LINE, DMAIC_COLORS)


# ============================================================ FOUNDATIONS
def foundations(d):
    C = d.C
    d.section("FOUNDATIONS", "Six Sigma Foundations", "00",
              "Quality · Lean · Six Sigma · Lean Six Sigma · Belt roles · The DMAIC roadmap")

    # ---- What is Quality
    d.big_statement("What is Quality?",
                    "Before we can improve quality, we have to agree what the word actually means.",
                    "FOUNDATIONS · QUALITY", color=BLUE)
    d.compare_panels("Three Common Answers — and Why Only One Holds Up", [
        ("Defect-free output", "\"Quality means zero defects\"",
         ["Necessary, but not sufficient.",
          "A product can be flawless and still not sell.",
          "Defect-free against WHOSE standard?"]),
        ("Meeting set standards", "\"Quality means meeting the spec\"",
         ["Better — it is measurable.",
          "But a spec can be set at the wrong level.",
          "Meeting a spec nobody wants is waste."]),
        ("Meeting customer expectations", "\"Quality means the customer is satisfied\"",
         ["This is the Six Sigma definition.",
          "The customer sets the standard.",
          "Everything else follows from this."]),
    ], kicker="WHAT IS QUALITY?", accent=BLUE)
    d.tile_grid("Quality in a Nutshell", [
        ("Understand requirements", "Find out what the customer actually needs — in their own words."),
        ("Design to satisfy them", "Build the product or service so it meets those requirements."),
        ("Deliver consistently", "Reduce variation so every customer gets the same experience."),
        ("Improve continuously", "Requirements move; the process has to keep up."),
    ], kicker="FOUR KEY ACTIVITIES", cols=2, size=15)

    # ---- What is Lean
    d.big_statement("What is Lean?",
                    "Lean maximises customer value by systematically removing everything the customer would not pay for.",
                    "FOUNDATIONS · LEAN", color=TEAL)
    d.tile_grid("Lean — The Core Idea", [
        ("Origin", "The Toyota Production System — refined in Japanese manufacturing from the 1950s."),
        ("Focus", "Speed and flow: shorten the time from customer request to delivery."),
        ("Enemy", "Waste (muda) — any effort that consumes resources but creates no customer value."),
        ("Method", "See the process, find the waste, remove it, then standardise the improvement."),
        ("Applies to", "Manufacturing AND service — hospitals, banks, IT service desks, government."),
        ("Yellow Belt use", "Waste walks, process mapping, 5S and small Kaizen improvements."),
    ], kicker="WHAT IS LEAN?", cols=2, size=14, accent=TEAL)
    d.flow_h("The Five Lean Principles", [
        "Specify VALUE from the customer's point of view",
        "Map the VALUE STREAM and expose the waste in it",
        "Create FLOW so work moves without interruption",
        "Let the customer PULL work rather than pushing it",
        "Pursue PERFECTION through continuous improvement",
    ], kicker="LEAN · FIVE PRINCIPLES", color=TEAL)

    # ---- What is Six Sigma
    d.big_statement("What is Six Sigma?",
                    "A disciplined, data-driven method to reduce variation and defects — so the process delivers the same result every time.",
                    "FOUNDATIONS · SIX SIGMA", color=VIOLET)
    d.tile_grid("Six Sigma — The Core Idea", [
        ("Origin", "Motorola, 1986 — later made famous by General Electric under Jack Welch."),
        ("Focus", "Consistency: reduce the variation that creates defects."),
        ("Enemy", "Variation — the spread that turns a good average into an unreliable experience."),
        ("Method", "DMAIC, driven by data and statistics rather than opinion."),
        ("The target", "No more than 3.4 defects per million opportunities (DPMO)."),
        ("Yellow Belt use", "Data collection, Pareto and run charts, root cause analysis."),
    ], kicker="WHAT IS SIX SIGMA?", cols=2, size=14, accent=VIOLET)
    d.normal_curve("Six Sigma as Standard Deviation",
                   kicker="THE STATISTICAL MEANING",
                   note="Sigma (σ) measures spread. The more sigmas that fit between the process mean and the "
                        "specification limits, the less likely the process is to produce a defect.")
    d.ladder("Sigma Level vs Defects per Million Opportunities", [
        ("1σ", "690,000 DPMO\n31% yield"),
        ("2σ", "308,000 DPMO\n69% yield"),
        ("3σ", "66,800 DPMO\n93.3% yield"),
        ("4σ", "6,210 DPMO\n99.38% yield"),
        ("5σ", "233 DPMO\n99.977% yield"),
        ("6σ", "3.4 DPMO\n99.99966% yield"),
    ], kicker="WHY 'SIX' SIGMA", accent=VIOLET,
        note="Each sigma level is a step change, not an increment — moving 3σ → 4σ removes about 90% of the defects.")
    d.two_col("Why 99% Is Not Good Enough",
              [("At 99% quality (about 3.8σ)", 0),
               ("20,000 lost articles of mail per hour", 1),
               ("Unsafe drinking water almost 15 minutes a day", 1),
               ("5,000 incorrect surgical operations per week", 1),
               ("Two short or long landings at major airports daily", 1)],
              [("At Six Sigma quality (3.4 DPMO)", 0),
               ("7 lost articles of mail per hour", 1),
               ("Unsafe drinking water 1 minute every 7 months", 1),
               ("1.7 incorrect surgical operations per week", 1),
               ("One short or long landing every 5 years", 1)],
              kicker="THE COST OF 'GOOD ENOUGH'", lhead="99% quality", rhead="99.99966% quality",
              lcolor=RED, rcolor=TEAL)

    # ---- Lean + Six Sigma
    d.vs_diagram("Lean vs Six Sigma vs Lean Six Sigma",
                 ("Lean", ["Removes waste", "Improves speed and flow",
                           "Question: is this step worth doing?", "Tools: VSM, 5S, Kaizen, poka-yoke"]),
                 ("Six Sigma", ["Reduces variation", "Improves consistency and accuracy",
                                "Question: why does the result vary?", "Tools: DMAIC, Pareto, SPC, root cause"]),
                 ("Lean Six Sigma",
                  "Faster AND more consistent — remove the waste, then control the variation that remains."),
                 kicker="THE COMBINED METHOD")
    d.timeline("A Short History of Lean Six Sigma", [
        ("1950s", "Toyota Production System — Lean is born"),
        ("1986", "Motorola coins Six Sigma"),
        ("1995", "GE adopts Six Sigma company-wide"),
        ("2000s", "Lean and Six Sigma merge"),
        ("Today", "Applied across service, healthcare, finance and IT"),
    ], kicker="HISTORY", accent=AMBER)
    d.big_statement("Y = f(X)",
                    "The output Y is a function of the process inputs X. To change the result, change the inputs that drive it — not the result itself.",
                    "THE CENTRAL EQUATION", color=BLUE)
    d.tile_grid("Y = f(X) in Practice — The Contoso Service Desk", [
        ("Y — the output", "Ticket assignment time, measured in hours from submission to assignment."),
        ("X — triage rules", "How clearly the routing rules are written and understood."),
        ("X — staffing", "How many agents are available at peak submission times."),
        ("X — ticket quality", "How complete the information is when the ticket arrives."),
    ], kicker="OUR COURSE SCENARIO", cols=2, size=14)

    # ---- Belt roles
    d.ladder("The Lean Six Sigma Belt Pathway", [
        ("White Belt", "Awareness of Six Sigma; supports local problem solving"),
        ("Yellow Belt", "Knows the basic tools; supports projects and runs small improvements"),
        ("Green Belt", "Leads smaller projects; assists Black Belts with analysis"),
        ("Black Belt", "Leads complex projects full time; coaches Green and Yellow Belts"),
        ("Master Black Belt", "Trains and mentors Belts; owns deployment strategy"),
    ], kicker="WHO DOES WHAT", accent=BLUE,
        note="This course certifies you at Yellow Belt — the level that supports projects and runs small improvements.")
    d.tile_grid("Your Role — the Lean Six Sigma Yellow Belt", [
        ("Has basic knowledge", "Understands the DMAIC roadmap and the 7 basic quality tools."),
        ("Supports the project", "Contributes process knowledge as the subject-matter expert."),
        ("Collects the data", "Runs check sheets and data collection under the project leader."),
        ("Maps the process", "Builds SIPOC and process maps that expose handoffs and waste."),
        ("Runs small improvements", "Leads Kaizen or PDCA improvements within their own work area."),
        ("Does not lead DMAIC", "Larger, cross-functional DMAIC projects belong to a Green or Black Belt."),
    ], kicker="LSS YELLOW BELT", cols=2, size=14, accent=AMBER)

    # ---- DMAIC roadmap
    d.dmaic_wheel("The DMAIC Roadmap", [
        ("D", "Define", ["Define the problem", "Capture VOC and CTQ", "Charter and scope", "Map with SIPOC"]),
        ("M", "Measure", ["Plan data collection", "Measure the baseline", "Calculate yield/DPMO", "Find the waste"]),
        ("A", "Analyze", ["Analyse the data", "Pareto and run charts", "5 Whys and Fishbone", "Prove the root cause"]),
        ("I", "Improve", ["Generate solutions", "Select and pilot", "5S and poka-yoke", "Standardise the work"]),
        ("C", "Control", ["Build the control plan", "Visual management", "Hand over to the owner", "Sustain the gain"]),
    ], kicker="THE COURSE ROADMAP · WE FOLLOW THIS ORDER")
    d.two_col("DMAIC vs PDCA — Which One Do I Use?",
              [("PDCA — Plan, Do, Check, Act", 0),
               ("For small, local, fast improvements", 1),
               ("Days to a few weeks", 1),
               ("A Yellow Belt can run this", 1),
               ("Lower data requirement", 1),
               ("Used in Activity 4", 1)],
              [("DMAIC — the full roadmap", 0),
               ("For larger, cross-functional problems", 1),
               ("Weeks to months", 1),
               ("Led by a Green or Black Belt", 1),
               ("Data and statistics required", 1),
               ("Supported by you from Activity 5 onward", 1)],
              kicker="CHOOSING YOUR APPROACH", lhead="Small improvement", rhead="Full project",
              lcolor=TEAL, rcolor=BLUE)
    d.flow_h("PDCA — The Small Improvement Cycle", [
        "PLAN — define the problem and plan the change",
        "DO — run the change at small scale",
        "CHECK — measure whether it actually worked",
        "ACT — adopt, adapt or abandon, then repeat",
    ], kicker="PDCA CYCLE", color=TEAL)
    d.tile_grid("What Makes a Good Yellow Belt Project?", [
        ("Related to your daily work", "You know the process and can observe it directly."),
        ("Manageable in timeframe", "Can be completed in weeks, not months."),
        ("Aligned to business goals", "Someone in management cares about the result."),
        ("Data is available", "You can measure the baseline and the improvement."),
    ], kicker="PROJECT SELECTION", cols=2, size=15, accent=TEAL)


# ============================================================ DEFINE
def define_phase(d):
    d.big_statement("Define — What problem are we solving, and for whom?",
                    "The Define phase converts a vague complaint into a scoped, measurable problem statement everyone agrees on.",
                    "DMAIC · D — DEFINE", color=DMAIC_COLORS[0])
    d.flow_h("Steps in the Define Phase", [
        "Capture the Voice of the Customer",
        "Translate VOC into CTQ requirements",
        "Write the problem and goal statements",
        "Charter and scope the project",
        "Map the process with SIPOC",
    ], kicker="DEFINE · ROADMAP", color=DMAIC_COLORS[0])

    # VOC
    d.big_statement("Voice of the Customer (VOC)",
                    "The needs and expectations of the customer, expressed in the customer's own language.",
                    "DEFINE · VOC", color=BLUE)
    d.tile_grid("Where VOC Comes From", [
        ("Surveys", "Structured and at scale, but limited to the questions you thought to ask."),
        ("Interviews", "Rich and open-ended; best for understanding the 'why' behind a complaint."),
        ("Complaints & tickets", "Already in your system — the cheapest and most honest VOC source."),
        ("Direct observation", "Go and watch the work happen; customers cannot always articulate the problem."),
    ], kicker="SOURCES OF VOC", cols=2, size=15)
    d.two_col("VOC → Need → CTQ: The Translation",
              [("The customer says (VOC)", 0),
               ("\"I don't want to wait too long\"", 1),
               ("\"I don't want cold pizza\"", 1),
               ("\"I never know where my ticket is\"", 1),
               ("Vague, emotional, unmeasurable", 1)],
              [("The measurable requirement (CTQ)", 0),
               ("Delivery in 30 minutes or less", 1),
               ("Pizza at 32°C minimum on arrival", 1),
               ("Status update within 4 working hours", 1),
               ("Specific, numeric, testable", 1)],
              kicker="THE CTQ TRANSLATION", lhead="Voice of the Customer", rhead="Critical to Quality",
              lcolor=AMBER, rcolor=TEAL)
    d.tile_grid("What Makes a Good CTQ?", [
        ("Specific", "Names exactly one characteristic of the output."),
        ("Measurable", "Has a number and a unit you can actually record."),
        ("Linked to VOC", "Traces back to something a customer genuinely said."),
        ("Has a target and limit", "States the target value and the acceptable range around it."),
    ], kicker="CTQ QUALITY CHECK", cols=2, size=15, accent=TEAL)

    # Charter
    d.tile_grid("The Project Charter", [
        ("Business case", "Why this project matters and what it is worth."),
        ("Problem statement", "What is wrong, quantified, over a stated time period."),
        ("Goal statement", "Metric, baseline, target and date."),
        ("Scope", "What is in, and explicitly what is out."),
        ("Team and roles", "Sponsor, project leader, Yellow Belt support and SMEs."),
        ("Milestones", "The dates each DMAIC phase is expected to complete."),
    ], kicker="DEFINE · THE PROJECT'S CONTRACT", cols=2, size=14)
    d.two_col("Problem Statements — Good vs Bad",
              [("Weak problem statement", 0),
               ("\"The service desk is too slow.\"", 1),
               ("No process named", 1),
               ("No time period", 1),
               ("No measure or baseline", 1),
               ("No customer impact stated", 1),
               ("Hints at a solution (\"we need more staff\")", 1)],
              [("Strong problem statement", 0),
               ("\"Between 1 Jan and 31 Mar, tickets took an average of 9.4 working hours to be assigned against a 4-hour target, affecting 38% of employees and generating 210 chase-up contacts.\"", 1),
               ("Process, period, measure, baseline and impact — and no solution.", 1)],
              kicker="WRITING THE PROBLEM STATEMENT", lhead="Avoid this", rhead="Aim for this",
              lcolor=RED, rcolor=TEAL)
    d.tile_grid("The Four Components of a Problem Statement", [
        ("What", "The specific process and the defect or gap observed."),
        ("When", "The time period the data covers."),
        ("How much", "The measured baseline against the requirement."),
        ("So what", "The impact on the customer and the business."),
    ], kicker="PROBLEM STATEMENT ANATOMY", cols=2, size=15, accent=BLUE)

    # SIPOC + process mapping
    d.big_statement("SIPOC — the macro 'as-is' map",
                    "One page that shows who supplies the process, what goes in, what happens, what comes out, and who receives it.",
                    "DEFINE · SIPOC", color=TEAL)
    d.sipoc_diagram("SIPOC — Contoso Service Desk Ticket Assignment", [
        ["Employees", "Line managers", "HR onboarding", "Monitoring tools"],
        ["Ticket form", "Category", "Priority", "Asset details", "Contact info"],
        ["1. Ticket submitted", "2. Auto-categorised", "3. Triage review", "4. Assigned to agent", "5. Agent acknowledges"],
        ["Assigned ticket", "Assignment notification", "Priority classification", "SLA clock started"],
        ["Employee", "Support agent", "Service desk manager", "IT leadership"],
    ], kicker="DEFINE · WORKED EXAMPLE")
    d.flow_h("How to Build a SIPOC", [
        "Name the process and agree its start and stop points",
        "List the high-level steps — 5 to 7, no more",
        "Identify the outputs and who receives them",
        "Identify the inputs each step needs",
        "Identify who supplies each input",
    ], kicker="SIPOC · METHOD", color=TEAL)
    d.tile_grid("Why Process Maps Matter", [
        ("Shows the real process", "Not the process in the procedure manual — the one people actually follow."),
        ("Exposes handoffs", "Delay and defects are usually created where work changes hands."),
        ("Builds shared understanding", "The team often discovers they each believed a different process."),
        ("Finds the waste", "Rework loops, waiting and duplicated approvals become visible."),
        ("Sets the baseline", "You cannot improve a process you have not described."),
        ("Guides data collection", "The map tells you where to put your measurement points."),
    ], kicker="DEFINE · PROCESS MAPPING", cols=2, size=14, accent=VIOLET)
    d.compare_panels("Three Levels of Process Map", [
        ("SIPOC", "Macro / 30,000 feet",
         ["5-7 steps on one page.", "Sets scope and boundaries.", "Built first, in the Define phase."]),
        ("Process flowchart", "Detailed / ground level",
         ["Every step, decision and loop.", "Uses standard symbols.", "Reveals rework and delay."]),
        ("Swimlane map", "Detailed + ownership",
         ["One lane per actor or team.", "Handoffs cross the lanes.", "Best for finding delay in handoffs."]),
    ], kicker="CHOOSING THE RIGHT MAP", accent=VIOLET)
    d.tile_grid("Standard Process Map Symbols", [
        ("Oval — Terminator", "The start or the end of the process."),
        ("Rectangle — Process step", "An activity or task being performed."),
        ("Diamond — Decision", "A yes/no branch point in the flow."),
        ("Arrow — Flow", "The direction work moves between steps."),
        ("Parallelogram — Data", "An input to, or output from, a step."),
        ("D shape — Delay", "Work waiting in a queue — usually where the waste is."),
    ], kicker="READING A PROCESS MAP", cols=2, size=14, accent=VIOLET)
    d.tile_grid("Your SIPOC & Process Map Builder", [
        ("Where", "alfredang.github.io/sipoc/ — no install, works in any browser."),
        ("Guided order", "Enter Process → Outputs → Customers → Inputs → Suppliers, the way the method teaches."),
        ("Enforces the rules", "Warns if you drift outside 5–7 steps, and tracks your pain-point count."),
        ("Tag pain points", "Waiting, rework loop, unclear ownership, duplicate entry, missing decision rule."),
        ("Swimlane for free", "Assign an actor to each step and the swimlane and handoff table build themselves."),
        ("Check my SIPOC", "Validates the same rules your activity work and assessment are marked against."),
    ], kicker="DEFINE · YOUR ONLINE TOOL", cols=2, size=13, accent=TEAL)
    d.flow_h("Using the SIPOC Builder in Activity 3", [
        "Set the process name, start point and stop point",
        "List the 5–7 process steps, then work outward to O, C, I, S",
        "Tag at least three pain points on the steps",
        "Assign an actor to each step — handoffs appear automatically",
        "Run 'Check my SIPOC', then export the PNG for your package",
    ], kicker="DEFINE · TOOL WALKTHROUGH", color=TEAL)


# ============================================================ MEASURE
def measure_phase(d):
    d.big_statement("Measure — How big is the problem, really?",
                    "The Measure phase replaces opinion with a trustworthy baseline you can improve against.",
                    "DMAIC · M — MEASURE", color=DMAIC_COLORS[1])
    d.flow_h("Steps in the Measure Phase", [
        "Identify the waste in the current process",
        "Decide what to measure and define it precisely",
        "Build the data collection plan and check sheet",
        "Collect the baseline data",
        "Calculate yield, DPMO and sigma level",
    ], kicker="MEASURE · ROADMAP", color=DMAIC_COLORS[1])

    # Waste
    d.big_statement("What is Waste?",
                    "Anything beyond the minimum information, equipment, material and effort absolutely required to add value for the customer.",
                    "MEASURE · WASTE (MUDA)", color=RED)
    d.waste_wheel("The Eight Wastes of Lean — DOWNTIME", [
        ("D", "Defects"), ("O", "Overproduction"), ("W", "Waiting"), ("N", "Non-utilised talent"),
        ("T", "Transport"), ("I", "Inventory"), ("M", "Motion"), ("E", "Extra-processing"),
    ], kicker="MEASURE · THE 8 WASTES")
    d.tile_grid("The Eight Wastes in a Service Process", [
        ("D — Defects", "Wrong ticket category, incomplete information, work that must be redone."),
        ("O — Overproduction", "Reports nobody reads; producing output before it is needed."),
        ("W — Waiting", "Tickets sitting in a queue waiting for triage or approval."),
        ("N — Non-utilised talent", "Skilled agents doing routine data entry a form could handle."),
        ("T — Transport", "Tickets bouncing between teams before reaching the right owner."),
        ("I — Inventory", "A growing backlog of unassigned tickets."),
        ("M — Motion", "Switching between four systems to resolve one ticket."),
        ("E — Extra-processing", "Approvals and checks that add no value to the customer."),
    ], kicker="DOWNTIME IN PRACTICE", cols=2, size=13, accent=RED)
    d.compare_panels("Value-Added vs Non-Value-Added", [
        ("Value-added (VA)", "The customer would pay for it",
         ["Changes the product or service.",
          "Done right the first time.",
          "The customer cares that it happened.",
          "Example: diagnosing the actual fault."]),
        ("Business-value-added (BVA)", "Required, but not by the customer",
         ["Needed for legal or regulatory reasons.",
          "Required to run the business.",
          "Minimise it — you cannot remove it.",
          "Example: mandatory audit logging."]),
        ("Non-value-added (NVA)", "Pure waste — remove it",
         ["Consumes time and resource for nothing.",
          "The customer would never pay for it.",
          "Attack this first.",
          "Example: a ticket waiting in a queue."]),
    ], kicker="MEASURE · VALUE ANALYSIS", accent=TEAL)
    d.big_statement("Waste is not the same as a defect.",
                    "A defect is an output that fails the CTQ requirement. Waste is any effort along the way that the customer would not willingly pay for. Every defect creates waste — but most waste is not a defect.",
                    "AN IMPORTANT DISTINCTION", color=AMBER)

    # Data types
    d.compare_panels("Types of Data — and Why It Matters", [
        ("Continuous data", "Measured on a scale",
         ["Any value within a range.",
          "Time, cost, temperature, length.",
          "More information per data point.",
          "Needs a smaller sample size."]),
        ("Discrete / attribute data", "Counted in whole units",
         ["Counts and categories only.",
          "Number of defects, pass/fail.",
          "Less information per data point.",
          "Needs a much larger sample."]),
    ], kicker="MEASURE · DATA TYPES", accent=BLUE)
    d.tile_grid("Nominal, Ordinal, Interval, Ratio", [
        ("Nominal", "Labels with no order — ticket category, agent name, department."),
        ("Ordinal", "Ordered categories, but the gaps are not equal — priority P1/P2/P3, satisfaction 1-5."),
        ("Interval", "Equal gaps, but no true zero — temperature in °C, calendar dates."),
        ("Ratio", "Equal gaps and a true zero — assignment time, cost, number of tickets."),
    ], kicker="THE FOUR MEASUREMENT SCALES", cols=2, size=14)
    d.big_statement("The data type decides the tool.",
                    "Choose your chart, your test and your sample size AFTER you know what kind of data you are holding — not before.",
                    "WHY THIS MATTERS", color=BLUE)

    # Data collection
    d.tile_grid("The Data Collection Plan", [
        ("What", "Which metric, and what exactly counts as one observation."),
        ("Why", "Which CTQ or problem statement this metric supports."),
        ("How", "Automated report preferred; manual capture only when unavoidable."),
        ("Who", "Someone who knows the process and is available to do it consistently."),
        ("When", "The frequency and the exact period the data covers."),
        ("How many", "The sample size — enough to be representative, not so many it is unaffordable."),
    ], kicker="MEASURE · PLANNING THE DATA", cols=2, size=14, accent=TEAL)
    d.big_statement("Operational definitions remove the argument.",
                    "\"Assignment time\" means nothing until you state it precisely: the elapsed working hours from ticket submission timestamp to the first agent assignment timestamp, excluding weekends and public holidays.",
                    "MEASURE · OPERATIONAL DEFINITIONS", color=TEAL)
    d.tile_grid("Check Sheets — the Simplest Reliable Tool", [
        ("One row per observation", "Never summarise as you collect — record the raw event."),
        ("Pre-printed categories", "Tick a box rather than writing free text; free text cannot be counted."),
        ("Mutually exclusive", "Every observation must fall into exactly one category."),
        ("Include the context", "Date, time, shift and who recorded it — you will need this later."),
    ], kicker="MEASURE · CHECK SHEETS", cols=2, size=15, accent=TEAL)
    d.tile_grid("Sampling Techniques", [
        ("Simple random", "Every unit has an equal chance of being selected."),
        ("Stratified random", "Split the population into groups, then sample randomly within each group."),
        ("Systematic", "Take every nth unit — simple, but beware of hidden cycles in the data."),
        ("Cluster", "Sample whole naturally occurring groups when individual sampling is impractical."),
    ], kicker="MEASURE · SAMPLING", cols=2, size=15)

    # Process metrics
    d.formula_card("Process Performance Metrics", [
        ("Yield", "Yield = (Good units / Total units) × 100",
         "950 of 1,000 tickets assigned on time → 95% yield"),
        ("DPU", "DPU = Defects / Units",
         "600 defects across 1,000 tickets → DPU = 0.6"),
        ("DPO", "DPO = Defects / (Units × Opportunities)",
         "600 defects, 1,000 tickets, 3 opportunities each → DPO = 0.2"),
        ("DPMO", "DPMO = DPO × 1,000,000",
         "DPO of 0.2 → 200,000 DPMO"),
    ], kicker="MEASURE · THE STANDARD METRICS", accent=VIOLET,
        note="An 'opportunity' is any single chance for a defect to occur on one unit — agree the count before you measure.")
    d.tile_grid("Yield — Three Different Questions", [
        ("Classic yield", "What fraction of units passed final inspection? Ignores any rework along the way."),
        ("First pass yield (FPY)", "What fraction passed with NO rework at any step? The honest number."),
        ("Rolled throughput yield (RTY)", "Multiply the FPY of every step — the probability a unit passes cleanly through the entire process."),
        ("Why RTY matters", "Five steps at 95% each give an RTY of only 77% — small defect rates compound fast."),
    ], kicker="MEASURE · YIELD", cols=2, size=14, accent=VIOLET)
    d.formula_card("From DPMO to Sigma Level", [
        ("Sigma level", "Look DPMO up in the sigma conversion table",
         "200,000 DPMO ≈ 2.3σ"),
        ("Our example", "Yield 99.5% → 5,000 DPMO",
         "5,000 DPMO ≈ 4.1σ"),
        ("The Six Sigma target", "3.4 DPMO",
         "99.99966% yield"),
    ], kicker="MEASURE · SIGMA LEVEL", accent=VIOLET,
        note="Sigma level is the common yardstick that lets you compare performance across completely different processes.")
    d.tile_grid("Cost of Poor Quality (COPQ)", [
        ("Internal failure", "Defects found before the customer sees them — rework, scrap, re-triage."),
        ("External failure", "Defects the customer finds — complaints, escalations, lost trust."),
        ("Appraisal cost", "The cost of inspecting and checking for defects."),
        ("Prevention cost", "The cost of stopping defects happening — training, poka-yoke, better design."),
    ], kicker="MEASURE · THE BUSINESS CASE", cols=2, size=15, accent=RED)


# ============================================================ ANALYZE
def analyze_phase(d):
    d.big_statement("Analyze — Why is this happening?",
                    "The Analyze phase moves the team from a measured symptom to a proven, actionable root cause.",
                    "DMAIC · A — ANALYZE", color=DMAIC_COLORS[2])
    d.flow_h("Steps in the Analyze Phase", [
        "Study the data and the process map",
        "Generate a list of potential causes (Xs)",
        "Organise the causes with a Fishbone diagram",
        "Drill down with the 5 Whys",
        "Test each candidate cause against the evidence",
    ], kicker="ANALYZE · ROADMAP", color=DMAIC_COLORS[2])

    # Variation
    d.compare_panels("Two Kinds of Variation — and Two Different Responses", [
        ("Common cause", "Built into the process",
         ["Always present, random, predictable range.",
          "The process is stable but imperfect.",
          "Response: change the PROCESS.",
          "Reacting to individual points makes it worse."]),
        ("Special cause", "An external, assignable signal",
         ["Unusual, traceable to a specific event.",
          "Something changed that should not have.",
          "Response: investigate THAT event.",
          "Fix the cause, then remove it for good."]),
    ], kicker="ANALYZE · UNDERSTANDING VARIATION", accent=AMBER)
    d.big_statement("Do not react to a single data point.",
                    "Treating common-cause variation as if it were special cause — called tampering — reliably makes the process worse, not better.",
                    "THE MOST COMMON ANALYSIS MISTAKE", color=RED)

    # Pareto
    d.big_statement("The Pareto Principle — the 80/20 rule",
                    "Roughly 80% of the effects come from 20% of the causes. Find that 20% and you get most of the improvement for a fraction of the effort.",
                    "ANALYZE · PARETO", color=AMBER)
    d.pareto_chart("Pareto Chart — Causes of Delayed Ticket Assignment", [
        ("Unclear\ntriage rules", 210),
        ("Peak-hour\nunderstaffing", 155),
        ("Incomplete\nticket info", 95),
        ("System\nslowness", 48),
        ("Wrong\ncategory", 30),
        ("Other", 12),
    ], kicker="ANALYZE · WORKED EXAMPLE",
        note="Two categories — unclear triage rules and peak-hour understaffing — account for about 66% of all delays. Start there.")
    d.flow_h("How to Build a Pareto Chart", [
        "Agree the categories and make them mutually exclusive",
        "Count the occurrences in each category",
        "Sort the categories in descending order",
        "Calculate the cumulative percentage",
        "Plot bars plus the cumulative line and read off the vital few",
    ], kicker="PARETO · METHOD", color=AMBER)

    # Run chart
    d.run_chart("Run Chart — Average Ticket Assignment Time by Day", [
        ("D1", 9.2), ("D2", 8.8), ("D3", 9.6), ("D4", 10.4), ("D5", 9.9),
        ("D6", 8.4), ("D7", 9.1), ("D8", 11.2), ("D9", 10.8), ("D10", 9.4),
    ], kicker="ANALYZE · SEEING BEHAVIOUR OVER TIME",
        note="A single point above the median is normal variation. A run of 7+ points on one side signals a real shift.")
    d.tile_grid("Reading a Run Chart — Five Patterns", [
        ("Trend", "7 or more consecutive points rising or falling — the process is drifting."),
        ("Shift", "8 or more consecutive points on one side of the median — something changed."),
        ("Cluster", "Points grouped together — suggests a periodic or batch effect."),
        ("Oscillation", "Rapid up-down swings — the process is unstable, often from over-adjustment."),
        ("Mixture", "Points avoiding the centre line — often two different processes combined."),
        ("No pattern", "Random scatter around the median — stable, common-cause variation only."),
    ], kicker="ANALYZE · RUN CHART RULES", cols=2, size=13, accent=TEAL)

    # Root cause
    d.big_statement("What is a root cause?",
                    "The deepest cause in the chain that you can actually act on — remove it, and the problem does not come back.",
                    "ANALYZE · ROOT CAUSE", color=VIOLET)
    d.big_statement("Fixing the wrong cause wastes the whole project.",
                    "If the analysis stops at the first plausible explanation, the team implements a change, the metric does not move, and confidence in the method is lost.",
                    "WHY EVIDENCE MATTERS", color=RED)
    d.tile_grid("The 5 Whys Technique", [
        ("Start with the problem", "State the effect precisely, using the data you measured."),
        ("Ask why — and answer with evidence", "Each answer must be something you can point to, not a guess."),
        ("Repeat about five times", "Five is a guide, not a rule — stop when you reach an actionable cause."),
        ("Watch for blame", "If an answer names a person rather than a process, ask why again."),
        ("Stop at actionable", "The root cause must be something within the team's power to change."),
        ("Verify with data", "Test the final cause against the evidence before acting on it."),
    ], kicker="ANALYZE · 5 WHYS", cols=2, size=14, accent=VIOLET)
    d.flow_h("5 Whys — Worked Example: Ticket Assignment Delay", [
        "PROBLEM: Tickets take 9.4 hours to assign vs a 4-hour target",
        "WHY? Tickets wait in the triage queue",
        "WHY? Only one agent triages, and only in the morning",
        "WHY? Triage is not in anyone's core role definition",
        "ROOT CAUSE: Triage ownership was never assigned when the process changed",
    ], kicker="ANALYZE · 5 WHYS IN ACTION", color=VIOLET)
    d.fishbone("Fishbone (Ishikawa) — Ticket Assignment Is Delayed",
               "Ticket\nassignment\nis delayed", [
                   ("Manpower", ["One triage agent only", "No cover at peak", "Unclear ownership"]),
                   ("Method", ["Triage rules ambiguous", "No priority definition", "Manual routing"]),
                   ("Machine", ["Ticket tool slow", "No auto-assignment", "Four systems to check"]),
                   ("Material", ["Incomplete ticket info", "Wrong category chosen", "No template"]),
                   ("Measurement", ["No SLA clock on triage", "Assignment time not tracked", "No baseline agreed"]),
               ], kicker="ANALYZE · CAUSE AND EFFECT · THE 5Ms")
    d.tile_grid("Building a Fishbone Diagram", [
        ("Write the effect", "Put the measured problem in the head of the fish — be specific."),
        ("Choose the categories", "5M: Manpower, Method, Machine, Material, Measurement. Service teams often use 4P."),
        ("Brainstorm into each bone", "Generate freely — no evaluation or debate during generation."),
        ("Go three levels deep", "Ask 'why does that happen?' on each cause to reach the real driver."),
        ("Shortlist with multi-voting", "Each team member votes; the causes with most votes go forward."),
        ("Verify with data", "A cause on the diagram is a HYPOTHESIS until the data supports it."),
    ], kicker="ANALYZE · FISHBONE METHOD", cols=2, size=14, accent=VIOLET)
    d.tile_grid("Brainstorming — Getting Good Causes Out", [
        ("Quantity first", "Generate a long list before evaluating anything."),
        ("No criticism", "Judging ideas during generation stops people contributing."),
        ("Build on ideas", "One person's half-idea is often another's breakthrough."),
        ("Everyone contributes", "Use round-robin or brainwriting so the loudest voice does not dominate."),
    ], kicker="ANALYZE · BRAINSTORMING", cols=2, size=15)
    d.tile_grid("Multi-Voting — Narrowing the List", [
        ("Why use it", "A long cause list needs to become a short, agreed shortlist."),
        ("How it works", "Each member gets N votes (about a third of the number of items)."),
        ("Vote independently", "Vote privately first so nobody anchors on the manager's choice."),
        ("Then verify", "The top-voted causes still have to be tested against the data."),
    ], kicker="ANALYZE · MULTI-VOTING", cols=2, size=15, accent=TEAL)
    d.tile_grid("Your Complete Online Toolkit", [
        ("SIPOC & Process Map", "Define — guided SIPOC, swimlane and handoffs — alfredang.github.io/sipoc/"),
        ("5 Whys", "Analyze — build and share the 5 Whys chain — alfredang.github.io/5whys/"),
        ("Fishbone Diagram", "Analyze — Ishikawa cause-and-effect builder — alfredang.github.io/fishbone/"),
        ("Pareto Chart (collaborative)", "Analyze — your team brainstorms and votes in one live session; the chart builds itself — alfredang.github.io/paretochart/"),
        ("NovaSPC", "Measure & Control — run charts, SPC charts and process capability from your CSV — alfredang.github.io/novaspc/"),
        ("All free", "No install, no sign-up. Everything stays in your browser."),
    ], kicker="YOUR ONLINE TOOLKIT · USED ACROSS DMAIC", cols=2, size=13, accent=BLUE)
    d.flow_h("Using the Collaborative Pareto Tool in Your Team", [
        "Facilitator creates a session and shares the access code",
        "Every team member joins with the code",
        "The team brainstorms candidate causes into the session",
        "Each member votes on the causes that matter most",
        "The live Pareto chart reveals the vital few",
    ], kicker="ANALYZE · TEAM ROOT CAUSE SESSION", color=AMBER)


# ============================================================ IMPROVE
def improve_phase(d):
    d.big_statement("Improve — What change will actually fix it?",
                    "The Improve phase generates, selects and pilots solutions that address the proven root cause.",
                    "DMAIC · I — IMPROVE", color=DMAIC_COLORS[3])
    d.flow_h("Steps in the Improve Phase", [
        "Generate candidate solutions against the root cause",
        "Select using weighted criteria",
        "Pilot the change at small scale",
        "Measure whether the metric actually moved",
        "Standardise the new method",
    ], kicker="IMPROVE · ROADMAP", color=DMAIC_COLORS[3])
    d.tile_grid("Generating Solutions", [
        ("Brainstorming", "Free generation against the specific root cause — not the general problem."),
        ("Brainwriting", "Written idea generation; avoids the loudest voice dominating the room."),
        ("Benchmarking", "Find who already does this well, internally or externally, and learn from them."),
        ("Anti-brainstorming", "Ask how to make the problem worse, then invert every answer."),
    ], kicker="IMPROVE · IDEA GENERATION", cols=2, size=15)
    d.matrix2x2("Prioritising Countermeasures — Impact vs Effort",
                "EFFORT REQUIRED  →", "IMPACT  →", [
                    ("Quick wins", "High impact, low effort. Do these first — they build momentum and credibility."),
                    ("Major projects", "High impact, high effort. Worth doing, but plan and resource them properly."),
                    ("Fill-ins", "Low impact, low effort. Do them if there is spare capacity."),
                    ("Thankless tasks", "Low impact, high effort. Avoid these entirely."),
                ], kicker="IMPROVE · PRIORITISATION", accent=TEAL)
    d.tile_grid("The Solution Selection Matrix", [
        ("List the criteria", "Effectiveness, cost, time to implement, risk, ease of adoption."),
        ("Weight each criterion", "Not all criteria matter equally — agree the weights first."),
        ("Score each solution", "Score every candidate against each criterion on a consistent scale."),
        ("Rank by weighted total", "Multiply score by weight, sum, and rank — the decision becomes defensible."),
    ], kicker="IMPROVE · CHOOSING OBJECTIVELY", cols=2, size=15, accent=BLUE)
    d.flow_h("5S — Organising the Workplace", [
        "SORT — remove what is not needed",
        "SET IN ORDER — a place for everything",
        "SHINE — clean and inspect regularly",
        "STANDARDISE — make the first 3S the norm",
        "SUSTAIN — audit and keep the discipline",
    ], kicker="IMPROVE · 5S", color=TEAL)
    d.tile_grid("5S Applied to Digital Work", [
        ("Sort", "Archive the ticket queues, folders and dashboards nobody uses."),
        ("Set in order", "One agreed place for templates, runbooks and knowledge articles."),
        ("Shine", "Regularly review and retire out-of-date knowledge base entries."),
        ("Standardise", "Agreed naming conventions and ticket templates for everyone."),
        ("Sustain", "A short monthly review to check the standard is still being followed."),
        ("Why it works", "Less searching, fewer mistakes, faster onboarding for new agents."),
    ], kicker="IMPROVE · 5S IN A SERVICE TEAM", cols=2, size=14, accent=TEAL)
    d.big_statement("Poka-Yoke — mistake proofing",
                    "Design the process so the error is difficult or impossible to make — rather than relying on people to be careful.",
                    "IMPROVE · POKA-YOKE", color=VIOLET)
    d.compare_panels("Three Levels of Mistake Proofing", [
        ("Prevention", "The error cannot happen",
         ["Strongest form — design it out.",
          "A required field blocks submission.",
          "A connector only fits one way."]),
        ("Detection", "The error is caught immediately",
         ["The error happens but is flagged at once.",
          "Validation warns on an invalid category.",
          "Weaker, but often easier to add."]),
        ("Mitigation", "The impact is reduced",
         ["The error happens and is not caught.",
          "But its consequence is limited.",
          "Weakest — use only when the others cannot apply."]),
    ], kicker="IMPROVE · POKA-YOKE LEVELS", accent=VIOLET)
    d.tile_grid("Standard Work", [
        ("What it is", "The documented, current best-known way to perform the task."),
        ("Why it matters", "You cannot improve a process that everyone performs differently."),
        ("What it contains", "The sequence, the time each step takes and the quality checks."),
        ("Who writes it", "The people who do the work — not a manager writing in isolation."),
        ("Keep it living", "Update it every time a better method is proven."),
        ("The Lean insight", "Standard work is the baseline for the NEXT improvement, not a straitjacket."),
    ], kicker="IMPROVE · STANDARD WORK", cols=2, size=14)
    d.tile_grid("Kaizen — Continuous Small Improvement", [
        ("The principle", "Many small improvements beat waiting for one perfect large one."),
        ("Who does it", "Everyone — Kaizen is explicitly not reserved for specialists."),
        ("Kaizen event", "A focused 3-5 day workshop to fix one process end to end."),
        ("Yellow Belt fit", "This is exactly the scale of improvement a Yellow Belt leads."),
    ], kicker="IMPROVE · KAIZEN", cols=2, size=15, accent=AMBER)
    d.tile_grid("Piloting Before Full Rollout", [
        ("Why pilot", "Exposes practical issues cheaply, before they affect every customer."),
        ("Keep it small", "One team, one shift or one ticket category is usually enough."),
        ("Measure the same way", "Use the identical operational definition as your baseline, or you cannot compare."),
        ("Run it long enough", "Cover a full business cycle so you see normal variation."),
        ("Decide honestly", "Adopt, adapt or abandon — a failed pilot that saves a bad rollout is a success."),
        ("Then standardise", "Only after the pilot proves the gain do you write it into standard work."),
    ], kicker="IMPROVE · PILOTING", cols=2, size=14, accent=BLUE)


# ============================================================ CONTROL
def control_phase(d):
    d.big_statement("Control — How do we make the gain stick?",
                    "Without the Control phase, processes drift back to the old way within months and the whole project is wasted.",
                    "DMAIC · C — CONTROL", color=DMAIC_COLORS[4])
    d.flow_h("Steps in the Control Phase", [
        "Build the control plan",
        "Set up monitoring and visual management",
        "Document the SOP and standard work",
        "Hand over to the process owner",
        "Close the project and share the learning",
    ], kicker="CONTROL · ROADMAP", color=DMAIC_COLORS[4])
    d.tile_grid("The Control Plan — Six Required Columns", [
        ("Metric", "What is being monitored — the same operational definition as the baseline."),
        ("Target", "The agreed acceptable value or range."),
        ("Method", "How the measurement is taken — report, dashboard, sample or audit."),
        ("Frequency", "How often it is checked: per shift, daily, weekly."),
        ("Owner", "The named person accountable — a role, never 'the team'."),
        ("Reaction plan", "Exactly what happens when the metric falls outside target."),
    ], kicker="CONTROL · THE CONTROL PLAN", cols=2, size=14, accent=BLUE)
    d.big_statement("A control plan without a named owner is a wish.",
                    "Every row needs a person accountable and a specific action to take when the number goes wrong — otherwise nothing happens.",
                    "CONTROL · ACCOUNTABILITY", color=RED)
    d.big_statement("What is process control?",
                    "A process is 'in control' when it varies consistently within expected limits over time — predictable, even if not yet perfect.",
                    "CONTROL · PROCESS CONTROL", color=VIOLET)
    d.two_col("Control Limits vs Specification Limits",
              [("Specification limits (LSL / USL)", 0),
               ("Given by the CUSTOMER", 1),
               ("Define what counts as a defect", 1),
               ("Do not change when the process changes", 1),
               ("Outside them = a defect", 1)],
              [("Control limits (LCL / UCL)", 0),
               ("Calculated from the PROCESS itself", 1),
               ("Typically the mean ± 3 standard deviations", 1),
               ("Change when the process changes", 1),
               ("Outside them = a special cause to investigate", 1)],
              kicker="CONTROL · A CRITICAL DISTINCTION", lhead="Set by the customer", rhead="Set by the process",
              lcolor=RED, rcolor=BLUE)
    d.tile_grid("Statistical Process Control (SPC)", [
        ("What it is", "Monitoring a process over time so problems are predicted, not discovered late."),
        ("The core idea", "Plot the metric against control limits and watch for non-random patterns."),
        ("Why it saves money", "Preventing defects always costs less than inspecting and reworking them."),
        ("Yellow Belt level", "You are expected to read and interpret a control chart, not to construct one."),
    ], kicker="CONTROL · SPC AWARENESS", cols=2, size=15, accent=VIOLET)
    d.tile_grid("Visual Management", [
        ("Visual boards", "Display the metric, the target and the current status where the team works."),
        ("Make it obvious", "Anyone should see whether performance is on target within a few seconds."),
        ("Team huddles", "A short daily stand-up at the board — 15 minutes maximum."),
        ("Drives ownership", "When performance is visible, the team owns it rather than the manager."),
        ("Surfaces issues early", "Problems are raised while they are still small and cheap to fix."),
        ("Keep it current", "An out-of-date board is worse than no board — it teaches people to ignore it."),
    ], kicker="CONTROL · MAKING IT VISIBLE", cols=2, size=14, accent=TEAL)
    d.tile_grid("Standard Operating Procedures (SOPs)", [
        ("Written instructions", "Describe how to perform the task to achieve the required result."),
        ("Include the measures", "State the benchmarks and quality checks, not only the steps."),
        ("Centrally accessible", "Held in one agreed place everyone can reach and search."),
        ("Version controlled", "It must be obvious which version is current."),
    ], kicker="CONTROL · SOPs", cols=2, size=15)
    d.tile_grid("Go to the Gemba", [
        ("Gemba means 'the real place'", "Where the work actually happens — not the meeting room."),
        ("Go and see", "Observe the process directly rather than relying on reports about it."),
        ("Ask, do not blame", "The purpose is to understand the process, never to audit the person."),
        ("Why it works", "Reports show what was recorded; Gemba shows what actually happens."),
    ], kicker="CONTROL · GO GEMBA", cols=2, size=15, accent=AMBER)
    d.tile_grid("The A3 — One Page That Tells the Whole Story", [
        ("Background", "Why this problem was worth working on."),
        ("Current state", "The baseline, with the data and process map."),
        ("Goal", "The target condition, stated as a measurable number."),
        ("Root cause analysis", "What the 5 Whys and Fishbone actually proved."),
        ("Countermeasures", "What was changed, and why that addresses the proven cause."),
        ("Results & follow-up", "Whether the metric moved, and who now owns the control plan."),
    ], kicker="CONTROL · THE A3 REPORT", cols=2, size=14, accent=BLUE)
    d.flow_h("Project Handover and Closure", [
        "Confirm the improvement held for a full cycle",
        "Hand the control plan to the named process owner",
        "Train everyone on the new standard work",
        "Document the financial or service benefit",
        "Share the learning so others can reuse it",
    ], kicker="CONTROL · CLOSING THE PROJECT", color=DMAIC_COLORS[4])
