# Lab 14 — Descriptive Statistics and Implementation Planning

**DMAIC phase:** CONTROL  |  **Lab type:** Elective  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

> **Elective lab.** Complete this lab if time allows during class, or afterwards as additional practice. It extends the same Contoso Service Desk scenario used by the core labs.

## Objective

Summarise data numerically and plan the rollout (A4, A5).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A descriptive statistics summary and a dated implementation plan.

**Tools and techniques:** Mean, median, range, standard deviation, implementation planning

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/assignment-times.csv`](data/assignment-times.csv) — 400 rows · columns: date, ticket_id, assignment_time_min
- [`data/daily-summary.csv`](data/daily-summary.csv) — 10 rows · columns: date, tickets, mean_assignment_min, median_assignment_min, defects, missed_30min_goal
- [`data/service-desk-tickets.csv`](data/service-desk-tickets.csv) — 400 rows · columns: ticket_id, date, ticket_type, channel, assigned_queue, agent, assignment_time_min, met_30min_goal, defect_count, defect_categories, reopened

**`templates/` — the worksheets you fill in:**

- [`templates/descriptive-statistics.csv`](templates/descriptive-statistics.csv) — columns: statistic, formula_or_function, your_value
- [`templates/implementation-plan.csv`](templates/implementation-plan.csv) — columns: action, owner, start_date, due_date, barrier, mitigation

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

> data/assignment-times.csv is the raw column for the statistics.

## Steps

### Step 1

Compute the mean and median for your assignment-time data and compare them.

### Step 2

Compute the range and standard deviation to describe the spread.

### Step 3

Explain what the mean-versus-median difference reveals about outliers and skew.

### Step 4

Write the implementation plan: action, owner, date, barriers and mitigation.

## Check your work

You can explain why the mean and median differ in your data, and every implementation action has an owner and a date.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
