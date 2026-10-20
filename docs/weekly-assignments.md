# Complete weekly assignments

Generated from `curriculum.json`. Core weeks are sequential; branch weeks are optional alternatives. Move dates after missed weeks. See resource library for assigned sections.

### W001 · S0.initial · Baseline and setup

**Deliverable:** Build a script reading five records and computing a count; make a branch and commit; complete arithmetic/logic diagnostic

**Pass:** Record baseline honestly; run script from fresh environment; explain each line

**Resources:** R01 functions; R03 Git Basics; R32 only if needed. **Time:** 5 hours (theory 0.5h, math 0.5h, exercise 1h, project 1h, debug 0.5h, review 0.5h, assessment 1h).

### W002 · S0.initial · Diagnostic and scope

**Deliverable:** Solve unseen parsing/filtering task; test Git conflict recovery; sample vectors, derivatives and probability; specify P1 fields and fixtures

**Pass:** Choose proceed/remediate per domain; no global exemption from self-reported confidence

**Resources:** R01 conditionals/loops; R15 diagnostic topics only. **Time:** 5 hours (theory 0.5h, math 1h, exercise 0.5h, project 1h, debug 0.5h, review 0.5h, assessment 1h).

### W003 · S1.initial · Functions and contracts

**Deliverable:** Write normalize_name and parse_tuition using simple documented input grammar; write example assertions

**Pass:** Five valid and five invalid examples; no silent conversion of unknown tuition to zero

**Resources:** R01 Functions/Variables and Conditionals; R02 chapter 4. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W004 · S1.initial · Collections and loops

**Deliverable:** Filter list of program dictionaries; count by state; deduplicate by stable identifier

**Pass:** Empty input, duplicate ID and missing field handled; explain why set/dict fits

**Resources:** R01 Loops; R02 chapter 5. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W005 · S1.initial · Files and provenance

**Deliverable:** Read local CSV fixture with standard library; emit JSON including source URL and retrieval date

**Pass:** Output parses; 20 fixture records preserve original source fields; no live scraping yet

**Resources:** R01 File I/O; R02 chapter 7. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W006 · S1.initial · Tests and retrieval checkpoint

**Deliverable:** Convert assertions to pytest; test malformed rows; reimplement one prior function without AI

**Pass:** Tests detect three intentionally seeded defects; fix errors and explain cause

**Resources:** R01 Unit Tests; R04 Get Started. **Time:** 5 hours (theory 0.5h, math 0h, exercise 0.5h, project 1h, debug 1h, review 0.5h, assessment 1.5h).

### W007 · S1.initial · Errors and command line

**Deliverable:** Add input/output paths, argparse help, nonzero error codes and specific exceptions

**Pass:** Missing file and invalid schema give helpful error; successful run exits zero

**Resources:** R01 Exceptions and Libraries; R02 chapters 6 and 8. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W008 · S1.initial · Pure functions and modules

**Deliverable:** Separate parse, normalize, validate and export; compare simple functions with a record class

**Pass:** I/O isolated; explain choice of abstraction; deterministic transformations tested

**Resources:** R02 chapters 6 and 9; R01 OOP selected. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W009 · S1.initial · Parser implementation

**Deliverable:** Write small field parser supporting commas in quoted names through CSV library; implement tuition-range grammar yourself

**Pass:** At least 15 specified parser cases including missing/invalid/range inputs; explain what grammar is unsupported

**Resources:** R01 Regular Expressions selected; R02 string methods. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W010 · S1.initial · Idempotent collection

**Deliverable:** Merge a second snapshot, track changed fields and preserve source metadata

**Pass:** Rerun yields identical normalized records; duplicate and conflicting records visibly resolved

**Resources:** R02 data structures and file handling review. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W011 · S1.initial · Debug and document

**Deliverable:** Fix two seeded bugs; write README quickstart and sample output; open local review diff

**Pass:** Clean-environment run works; explain one bug and prevention; no unmeasured speed claim

**Resources:** R32 Debugging/Profiling selected; R03 Branching. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W012 · S1.initial · Integration checkpoint and buffer

**Deliverable:** Demonstrate collector on unseen fixture; complete 45-minute no-AI function task; update skills ledger and review queue

**Pass:** 80/100 rubric; all integrity checks pass; if not, replace next planned week with remediation

**Resources:** R01/R04 only for failed objectives. **Time:** 5 hours (theory 0h, math 0h, exercise 0.5h, project 1h, debug 1h, review 0.5h, assessment 2h).

### W013 · S1.01 · Python abstractions — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Refactor collector using dataclasses, type annotations, generators and context managers. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Typed boundary validation; demonstrate generator memory behavior and two invalid-input cases.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W014 · S1.01 · Python abstractions — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P1: Refactor collector using dataclasses, type annotations, generators and context managers.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Typed boundary validation; demonstrate generator memory behavior and two invalid-input cases.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W015 · S1.01 · Python abstractions — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Typed boundary validation; demonstrate generator memory behavior and two invalid-input cases. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Typed boundary validation; demonstrate generator memory behavior and two invalid-input cases. Distinguish remaining failures from passes.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W016 · S1.01 · Python abstractions — Review, assess and repair

**Deliverable:** Demonstrate and explain python abstractions without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Typed boundary validation; demonstrate generator memory behavior and two invalid-input cases. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W017 · S1.02 · Design and debugging — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Separate pure transformations from I/O; compare procedural, OO and functional versions; profile a slow path. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain chosen design; locate two seeded bugs; compare before/after profile on identical input.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W018 · S1.02 · Design and debugging — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P1: Separate pure transformations from I/O; compare procedural, OO and functional versions; profile a slow path.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain chosen design; locate two seeded bugs; compare before/after profile on identical input.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W019 · S1.02 · Design and debugging — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain chosen design; locate two seeded bugs; compare before/after profile on identical input. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain chosen design; locate two seeded bugs; compare before/after profile on identical input. Distinguish remaining failures from passes.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W020 · S1.02 · Design and debugging — Review, assess and repair

**Deliverable:** Demonstrate and explain design and debugging without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain chosen design; locate two seeded bugs; compare before/after profile on identical input. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W021 · S1.03 · Release engineering — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Package the collector, add CI, changelog, documentation and a clean-environment install. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: One documented command processes fixtures; CI succeeds; closed-book parser task and release demo pass.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W022 · S1.03 · Release engineering — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P1: Package the collector, add CI, changelog, documentation and a clean-environment install.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: One documented command processes fixtures; CI succeeds; closed-book parser task and release demo pass.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W023 · S1.03 · Release engineering — Test and measure

**Deliverable:** Add adversarial tests and measurements for: One documented command processes fixtures; CI succeeds; closed-book parser task and release demo pass. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: One documented command processes fixtures; CI succeeds; closed-book parser task and release demo pass. Distinguish remaining failures from passes.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W024 · S1.03 · Release engineering — Review, assess and repair

**Deliverable:** Demonstrate and explain release engineering without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: One documented command processes fixtures; CI succeeds; closed-book parser task and release demo pass. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R01,R02,R03,R04. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W025 · S2.01 · Proofs and complexity — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Write loop invariants and operation counters for linear/binary search. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Prove termination and correctness; predict and measure scaling at three input sizes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W026 · S2.01 · Proofs and complexity — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Write loop invariants and operation counters for linear/binary search.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Prove termination and correctness; predict and measure scaling at three input sizes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W027 · S2.01 · Proofs and complexity — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Prove termination and correctness; predict and measure scaling at three input sizes. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Prove termination and correctness; predict and measure scaling at three input sizes. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W028 · S2.01 · Proofs and complexity — Review, assess and repair

**Deliverable:** Demonstrate and explain proofs and complexity without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Prove termination and correctness; predict and measure scaling at three input sizes. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W029 · S2.02 · Sorting and hashing — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement mergesort and a collision-handling hash table. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Match reference results on random/adversarial cases; explain worst-case versus expected costs.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W030 · S2.02 · Sorting and hashing — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Implement mergesort and a collision-handling hash table.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Match reference results on random/adversarial cases; explain worst-case versus expected costs.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W031 · S2.02 · Sorting and hashing — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Match reference results on random/adversarial cases; explain worst-case versus expected costs. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Match reference results on random/adversarial cases; explain worst-case versus expected costs. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W032 · S2.02 · Sorting and hashing — Review, assess and repair

**Deliverable:** Demonstrate and explain sorting and hashing without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Match reference results on random/adversarial cases; explain worst-case versus expected costs. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W033 · S2.03 · Trees and heaps — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement binary search tree operations and a heap-based top-k selector. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Property tests preserve ordering; handle duplicate/empty input; explain skewed-tree behavior.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W034 · S2.03 · Trees and heaps — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Implement binary search tree operations and a heap-based top-k selector.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Property tests preserve ordering; handle duplicate/empty input; explain skewed-tree behavior.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W035 · S2.03 · Trees and heaps — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Property tests preserve ordering; handle duplicate/empty input; explain skewed-tree behavior. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Property tests preserve ordering; handle duplicate/empty input; explain skewed-tree behavior. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W036 · S2.03 · Trees and heaps — Review, assess and repair

**Deliverable:** Demonstrate and explain trees and heaps without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Property tests preserve ordering; handle duplicate/empty input; explain skewed-tree behavior. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W037 · S2.04 · Graphs — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement BFS, DFS, topological ordering and Dijkstra on program/prerequisite graphs. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Detect cycles; compare shortest paths with tiny hand-solved examples; reject unsupported negative weights.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W038 · S2.04 · Graphs — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Implement BFS, DFS, topological ordering and Dijkstra on program/prerequisite graphs.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Detect cycles; compare shortest paths with tiny hand-solved examples; reject unsupported negative weights.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W039 · S2.04 · Graphs — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Detect cycles; compare shortest paths with tiny hand-solved examples; reject unsupported negative weights. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Detect cycles; compare shortest paths with tiny hand-solved examples; reject unsupported negative weights. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W040 · S2.04 · Graphs — Review, assess and repair

**Deliverable:** Demonstrate and explain graphs without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Detect cycles; compare shortest paths with tiny hand-solved examples; reject unsupported negative weights. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W041 · S2.05 · Dynamic programming — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement edit distance and one knapsack-style problem. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Derive recurrence and base cases; compare memoized and tabulated versions.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W042 · S2.05 · Dynamic programming — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Implement edit distance and one knapsack-style problem.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Derive recurrence and base cases; compare memoized and tabulated versions.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W043 · S2.05 · Dynamic programming — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Derive recurrence and base cases; compare memoized and tabulated versions. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Derive recurrence and base cases; compare memoized and tabulated versions. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W044 · S2.05 · Dynamic programming — Review, assess and repair

**Deliverable:** Demonstrate and explain dynamic programming without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Derive recurrence and base cases; compare memoized and tabulated versions. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W045 · S2.06 · Index and ranking — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build an inverted index and ranked keyword search over program fixtures. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Queries return known documents; explain tokenization and ranking; compare with linear scan.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W046 · S2.06 · Index and ranking — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Build an inverted index and ranked keyword search over program fixtures.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Queries return known documents; explain tokenization and ranking; compare with linear scan.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W047 · S2.06 · Index and ranking — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Queries return known documents; explain tokenization and ranking; compare with linear scan. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Queries return known documents; explain tokenization and ranking; compare with linear scan. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W048 · S2.06 · Index and ranking — Review, assess and repair

**Deliverable:** Demonstrate and explain index and ranking without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Queries return known documents; explain tokenization and ranking; compare with linear scan. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W049 · S2.07 · Integration and interview — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Integrate search into collector; solve unseen array and graph tasks. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: All P2 tests pass; defend complexity; solve two appropriately scoped unseen tasks with explanation.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W050 · S2.07 · Integration and interview — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P2: Integrate search into collector; solve unseen array and graph tasks.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: All P2 tests pass; defend complexity; solve two appropriately scoped unseen tasks with explanation.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W051 · S2.07 · Integration and interview — Test and measure

**Deliverable:** Add adversarial tests and measurements for: All P2 tests pass; defend complexity; solve two appropriately scoped unseen tasks with explanation. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: All P2 tests pass; defend complexity; solve two appropriately scoped unseen tasks with explanation. Distinguish remaining failures from passes.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W052 · S2.07 · Integration and interview — Review, assess and repair

**Deliverable:** Demonstrate and explain integration and interview without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: All P2 tests pass; defend complexity; solve two appropriately scoped unseen tasks with explanation. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R05,R06. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W053 · S3.01 · Relational modeling — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Model schools, programs, source snapshots and provenance in SQL. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Constraints reject invalid relations; migration and rollback work on fixtures.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W054 · S3.01 · Relational modeling — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Model schools, programs, source snapshots and provenance in SQL.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Constraints reject invalid relations; migration and rollback work on fixtures.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W055 · S3.01 · Relational modeling — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Constraints reject invalid relations; migration and rollback work on fixtures. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Constraints reject invalid relations; migration and rollback work on fixtures. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W056 · S3.01 · Relational modeling — Review, assess and repair

**Deliverable:** Demonstrate and explain relational modeling without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Constraints reject invalid relations; migration and rollback work on fixtures. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W057 · S3.02 · SQL and transactions — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement joins, aggregates, pagination and concurrent updates. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain transaction isolation; tests expose and prevent a lost update.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W058 · S3.02 · SQL and transactions — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Implement joins, aggregates, pagination and concurrent updates.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain transaction isolation; tests expose and prevent a lost update.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W059 · S3.02 · SQL and transactions — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain transaction isolation; tests expose and prevent a lost update. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain transaction isolation; tests expose and prevent a lost update. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W060 · S3.02 · SQL and transactions — Review, assess and repair

**Deliverable:** Demonstrate and explain sql and transactions without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain transaction isolation; tests expose and prevent a lost update. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W061 · S3.03 · HTTP and API contracts — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Inspect a raw HTTP request locally; build typed endpoints and validation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Contract tests cover status codes, malformed inputs and pagination bounds.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W062 · S3.03 · HTTP and API contracts — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Inspect a raw HTTP request locally; build typed endpoints and validation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Contract tests cover status codes, malformed inputs and pagination bounds.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W063 · S3.03 · HTTP and API contracts — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Contract tests cover status codes, malformed inputs and pagination bounds. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Contract tests cover status codes, malformed inputs and pagination bounds. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W064 · S3.03 · HTTP and API contracts — Review, assess and repair

**Deliverable:** Demonstrate and explain http and api contracts without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Contract tests cover status codes, malformed inputs and pagination bounds. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W065 · S3.04 · Authentication and security — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add maintained auth integration, role-based authorization and secret handling. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Anonymous writes and cross-user access denied; parameterized queries resist injection fixtures.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W066 · S3.04 · Authentication and security — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Add maintained auth integration, role-based authorization and secret handling.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Anonymous writes and cross-user access denied; parameterized queries resist injection fixtures.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W067 · S3.04 · Authentication and security — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Anonymous writes and cross-user access denied; parameterized queries resist injection fixtures. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Anonymous writes and cross-user access denied; parameterized queries resist injection fixtures. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W068 · S3.04 · Authentication and security — Review, assess and repair

**Deliverable:** Demonstrate and explain authentication and security without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Anonymous writes and cross-user access denied; parameterized queries resist injection fixtures. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W069 · S3.05 · Reliable ingestion — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Import source snapshots with idempotency, schema validation and retry budgets. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Second import creates zero duplicates; malformed records quarantined with provenance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W070 · S3.05 · Reliable ingestion — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Import source snapshots with idempotency, schema validation and retry budgets.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Second import creates zero duplicates; malformed records quarantined with provenance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W071 · S3.05 · Reliable ingestion — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Second import creates zero duplicates; malformed records quarantined with provenance. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Second import creates zero duplicates; malformed records quarantined with provenance. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W072 · S3.05 · Reliable ingestion — Review, assess and repair

**Deliverable:** Demonstrate and explain reliable ingestion without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Second import creates zero duplicates; malformed records quarantined with provenance. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W073 · S3.06 · Indexes and caching — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Profile SQL queries; add index and bounded cache with invalidation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Query plan and latency distribution recorded; stale-cache scenario tested.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W074 · S3.06 · Indexes and caching — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Profile SQL queries; add index and bounded cache with invalidation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Query plan and latency distribution recorded; stale-cache scenario tested.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W075 · S3.06 · Indexes and caching — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Query plan and latency distribution recorded; stale-cache scenario tested. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Query plan and latency distribution recorded; stale-cache scenario tested. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W076 · S3.06 · Indexes and caching — Review, assess and repair

**Deliverable:** Demonstrate and explain indexes and caching without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Query plan and latency distribution recorded; stale-cache scenario tested. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W077 · S3.07 · Deployment and CI — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Containerize API/database; add automated tests and repeatable staging deployment. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Fresh clone starts service; failed checks block release; rollback demonstrated.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W078 · S3.07 · Deployment and CI — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Containerize API/database; add automated tests and repeatable staging deployment.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Fresh clone starts service; failed checks block release; rollback demonstrated.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W079 · S3.07 · Deployment and CI — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Fresh clone starts service; failed checks block release; rollback demonstrated. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Fresh clone starts service; failed checks block release; rollback demonstrated. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W080 · S3.07 · Deployment and CI — Review, assess and repair

**Deliverable:** Demonstrate and explain deployment and ci without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Fresh clone starts service; failed checks block release; rollback demonstrated. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W081 · S3.08 · Operations — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add structured logs, health checks, metrics, backup and restore procedure. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Restore into empty database; diagnose injected outage; define one user-facing SLO.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W082 · S3.08 · Operations — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Add structured logs, health checks, metrics, backup and restore procedure.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Restore into empty database; diagnose injected outage; define one user-facing SLO.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W083 · S3.08 · Operations — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Restore into empty database; diagnose injected outage; define one user-facing SLO. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Restore into empty database; diagnose injected outage; define one user-facing SLO. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W084 · S3.08 · Operations — Review, assess and repair

**Deliverable:** Demonstrate and explain operations without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Restore into empty database; diagnose injected outage; define one user-facing SLO. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W085 · S3.09 · Release and job checkpoint — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Run load test, external review, architecture explanation and portfolio release. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P3 contract and mastery rubric pass; record bottleneck, limits and a reviewed change.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W086 · S3.09 · Release and job checkpoint — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P3: Run load test, external review, architecture explanation and portfolio release.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P3 contract and mastery rubric pass; record bottleneck, limits and a reviewed change.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W087 · S3.09 · Release and job checkpoint — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P3 contract and mastery rubric pass; record bottleneck, limits and a reviewed change. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P3 contract and mastery rubric pass; record bottleneck, limits and a reviewed change. Distinguish remaining failures from passes.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W088 · S3.09 · Release and job checkpoint — Review, assess and repair

**Deliverable:** Demonstrate and explain release and job checkpoint without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P3 contract and mastery rubric pass; record bottleneck, limits and a reviewed change. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R07,R08,R09,R10,R24. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W089 · S4.01 · Representation and architecture — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build small ALU simulation; inspect compiled arithmetic and cache-sensitive loops. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain signed/unsigned overflow and cache locality using measured examples.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W090 · S4.01 · Representation and architecture — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Build small ALU simulation; inspect compiled arithmetic and cache-sensitive loops.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain signed/unsigned overflow and cache locality using measured examples.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W091 · S4.01 · Representation and architecture — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain signed/unsigned overflow and cache locality using measured examples. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain signed/unsigned overflow and cache locality using measured examples. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W092 · S4.01 · Representation and architecture — Review, assess and repair

**Deliverable:** Demonstrate and explain representation and architecture without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain signed/unsigned overflow and cache locality using measured examples. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W093 · S4.02 · C and memory — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Write C array/string routines and a small owned buffer. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Compiler warnings clean; memory sanitizer finds then verifies repair of bounds/lifetime bugs.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W094 · S4.02 · C and memory — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Write C array/string routines and a small owned buffer.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Compiler warnings clean; memory sanitizer finds then verifies repair of bounds/lifetime bugs.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W095 · S4.02 · C and memory — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Compiler warnings clean; memory sanitizer finds then verifies repair of bounds/lifetime bugs. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Compiler warnings clean; memory sanitizer finds then verifies repair of bounds/lifetime bugs. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W096 · S4.02 · C and memory — Review, assess and repair

**Deliverable:** Demonstrate and explain c and memory without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Compiler warnings clean; memory sanitizer finds then verifies repair of bounds/lifetime bugs. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W097 · S4.03 · Processes and virtual memory — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Create process pipeline and inspect address-space/memory behavior. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain fork/exec, file descriptors and virtual versus physical memory; reap child processes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W098 · S4.03 · Processes and virtual memory — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Create process pipeline and inspect address-space/memory behavior.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain fork/exec, file descriptors and virtual versus physical memory; reap child processes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W099 · S4.03 · Processes and virtual memory — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain fork/exec, file descriptors and virtual versus physical memory; reap child processes. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain fork/exec, file descriptors and virtual versus physical memory; reap child processes. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W100 · S4.03 · Processes and virtual memory — Review, assess and repair

**Deliverable:** Demonstrate and explain processes and virtual memory without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain fork/exec, file descriptors and virtual versus physical memory; reap child processes. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W101 · S4.04 · Threads and synchronization — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build bounded producer-consumer queue with locks/conditions. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Stress test for races/deadlocks; explain each shared-state invariant.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W102 · S4.04 · Threads and synchronization — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Build bounded producer-consumer queue with locks/conditions.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Stress test for races/deadlocks; explain each shared-state invariant.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W103 · S4.04 · Threads and synchronization — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Stress test for races/deadlocks; explain each shared-state invariant. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Stress test for races/deadlocks; explain each shared-state invariant. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W104 · S4.04 · Threads and synchronization — Review, assess and repair

**Deliverable:** Demonstrate and explain threads and synchronization without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Stress test for races/deadlocks; explain each shared-state invariant. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W105 · S4.05 · Async and parallel work — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Compare threads, processes and async fetching on local simulated I/O. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Bound concurrency; measure CPU/I/O workloads; explain interpreter/runtime limits.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W106 · S4.05 · Async and parallel work — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Compare threads, processes and async fetching on local simulated I/O.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Bound concurrency; measure CPU/I/O workloads; explain interpreter/runtime limits.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W107 · S4.05 · Async and parallel work — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Bound concurrency; measure CPU/I/O workloads; explain interpreter/runtime limits. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Bound concurrency; measure CPU/I/O workloads; explain interpreter/runtime limits. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W108 · S4.05 · Async and parallel work — Review, assess and repair

**Deliverable:** Demonstrate and explain async and parallel work without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Bound concurrency; measure CPU/I/O workloads; explain interpreter/runtime limits. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W109 · S4.06 · Networking — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Write local TCP client/server with framing, timeouts and partial-read handling. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Fragmented messages reassemble; disconnect and timeout tests pass; explain DNS/TLS/HTTP roles.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W110 · S4.06 · Networking — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Write local TCP client/server with framing, timeouts and partial-read handling.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Fragmented messages reassemble; disconnect and timeout tests pass; explain DNS/TLS/HTTP roles.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W111 · S4.06 · Networking — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Fragmented messages reassemble; disconnect and timeout tests pass; explain DNS/TLS/HTTP roles. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Fragmented messages reassemble; disconnect and timeout tests pass; explain DNS/TLS/HTTP roles. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W112 · S4.06 · Networking — Review, assess and repair

**Deliverable:** Demonstrate and explain networking without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Fragmented messages reassemble; disconnect and timeout tests pass; explain DNS/TLS/HTTP roles. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W113 · S4.07 · Persistence and interpreters — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build append-only record log with recovery plus tiny expression parser/evaluator. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Recover valid prefix after truncated write; reject malformed expressions; explain AST and execution.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W114 · S4.07 · Persistence and interpreters — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Build append-only record log with recovery plus tiny expression parser/evaluator.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Recover valid prefix after truncated write; reject malformed expressions; explain AST and execution.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W115 · S4.07 · Persistence and interpreters — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Recover valid prefix after truncated write; reject malformed expressions; explain AST and execution. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Recover valid prefix after truncated write; reject malformed expressions; explain AST and execution. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W116 · S4.07 · Persistence and interpreters — Review, assess and repair

**Deliverable:** Demonstrate and explain persistence and interpreters without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Recover valid prefix after truncated write; reject malformed expressions; explain AST and execution. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W117 · S4.08 · Systems integration — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Integrate worker and log with ingestion; profile and document failure modes. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Kill worker mid-job and recover without duplicate committed records; P4 oral/debugging gate passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W118 · S4.08 · Systems integration — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P4: Integrate worker and log with ingestion; profile and document failure modes.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Kill worker mid-job and recover without duplicate committed records; P4 oral/debugging gate passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W119 · S4.08 · Systems integration — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Kill worker mid-job and recover without duplicate committed records; P4 oral/debugging gate passes. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Kill worker mid-job and recover without duplicate committed records; P4 oral/debugging gate passes. Distinguish remaining failures from passes.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.75h, math 0.25h, exercise 0.75h, project 1.75h, debug 0.75h, review 0.5h, assessment 0.25h).

### W120 · S4.08 · Systems integration — Review, assess and repair

**Deliverable:** Demonstrate and explain systems integration without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Kill worker mid-job and recover without duplicate committed records; P4 oral/debugging gate passes. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R11,R12,R13,R14,R32. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W121 · S5.01 · Vectors and geometry — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement dot products/projections and a least-squares geometry notebook. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Dimensions correct; explain span, rank, orthogonality and geometric interpretation.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W122 · S5.01 · Vectors and geometry — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Implement dot products/projections and a least-squares geometry notebook.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Dimensions correct; explain span, rank, orthogonality and geometric interpretation.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W123 · S5.01 · Vectors and geometry — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Dimensions correct; explain span, rank, orthogonality and geometric interpretation. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Dimensions correct; explain span, rank, orthogonality and geometric interpretation. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W124 · S5.01 · Vectors and geometry — Review, assess and repair

**Deliverable:** Demonstrate and explain vectors and geometry without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Dimensions correct; explain span, rank, orthogonality and geometric interpretation. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W125 · S5.02 · Linear algebra — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement small elimination solver; compare QR/SVD-based library solves. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Residuals reported; explain conditioning and why explicit inverse is avoided.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W126 · S5.02 · Linear algebra — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Implement small elimination solver; compare QR/SVD-based library solves.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Residuals reported; explain conditioning and why explicit inverse is avoided.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W127 · S5.02 · Linear algebra — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Residuals reported; explain conditioning and why explicit inverse is avoided. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Residuals reported; explain conditioning and why explicit inverse is avoided. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W128 · S5.02 · Linear algebra — Review, assess and repair

**Deliverable:** Demonstrate and explain linear algebra without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Residuals reported; explain conditioning and why explicit inverse is avoided. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W129 · S5.03 · Calculus — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Derive scalar/vector chain rules and implement finite-difference checks. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Check gradients on three functions; explain Jacobian shapes and numerical error.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W130 · S5.03 · Calculus — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Derive scalar/vector chain rules and implement finite-difference checks.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Check gradients on three functions; explain Jacobian shapes and numerical error.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W131 · S5.03 · Calculus — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Check gradients on three functions; explain Jacobian shapes and numerical error. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Check gradients on three functions; explain Jacobian shapes and numerical error. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W132 · S5.03 · Calculus — Review, assess and repair

**Deliverable:** Demonstrate and explain calculus without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Check gradients on three functions; explain Jacobian shapes and numerical error. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W133 · S5.04 · Probability — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Simulate conditional events and Bayes updates; compute moments. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Match analytical results within Monte Carlo uncertainty; distinguish independence/conditional independence.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W134 · S5.04 · Probability — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Simulate conditional events and Bayes updates; compute moments.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Match analytical results within Monte Carlo uncertainty; distinguish independence/conditional independence.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W135 · S5.04 · Probability — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Match analytical results within Monte Carlo uncertainty; distinguish independence/conditional independence. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Match analytical results within Monte Carlo uncertainty; distinguish independence/conditional independence. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W136 · S5.04 · Probability — Review, assess and repair

**Deliverable:** Demonstrate and explain probability without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Match analytical results within Monte Carlo uncertainty; distinguish independence/conditional independence. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W137 · S5.05 · Inference and experiment design — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Bootstrap a metric and simulate confidence-interval coverage. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain sampling unit, uncertainty, multiple comparisons and why association is not causation.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W138 · S5.05 · Inference and experiment design — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Bootstrap a metric and simulate confidence-interval coverage.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain sampling unit, uncertainty, multiple comparisons and why association is not causation.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W139 · S5.05 · Inference and experiment design — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain sampling unit, uncertainty, multiple comparisons and why association is not causation. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain sampling unit, uncertainty, multiple comparisons and why association is not causation. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W140 · S5.05 · Inference and experiment design — Review, assess and repair

**Deliverable:** Demonstrate and explain inference and experiment design without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain sampling unit, uncertainty, multiple comparisons and why association is not causation. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W141 · S5.06 · Optimization — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement gradient descent with learning-rate and regularization experiments. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Derive least-squares gradient; show convergent/divergent cases without hiding failures.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W142 · S5.06 · Optimization — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Implement gradient descent with learning-rate and regularization experiments.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Derive least-squares gradient; show convergent/divergent cases without hiding failures.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W143 · S5.06 · Optimization — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Derive least-squares gradient; show convergent/divergent cases without hiding failures. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Derive least-squares gradient; show convergent/divergent cases without hiding failures. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W144 · S5.06 · Optimization — Review, assess and repair

**Deliverable:** Demonstrate and explain optimization without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Derive least-squares gradient; show convergent/divergent cases without hiding failures. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W145 · S5.07 · Information and numerics — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement stable softmax/log-sum-exp, entropy and KL on discrete distributions. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Handle extreme logits; explain floating-point cancellation and KL directionality.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W146 · S5.07 · Information and numerics — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Implement stable softmax/log-sum-exp, entropy and KL on discrete distributions.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Handle extreme logits; explain floating-point cancellation and KL directionality.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W147 · S5.07 · Information and numerics — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Handle extreme logits; explain floating-point cancellation and KL directionality. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Handle extreme logits; explain floating-point cancellation and KL directionality. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W148 · S5.07 · Information and numerics — Review, assess and repair

**Deliverable:** Demonstrate and explain information and numerics without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Handle extreme logits; explain floating-point cancellation and KL directionality. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W149 · S5.08 · Math gate — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build PCA via SVD and defend derivations plus simulation notebook. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Pass five-domain diagnostic at 80% per domain; unseen gradient and probability tasks pass.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W150 · S5.08 · Math gate — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P5: Build PCA via SVD and defend derivations plus simulation notebook.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Pass five-domain diagnostic at 80% per domain; unseen gradient and probability tasks pass.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W151 · S5.08 · Math gate — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Pass five-domain diagnostic at 80% per domain; unseen gradient and probability tasks pass. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Pass five-domain diagnostic at 80% per domain; unseen gradient and probability tasks pass. Distinguish remaining failures from passes.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.5h, math 1.5h, exercise 1h, project 0.75h, debug 0.5h, review 0.5h, assessment 0.25h).

### W152 · S5.08 · Math gate — Review, assess and repair

**Deliverable:** Demonstrate and explain math gate without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Pass five-domain diagnostic at 80% per domain; unseen gradient and probability tasks pass. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R15,R16. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W153 · S6.01 · Data contracts and EDA — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Create versioned dataset, missingness report and provenance ledger. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Document labels, unit of observation, allowed usage and leakage risks.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W154 · S6.01 · Data contracts and EDA — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Create versioned dataset, missingness report and provenance ledger.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Document labels, unit of observation, allowed usage and leakage risks.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W155 · S6.01 · Data contracts and EDA — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Document labels, unit of observation, allowed usage and leakage risks. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Document labels, unit of observation, allowed usage and leakage risks. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W156 · S6.01 · Data contracts and EDA — Review, assess and repair

**Deliverable:** Demonstrate and explain data contracts and eda without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Document labels, unit of observation, allowed usage and leakage risks. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W157 · S6.02 · Regression from scratch — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement linear/ridge regression and compare to library reference. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Gradient check passes; residuals and baseline metric recorded.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W158 · S6.02 · Regression from scratch — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Implement linear/ridge regression and compare to library reference.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Gradient check passes; residuals and baseline metric recorded.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W159 · S6.02 · Regression from scratch — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Gradient check passes; residuals and baseline metric recorded. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Gradient check passes; residuals and baseline metric recorded. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W160 · S6.02 · Regression from scratch — Review, assess and repair

**Deliverable:** Demonstrate and explain regression from scratch without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Gradient check passes; residuals and baseline metric recorded. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W161 · S6.03 · Classification from scratch — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement logistic regression with stable loss. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Gradient and prediction checks pass; class imbalance and threshold trade-off explained.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W162 · S6.03 · Classification from scratch — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Implement logistic regression with stable loss.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Gradient and prediction checks pass; class imbalance and threshold trade-off explained.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W163 · S6.03 · Classification from scratch — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Gradient and prediction checks pass; class imbalance and threshold trade-off explained. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Gradient and prediction checks pass; class imbalance and threshold trade-off explained. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W164 · S6.03 · Classification from scratch — Review, assess and repair

**Deliverable:** Demonstrate and explain classification from scratch without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Gradient and prediction checks pass; class imbalance and threshold trade-off explained. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W165 · S6.04 · Trees and ensembles — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement tiny decision stump then compare tree and ensemble models. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Validate split logic; tuning uses only training/validation data.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W166 · S6.04 · Trees and ensembles — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Implement tiny decision stump then compare tree and ensemble models.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Validate split logic; tuning uses only training/validation data.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W167 · S6.04 · Trees and ensembles — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Validate split logic; tuning uses only training/validation data. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Validate split logic; tuning uses only training/validation data. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W168 · S6.04 · Trees and ensembles — Review, assess and repair

**Deliverable:** Demonstrate and explain trees and ensembles without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Validate split logic; tuning uses only training/validation data. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W169 · S6.05 · Unsupervised learning — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement k-means and compare PCA/cluster assignments. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain initialization sensitivity and why clusters are not ground truth.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W170 · S6.05 · Unsupervised learning — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Implement k-means and compare PCA/cluster assignments.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain initialization sensitivity and why clusters are not ground truth.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W171 · S6.05 · Unsupervised learning — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain initialization sensitivity and why clusters are not ground truth. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain initialization sensitivity and why clusters are not ground truth. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W172 · S6.05 · Unsupervised learning — Review, assess and repair

**Deliverable:** Demonstrate and explain unsupervised learning without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain initialization sensitivity and why clusters are not ground truth. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W173 · S6.06 · Evaluation and features — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build preprocessing pipeline with group/time-aware cross-validation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: No test-set fitting; compare dummy, linear and tree baselines with uncertainty.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W174 · S6.06 · Evaluation and features — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Build preprocessing pipeline with group/time-aware cross-validation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: No test-set fitting; compare dummy, linear and tree baselines with uncertainty.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W175 · S6.06 · Evaluation and features — Test and measure

**Deliverable:** Add adversarial tests and measurements for: No test-set fitting; compare dummy, linear and tree baselines with uncertainty. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: No test-set fitting; compare dummy, linear and tree baselines with uncertainty. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W176 · S6.06 · Evaluation and features — Review, assess and repair

**Deliverable:** Demonstrate and explain evaluation and features without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: No test-set fitting; compare dummy, linear and tree baselines with uncertainty. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W177 · S6.07 · Robustness and calibration — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Evaluate subgroup errors, calibration, drift and out-of-domain behavior. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Choose metric from task costs; report unsupported subgroup conclusions honestly.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W178 · S6.07 · Robustness and calibration — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Evaluate subgroup errors, calibration, drift and out-of-domain behavior.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Choose metric from task costs; report unsupported subgroup conclusions honestly.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W179 · S6.07 · Robustness and calibration — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Choose metric from task costs; report unsupported subgroup conclusions honestly. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Choose metric from task costs; report unsupported subgroup conclusions honestly. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W180 · S6.07 · Robustness and calibration — Review, assess and repair

**Deliverable:** Demonstrate and explain robustness and calibration without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Choose metric from task costs; report unsupported subgroup conclusions honestly. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W181 · S6.08 · Model service — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Package model and preprocessing together; add schema and drift checks. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Offline/online predictions match; rollback to baseline works; artifact/data versions traceable.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W182 · S6.08 · Model service — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Package model and preprocessing together; add schema and drift checks.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Offline/online predictions match; rollback to baseline works; artifact/data versions traceable.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W183 · S6.08 · Model service — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Offline/online predictions match; rollback to baseline works; artifact/data versions traceable. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Offline/online predictions match; rollback to baseline works; artifact/data versions traceable. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W184 · S6.08 · Model service — Review, assess and repair

**Deliverable:** Demonstrate and explain model service without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Offline/online predictions match; rollback to baseline works; artifact/data versions traceable. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W185 · S6.09 · ML release — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Freeze test set, run final experiment, produce model/data cards and technical defense. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P6 reproducibility and leakage gates pass; explain a failed model and whether ML adds value.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W186 · S6.09 · ML release — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P6: Freeze test set, run final experiment, produce model/data cards and technical defense.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P6 reproducibility and leakage gates pass; explain a failed model and whether ML adds value.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W187 · S6.09 · ML release — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P6 reproducibility and leakage gates pass; explain a failed model and whether ML adds value. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P6 reproducibility and leakage gates pass; explain a failed model and whether ML adds value. Distinguish remaining failures from passes.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W188 · S6.09 · ML release — Review, assess and repair

**Deliverable:** Demonstrate and explain ml release without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P6 reproducibility and leakage gates pass; explain a failed model and whether ML adds value. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R17,R19,R21. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W189 · S7.01 · Tensors and autograd — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build scalar autograd engine and a small tensor computation graph. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Finite-difference gradients match within declared tolerance on well-conditioned float64 examples.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W190 · S7.01 · Tensors and autograd — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Build scalar autograd engine and a small tensor computation graph.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Finite-difference gradients match within declared tolerance on well-conditioned float64 examples.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W191 · S7.01 · Tensors and autograd — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Finite-difference gradients match within declared tolerance on well-conditioned float64 examples. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Finite-difference gradients match within declared tolerance on well-conditioned float64 examples. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W192 · S7.01 · Tensors and autograd — Review, assess and repair

**Deliverable:** Demonstrate and explain tensors and autograd without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Finite-difference gradients match within declared tolerance on well-conditioned float64 examples. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W193 · S7.02 · MLP and backpropagation — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement two-layer network in NumPy then reproduce in PyTorch. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Derive gradients; overfit tiny batch; identify deliberately broken gradient.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W194 · S7.02 · MLP and backpropagation — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Implement two-layer network in NumPy then reproduce in PyTorch.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Derive gradients; overfit tiny batch; identify deliberately broken gradient.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W195 · S7.02 · MLP and backpropagation — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Derive gradients; overfit tiny batch; identify deliberately broken gradient. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Derive gradients; overfit tiny batch; identify deliberately broken gradient. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W196 · S7.02 · MLP and backpropagation — Review, assess and repair

**Deliverable:** Demonstrate and explain mlp and backpropagation without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Derive gradients; overfit tiny batch; identify deliberately broken gradient. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W197 · S7.03 · Training discipline — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement seeds, checkpointing, learning-rate schedules and regularization. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Resume training; compare controlled runs; separate optimization failure from overfitting.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W198 · S7.03 · Training discipline — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Implement seeds, checkpointing, learning-rate schedules and regularization.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Resume training; compare controlled runs; separate optimization failure from overfitting.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W199 · S7.03 · Training discipline — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Resume training; compare controlled runs; separate optimization failure from overfitting. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Resume training; compare controlled runs; separate optimization failure from overfitting. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W200 · S7.03 · Training discipline — Review, assess and repair

**Deliverable:** Demonstrate and explain training discipline without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Resume training; compare controlled runs; separate optimization failure from overfitting. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W201 · S7.04 · CNNs — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement a convolution reference and train small image classifier. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Compare operator to framework; report held-out accuracy and translation limitations.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W202 · S7.04 · CNNs — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Implement a convolution reference and train small image classifier.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Compare operator to framework; report held-out accuracy and translation limitations.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W203 · S7.04 · CNNs — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Compare operator to framework; report held-out accuracy and translation limitations. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Compare operator to framework; report held-out accuracy and translation limitations. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W204 · S7.04 · CNNs — Review, assess and repair

**Deliverable:** Demonstrate and explain cnns without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Compare operator to framework; report held-out accuracy and translation limitations. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W205 · S7.05 · Sequences and representations — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement recurrent cell and compare sequence baseline plus embeddings. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Handle padding/masks; explain vanishing gradients and representation geometry.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W206 · S7.05 · Sequences and representations — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Implement recurrent cell and compare sequence baseline plus embeddings.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Handle padding/masks; explain vanishing gradients and representation geometry.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W207 · S7.05 · Sequences and representations — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Handle padding/masks; explain vanishing gradients and representation geometry. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Handle padding/masks; explain vanishing gradients and representation geometry. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W208 · S7.05 · Sequences and representations — Review, assess and repair

**Deliverable:** Demonstrate and explain sequences and representations without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Handle padding/masks; explain vanishing gradients and representation geometry. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W209 · S7.06 · Tokenizer and data — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement small BPE tokenizer and licensed text split pipeline. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Round-trip tests pass; train/validation documents disjoint; unknown/Unicode behavior documented.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W210 · S7.06 · Tokenizer and data — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Implement small BPE tokenizer and licensed text split pipeline.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Round-trip tests pass; train/validation documents disjoint; unknown/Unicode behavior documented.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W211 · S7.06 · Tokenizer and data — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Round-trip tests pass; train/validation documents disjoint; unknown/Unicode behavior documented. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Round-trip tests pass; train/validation documents disjoint; unknown/Unicode behavior documented. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W212 · S7.06 · Tokenizer and data — Review, assess and repair

**Deliverable:** Demonstrate and explain tokenizer and data without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Round-trip tests pass; train/validation documents disjoint; unknown/Unicode behavior documented. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W213 · S7.07 · Attention — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement masked scaled dot-product and multi-head attention. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Reference parity and future-token leakage tests pass; shapes/complexity explained.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W214 · S7.07 · Attention — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Implement masked scaled dot-product and multi-head attention.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Reference parity and future-token leakage tests pass; shapes/complexity explained.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W215 · S7.07 · Attention — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Reference parity and future-token leakage tests pass; shapes/complexity explained. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Reference parity and future-token leakage tests pass; shapes/complexity explained. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W216 · S7.07 · Attention — Review, assess and repair

**Deliverable:** Demonstrate and explain attention without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Reference parity and future-token leakage tests pass; shapes/complexity explained. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W217 · S7.08 · Transformer — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build decoder blocks, normalization, residuals and generation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Causal prediction and checkpoint tests pass; compare outputs to reference primitives.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W218 · S7.08 · Transformer — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Build decoder blocks, normalization, residuals and generation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Causal prediction and checkpoint tests pass; compare outputs to reference primitives.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W219 · S7.08 · Transformer — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Causal prediction and checkpoint tests pass; compare outputs to reference primitives. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Causal prediction and checkpoint tests pass; compare outputs to reference primitives. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W220 · S7.08 · Transformer — Review, assess and repair

**Deliverable:** Demonstrate and explain transformer without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Causal prediction and checkpoint tests pass; compare outputs to reference primitives. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W221 · S7.09 · Small LM training — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Train tiny decoder; compare bigram baseline and one ablation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Validation loss and compute logged; no unsupported frontier-quality claim; explain unsuccessful runs.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W222 · S7.09 · Small LM training — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Train tiny decoder; compare bigram baseline and one ablation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Validation loss and compute logged; no unsupported frontier-quality claim; explain unsuccessful runs.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W223 · S7.09 · Small LM training — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Validation loss and compute logged; no unsupported frontier-quality claim; explain unsuccessful runs. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Validation loss and compute logged; no unsupported frontier-quality claim; explain unsuccessful runs. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W224 · S7.09 · Small LM training — Review, assess and repair

**Deliverable:** Demonstrate and explain small lm training without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Validation loss and compute logged; no unsupported frontier-quality claim; explain unsuccessful runs. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W225 · S7.10 · DL release — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Profile memory/throughput; publish architecture, experiment manifests and oral defense. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P7 correctness, derivation, reproducibility and compute-accounting gates pass.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W226 · S7.10 · DL release — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P7: Profile memory/throughput; publish architecture, experiment manifests and oral defense.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P7 correctness, derivation, reproducibility and compute-accounting gates pass.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W227 · S7.10 · DL release — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P7 correctness, derivation, reproducibility and compute-accounting gates pass. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P7 correctness, derivation, reproducibility and compute-accounting gates pass. Distinguish remaining failures from passes.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W228 · S7.10 · DL release — Review, assess and repair

**Deliverable:** Demonstrate and explain dl release without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P7 correctness, derivation, reproducibility and compute-accounting gates pass. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R18,R19,R22,R33. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W229 · S8.01 · Evaluation and baseline — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Define 60-question evidence-grounded search benchmark and lexical baseline. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Version questions/reference evidence; separate development and locked test queries.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W230 · S8.01 · Evaluation and baseline — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Define 60-question evidence-grounded search benchmark and lexical baseline.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Version questions/reference evidence; separate development and locked test queries.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W231 · S8.01 · Evaluation and baseline — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Version questions/reference evidence; separate development and locked test queries. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Version questions/reference evidence; separate development and locked test queries. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W232 · S8.01 · Evaluation and baseline — Review, assess and repair

**Deliverable:** Demonstrate and explain evaluation and baseline without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Version questions/reference evidence; separate development and locked test queries. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W233 · S8.02 · Retrieval — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement chunking, inverted retrieval and brute-force cosine search before vector index. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Recall@5 measured; duplicate and stale-source tests pass; explain index trade-offs.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W234 · S8.02 · Retrieval — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Implement chunking, inverted retrieval and brute-force cosine search before vector index.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Recall@5 measured; duplicate and stale-source tests pass; explain index trade-offs.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W235 · S8.02 · Retrieval — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Recall@5 measured; duplicate and stale-source tests pass; explain index trade-offs. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Recall@5 measured; duplicate and stale-source tests pass; explain index trade-offs. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W236 · S8.02 · Retrieval — Review, assess and repair

**Deliverable:** Demonstrate and explain retrieval without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Recall@5 measured; duplicate and stale-source tests pass; explain index trade-offs. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W237 · S8.03 · Grounded answer service — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add cited answer generation, abstention and structured output validation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Unsupported questions trigger abstention; cited statements trace to retrieved source spans.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W238 · S8.03 · Grounded answer service — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Add cited answer generation, abstention and structured output validation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Unsupported questions trigger abstention; cited statements trace to retrieved source spans.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W239 · S8.03 · Grounded answer service — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Unsupported questions trigger abstention; cited statements trace to retrieved source spans. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Unsupported questions trigger abstention; cited statements trace to retrieved source spans. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W240 · S8.03 · Grounded answer service — Review, assess and repair

**Deliverable:** Demonstrate and explain grounded answer service without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Unsupported questions trigger abstention; cited statements trace to retrieved source spans. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W241 · S8.04 · Reliable tool workflows — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement bounded state machine with allowlisted read-only tools. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Timeout/retry/token limits hold; invalid tool calls and malicious document instructions cannot expand permissions.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W242 · S8.04 · Reliable tool workflows — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Implement bounded state machine with allowlisted read-only tools.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Timeout/retry/token limits hold; invalid tool calls and malicious document instructions cannot expand permissions.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W243 · S8.04 · Reliable tool workflows — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Timeout/retry/token limits hold; invalid tool calls and malicious document instructions cannot expand permissions. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Timeout/retry/token limits hold; invalid tool calls and malicious document instructions cannot expand permissions. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W244 · S8.04 · Reliable tool workflows — Review, assess and repair

**Deliverable:** Demonstrate and explain reliable tool workflows without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Timeout/retry/token limits hold; invalid tool calls and malicious document instructions cannot expand permissions. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W245 · S8.05 · Evaluation hardening — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add prompt-injection, stale-source, malformed-output and cost regression suite. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P8 locked-test report includes human-audited grading and failure taxonomy.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W246 · S8.05 · Evaluation hardening — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Add prompt-injection, stale-source, malformed-output and cost regression suite.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P8 locked-test report includes human-audited grading and failure taxonomy.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W247 · S8.05 · Evaluation hardening — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P8 locked-test report includes human-audited grading and failure taxonomy. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P8 locked-test report includes human-audited grading and failure taxonomy. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W248 · S8.05 · Evaluation hardening — Review, assess and repair

**Deliverable:** Demonstrate and explain evaluation hardening without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P8 locked-test report includes human-audited grading and failure taxonomy. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W249 · S8.06 · Fine-tuning and LoRA — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Compare prompt/retrieval baseline to small LoRA adaptation. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Training/evaluation contamination checked; trainable parameter count derived; report whether adaptation helps.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W250 · S8.06 · Fine-tuning and LoRA — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Compare prompt/retrieval baseline to small LoRA adaptation.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Training/evaluation contamination checked; trainable parameter count derived; report whether adaptation helps.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W251 · S8.06 · Fine-tuning and LoRA — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Training/evaluation contamination checked; trainable parameter count derived; report whether adaptation helps. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Training/evaluation contamination checked; trainable parameter count derived; report whether adaptation helps. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W252 · S8.06 · Fine-tuning and LoRA — Review, assess and repair

**Deliverable:** Demonstrate and explain fine-tuning and lora without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Training/evaluation contamination checked; trainable parameter count derived; report whether adaptation helps. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W253 · S8.07 · Preference and synthetic data — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement toy DPO objective; audit synthetic labels and feedback bias. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Correct gradients; distinguish objective from proven safety; synthetic artifacts never silently enter locked evaluation.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W254 · S8.07 · Preference and synthetic data — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Implement toy DPO objective; audit synthetic labels and feedback bias.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Correct gradients; distinguish objective from proven safety; synthetic artifacts never silently enter locked evaluation.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W255 · S8.07 · Preference and synthetic data — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Correct gradients; distinguish objective from proven safety; synthetic artifacts never silently enter locked evaluation. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Correct gradients; distinguish objective from proven safety; synthetic artifacts never silently enter locked evaluation. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W256 · S8.07 · Preference and synthetic data — Review, assess and repair

**Deliverable:** Demonstrate and explain preference and synthetic data without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Correct gradients; distinguish objective from proven safety; synthetic artifacts never silently enter locked evaluation. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W257 · S8.08 · Production reliability — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add model routing, caching, budget limits, traces, fallback and privacy-aware logging. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Rate limits and simulated provider failures recover; cost per successful task and latency reported.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W258 · S8.08 · Production reliability — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Add model routing, caching, budget limits, traces, fallback and privacy-aware logging.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Rate limits and simulated provider failures recover; cost per successful task and latency reported.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W259 · S8.08 · Production reliability — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Rate limits and simulated provider failures recover; cost per successful task and latency reported. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Rate limits and simulated provider failures recover; cost per successful task and latency reported. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W260 · S8.08 · Production reliability — Review, assess and repair

**Deliverable:** Demonstrate and explain production reliability without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Rate limits and simulated provider failures recover; cost per successful task and latency reported. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W261 · S8.09 · AI application release — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Publish system/data/model cards, limitations, evaluation report and demo. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P8 contract passes; independent reviewer audits ten answers and one failure; no hidden agent privileges.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W262 · S8.09 · AI application release — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P8: Publish system/data/model cards, limitations, evaluation report and demo.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P8 contract passes; independent reviewer audits ten answers and one failure; no hidden agent privileges.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W263 · S8.09 · AI application release — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P8 contract passes; independent reviewer audits ten answers and one failure; no hidden agent privileges. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P8 contract passes; independent reviewer audits ten answers and one failure; no hidden agent privileges. Distinguish remaining failures from passes.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W264 · S8.09 · AI application release — Review, assess and repair

**Deliverable:** Demonstrate and explain ai application release without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P8 contract passes; independent reviewer audits ten answers and one failure; no hidden agent privileges. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R20,R21,R34,R35,R37. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W265 · S9.01 · Serving baseline — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build request/load generator and instrument a small-model inference endpoint. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Record time-to-first-token, inter-token latency, throughput, concurrency and memory under fixed workload.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W266 · S9.01 · Serving baseline — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Build request/load generator and instrument a small-model inference endpoint.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Record time-to-first-token, inter-token latency, throughput, concurrency and memory under fixed workload.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W267 · S9.01 · Serving baseline — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Record time-to-first-token, inter-token latency, throughput, concurrency and memory under fixed workload. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Record time-to-first-token, inter-token latency, throughput, concurrency and memory under fixed workload. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W268 · S9.01 · Serving baseline — Review, assess and repair

**Deliverable:** Demonstrate and explain serving baseline without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Record time-to-first-token, inter-token latency, throughput, concurrency and memory under fixed workload. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W269 · S9.02 · Batching and scheduling — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement bounded queue and simple batch scheduler. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Cancellation/backpressure/fairness tests pass; plot throughput versus tail latency.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W270 · S9.02 · Batching and scheduling — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Implement bounded queue and simple batch scheduler.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Cancellation/backpressure/fairness tests pass; plot throughput versus tail latency.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W271 · S9.02 · Batching and scheduling — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Cancellation/backpressure/fairness tests pass; plot throughput versus tail latency. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Cancellation/backpressure/fairness tests pass; plot throughput versus tail latency. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W272 · S9.02 · Batching and scheduling — Review, assess and repair

**Deliverable:** Demonstrate and explain batching and scheduling without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Cancellation/backpressure/fairness tests pass; plot throughput versus tail latency. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W273 · S9.03 · KV cache — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement small KV cache or simulator and compare cached/uncached decoding. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Logits agree within declared tolerance; memory growth versus sequence length measured.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W274 · S9.03 · KV cache — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Implement small KV cache or simulator and compare cached/uncached decoding.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Logits agree within declared tolerance; memory growth versus sequence length measured.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W275 · S9.03 · KV cache — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Logits agree within declared tolerance; memory growth versus sequence length measured. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Logits agree within declared tolerance; memory growth versus sequence length measured. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W276 · S9.03 · KV cache — Review, assess and repair

**Deliverable:** Demonstrate and explain kv cache without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Logits agree within declared tolerance; memory growth versus sequence length measured. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W277 · S9.04 · Quantization — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Compare supported low-precision configurations to full-precision baseline. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Quality delta and memory/latency reported; regressions block release.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W278 · S9.04 · Quantization — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Compare supported low-precision configurations to full-precision baseline.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Quality delta and memory/latency reported; regressions block release.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W279 · S9.04 · Quantization — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Quality delta and memory/latency reported; regressions block release. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Quality delta and memory/latency reported; regressions block release. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W280 · S9.04 · Quantization — Review, assess and repair

**Deliverable:** Demonstrate and explain quantization without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Quality delta and memory/latency reported; regressions block release. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W281 · S9.05 · Serving engine comparison — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Run compatible engine such as vLLM on fixed supported hardware/model. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Baseline and engine share workload/precision; report warmup and reproducibility details.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W282 · S9.05 · Serving engine comparison — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Run compatible engine such as vLLM on fixed supported hardware/model.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Baseline and engine share workload/precision; report warmup and reproducibility details.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W283 · S9.05 · Serving engine comparison — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Baseline and engine share workload/precision; report warmup and reproducibility details. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Baseline and engine share workload/precision; report warmup and reproducibility details. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W284 · S9.05 · Serving engine comparison — Review, assess and repair

**Deliverable:** Demonstrate and explain serving engine comparison without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Baseline and engine share workload/precision; report warmup and reproducibility details. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W285 · S9.06 · Distributed data — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement partitioned deterministic preprocessing with idempotent outputs. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Worker failure/replay tests pass; single/multiple-worker outputs agree.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W286 · S9.06 · Distributed data — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Implement partitioned deterministic preprocessing with idempotent outputs.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Worker failure/replay tests pass; single/multiple-worker outputs agree.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W287 · S9.06 · Distributed data — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Worker failure/replay tests pass; single/multiple-worker outputs agree. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Worker failure/replay tests pass; single/multiple-worker outputs agree. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W288 · S9.06 · Distributed data — Review, assess and repair

**Deliverable:** Demonstrate and explain distributed data without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Worker failure/replay tests pass; single/multiple-worker outputs agree. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W289 · S9.07 · Distributed training — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement synchronous gradient aggregation reference then PyTorch DDP. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Two CPU processes establish semantics; compare gradients to serial effective batch; explain sampler behavior.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W290 · S9.07 · Distributed training — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Implement synchronous gradient aggregation reference then PyTorch DDP.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Two CPU processes establish semantics; compare gradients to serial effective batch; explain sampler behavior.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W291 · S9.07 · Distributed training — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Two CPU processes establish semantics; compare gradients to serial effective batch; explain sampler behavior. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Two CPU processes establish semantics; compare gradients to serial effective batch; explain sampler behavior. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W292 · S9.07 · Distributed training — Review, assess and repair

**Deliverable:** Demonstrate and explain distributed training without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Two CPU processes establish semantics; compare gradients to serial effective batch; explain sampler behavior. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W293 · S9.08 · Checkpoint and recovery — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add atomic checkpoint metadata, resume and simulated worker failure. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: State restored without silent corruption; distinguish reproducible state from bitwise nondeterminism.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W294 · S9.08 · Checkpoint and recovery — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Add atomic checkpoint metadata, resume and simulated worker failure.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: State restored without silent corruption; distinguish reproducible state from bitwise nondeterminism.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W295 · S9.08 · Checkpoint and recovery — Test and measure

**Deliverable:** Add adversarial tests and measurements for: State restored without silent corruption; distinguish reproducible state from bitwise nondeterminism. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: State restored without silent corruption; distinguish reproducible state from bitwise nondeterminism. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W296 · S9.08 · Checkpoint and recovery — Review, assess and repair

**Deliverable:** Demonstrate and explain checkpoint and recovery without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: State restored without silent corruption; distinguish reproducible state from bitwise nondeterminism. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W297 · S9.09 · Profiling and capacity — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Profile compute, memory and communication; estimate bottleneck and cost per successful request. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Evidence supports optimization decision; scaling efficiency and hardware limits reported.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W298 · S9.09 · Profiling and capacity — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Profile compute, memory and communication; estimate bottleneck and cost per successful request.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Evidence supports optimization decision; scaling efficiency and hardware limits reported.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W299 · S9.09 · Profiling and capacity — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Evidence supports optimization decision; scaling efficiency and hardware limits reported. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Evidence supports optimization decision; scaling efficiency and hardware limits reported. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W300 · S9.09 · Profiling and capacity — Review, assess and repair

**Deliverable:** Demonstrate and explain profiling and capacity without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Evidence supports optimization decision; scaling efficiency and hardware limits reported. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### W301 · S9.10 · Systems release — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Run controlled benchmark, outage drill and design review. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P9 contract passes; present correctness/performance trade-off and production gaps.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W302 · S9.10 · Systems release — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P9: Run controlled benchmark, outage drill and design review.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P9 contract passes; present correctness/performance trade-off and production gaps.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W303 · S9.10 · Systems release — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P9 contract passes; present correctness/performance trade-off and production gaps. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P9 contract passes; present correctness/performance trade-off and production gaps. Distinguish remaining failures from passes.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### W304 · S9.10 · Systems release — Review, assess and repair

**Deliverable:** Demonstrate and explain systems release without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P9 contract passes; present correctness/performance trade-off and production gaps. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R25,R26,R36. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W001 · B1.01 · Consistency model — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Specify queue/store guarantees and failure model. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: State linearizability versus eventual-consistency expectations and forbidden histories.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W002 · B1.01 · Consistency model — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Specify queue/store guarantees and failure model.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: State linearizability versus eventual-consistency expectations and forbidden histories.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W003 · B1.01 · Consistency model — Test and measure

**Deliverable:** Add adversarial tests and measurements for: State linearizability versus eventual-consistency expectations and forbidden histories. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: State linearizability versus eventual-consistency expectations and forbidden histories. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W004 · B1.01 · Consistency model — Review, assess and repair

**Deliverable:** Demonstrate and explain consistency model without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: State linearizability versus eventual-consistency expectations and forbidden histories. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W005 · B1.02 · Replication — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement local replicated log simulator. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Replica replay yields matching state across reorder/delay scenarios.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W006 · B1.02 · Replication — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Implement local replicated log simulator.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Replica replay yields matching state across reorder/delay scenarios.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W007 · B1.02 · Replication — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Replica replay yields matching state across reorder/delay scenarios. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Replica replay yields matching state across reorder/delay scenarios. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W008 · B1.02 · Replication — Review, assess and repair

**Deliverable:** Demonstrate and explain replication without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Replica replay yields matching state across reorder/delay scenarios. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W009 · B1.03 · Consensus fundamentals — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement educational election/log-replication subset. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Partition tests show no conflicting committed entries under stated assumptions; label incomplete Raft scope.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W010 · B1.03 · Consensus fundamentals — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Implement educational election/log-replication subset.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Partition tests show no conflicting committed entries under stated assumptions; label incomplete Raft scope.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W011 · B1.03 · Consensus fundamentals — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Partition tests show no conflicting committed entries under stated assumptions; label incomplete Raft scope. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Partition tests show no conflicting committed entries under stated assumptions; label incomplete Raft scope. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W012 · B1.03 · Consensus fundamentals — Review, assess and repair

**Deliverable:** Demonstrate and explain consensus fundamentals without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Partition tests show no conflicting committed entries under stated assumptions; label incomplete Raft scope. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W013 · B1.04 · Durable queue — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement leases, retries and idempotent commits. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Duplicate delivery tolerated; poison messages quarantined; bounded retry behavior.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W014 · B1.04 · Durable queue — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Implement leases, retries and idempotent commits.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Duplicate delivery tolerated; poison messages quarantined; bounded retry behavior.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W015 · B1.04 · Durable queue — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Duplicate delivery tolerated; poison messages quarantined; bounded retry behavior. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Duplicate delivery tolerated; poison messages quarantined; bounded retry behavior. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W016 · B1.04 · Durable queue — Review, assess and repair

**Deliverable:** Demonstrate and explain durable queue without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Duplicate delivery tolerated; poison messages quarantined; bounded retry behavior. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W017 · B1.05 · Storage internals — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build page/index or LSM-style toy component. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Compare indexed scan costs; explain WAL/recovery and compaction trade-offs.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W018 · B1.05 · Storage internals — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Build page/index or LSM-style toy component.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Compare indexed scan costs; explain WAL/recovery and compaction trade-offs.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W019 · B1.05 · Storage internals — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Compare indexed scan costs; explain WAL/recovery and compaction trade-offs. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Compare indexed scan costs; explain WAL/recovery and compaction trade-offs. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W020 · B1.05 · Storage internals — Review, assess and repair

**Deliverable:** Demonstrate and explain storage internals without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Compare indexed scan costs; explain WAL/recovery and compaction trade-offs. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W021 · B1.06 · Cloud primitives — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Deploy isolated staging with IAM, networking and object storage or local equivalents. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Least-privilege policy and teardown plan tested; distinguish simulation from provider experience.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W022 · B1.06 · Cloud primitives — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Deploy isolated staging with IAM, networking and object storage or local equivalents.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Least-privilege policy and teardown plan tested; distinguish simulation from provider experience.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W023 · B1.06 · Cloud primitives — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Least-privilege policy and teardown plan tested; distinguish simulation from provider experience. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Least-privilege policy and teardown plan tested; distinguish simulation from provider experience. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W024 · B1.06 · Cloud primitives — Review, assess and repair

**Deliverable:** Demonstrate and explain cloud primitives without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Least-privilege policy and teardown plan tested; distinguish simulation from provider experience. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W025 · B1.07 · Kubernetes — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Deploy same service to local cluster with resource limits and probes. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Rolling restart preserves stated service guarantees; rollback tested.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W026 · B1.07 · Kubernetes — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Deploy same service to local cluster with resource limits and probes.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Rolling restart preserves stated service guarantees; rollback tested.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W027 · B1.07 · Kubernetes — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Rolling restart preserves stated service guarantees; rollback tested. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Rolling restart preserves stated service guarantees; rollback tested. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W028 · B1.07 · Kubernetes — Review, assess and repair

**Deliverable:** Demonstrate and explain kubernetes without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Rolling restart preserves stated service guarantees; rollback tested. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W029 · B1.08 · Scheduling — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add fair scheduling, quotas and load shedding. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Overload does not create unbounded queue or starve one tenant.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W030 · B1.08 · Scheduling — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Add fair scheduling, quotas and load shedding.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Overload does not create unbounded queue or starve one tenant.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W031 · B1.08 · Scheduling — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Overload does not create unbounded queue or starve one tenant. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Overload does not create unbounded queue or starve one tenant. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W032 · B1.08 · Scheduling — Review, assess and repair

**Deliverable:** Demonstrate and explain scheduling without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Overload does not create unbounded queue or starve one tenant. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W033 · B1.09 · Observability — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Trace job through API, broker and workers. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Diagnose one unknown injected failure from telemetry.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W034 · B1.09 · Observability — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Trace job through API, broker and workers.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Diagnose one unknown injected failure from telemetry.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W035 · B1.09 · Observability — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Diagnose one unknown injected failure from telemetry. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Diagnose one unknown injected failure from telemetry. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W036 · B1.09 · Observability — Review, assess and repair

**Deliverable:** Demonstrate and explain observability without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Diagnose one unknown injected failure from telemetry. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W037 · B1.10 · Reliability — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Exercise backup, restore, zonal-failure simulation and capacity reduction. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: State RPO/RTO, measure recovery, write blameless postmortem.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W038 · B1.10 · Reliability — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Exercise backup, restore, zonal-failure simulation and capacity reduction.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: State RPO/RTO, measure recovery, write blameless postmortem.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W039 · B1.10 · Reliability — Test and measure

**Deliverable:** Add adversarial tests and measurements for: State RPO/RTO, measure recovery, write blameless postmortem. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: State RPO/RTO, measure recovery, write blameless postmortem. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W040 · B1.10 · Reliability — Review, assess and repair

**Deliverable:** Demonstrate and explain reliability without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: State RPO/RTO, measure recovery, write blameless postmortem. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W041 · B1.11 · Contribution — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Submit reproducible bug report or focused improvement to an existing infrastructure project. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Maintainer-readable test and rationale; acceptance not required for completion.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W042 · B1.11 · Contribution — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Submit reproducible bug report or focused improvement to an existing infrastructure project.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Maintainer-readable test and rationale; acceptance not required for completion.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W043 · B1.11 · Contribution — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Maintainer-readable test and rationale; acceptance not required for completion. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Maintainer-readable test and rationale; acceptance not required for completion. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W044 · B1.11 · Contribution — Review, assess and repair

**Deliverable:** Demonstrate and explain contribution without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Maintainer-readable test and rationale; acceptance not required for completion. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B1-W045 · B1.12 · Infrastructure defense — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Publish workload/chaos results and design review. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P10 gate and independent review pass; distinguish local fault simulation from fleet operations.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W046 · B1.12 · Infrastructure defense — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P10: Publish workload/chaos results and design review.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P10 gate and independent review pass; distinguish local fault simulation from fleet operations.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W047 · B1.12 · Infrastructure defense — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P10 gate and independent review pass; distinguish local fault simulation from fleet operations. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P10 gate and independent review pass; distinguish local fault simulation from fleet operations. Distinguish remaining failures from passes.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B1-W048 · B1.12 · Infrastructure defense — Review, assess and repair

**Deliverable:** Demonstrate and explain infrastructure defense without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P10 gate and independent review pass; distinguish local fault simulation from fleet operations. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R23,R24,R27,R38. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W001 · B2.01 · C++ foundations — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement owned arrays, templates and RAII wrappers. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain lifetimes/moves; sanitizers and warning checks pass.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W002 · B2.01 · C++ foundations — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Implement owned arrays, templates and RAII wrappers.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain lifetimes/moves; sanitizers and warning checks pass.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W003 · B2.01 · C++ foundations — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain lifetimes/moves; sanitizers and warning checks pass. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain lifetimes/moves; sanitizers and warning checks pass. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W004 · B2.01 · C++ foundations — Review, assess and repair

**Deliverable:** Demonstrate and explain c++ foundations without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain lifetimes/moves; sanitizers and warning checks pass. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W005 · B2.02 · C++ interfaces — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build benchmark harness and small numerical library. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Independent oracle and API invariants tested.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W006 · B2.02 · C++ interfaces — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Build benchmark harness and small numerical library.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Independent oracle and API invariants tested.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W007 · B2.02 · C++ interfaces — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Independent oracle and API invariants tested. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Independent oracle and API invariants tested. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W008 · B2.02 · C++ interfaces — Review, assess and repair

**Deliverable:** Demonstrate and explain c++ interfaces without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Independent oracle and API invariants tested. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W009 · B2.03 · CPU performance — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Measure cache locality, vectorization and allocation costs. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Compiler output and profiles support conclusions.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W010 · B2.03 · CPU performance — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Measure cache locality, vectorization and allocation costs.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Compiler output and profiles support conclusions.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W011 · B2.03 · CPU performance — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Compiler output and profiles support conclusions. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Compiler output and profiles support conclusions. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W012 · B2.03 · CPU performance — Review, assess and repair

**Deliverable:** Demonstrate and explain cpu performance without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Compiler output and profiles support conclusions. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W013 · B2.04 · GPU architecture — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Model grids, warps, memory spaces and occupancy. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Explain bandwidth versus compute bound examples.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W014 · B2.04 · GPU architecture — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Model grids, warps, memory spaces and occupancy.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Explain bandwidth versus compute bound examples.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W015 · B2.04 · GPU architecture — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Explain bandwidth versus compute bound examples. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Explain bandwidth versus compute bound examples. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W016 · B2.04 · GPU architecture — Review, assess and repair

**Deliverable:** Demonstrate and explain gpu architecture without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Explain bandwidth versus compute bound examples. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W017 · B2.05 · CUDA vector operations — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement vector add and reductions. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Boundary/nonmultiple-size tests pass; compare CPU oracle.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W018 · B2.05 · CUDA vector operations — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Implement vector add and reductions.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Boundary/nonmultiple-size tests pass; compare CPU oracle.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W019 · B2.05 · CUDA vector operations — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Boundary/nonmultiple-size tests pass; compare CPU oracle. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Boundary/nonmultiple-size tests pass; compare CPU oracle. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W020 · B2.05 · CUDA vector operations — Review, assess and repair

**Deliverable:** Demonstrate and explain cuda vector operations without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Boundary/nonmultiple-size tests pass; compare CPU oracle. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W021 · B2.06 · CUDA memory — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Compare coalesced and strided access patterns. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Bandwidth measured with warmup/synchronization and identical data.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W022 · B2.06 · CUDA memory — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Compare coalesced and strided access patterns.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Bandwidth measured with warmup/synchronization and identical data.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W023 · B2.06 · CUDA memory — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Bandwidth measured with warmup/synchronization and identical data. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Bandwidth measured with warmup/synchronization and identical data. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W024 · B2.06 · CUDA memory — Review, assess and repair

**Deliverable:** Demonstrate and explain cuda memory without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Bandwidth measured with warmup/synchronization and identical data. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W025 · B2.07 · CUDA matrix multiply — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement naive then tiled matrix multiply. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Tolerance-based correctness across shape sweep; explain shared-memory design.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W026 · B2.07 · CUDA matrix multiply — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Implement naive then tiled matrix multiply.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Tolerance-based correctness across shape sweep; explain shared-memory design.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W027 · B2.07 · CUDA matrix multiply — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Tolerance-based correctness across shape sweep; explain shared-memory design. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Tolerance-based correctness across shape sweep; explain shared-memory design. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W028 · B2.07 · CUDA matrix multiply — Review, assess and repair

**Deliverable:** Demonstrate and explain cuda matrix multiply without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Tolerance-based correctness across shape sweep; explain shared-memory design. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W029 · B2.08 · Numerical precision — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Evaluate FP32 and supported lower precision. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Worst-case error and downstream quality recorded.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W030 · B2.08 · Numerical precision — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Evaluate FP32 and supported lower precision.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Worst-case error and downstream quality recorded.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W031 · B2.08 · Numerical precision — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Worst-case error and downstream quality recorded. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Worst-case error and downstream quality recorded. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W032 · B2.08 · Numerical precision — Review, assess and repair

**Deliverable:** Demonstrate and explain numerical precision without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Worst-case error and downstream quality recorded. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W033 · B2.09 · Triton basics — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement vector add and fused softmax independently. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Match references across awkward shapes; explain masking.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W034 · B2.09 · Triton basics — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Implement vector add and fused softmax independently.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Match references across awkward shapes; explain masking.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W035 · B2.09 · Triton basics — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Match references across awkward shapes; explain masking. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Match references across awkward shapes; explain masking. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W036 · B2.09 · Triton basics — Review, assess and repair

**Deliverable:** Demonstrate and explain triton basics without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Match references across awkward shapes; explain masking. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W037 · B2.10 · Kernel fusion — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Fuse normalization or bias/activation operations. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Demonstrate removed memory traffic; report cases slower than library.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W038 · B2.10 · Kernel fusion — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Fuse normalization or bias/activation operations.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Demonstrate removed memory traffic; report cases slower than library.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W039 · B2.10 · Kernel fusion — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Demonstrate removed memory traffic; report cases slower than library. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Demonstrate removed memory traffic; report cases slower than library. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W040 · B2.10 · Kernel fusion — Review, assess and repair

**Deliverable:** Demonstrate and explain kernel fusion without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Demonstrate removed memory traffic; report cases slower than library. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W041 · B2.11 · Triton matmul — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement and tune tiled multiplication. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Publish shape-dependent performance versus optimized library.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W042 · B2.11 · Triton matmul — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Implement and tune tiled multiplication.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Publish shape-dependent performance versus optimized library.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W043 · B2.11 · Triton matmul — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Publish shape-dependent performance versus optimized library. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Publish shape-dependent performance versus optimized library. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W044 · B2.11 · Triton matmul — Review, assess and repair

**Deliverable:** Demonstrate and explain triton matmul without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Publish shape-dependent performance versus optimized library. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W045 · B2.12 · Profiling — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Use supported GPU profiler to identify stalls and occupancy limits. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: One bottleneck prediction verified or falsified by trace.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W046 · B2.12 · Profiling — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Use supported GPU profiler to identify stalls and occupancy limits.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: One bottleneck prediction verified or falsified by trace.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W047 · B2.12 · Profiling — Test and measure

**Deliverable:** Add adversarial tests and measurements for: One bottleneck prediction verified or falsified by trace. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: One bottleneck prediction verified or falsified by trace. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W048 · B2.12 · Profiling — Review, assess and repair

**Deliverable:** Demonstrate and explain profiling without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: One bottleneck prediction verified or falsified by trace. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W049 · B2.13 · Autotuning — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Select kernel configurations without test-workload leakage. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Separate tuning/evaluation shape sets; include tuning overhead.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W050 · B2.13 · Autotuning — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Select kernel configurations without test-workload leakage.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Separate tuning/evaluation shape sets; include tuning overhead.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W051 · B2.13 · Autotuning — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Separate tuning/evaluation shape sets; include tuning overhead. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Separate tuning/evaluation shape sets; include tuning overhead. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W052 · B2.13 · Autotuning — Review, assess and repair

**Deliverable:** Demonstrate and explain autotuning without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Separate tuning/evaluation shape sets; include tuning overhead. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W053 · B2.14 · Integration — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Replace one small-model operation with custom kernel. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Model outputs and quality stay within predeclared tolerance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W054 · B2.14 · Integration — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Replace one small-model operation with custom kernel.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Model outputs and quality stay within predeclared tolerance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W055 · B2.14 · Integration — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Model outputs and quality stay within predeclared tolerance. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Model outputs and quality stay within predeclared tolerance. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W056 · B2.14 · Integration — Review, assess and repair

**Deliverable:** Demonstrate and explain integration without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Model outputs and quality stay within predeclared tolerance. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W057 · B2.15 · Contribution — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Prepare targeted performance fix or benchmark for existing project. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Minimal reproduction and correctness oracle accompany proposed change.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W058 · B2.15 · Contribution — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Prepare targeted performance fix or benchmark for existing project.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Minimal reproduction and correctness oracle accompany proposed change.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W059 · B2.15 · Contribution — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Minimal reproduction and correctness oracle accompany proposed change. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Minimal reproduction and correctness oracle accompany proposed change. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W060 · B2.15 · Contribution — Review, assess and repair

**Deliverable:** Demonstrate and explain contribution without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Minimal reproduction and correctness oracle accompany proposed change. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B2-W061 · B2.16 · GPU defense — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Publish kernel suite and performance report. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P11 gate passes; no claim of general speedup from one favorable shape.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W062 · B2.16 · GPU defense — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P11: Publish kernel suite and performance report.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P11 gate passes; no claim of general speedup from one favorable shape.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W063 · B2.16 · GPU defense — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P11 gate passes; no claim of general speedup from one favorable shape. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P11 gate passes; no claim of general speedup from one favorable shape. Distinguish remaining failures from passes.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B2-W064 · B2.16 · GPU defense — Review, assess and repair

**Deliverable:** Demonstrate and explain gpu defense without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P11 gate passes; no claim of general speedup from one favorable shape. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R28,R29,R30. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W001 · B3.01 · Paper selection — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Choose small LoRA or optimization result with accessible code/data. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Claim, dependencies and compute feasibility approved in written protocol.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W002 · B3.01 · Paper selection — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Choose small LoRA or optimization result with accessible code/data.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Claim, dependencies and compute feasibility approved in written protocol.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W003 · B3.01 · Paper selection — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Claim, dependencies and compute feasibility approved in written protocol. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Claim, dependencies and compute feasibility approved in written protocol. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W004 · B3.01 · Paper selection — Review, assess and repair

**Deliverable:** Demonstrate and explain paper selection without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Claim, dependencies and compute feasibility approved in written protocol. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W005 · B3.02 · Literature map — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Read target plus two closely related papers. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Distinguish established evidence, author claims and open questions.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W006 · B3.02 · Literature map — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Read target plus two closely related papers.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Distinguish established evidence, author claims and open questions.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W007 · B3.02 · Literature map — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Distinguish established evidence, author claims and open questions. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Distinguish established evidence, author claims and open questions. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W008 · B3.02 · Literature map — Review, assess and repair

**Deliverable:** Demonstrate and explain literature map without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Distinguish established evidence, author claims and open questions. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W009 · B3.03 · Protocol — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Predeclare metrics, split, seeds, compute cap and deviation rules. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Replication target and failure criteria unambiguous.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W010 · B3.03 · Protocol — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Predeclare metrics, split, seeds, compute cap and deviation rules.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Replication target and failure criteria unambiguous.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W011 · B3.03 · Protocol — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Replication target and failure criteria unambiguous. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Replication target and failure criteria unambiguous. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W012 · B3.03 · Protocol — Review, assess and repair

**Deliverable:** Demonstrate and explain protocol without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Replication target and failure criteria unambiguous. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W013 · B3.04 · Baseline implementation — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement relevant baseline and parity tests. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Baseline behavior agrees with published or official reference within scoped expectations.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W014 · B3.04 · Baseline implementation — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Implement relevant baseline and parity tests.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Baseline behavior agrees with published or official reference within scoped expectations.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W015 · B3.04 · Baseline implementation — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Baseline behavior agrees with published or official reference within scoped expectations. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Baseline behavior agrees with published or official reference within scoped expectations. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W016 · B3.04 · Baseline implementation — Review, assess and repair

**Deliverable:** Demonstrate and explain baseline implementation without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Baseline behavior agrees with published or official reference within scoped expectations. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W017 · B3.05 · Method implementation — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement target modification from equations. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Equation-to-code trace and independent correctness checks pass.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W018 · B3.05 · Method implementation — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Implement target modification from equations.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Equation-to-code trace and independent correctness checks pass.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W019 · B3.05 · Method implementation — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Equation-to-code trace and independent correctness checks pass. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Equation-to-code trace and independent correctness checks pass. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W020 · B3.05 · Method implementation — Review, assess and repair

**Deliverable:** Demonstrate and explain method implementation without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Equation-to-code trace and independent correctness checks pass. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W021 · B3.06 · Pilot — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Run miniature end-to-end experiment and profile cost. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Projected full experiment fits cap or rescope before launch.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W022 · B3.06 · Pilot — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Run miniature end-to-end experiment and profile cost.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Projected full experiment fits cap or rescope before launch.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W023 · B3.06 · Pilot — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Projected full experiment fits cap or rescope before launch. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Projected full experiment fits cap or rescope before launch. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W024 · B3.06 · Pilot — Review, assess and repair

**Deliverable:** Demonstrate and explain pilot without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Projected full experiment fits cap or rescope before launch. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W025 · B3.07 · Replication — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Execute fixed runs and preserve raw logs. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Failed runs retained; seed/config/code/data identifiers complete.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W026 · B3.07 · Replication — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Execute fixed runs and preserve raw logs.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Failed runs retained; seed/config/code/data identifiers complete.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W027 · B3.07 · Replication — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Failed runs retained; seed/config/code/data identifiers complete. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Failed runs retained; seed/config/code/data identifiers complete. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W028 · B3.07 · Replication — Review, assess and repair

**Deliverable:** Demonstrate and explain replication without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Failed runs retained; seed/config/code/data identifiers complete. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W029 · B3.08 · Statistical analysis — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Estimate uncertainty with appropriate unit of resampling. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Do not treat dependent examples/seeds as independent evidence.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W030 · B3.08 · Statistical analysis — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Estimate uncertainty with appropriate unit of resampling.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Do not treat dependent examples/seeds as independent evidence.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W031 · B3.08 · Statistical analysis — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Do not treat dependent examples/seeds as independent evidence. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Do not treat dependent examples/seeds as independent evidence. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W032 · B3.08 · Statistical analysis — Review, assess and repair

**Deliverable:** Demonstrate and explain statistical analysis without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Do not treat dependent examples/seeds as independent evidence. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W033 · B3.09 · Ablations — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Run two focused ablations within budget. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Only intended variable changes; negative results retained.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W034 · B3.09 · Ablations — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Run two focused ablations within budget.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Only intended variable changes; negative results retained.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W035 · B3.09 · Ablations — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Only intended variable changes; negative results retained. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Only intended variable changes; negative results retained. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W036 · B3.09 · Ablations — Review, assess and repair

**Deliverable:** Demonstrate and explain ablations without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Only intended variable changes; negative results retained. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W037 · B3.10 · Extension — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Test one justified hypothesis at equal budget. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Label exploratory analysis and avoid post-hoc success criteria.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W038 · B3.10 · Extension — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Test one justified hypothesis at equal budget.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Label exploratory analysis and avoid post-hoc success criteria.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W039 · B3.10 · Extension — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Label exploratory analysis and avoid post-hoc success criteria. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Label exploratory analysis and avoid post-hoc success criteria. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W040 · B3.10 · Extension — Review, assess and repair

**Deliverable:** Demonstrate and explain extension without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Label exploratory analysis and avoid post-hoc success criteria. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W041 · B3.11 · External feedback — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Request technical critique and prepare contribution. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Reviewer can reproduce a subset; deviations documented.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W042 · B3.11 · External feedback — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Request technical critique and prepare contribution.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Reviewer can reproduce a subset; deviations documented.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W043 · B3.11 · External feedback — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Reviewer can reproduce a subset; deviations documented. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Reviewer can reproduce a subset; deviations documented. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W044 · B3.11 · External feedback — Review, assess and repair

**Deliverable:** Demonstrate and explain external feedback without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Reviewer can reproduce a subset; deviations documented. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B3-W045 · B3.12 · Research defense — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Release reproducibility package and paper-style report. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P12 gate passes; describe scaled reproduction limits and unsupported generalization.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W046 · B3.12 · Research defense — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P12: Release reproducibility package and paper-style report.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P12 gate passes; describe scaled reproduction limits and unsupported generalization.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W047 · B3.12 · Research defense — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P12 gate passes; describe scaled reproduction limits and unsupported generalization. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P12 gate passes; describe scaled reproduction limits and unsupported generalization. Distinguish remaining failures from passes.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 1h, math 0.5h, exercise 0.5h, project 1.5h, debug 0.75h, review 0.5h, assessment 0.25h).

### B3-W048 · B3.12 · Research defense — Review, assess and repair

**Deliverable:** Demonstrate and explain research defense without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P12 gate passes; describe scaled reproduction limits and unsupported generalization. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R22,R33,R34,R35. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W001 · B4.01 · Language semantics — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Specify typed expression language and interpreter. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Reference semantics handle shape/type errors explicitly.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W002 · B4.01 · Language semantics — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Specify typed expression language and interpreter.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Reference semantics handle shape/type errors explicitly.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W003 · B4.01 · Language semantics — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Reference semantics handle shape/type errors explicitly. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Reference semantics handle shape/type errors explicitly. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W004 · B4.01 · Language semantics — Review, assess and repair

**Deliverable:** Demonstrate and explain language semantics without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Reference semantics handle shape/type errors explicitly. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W005 · B4.02 · Lexer and parser — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Build lexer, parser and AST. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Malformed/ambiguous expressions covered by tests.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W006 · B4.02 · Lexer and parser — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Build lexer, parser and AST.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Malformed/ambiguous expressions covered by tests.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W007 · B4.02 · Lexer and parser — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Malformed/ambiguous expressions covered by tests. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Malformed/ambiguous expressions covered by tests. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W008 · B4.02 · Lexer and parser — Review, assess and repair

**Deliverable:** Demonstrate and explain lexer and parser without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Malformed/ambiguous expressions covered by tests. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W009 · B4.03 · Type checking — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement scalar/tensor type and shape checks. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Invalid programs fail before execution.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W010 · B4.03 · Type checking — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Implement scalar/tensor type and shape checks.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Invalid programs fail before execution.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W011 · B4.03 · Type checking — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Invalid programs fail before execution. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Invalid programs fail before execution. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W012 · B4.03 · Type checking — Review, assess and repair

**Deliverable:** Demonstrate and explain type checking without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Invalid programs fail before execution. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W013 · B4.04 · IR generation — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Lower expressions to LLVM IR. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Compiled output matches interpreter on generated cases.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W014 · B4.04 · IR generation — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Lower expressions to LLVM IR.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Compiled output matches interpreter on generated cases.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W015 · B4.04 · IR generation — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Compiled output matches interpreter on generated cases. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Compiled output matches interpreter on generated cases. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W016 · B4.04 · IR generation — Review, assess and repair

**Deliverable:** Demonstrate and explain ir generation without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Compiled output matches interpreter on generated cases. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W017 · B4.05 · Control flow — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Add branches and loops. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Control-flow graphs and execution agree on boundary cases.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W018 · B4.05 · Control flow — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Add branches and loops.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Control-flow graphs and execution agree on boundary cases.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W019 · B4.05 · Control flow — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Control-flow graphs and execution agree on boundary cases. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Control-flow graphs and execution agree on boundary cases. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W020 · B4.05 · Control flow — Review, assess and repair

**Deliverable:** Demonstrate and explain control flow without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Control-flow graphs and execution agree on boundary cases. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W021 · B4.06 · Optimization basics — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement constant folding and dead-code elimination. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Differential tests preserve semantics.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W022 · B4.06 · Optimization basics — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Implement constant folding and dead-code elimination.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Differential tests preserve semantics.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W023 · B4.06 · Optimization basics — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Differential tests preserve semantics. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Differential tests preserve semantics. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W024 · B4.06 · Optimization basics — Review, assess and repair

**Deliverable:** Demonstrate and explain optimization basics without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Differential tests preserve semantics. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W025 · B4.07 · Numerical legality — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Explore reassociation and floating-point constraints. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Document where mathematically equivalent rewrites alter numeric results.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W026 · B4.07 · Numerical legality — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Explore reassociation and floating-point constraints.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Document where mathematically equivalent rewrites alter numeric results.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W027 · B4.07 · Numerical legality — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Document where mathematically equivalent rewrites alter numeric results. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Document where mathematically equivalent rewrites alter numeric results. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W028 · B4.07 · Numerical legality — Review, assess and repair

**Deliverable:** Demonstrate and explain numerical legality without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Document where mathematically equivalent rewrites alter numeric results. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W029 · B4.08 · JIT integration — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Expose compiled functions to Python benchmark. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Compile time separated from execution time.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W030 · B4.08 · JIT integration — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Expose compiled functions to Python benchmark.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Compile time separated from execution time.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W031 · B4.08 · JIT integration — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Compile time separated from execution time. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Compile time separated from execution time. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W032 · B4.08 · JIT integration — Review, assess and repair

**Deliverable:** Demonstrate and explain jit integration without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Compile time separated from execution time. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W033 · B4.09 · Tensor lowering — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Implement restricted tensor-operation lowering. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Shape/stride correctness verified; unsupported cases rejected.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W034 · B4.09 · Tensor lowering — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Implement restricted tensor-operation lowering.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Shape/stride correctness verified; unsupported cases rejected.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W035 · B4.09 · Tensor lowering — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Shape/stride correctness verified; unsupported cases rejected. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Shape/stride correctness verified; unsupported cases rejected. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W036 · B4.09 · Tensor lowering — Review, assess and repair

**Deliverable:** Demonstrate and explain tensor lowering without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Shape/stride correctness verified; unsupported cases rejected. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W037 · B4.10 · Performance study — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Compare generated kernels to interpreter and library. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Report compile overhead and break-even workload.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W038 · B4.10 · Performance study — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Compare generated kernels to interpreter and library.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Report compile overhead and break-even workload.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W039 · B4.10 · Performance study — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Report compile overhead and break-even workload. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Report compile overhead and break-even workload. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W040 · B4.10 · Performance study — Review, assess and repair

**Deliverable:** Demonstrate and explain performance study without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Report compile overhead and break-even workload. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W041 · B4.11 · Contribution — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Prepare focused compiler test/bugfix for external project. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: Minimal IR reproducer and explanation included.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W042 · B4.11 · Contribution — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Prepare focused compiler test/bugfix for external project.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: Minimal IR reproducer and explanation included.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W043 · B4.11 · Contribution — Test and measure

**Deliverable:** Add adversarial tests and measurements for: Minimal IR reproducer and explanation included. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: Minimal IR reproducer and explanation included. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W044 · B4.11 · Contribution — Review, assess and repair

**Deliverable:** Demonstrate and explain contribution without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: Minimal IR reproducer and explanation included. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).

### B4-W045 · B4.12 · Compiler defense — Explain and implement

**Deliverable:** Write a one-page explanation and minimal reference implementation for: Release compiler demo and correctness/performance report. Define input/output examples and expected behavior.

**Pass:** Reference implementation runs on a tiny hand-checkable case; explanation names an invariant and limitation. Target: P13 gate passes; explain limitations versus production compiler stack.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W046 · B4.12 · Compiler defense — Apply and integrate

**Deliverable:** Complete the working implementation and integrate it into P13: Release compiler demo and correctness/performance report.

**Pass:** A reproducible demo exercises the module's intended behavior. Target: P13 gate passes; explain limitations versus production compiler stack.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W047 · B4.12 · Compiler defense — Test and measure

**Deliverable:** Add adversarial tests and measurements for: P13 gate passes; explain limitations versus production compiler stack. Save commands, data/config versions and results.

**Pass:** Evidence covers module criteria: P13 gate passes; explain limitations versus production compiler stack. Distinguish remaining failures from passes.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.5h, math 0.25h, exercise 0.5h, project 2.25h, debug 0.75h, review 0.5h, assessment 0.25h).

### B4-W048 · B4.12 · Compiler defense — Review, assess and repair

**Deliverable:** Demonstrate and explain compiler defense without AI. Revisit one older skill. Repair failed acceptance checks; record evidence and next review date.

**Pass:** Module criteria pass: P13 gate passes; explain limitations versus production compiler stack. Score at least 80/100, each dimension at least 60%; mandatory integrity gates pass. Otherwise create remediation and do not advance.

**Resources:** R31,R28. **Time:** 5 hours (theory 0.25h, math 0.25h, exercise 0.25h, project 0.75h, debug 1h, review 0.5h, assessment 2h).
