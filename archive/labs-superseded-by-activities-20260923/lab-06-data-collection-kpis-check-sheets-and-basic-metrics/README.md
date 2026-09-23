# Lab 6 — Data Collection, KPIs, Check Sheets, and Basic Metrics

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

## Objective

Plan and execute data collection against defined quality standards (A4).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A data collection plan, an operational definition set and a working check sheet.

**Tools and techniques:** KPI definition, operational definitions, check sheets, sampling, data types

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/daily-summary.csv`](data/daily-summary.csv) — 10 rows · columns: date, tickets, mean_assignment_min, median_assignment_min, defects, missed_30min_goal
- [`data/service-desk-tickets.csv`](data/service-desk-tickets.csv) — 400 rows · columns: ticket_id, date, ticket_type, channel, assigned_queue, agent, assignment_time_min, met_30min_goal, defect_count, defect_categories, reopened

**`templates/` — the worksheets you fill in:**

- [`templates/check-sheet.csv`](templates/check-sheet.csv) — columns: date, ticket_id, ticket_type, assignment_time_min, defect_category, rework_required, notes
- [`templates/data-collection-plan.csv`](templates/data-collection-plan.csv) — columns: kpi, operational_definition, data_type, data_source, frequency, who_collects, bias_risk

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

> data/service-desk-tickets.csv is the full two-week extract (400 tickets).

## Steps

### Step 1

Classify your data: continuous vs discrete, nominal vs ordinal — and why it matters.

### Step 2

Define KPIs with operational definitions, data source and collection frequency.

### Step 3

Design a check sheet capturing date, ticket ID, type, assignment time and defect category.

### Step 4

Define mutually exclusive defect categories so every observation lands in exactly one.

### Step 5

Plan sampling: how many, how often, by whom — and identify possible bias.

### Step 6

State which KPI best reflects the customer pain point from your VOC work.

## Check your work

Two different people reading your operational definition would record the same value for the same event.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
