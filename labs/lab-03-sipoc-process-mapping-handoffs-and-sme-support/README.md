# Lab 3 — SIPOC, Process Mapping, Handoffs, and SME Support

**DMAIC phase:** DEFINE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training (TGS-2025053922)

## Objective

Map a process with SIPOC and a detailed process map to expose handoffs (A2, A3).

## Scenario

Contoso Service Desk handles employee IT requests. Employees complain that tickets take too long to be assigned, that they must keep chasing for status, and that agents apply different definitions of what counts as "resolved". You are supporting the improvement team as a Yellow Belt.

**The data.** Two weeks of ticket data have been collected: **400 tickets**, of which **96 contained at least one defect**, with **120 defects** recorded in total across **6 defect opportunities per ticket**. Mean assignment time is **55 minutes** against a **30-minute** improvement goal. The files in this lab's `data/` folder are that extract.

## What you will build

A completed SIPOC and a detailed process map with pain points marked.

**Tools and techniques:** SIPOC & Process Map Builder, process flowchart, swimlane map, standard process symbols

## Files in this lab folder

**`data/` — the mock data you analyse:**

- [`data/process-steps.csv`](data/process-steps.csv) — 7 rows · columns: step_no, activity, actor, system, process_time_min, wait_time_min, handoff_to

**`templates/` — the worksheets you fill in:**

- [`templates/handoff-register.csv`](templates/handoff-register.csv) — columns: handoff_no, from_actor, to_actor, trigger, owner_both_sides, pain_point
- [`templates/sipoc.csv`](templates/sipoc.csv) — columns: suppliers, inputs, process_step, outputs, customers

Open the CSV files in Excel, LibreOffice Calc or Google Sheets. Work on a copy so the originals stay clean for revision.

> data/process-steps.csv holds the as-is step, actor, system and timing data.

### Online tools used in this lab

- **SIPOC & Process Map Builder** — https://alfredang.github.io/sipoc/

## Steps

### Step 1

Set the process boundaries — agree the explicit start and stop points first.

### Step 2

Build the SIPOC with the online builder: Suppliers, Inputs, Process (5-7 high-level steps), Outputs, Customers.

Open the tool: <https://alfredang.github.io/sipoc/>

### Step 3

Expand into a detailed process map: Step, Actor, Activity, System, Handoff.

### Step 4

Assign an actor to each step — the tool generates the swimlane and detects every handoff for you.

### Step 5

Tag pain points on the steps — waiting, rework loop, unclear ownership, duplicate entry or missing decision rule (at least three).

### Step 6

Prepare SME notes for the Green Belt: what you observed and what needs validation.

## Check your work

Run 'Check my SIPOC' in the tool — all five columns populated, 5-7 steps, at least three pain points, and every handoff owned on both sides.

## Deliverable

Save your output — it forms part of your Contoso improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Yellow Belt (CLSSYB) Training · TGS-2025053922 · Version v8 · © 2026 Tertiary Infotech Academy Pte Ltd*
