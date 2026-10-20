# 6. Integrated capstone architecture

Build a connected portfolio, not a single ever-growing production application. The directory, numerical workbench, small LM and systems experiments can be separate repositories, with a central index of evidence. Reuse clean data contracts and test harnesses; do not carry unnecessary dependencies into every project.

| Sequence | Architecture and evidence | Interview competencies |
|---|---|---|
| P1→P2 | Snapshot files → validated records → own index → CLI search | Independent programming, data structures, complexity, debugging |
| P3 | Ingestion → provenance DB → API → optional thin UI; CI/deployment/restore | Backend design, SQL, security, API contracts, operations |
| P4 | Framed jobs → bounded queue → workers → recovery log → DB | Concurrency, OS/network understanding, failure semantics |
| P5→P6 | Numerical references → versioned data → evaluation pipeline → model artifact/service | Derivations, statistics, leakage, metrics, ML deployment |
| P7 | Licensed corpus → tokenizer → small decoder → train/checkpoint → evaluation | Backprop, attention, optimization, tensor debugging |
| P8 | User query → permission checks → retrieval → model → schema/citation checks → answer or abstain | Retrieval quality, evaluation design, reliability, threat modeling |
| P9 | Request scheduler → model workers/KV cache → benchmark harness; separate DDP experiment | Throughput/latency, capacity, distributed gradients, recovery |
| One of P10/P11/P12 | Deeper distributed service, GPU suite, or research reproduction | Chosen specialty depth and externally reviewed contribution |
| P13 optional after P11 | Language → type checker → IR → optimizer → executable | Compiler correctness, numerical legality, code generation |

## Compute ladder and spending controls

These are **budget allowances, not verified provider price quotes**. No purchase is required to start. Recheck available hardware, quotas and current pricing before any paid run.

1. **S0–S6:** ordinary laptop; use small data and CPU models. Eight GB RAM can support reduced examples; 16 GB is more comfortable. Store larger synthetic data on disk and stream it. Local staging substitutes for paid hosting; document that difference.
2. **S7:** start around 1–10 million parameters and short sequences for debugging on CPU. If available, a compatible GPU makes larger experiments practical. A 10–50M-parameter educational decoder may be a reasonable next scope, but actual memory depends on sequence length, batch size, optimizer, precision and activations. Estimate parameter/gradient/optimizer/activation memory before choosing a configuration; do not promise a hardware fit from parameter count alone.
3. **S8:** small local models or a capped API budget; adaptation only after a baseline. An optional **$20–$50 monthly experiment allowance** is a planning ceiling, not an instruction to spend or a guarantee of adequate compute. Tool/agent testing can use deterministic fake models until logic is correct.
4. **S9:** CPU multi-process experiments prove distributed semantics. GPU serving experiments need a supported accelerator/model stack; Apple acceleration is not equivalent to CUDA. Use a small remote GPU only for experiments unavailable locally. Provision a fixed run window, then shut down and verify billing/storage state.
5. **B2/B3:** a provisional **$50–$150 per bounded experiment** cap can guide scope, subject to actual quotes. Run a short pilot, project cost from measured seconds/step, add a failure margin and reduce model/data/replicates before overspending. If no GPU budget exists, postpone the GPU gate; CPU simulations do not satisfy it.

For each experiment compute estimated cost = quoted hourly rate × expected runtime + storage/transfer. Record actual spend, queue time and failed runs. Dollar figures do not include an unapproved new computer purchase. Free notebook GPUs may be unavailable and are not a prerequisite assumption.

Frontier pretraining, hundreds/thousands of accelerators, high-speed fabric tuning, fleet scheduling, large human-feedback programs and industrial incident response cannot be reproduced credibly on a hobby budget. Small replicas demonstrate mechanisms, not experience operating those systems. This distinction belongs in every advanced README and interview explanation.

## Graduation evidence

Pin four strongest public repositories, not every exercise: one reliable software service, one evaluated ML project, one transformer/inference workbench, and one chosen specialty. Put a concise evidence index on Simpyll: problem, personal contribution, measured result, limitations and reproduction link. RNtoNP's actual user needs should drive product decisions; synthetic tests should remain distinguishable from real usage.
