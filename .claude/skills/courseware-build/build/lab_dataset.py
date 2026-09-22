"""Canonical Contoso Service Desk dataset — the single source for every lab data file.

Deterministic (fixed seeds) and reconciled EXACTLY to the Case Study answer key:

  400 tickets · 96 defective · 120 defects · 6 defect opportunities per unit
  Yield 76% · DPU 0.30 · DPO 0.05 · DPMO 50,000 · sigma level ~3.1
  Pareto vital few: Delayed assignment 40% + Missing information 25% = 65%
  Mean assignment time 55 min, median 46 min (right skew — the Lab 14 mean-vs-median question)
  A deliberate process SHIFT from day 7 (server migration) so the Lab 7 run chart
  carries a real special-cause signal to find.

`import lab_dataset` gives the verified data silently; running the file prints
the full reconciliation against the answer key.
"""
import random, datetime, statistics, math
from collections import Counter

MU, BUMP, SG, SEED = 3.74, 0.40, 0.50, 601
N, OPP, PER, N_DEF = 400, 6, 40, 96
TARGET_MIN, SLA_MIN = 30, 60
BASELINE_MEAN = 55

DEFECTS = [("Delayed assignment", 48), ("Missing information", 30), ("Wrong queue", 18),
           ("Reopened ticket", 12), ("Duplicate ticket", 8), ("Unclear status", 4)]

TYPES = [("Password reset", .24), ("Software install", .18), ("Hardware fault", .14),
         ("Access request", .16), ("Network issue", .12), ("Email problem", .10), ("Other", .06)]
CHANNELS = ["Portal", "Email", "Phone", "Walk-in"]
AGENTS = ["A-01", "A-02", "A-03", "A-04", "A-05"]
QUEUES = ["Desktop Support", "Network", "Applications", "Security", "Accounts"]


def _days():
    out = []
    d = datetime.date(2026, 6, 1)
    while len(out) < 10:
        if d.weekday() < 5:
            out.append(d)
        d += datetime.timedelta(days=1)
    return out


def _build():
    days = _days()
    random.seed(SEED)
    times = [max(6, round(math.exp(random.gauss(MU + (BUMP if i // PER >= 6 else 0), SG))))
             for i in range(N)]

    random.seed(20260720)

    def pick(ws):
        r = random.random(); c = 0
        for v, w in ws:
            c += w
            if r <= c:
                return v
        return ws[-1][0]

    # The 48 "Delayed assignment" defects sit on the 48 slowest tickets — the tail
    # the triage team escalates — so root-cause analysis on the data holds together.
    delayed = set(sorted(range(N), key=lambda i: -times[i])[:48])
    assign = {i: [] for i in range(N)}
    for i in delayed:
        assign[i].append("Delayed assignment")

    others = []
    for n, c in DEFECTS:
        if n != "Delayed assignment":
            others += [n] * c
    random.shuffle(others)
    rest = [i for i in range(N) if i not in delayed]
    random.shuffle(rest)
    carriers = rest[:N_DEF - 48]
    # one defect each first, so the defective-ticket count lands exactly on 96
    for t, s in zip(carriers, others[:48]):
        assign[t].append(s)
    for s in others[48:]:
        pool = [t for t in carriers if s not in assign[t] and len(assign[t]) < 3]
        assign[random.choice(pool)].append(s)

    rows = []
    tid = 4100
    for i in range(N):
        tid += 1
        ds = assign[i]
        at = times[i]
        rows.append(dict(
            ticket_id=f"INC-{tid}", date=days[i // PER].isoformat(),
            ticket_type=pick(TYPES), channel=random.choice(CHANNELS),
            assigned_queue=random.choice(QUEUES), agent=random.choice(AGENTS),
            assignment_time_min=at,
            met_30min_goal="Yes" if at <= TARGET_MIN else "No",
            defect_count=len(ds),
            defect_categories="; ".join(ds) if ds else "None",
            reopened="Yes" if "Reopened ticket" in ds else "No"))

    daily = []
    for d in range(10):
        chunk = rows[d * PER:(d + 1) * PER]
        daily.append(dict(
            date=days[d].isoformat(), tickets=len(chunk),
            mean_assignment_min=round(statistics.mean(r["assignment_time_min"] for r in chunk), 1),
            median_assignment_min=round(statistics.median(r["assignment_time_min"] for r in chunk), 1),
            defects=sum(r["defect_count"] for r in chunk),
            missed_30min_goal=sum(1 for r in chunk if r["met_30min_goal"] == "No")))

    # ---- verify against the Case Study answer key; fail loudly if content drifts
    c = Counter()
    for r in rows:
        if r["defect_categories"] != "None":
            for x in r["defect_categories"].split("; "):
                c[x] += 1
    defective = sum(1 for r in rows if r["defect_count"] > 0)
    total = sum(c.values())
    for n, cnt in DEFECTS:
        assert c[n] == cnt, f"{n}: {c[n]} != {cnt}"
    assert defective == N_DEF, defective
    assert total == 120, total
    at = [r["assignment_time_min"] for r in rows]
    assert abs(statistics.mean(at) - BASELINE_MEAN) <= 0.2, statistics.mean(at)
    return rows, daily, days


ROWS, DAILY, DAYS = _build()
DATA = dict(rows=ROWS, daily=DAILY, days=DAYS, defects=DEFECTS)

# headline metrics, computed (never hard-coded) so they can never drift
DEFECTIVE = sum(1 for r in ROWS if r["defect_count"] > 0)
TOTAL_DEFECTS = sum(r["defect_count"] for r in ROWS)
YIELD = (N - DEFECTIVE) / N
DPU = TOTAL_DEFECTS / N
DPO = TOTAL_DEFECTS / (N * OPP)
DPMO = DPO * 1_000_000
SIGMA = round(statistics.NormalDist().inv_cdf(1 - DPO) + 1.5, 1)
MEAN_MIN = round(statistics.mean(r["assignment_time_min"] for r in ROWS))  # 55 — the published baseline
MEDIAN_MIN = round(statistics.median(r["assignment_time_min"] for r in ROWS))
SD_MIN = round(statistics.stdev(r["assignment_time_min"] for r in ROWS), 1)


def pareto():
    """Pareto table rows: (category, count, percent, cumulative percent)."""
    out = []
    cum = 0
    for n, cnt in DEFECTS:
        cum += cnt
        out.append((n, cnt, round(cnt / TOTAL_DEFECTS * 100, 1), round(cum / TOTAL_DEFECTS * 100, 1)))
    return out


if __name__ == "__main__":
    print(f"VERIFIED  {N} tickets · {DEFECTIVE} defective · {TOTAL_DEFECTS} defects · {OPP} opportunities")
    print(f"Yield {YIELD*100:.0f}%  DPU {DPU:.2f}  DPO {DPO:.4f}  DPMO {DPMO:,.0f}  sigma ~{SIGMA}")
    print(f"Assignment time: mean {MEAN_MIN} · median {MEDIAN_MIN} · sd {SD_MIN}")
    assert MEAN_MIN == 55, MEAN_MIN
    print("\nPareto")
    for n, cnt, pc, cum in pareto():
        print(f"  {n:22}{cnt:4}{pc:7.1f}%{cum:8.1f}%")
    print("\nDaily")
    for d in DAILY:
        print(f"  {d['date']}  mean {d['mean_assignment_min']:5}  defects {d['defects']:3}")
