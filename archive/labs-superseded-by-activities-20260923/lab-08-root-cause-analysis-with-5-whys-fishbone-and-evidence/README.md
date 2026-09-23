# Lab 8 — Root Cause Analysis with 5 Whys, Fishbone, and Evidence

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

## Objective

Identify root causes of variation using structured analysis (A3).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A completed 5 Whys chain, a Fishbone diagram and an evidence-tested cause shortlist.

**Tools and techniques:** 5 Whys tool, Fishbone tool, 5M categories, brainstorming, multi-voting

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/daily-summary.csv`](data/daily-summary.csv) — 10 rows · columns: date, tickets, mean_assignment_min, median_assignment_min, defects, missed_30min_goal
- [`data/defect-counts.csv`](data/defect-counts.csv) — 6 rows · columns: defect_category, count
- [`data/root-cause-evidence.csv`](data/root-cause-evidence.csv) — 8 rows · columns: evidence_id, observation, source, supports_cause

**`templates/` — the worksheets you fill in:**

- [`templates/cause-evidence-test.csv`](templates/cause-evidence-test.csv) — columns: candidate_cause, evidence_that_supports_it, evidence_that_contradicts_it, verdict
- [`templates/fishbone-causes.csv`](templates/fishbone-causes.csv) — columns: category, possible_cause, supported_by_evidence
- [`templates/five-whys.csv`](templates/five-whys.csv) — columns: why_level, question, answer, evidence_needed, evidence_found

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

> Test every candidate cause against the Lab 7 data before shortlisting it.

### Online tools used in this lab

- **5 Whys** — https://alfredang.github.io/5whys/
- **Fishbone Diagram** — https://alfredang.github.io/fishbone/

## Steps

### Step 1

Write the problem statement precisely — the effect you are explaining.

### Step 2

Complete a 5 Whys chain with the online 5 Whys tool, continuing until you reach an actionable cause.

Open the tool: <https://alfredang.github.io/5whys/>

### Step 3

Build a Fishbone diagram with the online Fishbone tool using the 5M categories: Manpower, Method, Machine, Material, Measurement.

Open the tool: <https://alfredang.github.io/fishbone/>

### Step 4

Brainstorm candidate causes into each category — no evaluation during generation.

### Step 5

Use multi-voting to shortlist the most likely causes as a team.

### Step 6

Test each shortlisted cause against your Lab 7 data — does the evidence support it?

### Step 7

State why the team must not jump straight to solutions.

## Check your work

Each shortlisted root cause is supported by named evidence, and your 5 Whys chain ends at something you can act on.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
