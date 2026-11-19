# Crucible domain failure-mode checklists

Critics, contract writers and debunkers: read the sections relevant to your scope. Each item is a check you **run**, not a question to ask. A claim only survives when every applicable check ran and passed; checks that could not run (no data, no access) are listed as such, never silently skipped. Compute, don't argue.

## 0. Any claim (always applies)
- [ ] Every number re-computed from its source or artifact; every quote found verbatim in the opened source (misquoting a real source is the common 2026 failure mode, not invented papers).
- [ ] The claim answers the pinned statement, not an easier, weaker or vacuous reading of it.
- [ ] Executable checks actually test the claim as stated (a passing test or Lean proof certifies only what it encodes).
- [ ] Evidence labels honest: "executed" really was run this session; "cited" really was opened.
- [ ] Claims stop where the evidence stops (no "therefore in general").
- [ ] No forbidden shortcut: edited/deleted tests, hardcoded outputs, reading answer keys, look-ahead data, solving a different problem.

## 1. Research and factual questions
- [ ] Primary source opened for each decisive claim; SEO/aggregator pages are leads only.
- [ ] Decisive, numeric, recent or disputed claims confirmed by a second source that does not derive from the first.
- [ ] Conflicts between sources reported, not silently resolved.
- [ ] Dates checked: "latest" claims verified against the current date; superseded versions flagged.
- [ ] Novelty claims: search for prior art under alternative names before calling anything new.

## 2. Quant research, algo trading, news-driven alpha
**Leakage / look-ahead**
- [ ] Point-in-time join audit: `feature_available_ts ≤ decision_ts − latency` for every feature; fundamentals by filing date (not period end); macro by vintage; index membership and corporate actions as-of each date.
- [ ] News timestamps: publication/receipt time in exchange timezone; headline edits/updates handled; trade at the next tradable price after receipt + embargo.
- [ ] LLM look-ahead: backtest window vs model training cutoff; placebo (shuffled dates) and entity-masking tests; pre- vs post-cutoff performance; prefer chronologically consistent models (Glasserman & Lin 2309.17322; ChronoBERT/ChronoGPT 2502.21206).
- [ ] Fit-on-train-only: scalers, PCA, winsorization bounds, universe filters, hyperparameters fit inside each fold (grep for `.fit(` on full data).
- [ ] Survivorship: delisted names with delisting returns included; membership as-of date.

**Validation protocol**
- [ ] Walk-forward or purged k-fold with embargo; plain k-fold on overlapping labels is a defect.
- [ ] One untouched final hold-out, opened once (log it).
- [ ] Trial count N logged. No N → cannot deflate → status unverified.

**Overfitting statistics**
- [ ] Deflated Sharpe Ratio vs expected max Sharpe of N skill-free trials (Bailey & López de Prado 2014).
- [ ] PBO via CSCV (Bailey, Borwein, López de Prado, Zhu 2015): promote only at PBO ≤ 0.05; 0.05–0.25 → human review; > 0.25 → reject.
- [ ] Multiple-testing hurdle: t > 3.0 (Harvey, Liu & Zhu 2016) plus BHY/Holm over the trials actually run.
- [ ] Permutation/placebo: shuffle signal timestamps vs returns; real Sharpe deep in the null tail.

**Execution realism**
- [ ] Costs: spread, commission, impact scaled to participation (e.g. square-root); rerun at 2× costs; report breakeven cost.
- [ ] Capacity (% ADV at target AUM), borrow availability/fees, halts, limit-up/down, auctions, realistic fills.
- [ ] Sub-period / regime stability, sector & size neutrality, turnover, plausible gross-to-net decay.
- [ ] Engine sanity: buy-and-hold reproduces benchmark; zero signal loses exactly costs; injected synthetic alpha is recovered.

## 3. RLVR environments, verifiers and reward design
- [ ] Hack-probe suite against the verifier: empty / format-only answer, answer without reasoning, multiple hedged answers, enumeration, hardcoded test outputs, editing/deleting tests, reading the answer key from disk, `sys.exit(0)` / monkeypatching the harness, LaTeX/format confusions. Each must score 0 (ImpossibleBench 2510.20270; EvilGenie 2511.21654).
- [ ] Verifier FP/FN audit by metamorphic testing: equivalent answer forms, near-miss wrong answers, adversarial formats; report FP/FN per category.
- [ ] Out-of-band held-out evaluation is mandatory; training reward is never evidence of correctness (accepted errors are undetectable from training observations alone).
- [ ] Instance enumeration vs rule learning: held-out instances never seen in training.
- [ ] Constraint satisfaction vs substance: answers address the request, not only the format constraints.
- [ ] Plant a known exploit and confirm the monitoring catches it.
- [ ] Data poisoning screen on training sets; isolate verifier environment from shared agent code/memory.
- [ ] Reward-curve sanity: reward up while held-out down, single-step reward jumps, length/format drift.

## 4. Code and data pipelines
- [ ] Fail-then-pass: each claimed fix has a test that fails on the parent and passes on the fix; the critic runs both.
- [ ] Hidden/held-out tests the solver never saw where possible.
- [ ] Test-tampering diff check: reject diffs touching tests, fixtures, CI config or thresholds unless the brief allows it.
- [ ] Mutation testing on changed lines (mutmut / cosmic-ray / PIT / Stryker); surviving mutants on critical logic are defects.
- [ ] Property-based invariants (Hypothesis): idempotence, round-trip, monotonicity, conservation (row counts, sums), order independence.
- [ ] Data contracts: schema, nulls, key uniqueness, referential integrity, ranges, freshness/lateness, row counts before/after each join, timezone/DST.
- [ ] Determinism: same input → identical output hash; partition rerun has no duplication; one-day backfill diffs clean.
- [ ] Golden-file diff on a fixed sample, each difference explained.
- [ ] End-to-end check the way a user would do it, beyond unit tests.

## 5. Product specs, designs and architecture decisions
- [ ] Every requirement in the spec traced to a component/decision; every component traced back to a requirement (no orphans either way).
- [ ] Explicit non-goals and assumptions; each assumption marked validated / to validate, with how.
- [ ] Failure modes and edge cases enumerated per component (scale, latency, cost, security, data loss, abuse).
- [ ] Alternatives considered with the reason each lost; the chosen option survives the strongest alternative's best argument.
- [ ] Cost and effort estimates grounded in comparable data, not vibes; uncertainty stated.
- [ ] A cheap experiment or prototype that would falsify the riskiest assumption is named.
