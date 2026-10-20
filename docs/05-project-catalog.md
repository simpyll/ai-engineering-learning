# 5. Project catalog and implementation ladder

Every project follows **explain → implement a small core → apply → engineer → demonstrate**. From-scratch parts are pedagogical: production cryptography, authentication, database engines and numerical libraries should use maintained components. Implement the small reference first, then compare it with the library. Never describe a deliberately simplified implementation as production infrastructure.

Project hours below are **included within stage hours**, not added to them. They cover implementation, integration, testing and project documentation. Remaining stage time covers theory, exercises, review and assessments. The stage/module definitions and criteria in `curriculum.json` control advancement; these contracts add project-wide release requirements.

## Shared release contract

Every P1–P13 release includes a problem statement, reproducible install/run commands, source/data licenses, input/output contract, tests, CI, architecture or data-flow diagram, at least one ADR, raw benchmark/experiment results where relevant, known limitations and a five-minute technical demonstration. Secrets and private data are excluded. Provide a clean-clone smoke test and a short account of AI assistance. For math/research notebooks, also provide a script that reproduces the central result without manually ordered cells.

Definition of done: all listed acceptance checks pass, the stage rubric passes, one unseen change/debugging task is explained without AI, and a reviewer or a documented independent self-review verifies the release. External review is preferred; self-review must not be labeled independent validation. Later capstones require an external technical review attempt, and any lack of independent confirmation must be disclosed.

Performance claims always identify hardware, runtime/library versions, dataset, input distribution, batch/concurrency, warmup, repetitions and quality constraints. A negative optimization result is valid evidence if correctly measured. Never optimize away correctness.

## P0 — Learning control repository

**Stage/budget:** S0, 6 project hours within 10 total. **Skills:** Git, reproducibility, honest self-assessment.

**Requirements:** create environment instructions, diagnostic records, time log and one runnable Python script. **Acceptance:** another terminal/environment can run it; branch/merge/conflict recovery explained; diagnostics identify gaps rather than assign a flattering label. **Performance:** not relevant. **Documentation/presentation:** README links the active week and evidence ledger. **Done:** the S0 diagnostic decision is recorded. No public GitHub posting is necessary until sensitive notes are removed.

## P1 — Program-data command-line collector

**Stage/budget:** S1, 60 project hours within 110. **Skills:** Python, parsing, types, functional decomposition, OOP trade-offs, errors, tests, packaging, Git and debugging.

**Functional requirements:** load local CSV/JSON snapshots; normalize school/program names; preserve missing tuition distinctly from zero; filter, deduplicate, merge snapshots and export normalized data with provenance. **Technical:** separate pure logic from I/O, typed interfaces, explicit grammar, specific exceptions, deterministic output, bounded memory via streaming where appropriate.

**Acceptance:** valid/malformed/empty/duplicate fixtures; rerun equality; quoted text and Unicode handled; CLI errors nonzero; clean install runs. Tests must catch three seeded bugs. **Performance:** benchmark 10,000 synthetic records and peak memory; target under five seconds on the recorded development machine, then diagnose rather than hide misses. This is a project target, not a hardware-independent requirement. **Documentation:** schema, parser grammar and change-conflict policy. **GitHub:** example input/output, CI badge, tagged v0.1 release. **Done:** shared contract plus S1 exit, not merely week 12.

## P2 — Search and algorithm laboratory

**Stage/budget:** S2, 70/140 hours. **Skills:** complexity, discrete proofs, hashes/trees/heaps, graphs, dynamic programming and ranking.

**Functional:** index P1 records and return ranked keyword results; separate educational algorithms from service search implementation. **Technical:** own inverted index; small from-scratch hash/heap/graph/DP exercises with invariant notes.

**Acceptance:** golden queries, empty/no-result cases, reference comparisons, property tests, BFS/Dijkstra hand examples, cycle detection, edit-distance fixtures. **Performance:** compare indexed search to scan at 1,000/10,000/100,000 synthetic documents; report index build cost and memory. **Documentation:** correctness argument and complexity table. **GitHub:** algorithm lab appendix plus practical search demo, not twenty disconnected repositories. **Done:** two unseen algorithm tasks and design defense pass.

## P3 — RNtoNP directory backend, or equivalent public-data directory

**Stage/budget:** S3, 110/180 hours. **Skills:** SQL, migrations, REST, security, ingestion, caching, deployment, observability and recovery.

**Functional:** browse/filter programs, authenticated editor updates, source timestamps, historical snapshots and refresh jobs. Begin with permitted small public datasets or synthetic records; no clinical records are needed. **Technical:** PostgreSQL, typed Python API, maintained authentication, parameterized SQL, transactions, idempotent ingestion, container deployment, logs and health checks. Add source permission/terms review before live collection; enforce conservative request rates and respect access restrictions.

**Acceptance:** CRUD/validation/role tests; import twice without duplicates; migration and restore into empty DB; denied cross-user modification; fresh deployment; failed deployment rollback. **Performance:** on a documented machine, 10,000 records and 20 concurrent read clients for five minutes; proposed target p95 under 300ms and under 1% unexpected errors. Predeclare scope (local versus network); explain misses and measured bottlenecks. **Documentation:** ER diagram, API spec, threat model, backup/runbook and SLO. **GitHub:** deployed staging demo or reproducible local video, benchmark report and reviewed change. **Done:** first employment checkpoint only when able to explain and modify unfamiliar code as well as this service.

## P4 — Durable concurrent ingestion worker

**Stage/budget:** S4, 90/160 hours. **Skills:** C/memory, CPU/cache, processes/threads, sockets, interpreter basics and crash recovery.

**Functional:** receive framed jobs, process bounded concurrent tasks, append results durably and resume interrupted work. **Technical:** local socket service, bounded queue, explicit timeouts, append log with record boundaries/checksums; isolated C memory lab and expression evaluator as supporting exercises.

**Acceptance:** partial reads/disconnects, queue saturation, worker kill/restart, truncated log, deterministic committed output; sanitizer detects and then verifies repaired memory errors. **Performance:** compare serial/thread/process/async approaches on simulated CPU and I/O workloads; report throughput, memory and saturation. **Documentation:** ownership model, queue invariants and delivery semantics. **GitHub:** failure injection scripts and postmortem. **Done:** describe why repeated delivery is possible and how duplicate effects are prevented within the stated design.

## P5 — Numerical foundations notebook and library

**Stage/budget:** S5, 85/160 hours. **Skills:** all mathematical families in the dependency map.

**Functional:** linear solves, projection/PCA, finite-difference gradients, probability simulations, confidence intervals, stable softmax and gradient descent. **Technical:** small hand-derived reference code plus NumPy/library comparison; explicit dtype, random seed and error tolerances.

**Acceptance:** small cases solved by hand, residual/error tables, gradient checks, simulation uncertainty, ill-conditioned example, stable extreme-logit example. **Performance:** compare vectorized and loop implementations without requiring speedup on tiny inputs. **Documentation:** derivations, dimensions, assumptions and where each numerical method fails. **GitHub:** readable notebooks plus executable reproductions. **Done:** per-domain math gate passes; plots alone are insufficient.

## P6 — Evaluated model and prediction service

**Stage/budget:** S6, 110/180 hours. **Skills:** data quality, regression/classification, trees/ensembles, clustering, feature engineering, evaluation, calibration, deployment and drift.

**Functional:** choose a genuine prediction task with adequate licensed labels. Tuition estimation is optional and only justified if cohort definitions, missingness and sample size support it; otherwise use a suitable open tabular dataset. **Technical:** versioned dataset; group/time split where needed; dummy baseline; from-scratch linear/logistic implementations; library pipeline; packaged preprocessing and model.

**Acceptance:** no test leakage, train/serve parity, metric justified by decision costs, interval/subgroup analysis, rerun from manifest, rollback to baseline. **Performance:** log training time and service p95 on specified workload; small-model target p95 under 100ms locally excluding network, with justified hardware adjustment. Predictive improvement is desirable, not mandatory: a rigorously supported finding that ML does not help is acceptable. **Documentation:** data/model cards, test-set lock, experiment table and failure analysis. **GitHub:** report and inference demo. **Done:** explain validation design and one negative experiment without notes.

## P7 — Autograd, transformer and small-language-model laboratory

**Stage/budget:** S7, 125/200 hours. **Skills:** backprop, CNN/RNN survey, attention, tokenization, training, embeddings and profiling.

**Functional:** implement scalar autograd, two-layer NumPy network, convolution/recurrent reference exercises, BPE tokenizer and decoder-only transformer; train on licensed text. **Technical:** PyTorch tensor primitives permitted for transformer, no prebuilt transformer block in the from-scratch path; mask, normalization, checkpoint and generation implementations inspected.

**Acceptance:** gradient checks with declared tolerances; overfit tiny batch; tokenizer round trip; no future-token influence on earlier logits; checkpoint recovery; held-out document split; bigram baseline and one ablation. **Performance:** measure tokens/s, memory, validation loss and total compute; select a CPU-small model initially and scale only after profiling. **Documentation:** equations, architecture dimensions, parameter count, loss curves, data licenses and training manifest. **GitHub:** reproduce a short run; downloadable weights only if license allows. **Done:** explain why the project demonstrates language-model engineering but does not replicate frontier pretraining.

## P8 — Evidence-grounded program-search assistant

**Stage/budget:** S8, 110/180 hours. **Skills:** retrieval/vector search, prompting, structured outputs, constrained agents, evals, LoRA, preference basics and reliability.

**Functional:** answer directory questions with citations; abstain when evidence is absent; use bounded read-only tools. This is directory assistance, not clinical guidance. **Technical:** lexical and brute-force dense baselines before vector indexing; source-level provenance; output schema; permission checks outside model text; per-request cost/time caps; LoRA comparison and toy DPO exercise in separate experiment module.

**Acceptance:** 60 manually authored questions, with 40 development and 20 locked test questions, including unsupported and adversarial cases; no training on locked questions. Proposed release targets: at least 90% correct supporting citations on answerable test cases, at least 90% abstention on unsupported cases, and zero unauthorized actions in adversarial tests. Publish denominators and uncertainty: this small suite cannot establish general safety. Failure means keep as prototype or explicitly narrow scope; do not weaken thresholds after viewing test results. **Performance:** log p50/p95 latency, cost per successful task, retrieval recall@5 and failure rate; external-model latency is measured, not guaranteed. **Documentation:** eval rubric, audited scores, prompt-injection threat model, data/model cards, adaptation findings. **GitHub:** full evaluation runner and inspectable traces with sensitive content removed. **Done:** quality, budget and permissions gates hold under simulated failures.

## P9 — Small-model serving and distributed training workbench

**Stage/budget:** S9, 125/200 hours. **Skills:** inference, batching, KV caching, quantization, distributed data/training, collectives, profiling and recovery.

**Functional:** serve model requests under bounded load; benchmark a reference against a supported optimized engine; run deterministic partitioned preprocessing and a two-process training job. **Technical:** fixed model/tokenizer/precision where comparison requires parity; CPU process-based gradient reference; DDP; atomic checkpoint metadata; model-parallel memory/communication worksheet.

**Acceptance:** serial versus distributed gradients for equal effective batches; worker/replay tests; cached/uncached output checks; quantified quality regression thresholds before performance experiments; cancellation/backpressure and checkpoint recovery. **Performance:** throughput, time-to-first-token, inter-token latency, p95, memory, utilization and cost; warmup plus at least five timed repetitions for short benchmarks. Report distributions and any non-comparable configurations. **Documentation:** workload generator, hardware/software manifest, bottleneck analysis and precision/quality trade-off. **GitHub:** benchmark reproduction plus outage demo. **Done:** defend optimization based on measurements; two local processes do not count as multi-node fleet experience.

## P10 — Failure-tested distributed job infrastructure

**Stage/budget:** B1, 150/240 hours. **Skills:** consensus concepts, durable queues/storage, orchestration, cloud IAM, SRE, resource scheduling and collaboration.

**Functional:** queue and worker system with replay, leases, quotas and failure recovery. **Technical:** educational replication/consensus simulator clearly separated from maintained production components; local Kubernetes then optional small cloud staging; database internals exercise.

**Acceptance:** partition, crash, duplicate delivery, delayed messages, poison jobs, storage recovery, authorization and overload tests; document RPO/RTO. **Performance:** load sweep and recovery time at fixed resources; do not claim linear scaling without evidence. **Documentation:** failure model, consistency contract, incident report and cloud teardown. **GitHub:** original design plus substantive external issue/patch. **Done:** outside review attempted and feedback addressed; real fleet operation remains a separate experience requirement.

## P11 — Correctness-first GPU kernel suite

**Stage/budget:** B2, 200/320 hours. **Skills:** C++/RAII, CUDA, Triton, GPU architecture, numerics, fusion, roofline reasoning and profiling.

**Functional:** vector/reduction, tiled matrix multiply, fused softmax or normalization; integrate one operation into a small model. **Technical:** CPU/reference oracle; synchronized GPU timings; multiple shapes/dtypes; tuning and test shapes separate.

**Acceptance:** awkward and empty/edge shapes where supported; numerical tolerance by dtype; model quality gate; sanitizer/tool checks where supported; no race or invalid access. **Performance:** compare against optimized library, not just own naive kernel; report slower cases and tuning overhead. **Documentation:** roofline estimate, profiler evidence, shape-dependent results and limits. **GitHub:** correctness/benchmark runners and focused external performance contribution. **Done:** explain memory traffic and justify or retract each speedup claim.

## P12 — Controlled research reproduction

**Stage/budget:** B3, 150/240 hours. **Skills:** paper analysis, reproducibility, statistical evaluation, ablations, research code, scaling reasoning and technical writing.

**Functional:** reproduce a narrow LoRA or training-method claim at affordable scale, then test one justified extension. **Technical:** preregistered protocol, code/data versions, fixed compute cap, pilot, multiple seeds when affordable, retained failed runs; fit only local empirical scaling trends and mark extrapolation limitations.

**Acceptance:** baseline parity, equation-to-code trace, documented deviations, appropriate uncertainty, two ablations and one extension; external reproduction attempt of a small subset. **Performance:** time/memory/compute ledger; small-scale reproduction cannot validate original large-scale claims. **Documentation:** paper-style report, experiment manifests, negative results and reproducibility checklist. **GitHub:** scripts and results, upstream issue/patch where relevant. **Done:** valid negative reproduction passes if diagnosis and limitations are rigorous; a positive result is not required.

## P13 — Small numerical language/compiler

**Stage/budget:** B4, 150/240 hours. **Skills:** parsing, types, AST/IR, JIT, optimization, numeric legality and differential testing.

**Functional:** execute a restricted typed numerical language and compile supported operations; reject unsupported shapes/programs. **Technical:** interpreter oracle, LLVM tutorial-derived infrastructure with attribution, original extensions, semantic-preserving passes.

**Acceptance:** generated-program differential tests; invalid programs; floating-point counterexamples; compiler and runtime errors handled. **Performance:** compile versus execution time separated; break-even workload measured against interpreter and library. **Documentation:** grammar, type rules, IR examples, optimization legality and limits. **GitHub:** compiler demo, test corpus and minimal external bug report/contribution. **Done:** explain each lowering and why a faster transformation remains valid.
