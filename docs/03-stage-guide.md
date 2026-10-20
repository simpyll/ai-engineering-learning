# 3. Multiyear curriculum

Generated from `curriculum.json`, the authority for prerequisites, estimates and module criteria. A 20-hour module has four five-hour weeks: reference implementation, application, engineering/testing, demonstration/review/repair. All reading, project and assessment time is included. See weekly assignments for deliverables and project catalog for release contracts.

## S0 — Diagnostic and working environment

**Objective:** Establish what can be skipped and make one reproducible Python repository.

**Prerequisites:** none. **Budget:** 10h / 2 active weeks / 0.04 calendar years at 46 active weeks/year. **Project:** P0. **Resources:** R01, R03, R32.

**Career relevance:** Baseline, no employment claim.

Follow weeks 1–2 in the initial plan for diagnostic exit.

**Exit/portfolio:** all stage criteria, P0 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S1 — Independent Python software

**Objective:** Build, test and explain a complete command-line data application.

**Prerequisites:** S0. **Budget:** 110h / 22 active weeks / 0.48 calendar years at 46 active weeks/year. **Project:** P1. **Resources:** R01, R02, R03, R04.

**Career relevance:** Small automation work; foundation for junior applications.

First complete weeks 3–12 (50 hours), then these three modules (60 hours).

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S1.01 — Python abstractions | Refactor collector using dataclasses, type annotations, generators and context managers | 20 | Typed boundary validation; demonstrate generator memory behavior and two invalid-input cases |
| S1.02 — Design and debugging | Separate pure transformations from I/O; compare procedural, OO and functional versions; profile a slow path | 20 | Explain chosen design; locate two seeded bugs; compare before/after profile on identical input |
| S1.03 — Release engineering | Package the collector, add CI, changelog, documentation and a clean-environment install | 20 | One documented command processes fixtures; CI succeeds; closed-book parser task and release demo pass |

**Exit/portfolio:** all stage criteria, P1 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S2 — Algorithms and discrete reasoning

**Objective:** Choose algorithms using invariants and measured scaling.

**Prerequisites:** S1. **Budget:** 140h / 28 active weeks / 0.61 calendar years at 46 active weeks/year. **Project:** P2. **Resources:** R05, R06.

**Career relevance:** Junior coding interviews and performance literacy.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S2.01 — Proofs and complexity | Write loop invariants and operation counters for linear/binary search | 20 | Prove termination and correctness; predict and measure scaling at three input sizes |
| S2.02 — Sorting and hashing | Implement mergesort and a collision-handling hash table | 20 | Match reference results on random/adversarial cases; explain worst-case versus expected costs |
| S2.03 — Trees and heaps | Implement binary search tree operations and a heap-based top-k selector | 20 | Property tests preserve ordering; handle duplicate/empty input; explain skewed-tree behavior |
| S2.04 — Graphs | Implement BFS, DFS, topological ordering and Dijkstra on program/prerequisite graphs | 20 | Detect cycles; compare shortest paths with tiny hand-solved examples; reject unsupported negative weights |
| S2.05 — Dynamic programming | Implement edit distance and one knapsack-style problem | 20 | Derive recurrence and base cases; compare memoized and tabulated versions |
| S2.06 — Index and ranking | Build an inverted index and ranked keyword search over program fixtures | 20 | Queries return known documents; explain tokenization and ranking; compare with linear scan |
| S2.07 — Integration and interview | Integrate search into collector; solve unseen array and graph tasks | 20 | All P2 tests pass; defend complexity; solve two appropriately scoped unseen tasks with explanation |

**Exit/portfolio:** all stage criteria, P2 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S3 — Backend engineering and data products

**Objective:** Deliver a reliable database-backed service with a repeatable deployment.

**Prerequisites:** S2. **Budget:** 180h / 36 active weeks / 0.78 calendar years at 46 active weeks/year. **Project:** P3. **Resources:** R07, R08, R09, R10, R24.

**Career relevance:** Earliest planned junior/backend job-search checkpoint.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S3.01 — Relational modeling | Model schools, programs, source snapshots and provenance in SQL | 20 | Constraints reject invalid relations; migration and rollback work on fixtures |
| S3.02 — SQL and transactions | Implement joins, aggregates, pagination and concurrent updates | 20 | Explain transaction isolation; tests expose and prevent a lost update |
| S3.03 — HTTP and API contracts | Inspect a raw HTTP request locally; build typed endpoints and validation | 20 | Contract tests cover status codes, malformed inputs and pagination bounds |
| S3.04 — Authentication and security | Add maintained auth integration, role-based authorization and secret handling | 20 | Anonymous writes and cross-user access denied; parameterized queries resist injection fixtures |
| S3.05 — Reliable ingestion | Import source snapshots with idempotency, schema validation and retry budgets | 20 | Second import creates zero duplicates; malformed records quarantined with provenance |
| S3.06 — Indexes and caching | Profile SQL queries; add index and bounded cache with invalidation | 20 | Query plan and latency distribution recorded; stale-cache scenario tested |
| S3.07 — Deployment and CI | Containerize API/database; add automated tests and repeatable staging deployment | 20 | Fresh clone starts service; failed checks block release; rollback demonstrated |
| S3.08 — Operations | Add structured logs, health checks, metrics, backup and restore procedure | 20 | Restore into empty database; diagnose injected outage; define one user-facing SLO |
| S3.09 — Release and job checkpoint | Run load test, external review, architecture explanation and portfolio release | 20 | P3 contract and mastery rubric pass; record bottleneck, limits and a reviewed change |

**Exit/portfolio:** all stage criteria, P3 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S4 — Computer systems and concurrency

**Objective:** Understand how programs use CPUs, memory, operating systems and networks.

**Prerequisites:** S3. **Budget:** 160h / 32 active weeks / 0.70 calendar years at 46 active weeks/year. **Project:** P4. **Resources:** R11, R12, R13, R14, R32.

**Career relevance:** Backend depth and preparation for infrastructure.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S4.01 — Representation and architecture | Build small ALU simulation; inspect compiled arithmetic and cache-sensitive loops | 20 | Explain signed/unsigned overflow and cache locality using measured examples |
| S4.02 — C and memory | Write C array/string routines and a small owned buffer | 20 | Compiler warnings clean; memory sanitizer finds then verifies repair of bounds/lifetime bugs |
| S4.03 — Processes and virtual memory | Create process pipeline and inspect address-space/memory behavior | 20 | Explain fork/exec, file descriptors and virtual versus physical memory; reap child processes |
| S4.04 — Threads and synchronization | Build bounded producer-consumer queue with locks/conditions | 20 | Stress test for races/deadlocks; explain each shared-state invariant |
| S4.05 — Async and parallel work | Compare threads, processes and async fetching on local simulated I/O | 20 | Bound concurrency; measure CPU/I/O workloads; explain interpreter/runtime limits |
| S4.06 — Networking | Write local TCP client/server with framing, timeouts and partial-read handling | 20 | Fragmented messages reassemble; disconnect and timeout tests pass; explain DNS/TLS/HTTP roles |
| S4.07 — Persistence and interpreters | Build append-only record log with recovery plus tiny expression parser/evaluator | 20 | Recover valid prefix after truncated write; reject malformed expressions; explain AST and execution |
| S4.08 — Systems integration | Integrate worker and log with ingestion; profile and document failure modes | 20 | Kill worker mid-job and recover without duplicate committed records; P4 oral/debugging gate passes |

**Exit/portfolio:** all stage criteria, P4 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S5 — Mathematics and numerical experiments

**Objective:** Derive and numerically verify the mathematics needed for learning systems.

**Prerequisites:** S2. **Budget:** 160h / 32 active weeks / 0.70 calendar years at 46 active weeks/year. **Project:** P5. **Resources:** R15, R16.

**Career relevance:** Prerequisite for ML; diagnostic credit available.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S5.01 — Vectors and geometry | Implement dot products/projections and a least-squares geometry notebook | 20 | Dimensions correct; explain span, rank, orthogonality and geometric interpretation |
| S5.02 — Linear algebra | Implement small elimination solver; compare QR/SVD-based library solves | 20 | Residuals reported; explain conditioning and why explicit inverse is avoided |
| S5.03 — Calculus | Derive scalar/vector chain rules and implement finite-difference checks | 20 | Check gradients on three functions; explain Jacobian shapes and numerical error |
| S5.04 — Probability | Simulate conditional events and Bayes updates; compute moments | 20 | Match analytical results within Monte Carlo uncertainty; distinguish independence/conditional independence |
| S5.05 — Inference and experiment design | Bootstrap a metric and simulate confidence-interval coverage | 20 | Explain sampling unit, uncertainty, multiple comparisons and why association is not causation |
| S5.06 — Optimization | Implement gradient descent with learning-rate and regularization experiments | 20 | Derive least-squares gradient; show convergent/divergent cases without hiding failures |
| S5.07 — Information and numerics | Implement stable softmax/log-sum-exp, entropy and KL on discrete distributions | 20 | Handle extreme logits; explain floating-point cancellation and KL directionality |
| S5.08 — Math gate | Build PCA via SVD and defend derivations plus simulation notebook | 20 | Pass five-domain diagnostic at 80% per domain; unseen gradient and probability tasks pass |

**Exit/portfolio:** all stage criteria, P5 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S6 — Classical machine learning and data quality

**Objective:** Build a valid experiment and deploy a model whose limitations are measurable.

**Prerequisites:** S3, S5. **Budget:** 180h / 36 active weeks / 0.78 calendar years at 46 active weeks/year. **Project:** P6. **Resources:** R17, R19, R21.

**Career relevance:** Applied ML portfolio, strongest with prior software work.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S6.01 — Data contracts and EDA | Create versioned dataset, missingness report and provenance ledger | 20 | Document labels, unit of observation, allowed usage and leakage risks |
| S6.02 — Regression from scratch | Implement linear/ridge regression and compare to library reference | 20 | Gradient check passes; residuals and baseline metric recorded |
| S6.03 — Classification from scratch | Implement logistic regression with stable loss | 20 | Gradient and prediction checks pass; class imbalance and threshold trade-off explained |
| S6.04 — Trees and ensembles | Implement tiny decision stump then compare tree and ensemble models | 20 | Validate split logic; tuning uses only training/validation data |
| S6.05 — Unsupervised learning | Implement k-means and compare PCA/cluster assignments | 20 | Explain initialization sensitivity and why clusters are not ground truth |
| S6.06 — Evaluation and features | Build preprocessing pipeline with group/time-aware cross-validation | 20 | No test-set fitting; compare dummy, linear and tree baselines with uncertainty |
| S6.07 — Robustness and calibration | Evaluate subgroup errors, calibration, drift and out-of-domain behavior | 20 | Choose metric from task costs; report unsupported subgroup conclusions honestly |
| S6.08 — Model service | Package model and preprocessing together; add schema and drift checks | 20 | Offline/online predictions match; rollback to baseline works; artifact/data versions traceable |
| S6.09 — ML release | Freeze test set, run final experiment, produce model/data cards and technical defense | 20 | P6 reproducibility and leakage gates pass; explain a failed model and whether ML adds value |

**Exit/portfolio:** all stage criteria, P6 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S7 — Deep learning and a small language model

**Objective:** Implement differentiation, attention and a trainable transformer.

**Prerequisites:** S4, S6. **Budget:** 200h / 40 active weeks / 0.87 calendar years at 46 active weeks/year. **Project:** P7. **Resources:** R18, R19, R22, R33.

**Career relevance:** Deep-learning/research-engineering foundations.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S7.01 — Tensors and autograd | Build scalar autograd engine and a small tensor computation graph | 20 | Finite-difference gradients match within declared tolerance on well-conditioned float64 examples |
| S7.02 — MLP and backpropagation | Implement two-layer network in NumPy then reproduce in PyTorch | 20 | Derive gradients; overfit tiny batch; identify deliberately broken gradient |
| S7.03 — Training discipline | Implement seeds, checkpointing, learning-rate schedules and regularization | 20 | Resume training; compare controlled runs; separate optimization failure from overfitting |
| S7.04 — CNNs | Implement a convolution reference and train small image classifier | 20 | Compare operator to framework; report held-out accuracy and translation limitations |
| S7.05 — Sequences and representations | Implement recurrent cell and compare sequence baseline plus embeddings | 20 | Handle padding/masks; explain vanishing gradients and representation geometry |
| S7.06 — Tokenizer and data | Implement small BPE tokenizer and licensed text split pipeline | 20 | Round-trip tests pass; train/validation documents disjoint; unknown/Unicode behavior documented |
| S7.07 — Attention | Implement masked scaled dot-product and multi-head attention | 20 | Reference parity and future-token leakage tests pass; shapes/complexity explained |
| S7.08 — Transformer | Build decoder blocks, normalization, residuals and generation | 20 | Causal prediction and checkpoint tests pass; compare outputs to reference primitives |
| S7.09 — Small LM training | Train tiny decoder; compare bigram baseline and one ablation | 20 | Validation loss and compute logged; no unsupported frontier-quality claim; explain unsuccessful runs |
| S7.10 — DL release | Profile memory/throughput; publish architecture, experiment manifests and oral defense | 20 | P7 correctness, derivation, reproducibility and compute-accounting gates pass |

**Exit/portfolio:** all stage criteria, P7 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S8 — Evidence-grounded AI applications

**Objective:** Engineer evaluated retrieval, constrained tool use and model adaptation.

**Prerequisites:** S7. **Budget:** 180h / 36 active weeks / 0.78 calendar years at 46 active weeks/year. **Project:** P8. **Resources:** R20, R21, R34, R35, R37.

**Career relevance:** AI application roles; transferable evaluation expertise.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S8.01 — Evaluation and baseline | Define 60-question evidence-grounded search benchmark and lexical baseline | 20 | Version questions/reference evidence; separate development and locked test queries |
| S8.02 — Retrieval | Implement chunking, inverted retrieval and brute-force cosine search before vector index | 20 | Recall@5 measured; duplicate and stale-source tests pass; explain index trade-offs |
| S8.03 — Grounded answer service | Add cited answer generation, abstention and structured output validation | 20 | Unsupported questions trigger abstention; cited statements trace to retrieved source spans |
| S8.04 — Reliable tool workflows | Implement bounded state machine with allowlisted read-only tools | 20 | Timeout/retry/token limits hold; invalid tool calls and malicious document instructions cannot expand permissions |
| S8.05 — Evaluation hardening | Add prompt-injection, stale-source, malformed-output and cost regression suite | 20 | P8 locked-test report includes human-audited grading and failure taxonomy |
| S8.06 — Fine-tuning and LoRA | Compare prompt/retrieval baseline to small LoRA adaptation | 20 | Training/evaluation contamination checked; trainable parameter count derived; report whether adaptation helps |
| S8.07 — Preference and synthetic data | Implement toy DPO objective; audit synthetic labels and feedback bias | 20 | Correct gradients; distinguish objective from proven safety; synthetic artifacts never silently enter locked evaluation |
| S8.08 — Production reliability | Add model routing, caching, budget limits, traces, fallback and privacy-aware logging | 20 | Rate limits and simulated provider failures recover; cost per successful task and latency reported |
| S8.09 — AI application release | Publish system/data/model cards, limitations, evaluation report and demo | 20 | P8 contract passes; independent reviewer audits ten answers and one failure; no hidden agent privileges |

**Exit/portfolio:** all stage criteria, P8 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## S9 — Serving and distributed ML systems

**Objective:** Measure and improve inference/training infrastructure with correctness gates.

**Prerequisites:** S8. **Budget:** 200h / 40 active weeks / 0.87 calendar years at 46 active weeks/year. **Project:** P9. **Resources:** R23, R24, R25, R26, R36.

**Career relevance:** ML systems/inference entry portfolio plus prior production experience.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| S9.01 — Serving baseline | Build request/load generator and instrument a small-model inference endpoint | 20 | Record time-to-first-token, inter-token latency, throughput, concurrency and memory under fixed workload |
| S9.02 — Batching and scheduling | Implement bounded queue and simple batch scheduler | 20 | Cancellation/backpressure/fairness tests pass; plot throughput versus tail latency |
| S9.03 — KV cache | Implement small KV cache or simulator and compare cached/uncached decoding | 20 | Logits agree within declared tolerance; memory growth versus sequence length measured |
| S9.04 — Quantization | Compare supported low-precision configurations to full-precision baseline | 20 | Quality delta and memory/latency reported; regressions block release |
| S9.05 — Serving engine comparison | Run compatible engine such as vLLM on fixed supported hardware/model | 20 | Baseline and engine share workload/precision; report warmup and reproducibility details |
| S9.06 — Distributed data | Implement partitioned deterministic preprocessing with idempotent outputs | 20 | Worker failure/replay tests pass; single/multiple-worker outputs agree |
| S9.07 — Distributed training | Implement synchronous gradient aggregation reference then PyTorch DDP | 20 | Two CPU processes establish semantics; compare gradients to serial effective batch; explain sampler behavior |
| S9.08 — Checkpoint and recovery | Add atomic checkpoint metadata, resume and simulated worker failure | 20 | State restored without silent corruption; distinguish reproducible state from bitwise nondeterminism |
| S9.09 — Profiling and capacity | Profile compute, memory and communication; estimate bottleneck and cost per successful request | 20 | Evidence supports optimization decision; scaling efficiency and hardware limits reported |
| S9.10 — Systems release | Run controlled benchmark, outage drill and design review | 20 | P9 contract passes; present correctness/performance trade-off and production gaps |

**Exit/portfolio:** all stage criteria, P9 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## B1 — Distributed infrastructure specialization

**Objective:** Deepen reliability, storage and orchestration through failure-tested systems.

**Prerequisites:** S9. **Budget:** 240h / 48 active weeks / 1.04 calendar years at 46 active weeks/year. **Project:** P10. **Resources:** R23, R24, R27, R38.

**Career relevance:** Distributed systems and AI infrastructure.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| B1.01 — Consistency model | Specify queue/store guarantees and failure model | 20 | State linearizability versus eventual-consistency expectations and forbidden histories |
| B1.02 — Replication | Implement local replicated log simulator | 20 | Replica replay yields matching state across reorder/delay scenarios |
| B1.03 — Consensus fundamentals | Implement educational election/log-replication subset | 20 | Partition tests show no conflicting committed entries under stated assumptions; label incomplete Raft scope |
| B1.04 — Durable queue | Implement leases, retries and idempotent commits | 20 | Duplicate delivery tolerated; poison messages quarantined; bounded retry behavior |
| B1.05 — Storage internals | Build page/index or LSM-style toy component | 20 | Compare indexed scan costs; explain WAL/recovery and compaction trade-offs |
| B1.06 — Cloud primitives | Deploy isolated staging with IAM, networking and object storage or local equivalents | 20 | Least-privilege policy and teardown plan tested; distinguish simulation from provider experience |
| B1.07 — Kubernetes | Deploy same service to local cluster with resource limits and probes | 20 | Rolling restart preserves stated service guarantees; rollback tested |
| B1.08 — Scheduling | Add fair scheduling, quotas and load shedding | 20 | Overload does not create unbounded queue or starve one tenant |
| B1.09 — Observability | Trace job through API, broker and workers | 20 | Diagnose one unknown injected failure from telemetry |
| B1.10 — Reliability | Exercise backup, restore, zonal-failure simulation and capacity reduction | 20 | State RPO/RTO, measure recovery, write blameless postmortem |
| B1.11 — Contribution | Submit reproducible bug report or focused improvement to an existing infrastructure project | 20 | Maintainer-readable test and rationale; acceptance not required for completion |
| B1.12 — Infrastructure defense | Publish workload/chaos results and design review | 20 | P10 gate and independent review pass; distinguish local fault simulation from fleet operations |

**Exit/portfolio:** all stage criteria, P10 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## B2 — GPU and performance engineering

**Objective:** Build correct accelerator kernels and explain measured bottlenecks.

**Prerequisites:** S9. **Budget:** 320h / 64 active weeks / 1.39 calendar years at 46 active weeks/year. **Project:** P11. **Resources:** R28, R29, R30.

**Career relevance:** GPU/ML performance roles; substantial specialization.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| B2.01 — C++ foundations | Implement owned arrays, templates and RAII wrappers | 20 | Explain lifetimes/moves; sanitizers and warning checks pass |
| B2.02 — C++ interfaces | Build benchmark harness and small numerical library | 20 | Independent oracle and API invariants tested |
| B2.03 — CPU performance | Measure cache locality, vectorization and allocation costs | 20 | Compiler output and profiles support conclusions |
| B2.04 — GPU architecture | Model grids, warps, memory spaces and occupancy | 20 | Explain bandwidth versus compute bound examples |
| B2.05 — CUDA vector operations | Implement vector add and reductions | 20 | Boundary/nonmultiple-size tests pass; compare CPU oracle |
| B2.06 — CUDA memory | Compare coalesced and strided access patterns | 20 | Bandwidth measured with warmup/synchronization and identical data |
| B2.07 — CUDA matrix multiply | Implement naive then tiled matrix multiply | 20 | Tolerance-based correctness across shape sweep; explain shared-memory design |
| B2.08 — Numerical precision | Evaluate FP32 and supported lower precision | 20 | Worst-case error and downstream quality recorded |
| B2.09 — Triton basics | Implement vector add and fused softmax independently | 20 | Match references across awkward shapes; explain masking |
| B2.10 — Kernel fusion | Fuse normalization or bias/activation operations | 20 | Demonstrate removed memory traffic; report cases slower than library |
| B2.11 — Triton matmul | Implement and tune tiled multiplication | 20 | Publish shape-dependent performance versus optimized library |
| B2.12 — Profiling | Use supported GPU profiler to identify stalls and occupancy limits | 20 | One bottleneck prediction verified or falsified by trace |
| B2.13 — Autotuning | Select kernel configurations without test-workload leakage | 20 | Separate tuning/evaluation shape sets; include tuning overhead |
| B2.14 — Integration | Replace one small-model operation with custom kernel | 20 | Model outputs and quality stay within predeclared tolerance |
| B2.15 — Contribution | Prepare targeted performance fix or benchmark for existing project | 20 | Minimal reproduction and correctness oracle accompany proposed change |
| B2.16 — GPU defense | Publish kernel suite and performance report | 20 | P11 gate passes; no claim of general speedup from one favorable shape |

**Exit/portfolio:** all stage criteria, P11 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## B3 — Research engineering specialization

**Objective:** Reproduce a bounded research claim and make one controlled extension.

**Prerequisites:** S9. **Budget:** 240h / 48 active weeks / 1.04 calendar years at 46 active weeks/year. **Project:** P12. **Resources:** R22, R33, R34, R35.

**Career relevance:** Research-engineering evidence, not scientist qualification.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| B3.01 — Paper selection | Choose small LoRA or optimization result with accessible code/data | 20 | Claim, dependencies and compute feasibility approved in written protocol |
| B3.02 — Literature map | Read target plus two closely related papers | 20 | Distinguish established evidence, author claims and open questions |
| B3.03 — Protocol | Predeclare metrics, split, seeds, compute cap and deviation rules | 20 | Replication target and failure criteria unambiguous |
| B3.04 — Baseline implementation | Implement relevant baseline and parity tests | 20 | Baseline behavior agrees with published or official reference within scoped expectations |
| B3.05 — Method implementation | Implement target modification from equations | 20 | Equation-to-code trace and independent correctness checks pass |
| B3.06 — Pilot | Run miniature end-to-end experiment and profile cost | 20 | Projected full experiment fits cap or rescope before launch |
| B3.07 — Replication | Execute fixed runs and preserve raw logs | 20 | Failed runs retained; seed/config/code/data identifiers complete |
| B3.08 — Statistical analysis | Estimate uncertainty with appropriate unit of resampling | 20 | Do not treat dependent examples/seeds as independent evidence |
| B3.09 — Ablations | Run two focused ablations within budget | 20 | Only intended variable changes; negative results retained |
| B3.10 — Extension | Test one justified hypothesis at equal budget | 20 | Label exploratory analysis and avoid post-hoc success criteria |
| B3.11 — External feedback | Request technical critique and prepare contribution | 20 | Reviewer can reproduce a subset; deviations documented |
| B3.12 — Research defense | Release reproducibility package and paper-style report | 20 | P12 gate passes; describe scaled reproduction limits and unsupported generalization |

**Exit/portfolio:** all stage criteria, P12 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.

## B4 — AI compiler specialization

**Objective:** Trace a numerical program from language to optimized execution.

**Prerequisites:** B2. **Budget:** 240h / 48 active weeks / 1.04 calendar years at 46 active weeks/year. **Project:** P13. **Resources:** R31, R28.

**Career relevance:** AI compiler roles; optional after GPU competence.

| Module | Implementation / increment | Hours | Acceptance |
|---|---|---:|---|
| B4.01 — Language semantics | Specify typed expression language and interpreter | 20 | Reference semantics handle shape/type errors explicitly |
| B4.02 — Lexer and parser | Build lexer, parser and AST | 20 | Malformed/ambiguous expressions covered by tests |
| B4.03 — Type checking | Implement scalar/tensor type and shape checks | 20 | Invalid programs fail before execution |
| B4.04 — IR generation | Lower expressions to LLVM IR | 20 | Compiled output matches interpreter on generated cases |
| B4.05 — Control flow | Add branches and loops | 20 | Control-flow graphs and execution agree on boundary cases |
| B4.06 — Optimization basics | Implement constant folding and dead-code elimination | 20 | Differential tests preserve semantics |
| B4.07 — Numerical legality | Explore reassociation and floating-point constraints | 20 | Document where mathematically equivalent rewrites alter numeric results |
| B4.08 — JIT integration | Expose compiled functions to Python benchmark | 20 | Compile time separated from execution time |
| B4.09 — Tensor lowering | Implement restricted tensor-operation lowering | 20 | Shape/stride correctness verified; unsupported cases rejected |
| B4.10 — Performance study | Compare generated kernels to interpreter and library | 20 | Report compile overhead and break-even workload |
| B4.11 — Contribution | Prepare focused compiler test/bugfix for external project | 20 | Minimal IR reproducer and explanation included |
| B4.12 — Compiler defense | Release compiler demo and correctness/performance report | 20 | P13 gate passes; explain limitations versus production compiler stack |

**Exit/portfolio:** all stage criteria, P13 release contract and mastery rubric pass. Publish original implementation, tests, decision records, limitations and reproducible demo. S0 records diagnostic decisions instead. Completing reading alone is insufficient.
