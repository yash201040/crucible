# usage-and-costs/costs

* [Agent team token costs](agent-team-token-costs.md) - Agent teams run several Claude Code instances, so tokens scale with team size; tips and the roughly 7x figure in plan mode. **[high]**
* [Background token use and long-session growth](background-and-long-session-usage.md) - Idle-time token consumers (recap, suggestions, loops, goal check-ins, cross-session messages) and why long sessions use more of the plan. **[high]**
* [Cloud provider cost attribution](cloud-provider-cost-attribution.md) - On Bedrock, Google Cloud's Agent Platform and Foundry billing is on the cloud account; per-user attribution via OpenTelemetry or gateways.
* [Console workspace and rate limit recommendations](console-workspace-and-rate-limits.md) - The auto-created Claude Code workspace on the Console and recommended per-user TPM and RPM by team size.
* [Reduce tokens: context, model and prompts](context-and-model-savings.md) - Habits that cut token use: clear between tasks, custom compaction, Sonnet over Opus, specific prompts, plan mode, checkpoints. **[high]**
* [Reduce tokens: thinking and subagents](extended-thinking-and-subagent-cost.md) - Lower extended-thinking cost with effort levels or MAX_THINKING_TOKENS, and delegate verbose work to cheaper subagents. **[high]**
* [/insights usage report](insights-report.md) - /insights analyzes up to 200 recent sessions and writes an HTML report on how you work, to ~/.claude/usage-data/report.html.
* [Which limit a developer hit](limit-messages-admin-triage.md) - How to tell session/weekly seat limits, usage-credit spend limits, gateway caps and context warnings apart, with remedies. **[high]**
* [Reduce tokens: MCP, plugins, hooks, skills](mcp-plugins-skills-overhead.md) - Cut context use by deferring MCP tools, preferring CLI tools, using code intelligence plugins, hooks that filter output, and skills. **[high]**
* [Plan usage breakdown and recommendations](plan-usage-breakdown.md) - On subscription plans /usage attributes usage to skills, subagents, plugins and MCP servers, recommends changes, and lists heavy loops. **[high]**
* [Prompt cache statistics line](prompt-cache-statistics.md) - A Prompt cache (main) line in the /usage Session block reporting cache hit share, misses, expected rebuilds and warm/cold state. **[high]**
* [Report spend at contracted rates](report-spend-at-contracted-rates.md) - Set the modelPricing managed setting so cost figures in /usage, the status line and OpenTelemetry match contracted rates. **[high]**
* [Where to see and cap spend by setup](spend-controls-by-setup.md) - Table mapping Teams/Enterprise, Console and cloud-provider setups to spend visibility, caps and per-user reporting. **[high]**
* [Token count beside the spinner](spinner-token-count.md) - The live approximate output-token count shown next to the working spinner, what it covers and when it resets.
* [Teams and Enterprise allowance and spend caps](teams-enterprise-spend-controls.md) - Per-seat usage windows, spend report, usage credits and limits, and the Enterprise Analytics API for Claude for Teams and Enterprise.
* [/usage session cost block](usage-command-session-cost.md) - The /usage Session block shows locally computed token usage and estimated dollar cost for the current session. **[high]**
* [Usage credits row and usage-request failures](usage-credits-spend-and-failures.md) - The /usage usage-credits row, the /usage-credits command by role, and how /usage behaves when the usage request is rate limited.
* [Fix shortcut in /usage](usage-fix-shortcut.md) - Pressing f in /usage runs recommended /effort commands and prompts Claude to apply other recommendations.
