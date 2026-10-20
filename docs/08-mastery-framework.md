# 8. Mastery evaluation and remediation

Completing content earns no mastery credit. Each module needs a runnable artifact, explicit evidence for its acceptance criteria, an explanation and a transfer task. Save the task, result, reviewer, date, commit and assistance level.

| Dimension | Points | Evidence |
|---|---:|---|
| Functional correctness and test quality | 30 | Normal, boundary and failure cases; tests detect intentional defects |
| Conceptual/mathematical explanation | 20 | Explain invariants, assumptions and trade-offs; derive relevant relationships |
| Independent transfer/debugging | 20 | Unseen variation or seeded bug solved without generated solutions |
| Engineering and reproducibility | 20 | Clean run, readable boundaries, versioned dependencies/data, appropriate security |
| Communication and honest measurement | 10 | Clear README/design explanation; comparable benchmarks; limitations |

Pass: **80/100 overall and at least 60% in each dimension**, plus every mandatory gate. This is a curriculum threshold, not a claim of employer equivalence. For S0 use the diagnostic outcome rather than a graduation score. A module can use a short task; a stage exit requires an integrated demonstration and cumulative transfer task.

Mandatory gates: no known data leakage; no exposed secrets/private data; required authorization boundaries hold; no fabricated results; numerical comparisons use specified tolerances; failed tests are not hidden; source/data licenses and attribution documented. Any failure blocks release regardless of score. For ML, statistical correctness matters more than beating a chosen benchmark. For speed work, outputs must remain acceptable. For a deliberately educational security/storage component, the limitation must be explicit and it must not be presented as production safe.

## Assessment instruments

- **Programming:** 45-minute unseen function/change task, with explicit input/output examples, then 15-minute explanation. Ordinary language documentation can be allowed; AI-generated solutions are not. Example: add deterministic conflict handling for records with equal timestamps.
- **Algorithms:** explain an invariant, derive complexity, implement an unfamiliar variation and test adversarial cases. Tasks must fit the time limit; competitive-programming tricks are not the curriculum objective.
- **Math:** derive a gradient, interpret matrix dimensions, solve conditional probability, explain uncertainty and diagnose numerical instability. Each domain needs 80%; a strong average cannot hide a missing prerequisite.
- **Systems:** diagnose an unknown concurrency/retry/recovery defect; use evidence rather than guesses. Explain the failure model and what the test does not cover.
- **ML:** identify leakage in a deliberately flawed pipeline, choose a split and metric, interpret a baseline comparison and describe uncertainty.
- **Deep learning:** derive attention shapes, trace a gradient, diagnose a causal-mask bug, recover a checkpoint and explain training failure.
- **AI product:** audit citations, handle unsupported questions, inspect a tool-boundary attack and justify cost/latency/quality choices.
- **Research/performance:** critique an experiment, distinguish controlled from confounded comparisons, reproduce a small result and defend a negative finding.
- **Design:** 30–45-minute discussion of requirements, scale assumptions, alternatives, failure handling and a changed constraint. Use system-design interviews as practice, not as proof of operating the design.

Use mentor/peer review at S3, S6, S9 and branch exit if available. A reviewer should choose the unseen variation. Without one, record a delayed attempt from a fresh prompt and mark it self-assessed; AI-only grading is not independent validation. Do not claim external credibility until another person has actually reviewed the evidence.

## Diagnostic acceleration

For a module you may already know: take an unseen practical task, explain its core idea, satisfy its normal acceptance tests and pass the rubric. Recheck a different task after two weeks. Only then mark exempt/retained; log actual assessment hours and remove unused planned hours from the forecast. For mathematics, diagnose linear algebra, calculus, probability, statistics and numerics separately. Linux comfort can exempt shell navigation but not memory, concurrency or networking.

## Remediation protocol

1. Classify the failure: missing concept, syntax/tool gap, flawed test, design issue, unreliable recall or overbroad scope.
2. Make the smallest counterexample and explain the observed versus expected behavior.
3. Select one targeted resource section, not another entire course.
4. Spend 5–15 hours on a simpler implementation and two new cases; log the extension.
5. Retry with a different task. Two failures trigger prerequisite reassessment or mentor feedback.
6. Schedule retrieval in 1, 3 and 8 weeks and at the next cumulative review.

Examples: a broken gradient → hand-derive a two-parameter function and compare finite differences before returning to the network; duplicate imports → specify idempotency keys and test repeated/reordered inputs before adding concurrency; confusing confidence intervals → simulate coverage before reporting model comparisons; slow kernel → verify timing synchronization and memory traffic before trying another tile size.

## AI assistance policy

Before asking AI, write the expected behavior, your attempted approach and smallest failing case. Ask for a hint, counterexample, review or explanation. Record significant generated suggestions and verify them. Reference implementations, transfer tasks and conceptual defenses must be completed independently; subsequently compare to AI/library implementations. Production tooling may use AI more freely once the skill is demonstrated, with review and tests.

At each release include a short live or recorded walkthrough, a real design alternative, a measured failure and a small unprepared modification. These are stronger evidence of understanding than commit count, polished prose or unexplained generated code.
