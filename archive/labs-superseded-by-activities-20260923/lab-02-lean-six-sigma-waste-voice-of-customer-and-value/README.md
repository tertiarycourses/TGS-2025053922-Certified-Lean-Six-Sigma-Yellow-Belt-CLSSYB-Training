# Lab 2 — Lean, Six Sigma, Waste, Voice of Customer, and Value

**DMAIC phase:** DEFINE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

## Objective

Apply Lean and Six Sigma concepts — value, waste, defects, variation (K1, A2).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A VOC-to-CTQ translation table, a value-added analysis, and a waste walk log.

**Tools and techniques:** VOC, CTQ tree, DOWNTIME eight wastes, value-added analysis

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/voice-of-customer.csv`](data/voice-of-customer.csv) — 10 rows · columns: id, customer_statement, source, date
- [`data/waste-walk-observations.csv`](data/waste-walk-observations.csv) — 10 rows · columns: obs_id, observation, process_step, time_lost_min, waste_type

**`templates/` — the worksheets you fill in:**

- [`templates/value-added-analysis.csv`](templates/value-added-analysis.csv) — columns: step_no, activity, VA_BVA_NVA, justification
- [`templates/voc-to-ctq.csv`](templates/voc-to-ctq.csv) — columns: voc_id, customer_statement, need, ctq_requirement, measure, target

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

> Tag every waste-walk observation with one of the eight DOWNTIME waste types.

## Steps

### Step 1

Capture the Voice of the Customer — record at least five verbatim customer statements.

### Step 2

Translate each VOC statement into a need, then into a measurable CTQ requirement.

### Step 3

Classify each process activity as value-added, business-value-added or non-value-added.

### Step 4

Conduct a waste walk and tag each observation against the eight wastes (DOWNTIME).

### Step 5

Distinguish a defect (output fails CTQ) from waste (effort the customer will not pay for).

### Step 6

Identify which single waste type appears most often in your scenario.

## Check your work

Every CTQ is measurable with a target, and each waste observation is tagged to one of the eight waste types.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
