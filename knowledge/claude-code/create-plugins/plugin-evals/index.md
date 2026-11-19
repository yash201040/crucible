# create-plugins/plugin-evals

* [No-plugin baseline and ablation scoring](baseline-and-ablation-scoring.md) - With-arm versus without-arm runs, when only one arm runs, and which graders are excluded from the score. **[high]**
* [case.yaml fields and workspace seeding](case-yaml-fields.md) - case.yaml adds scaffold scripts, history transcripts and read-only directories, and can hold a whole case. **[high]**
* [claude plugin eval options and targets](command-options.md) - Targets and flags for run count, concurrency, models, threshold, cost ceiling, grants, mocks and output. **[high]**
* [Create and run your first eval suite](create-first-eval-suite.md) - Walkthrough: eval init, run claude plugin eval ., read the summary table and report, iterate with one arm. **[high]**
* [Using a different eval directory](custom-eval-directory.md) - Move the suite from evals/ with the experimental.evals manifest key or --eval-dir.
* [Eval results: HTML report and JSON](eval-results-report-and-json.md) - results/<timestamp>/ contents, the self-contained HTML report, optional artifact publishing, and the aggregate-result.json fields. **[high]**
* [What an eval run can access: trust and isolation](eval-trust-and-isolation.md) - Trust prompt, flag-gated capabilities, and the isolation model: temp home, no personal config, hidden case files. **[high]**
* [Grader types, options and targets](grader-types.md) - The six grader types (regex, tool_used, tool_order, file_exists, llm, baseline), common keys and what a grader can look at. **[high]**
* [Granting tools to eval runs and the shell sandbox](grant-tools-and-sandbox.md) - Runs never prompt; only read-only tools plus --allow-tools grants exist, and any Bash grant requires an OS sandbox. **[high]**
* [How an eval run works and is scored](how-an-eval-run-works.md) - Isolated non-interactive sessions per run, three runs per case by default, scoring, threshold and cost shape. **[high]**
* [Mocking MCP servers in evals](mock-mcp-servers.md) - Per-tool mock files answer MCP calls so skills can be evaluated without the real service; fixed or agent-answered. **[high]**
* [claude plugin eval overview and requirements](plugin-eval-overview.md) - A shell command that runs a plugin against test cases with graders, scored with and without the plugin. **[high]**
* [Plugin eval troubleshooting](plugin-eval-troubleshooting.md) - Errors and symptoms of claude plugin eval: trust, old git, missing baseline, zero scores, API errors, mock budget, timeouts. **[high]**
* [prompt.md frontmatter fields](prompt-md-frontmatter.md) - Every frontmatter field of an eval case's prompt.md with defaults; an unknown key is an error. **[high]**
* [Run evals in CI and exit codes](run-evals-in-ci.md) - A recommended CI invocation with pinned models and a cost ceiling, and the meaning of exit codes 0, 1, 2, 130 and 143. **[high]**
* [Writing eval cases and graders by hand](write-eval-cases.md) - Case directory layout, a manual prompt.md plus two graders, and habits that keep scores stable. **[high]**
