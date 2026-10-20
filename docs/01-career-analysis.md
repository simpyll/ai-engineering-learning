# 1. Career competency analysis

Research snapshot: October 20, 2026. This is a curriculum designer's synthesis of public evidence, not a claim that representatives of these companies participated. US postings are used for compensation examples because the requested employers publish them; eligibility, location, openings and packages change. The sample is selective and cannot establish hiring probabilities or market-wide medians.

## Recommendation

Start with **Python backend and data engineering**, seek work once you can maintain a deployed service, then specialize in **ML systems, evaluation and inference**. This gives you useful software skills before the much longer mathematical and research sequence. Your Linux familiarity reduces tool-learning overhead; it does not substitute for application design, testing or systems internals. RNtoNP can supply a meaningful directory/data problem and Simpyll can present the evidence. Neither is required: a public-library or open-course directory works equally well.

This is a judgment about option value and prerequisite overlap, not a verified claim that one track has the highest expected earnings. A narrow GPU or research-scientist path would postpone your earliest employable work substantially. Reconsider after actual systems and ML projects reveal what you enjoy and perform well at.

## What the postings establish

- Google's sampled **Staff Software Engineer, BigQuery ML** posting requires eight years in software development, substantial launch/design experience, and five years of ML infrastructure experience. It lists US base salary of **$207,000–$301,000**, a **20% bonus target**, equity and benefits. This illustrates why a portfolio is not a substitute for a Staff history. [Google posting](https://www.google.com/about/careers/applications/jobs/results/135262336041525958-staff-software-engineer-bigquery-machine-learning)
- OpenAI's **Research Engineer** posting emphasizes programming and large distributed systems, with high-performance deep-learning implementation as a useful additional qualification. It lists **$250,000–$445,000 base pay**, equity and eligible performance bonuses. It does not make a PhD a stated requirement on this page. [OpenAI posting](https://openai.com/careers/research-engineer-san-francisco/)
- Anthropic's **Performance Engineer, Inference Systems** posting emphasizes profiling, roofline reasoning, production debugging, correctness evaluation, telemetry and written influence. Its posted **Annual Salary is $350,000–$850,000**; the page does not give a quantified total compensation package. That unusually wide range is an exceptional employer/role example, not an attainable starting salary or a typical performance-engineering wage. [Anthropic posting](https://job-boards.greenhouse.io/anthropic/jobs/5224564008)
- Google's sampled **Distinguished Engineer, Product SRE** posting asks for 15 years of software experience, distributed-systems architecture, concurrency and cross-organization influence. This is evidence of scope and history, not a universal tenure rule. [Google posting](https://www.google.com/about/careers/applications/jobs/results/114070756412793542-distinguished-engineer-google-product-site-reliability)
- Google's sampled **Senior AI/ML** role asks for five years of software development experience. Titles vary; do not treat these examples as automatic promotion schedules. [Google posting](https://www.google.com/about/careers/applications/jobs/results/95439503962841798-senior-software-engineer-aiml-gen-ai-geo)
- OpenAI's **Research Scientist** posting asks for original contributions, such as first-author publications or projects, and the ability to pursue a research agenda. DeepMind describes research engineers as combining engineering, mathematics and ML, while research scientists generally bring doctoral-level research preparation. A doctorate is a common route, not a universal legal or technical prerequisite. [OpenAI scientist](https://openai.com/careers/research-scientist-san-francisco/), [DeepMind careers](https://deepmind.google/careers/)

Base salary is cash salary. An offer's annualized total compensation may add target bonus and equity vesting value; sign-on grants, refreshers and liquidity conditions must be separated. Private equity is not equivalent to spendable cash. The sources above do not establish comparable TC medians, so none are invented. Exceptional million-dollar packages sometimes discussed publicly should be treated as outliers, not a curriculum target or a probability estimate. No numerical forecast of your compensation is defensible from these data.

## Competency matrix

H = central hiring evidence; M = supporting competence; L = limited emphasis. These are synthesized priorities, not employer scoring systems. All roles still require communication, collaboration and security judgment.

| Track | Software / algorithms | Systems / reliability | ML / math | Experiments / research | GPU / compiler | Leadership evidence | Accessibility from this profile |
|---|---|---|---|---|---|---|---|
| Senior/Staff software | H | H | L–M | L | L | H | Broadest base; seniority requires shipped outcomes |
| Principal/Distinguished software | H | H | Domain-dependent | M | Domain-dependent | H across organizations | Very long experience path, not a self-study endpoint |
| Senior/Staff ML engineer | H | H | H | H evaluation | M | H | Accessible through software + deployed ML experience |
| AI research engineer | H | H | H | H | M–H | M–H | Difficult; strong implementations and credible experiments |
| Research scientist | M–H | M | H | H original research | Domain-dependent | H intellectual direction | Highest research barrier; doctoral work or equivalent record |
| AI infrastructure | H | H | M | M | M | H at senior levels | Good continuation from backend/systems |
| Distributed systems | H | H | L–M | M measurement | L–M | H | Durable general track; AI domain is optional |
| LLM training/inference | H | H | H | H evaluation | H for some teams | M–H | Strong overlap with recommended later path |
| ML systems performance | H | H | M–H numerics | H measurement | H | H influence | Smaller specialized market; demonstrated bottleneck analysis |
| AI compiler/GPU | H C++ | H architecture | M–H numerics | H benchmarking | H | M–H | Long prerequisite chain; optional focused specialization |

The compiler specialization follows the compiler/GPU skills in NVIDIA's public role materials and its LLVM-based compiler role, but those are not a representative salary sample. [NVIDIA compiler role](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Raytracing-Compiler-Engineer---Developer-and-Performance-Technology_JR2012859)

## Levels of professional scope

| Level | Evidence expected | What self-study can establish | What it cannot establish alone |
|---|---|---|---|
| Entry | Implement scoped changes, tests, Git, debugging, SQL/API basics, ask useful questions | P1–P3, unfamiliar-code exercise, reviewed change | Sustained delivery in a team |
| Strong midlevel | Own a service or feature through design, deployment and operation | P3/P4/P6 and externally reviewed contributions approximate parts | Repeated production responsibility and stakeholder judgment |
| Senior | Resolve ambiguity, make sound trade-offs, mentor, improve reliability | Design reviews and incident simulations rehearse skills | Multi-cycle ownership and real incident leadership |
| Staff | Coordinate architecture and technical direction across teams; measurable leverage | Cross-project work and substantial OSS collaboration provide partial evidence | Organization-level trust, adoption and sustained outcomes |
| Principal/Distinguished | Set broad technical strategy, resolve systemic constraints, grow other technical leaders | Deep specialization and public work can build credibility | Years of consequential, cross-organization decisions |
| Research scientist | Create and validate new knowledge and guide research | Reproduction, rigorous extensions and original papers | Guaranteed novelty, peer recognition, or equivalence to doctoral training |

## Interview implications

Prepare coding, debugging, system design, behavioral examples and, for ML roles, data/evaluation design. Research roles add paper discussions, mathematical reasoning and experiment criticism; performance roles add profiling and architecture reasoning. These are preparation categories, not a promise of a particular interview loop. Meta's official preparation page was rate-limited during verification, so exact current rounds and AI-use rules are deliberately not asserted. Verify the actual interview packet with the recruiter. [Meta preparation page](https://www.metacareers.com/swe-prep-onsite)

Engineering publications reinforce the emphasis on evaluation and realistic workloads: Anthropic discusses task/trial/grader design; PagedAttention studies KV-cache management and serving throughput under explicit experimental settings. The curriculum therefore requires quality checks alongside performance claims. [Anthropic evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [PagedAttention](https://arxiv.org/abs/2309.06180)
