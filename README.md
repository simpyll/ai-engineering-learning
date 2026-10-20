# AI Engineering: a project-based learning system

**Designed for five hours per week. Research checked October 20, 2026.**

Recommended route: **Python backend/data engineering → employment and real team experience → ML systems and inference → one advanced specialization.**

The first planned backend job-search checkpoint is 440 hours, approximately 1.9 years at 46 active weeks per year. The complete common AI engineering path is 1,520 hours, approximately 6.6 years on that schedule. It is a foundation for advanced work, not certification of frontier, Staff or Distinguished competence. Such roles require sustained external evidence and experience. Hours are scoped estimates, with assessments and review included; remediation can extend them.

## Start here

Read [the career recommendation](docs/01-career-analysis.md), then [the first twelve weeks](docs/11-first-12-weeks.md). Your next action is in [NOW.md](NOW.md). No paid compute is needed to start. The full plan is also available as [one document](../AI-Engineering-Curriculum.md).

## Deliverables in requested order

1. [Career competency analysis](docs/01-career-analysis.md)
2. [Complete skills dependency graph](docs/02-dependencies.md)
3. [Multiyear curriculum](docs/03-stage-guide.md)
4. [Weekly time allocation](docs/04-time-allocation.md)
5. [Project catalog](docs/05-project-catalog.md)
6. [Capstone architecture](docs/06-capstone-architecture.md)
7. [Educational resource library](docs/07-resource-library.md)
8. [Mastery evaluation framework](docs/08-mastery-framework.md)
9. [Career transition strategy](docs/09-career-transition.md)
10. [GitHub curriculum repository](docs/10-github-management.md)
11. [First 12 weeks](docs/11-first-12-weeks.md)
12. [Long-term maintenance strategy](docs/12-maintenance.md)

## Stage sequence

| Stage | Focus | Hours | Active weeks | Cumulative core hours |
|---|---|---:|---:|---:|
| S0 | Diagnostic and working environment | 10 | 2 | 10 |
| S1 | Independent Python software | 110 | 22 | 120 |
| S2 | Algorithms and discrete reasoning | 140 | 28 | 260 |
| S3 | Backend engineering and data products | 180 | 36 | 440 |
| S4 | Computer systems and concurrency | 160 | 32 | 600 |
| S5 | Mathematics and numerical experiments | 160 | 32 | 760 |
| S6 | Classical machine learning and data quality | 180 | 36 | 940 |
| S7 | Deep learning and a small language model | 200 | 40 | 1140 |
| S8 | Evidence-grounded AI applications | 180 | 36 | 1320 |
| S9 | Serving and distributed ML systems | 200 | 40 | 1520 |
| B1 | Distributed infrastructure specialization | 240 | 48 | optional |
| B2 | GPU and performance engineering | 320 | 64 | optional |
| B3 | Research engineering specialization | 240 | 48 | optional |
| B4 | AI compiler specialization | 240 | 48 | optional |

All project hours are contained within the stage budgets. The branches are alternatives; B4 requires B2. S5 can move earlier after S2 without increasing weekly hours. See [dependencies](docs/02-dependencies.md) for the full prerequisite map.

## Operational files

- [Complete weekly assignments](docs/weekly-assignments.md): 304 core weeks plus 208 optional branch weeks, grouped around coherent project increments.
- [Canonical plan](curriculum.json): prerequisites, hours, criteria, resource assignments and weekly allocations.
- `tracking/`: blank progress, skill, assessment, review and time-log files; no accomplishments have been prefilled.
- `templates/` and `.github/ISSUE_TEMPLATE/`: assessment, experiment, decision, retrospective, weekly and remediation templates.
- `scripts/validate.py`: checks time budgets, identifiers and prerequisite consistency.
- `scripts/render.py`: regenerates the stage guide and weekly views from the canonical plan.

Run `python3 scripts/validate.py` from this folder. After modifying the plan, run `python3 scripts/render.py` and validate again. Review/update explanatory prose for material changes.

## Scope and verification

This is a locally prepared repository scaffold, not a published GitHub repository. No remote issues, board, purchase, deployment or automation has been created. Forty resource landing pages were successfully retrieved; Meta's interview page was rate-limited and is labeled accordingly. Link availability does not guarantee public access to every course grader or future page. The compensation examples are posted salary figures, not invented total-compensation estimates or projected earnings.

Independent project acceptance checks and benchmarks are future learner tasks. The preparation validation checks the curriculum's structure; it does not claim that any learner projects or competencies have already been completed.
