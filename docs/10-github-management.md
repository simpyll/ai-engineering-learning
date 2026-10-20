# 10. GitHub curriculum repository and public evidence

This folder is a ready-to-upload repository scaffold. It has **not** been published to GitHub and no remote issues or boards have been created. All management can start locally; publishing can follow a review for personal data.

```text
README.md                     entry point and delivery index
curriculum.json               canonical stages, prerequisites, hours, resources, weeks
NOW.md                        current week and next action
CHANGELOG.md                  curriculum revisions
docs/                         twelve deliverables and generated weekly plan
tracking/
  skills.json                 mastery/evidence/review dates
  progress.json               weekly status and evidence links
  time-log.jsonl              actual sessions (initially empty)
  assessments.jsonl           task, score, evidence and reviewer (initially empty)
  reviews.json                due retrieval tasks
templates/                    ADR, assessment, experiment, retrospective
.github/ISSUE_TEMPLATE/        weekly work and remediation forms
.github/workflows/validate.yml canonical consistency check
scripts/validate.py            hours, identifiers, DAG and schedule checks
scripts/render.py              regenerate curriculum views after canonical changes
```

## GitHub setup

Create one central roadmap repository from this folder; keep personal diagnostics private if desired. Create milestones S0–S9, then only the selected branch. Use a Project board with **Backlog, Ready, In progress, Review, Done, Blocked**. Fields: stage, module, planned hours, actual hours, due review, evidence URL and assessment status. Use labels `learning`, `project`, `assessment`, `remediation`, `career`, `blocked-prerequisite`.

Open only the next four weekly issues using the supplied form and canonical weekly records. Each issue names its module, required prior evidence, five-hour budget, deliverable and completion criteria. Link dependencies explicitly in the issue body if your GitHub plan lacks dependency fields. A stage milestone closes only after all mandatory project and assessment evidence passes. An issue checked off without evidence is not mastery.

Work-in-progress limit: one module, one main project, one optional small collaboration task. No new language/framework unless the current project requires it. Put ideas in Backlog and review only at a module boundary. Do not spend weekly time perfecting the board.

## Always-visible dashboard

`NOW.md` answers: current week; reason; next build; planned hours; success criterion; resulting skill; blocked next step. At the end of each session record minutes, category, artifact/commit and next action in `time-log.jsonl`. After a gate, update progress/skills and schedule reviews. At every fourth week, write a short retrospective: actual versus planned, failure cause, scope change and next action.

Canonical editing rule: change prerequisites/hours/criteria in `curriculum.json`, validate and regenerate derived schedules. Update explanatory prose if architecture changes, record why in CHANGELOG, and keep past assessment evidence. Never silently overwrite actual hours or retroactively move failed results into passing categories. Module project contracts remain release gates in deliverable 5; changes to them need a documented curriculum revision.

## Public repository quality

Every meaningful original project or contribution needs: problem/users; personal contribution; installation; sample inputs/outputs; architecture; tests/CI; data/source license; benchmark/experiment commands and raw results; ADRs; known limitations; and what you would change at greater scale. Set a code license deliberately; do not assume dataset or model licenses match it. Use fake secrets and sanitized fixtures. Restrict publishing of course exercise answers according to course policy.

A good project claim is “On the specified 10k-record workload, this index changed p95 latency from X to Y; here are the scripts and trade-offs,” with actual measurements filled in after work. “Production-grade,” “scalable,” and “state of the art” require evidence and should not be default labels.

Make Simpyll a compact evidence index with four strong projects, not a second large front-end curriculum. Link failures, design decisions and independently reviewed changes. Git history helps explain work but is not proof of authorship; a live modification and technical defense are stronger.
