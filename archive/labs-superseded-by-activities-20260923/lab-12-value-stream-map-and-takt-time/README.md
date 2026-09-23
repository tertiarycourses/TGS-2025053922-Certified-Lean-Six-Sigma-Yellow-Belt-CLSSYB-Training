# Lab 12 — Value Stream Map and Takt Time

**DMAIC phase:** MEASURE  |  **Lab type:** Elective  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

> **Elective lab.** Complete this lab if time allows during class, or afterwards as additional practice. It extends the same Contoso Service Desk scenario used by the core labs.

## Objective

Quantify flow, lead time and takt time across the value stream (A3, A4).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A value stream map with lead time, process time and a calculated takt time.

**Tools and techniques:** SIPOC & Process Map Builder, value stream mapping, lead time, WIP, takt time

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/process-steps.csv`](data/process-steps.csv) — 7 rows · columns: step_no, activity, actor, system, process_time_min, wait_time_min, handoff_to

**`templates/` — the worksheets you fill in:**

- [`templates/takt-time.csv`](templates/takt-time.csv) — columns: input, value
- [`templates/value-stream-map.csv`](templates/value-stream-map.csv) — columns: step_no, activity, process_time_min, wait_time_min, VA_or_NVA

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

### Online tools used in this lab

- **SIPOC & Process Map Builder** — https://alfredang.github.io/sipoc/

## Steps

### Step 1

Map the value stream: each step with its process time and the wait time between steps. Start from your Lab 3 process map.

Open the tool: <https://alfredang.github.io/sipoc/>

### Step 2

Total the value-added time and the lead time, then compute process cycle efficiency.

### Step 3

Calculate takt time = available working time / customer demand.

### Step 4

Compare cycle time against takt time to identify the bottleneck step.

## Check your work

Your lead time equals the sum of all process and wait times, and takt time is expressed per unit.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
