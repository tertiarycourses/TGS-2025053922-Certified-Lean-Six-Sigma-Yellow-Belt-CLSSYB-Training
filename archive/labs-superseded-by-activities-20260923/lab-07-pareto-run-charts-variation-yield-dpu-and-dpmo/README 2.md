# Lab 7 — Pareto, Run Charts, Variation, Yield, DPU, and DPMO

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

## Objective

Analyse process performance data to quantify and prioritise (A3, A4).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A Pareto chart, a run chart and calculated yield, DPU, DPO, DPMO and sigma level.

**Tools and techniques:** Pareto Chart tool (collaborative), NovaSPC, yield/DPU/DPO/DPMO, sigma level, variation

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/assignment-times.csv`](data/assignment-times.csv) — 400 rows · columns: date, ticket_id, assignment_time_min
- [`data/daily-summary.csv`](data/daily-summary.csv) — 10 rows · columns: date, tickets, mean_assignment_min, median_assignment_min, defects, missed_30min_goal
- [`data/defect-counts.csv`](data/defect-counts.csv) — 6 rows · columns: defect_category, count
- [`data/service-desk-tickets.csv`](data/service-desk-tickets.csv) — 400 rows · columns: ticket_id, date, ticket_type, channel, assigned_queue, agent, assignment_time_min, met_30min_goal, defect_count, defect_categories, reopened

**`templates/` — the worksheets you fill in:**

- [`templates/pareto-table.csv`](templates/pareto-table.csv) — columns: defect_category, count, percent, cumulative_percent
- [`templates/process-metrics.csv`](templates/process-metrics.csv) — columns: metric, formula, your_calculation

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

> Upload data/assignment-times.csv to NovaSPC for the run chart. Worked answers are in solution/pareto-table-answers.csv and solution/process-metrics-answers.csv — attempt the lab before opening them.

### Online tools used in this lab

- **Pareto Chart (collaborative)** — https://alfredang.github.io/paretochart/
- **NovaSPC** — https://alfredang.github.io/novaspc/

## Steps

### Step 1

Build the Pareto table: category, count, percentage and cumulative percentage.

### Step 2

In your group, open the collaborative Pareto tool — one member creates the session and shares the code, then everyone joins, brainstorms and votes to produce the live Pareto chart.

Open the tool: <https://alfredang.github.io/paretochart/>

### Step 3

Identify the vital few categories driving about 80% of the problem.

### Step 4

Export your assignment-time data as CSV and plot a run chart in NovaSPC.

Open the tool: <https://alfredang.github.io/novaspc/>

### Step 5

Interpret the run chart for trend, shift, cluster and oscillation patterns.

### Step 6

Calculate yield, DPU, DPO and DPMO from your defect data.

### Step 7

Convert DPMO to a sigma level and interpret what it says about the process.

### Step 8

Distinguish common-cause from special-cause variation and why the response differs.

## Check your work

Your cumulative percentage column reaches 100%, and you can state the sigma level with the DPMO it came from.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
