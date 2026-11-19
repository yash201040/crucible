# use-claude-code/best-practices

* [Choosing a permission mode and tuning auto mode](auto-mode-and-permission-mode.md) - Manual, bypassPermissions and auto mode tradeoffs, classifier block thresholds, and the autoMode settings block with $defaults. **[high]**
* [Connect the tools Claude needs](connect-tools-cli-mcp.md) - Prefer an existing CLI (e.g. gh) for external systems, use MCP when none exists, and trim idle MCP servers.
* [Deterministic vs non-deterministic instructions](deterministic-vs-non-deterministic.md) - Prompts, CLAUDE.md and skills are decided by the model; hooks, deny rules and managed settings are enforced by the harness. **[high]**
* [Enforce rules: hooks, permission rules, sandbox](enforce-with-hooks-permissions-sandbox.md) - Hook handler types, onFailure block, deny rules that hold in every mode, sandbox limits, and where a rule's scope lives. **[high]**
* [Give Claude a check: goal, review, Stop hook](give-claude-a-check.md) - Verification options from prompt to /goal to a Stop hook to /code-review, including the Stop-hook block cap of eight and its env var. **[high]**
* [Model and effort guidance](model-and-effort-guidance.md) - Defaults (Opus 5.5 at medium effort) and when to raise or lower effort, use max, ultrathink, Sonnet, Haiku or Fable. **[high]**
* [Prompting, CLAUDE.md, rules and skills guidance](prompting-and-claude-md-guidance.md) - Write down only what Claude cannot see in the repo; specific prompts, interview-to-SPEC.md, short CLAUDE.md, path-scoped rules, team skills.
* [Scheduling runs and parallel worktree sessions](scheduling-and-parallel-sessions.md) - /loop, /schedule cloud tasks, claude -w worktrees, .worktreeinclude, cleanup, /batch and claude agents (research preview). **[high]**
* [Steering and rewinding a session](steer-the-session.md) - Esc, /rewind, /clear, /btw, /rename and resume by name, plus the checkpoint limit for Bash-only changes.
* [What subagents cost and keeping context cost down](subagent-costs-and-context-costs.md) - Subagents cost tokens and sometimes time; use haiku, tool limits and /usage; /clear, /compact and the one-hour idle compaction note. **[high]**
* [Letting Claude run unattended and from scripts](unattended-runs-and-scripting.md) - Five-question readiness checklist, claude -p flags for scripts (--bare, dontAsk, max-turns), and auto mode behavior with -p. **[high]**
* [Advice current models made unnecessary](what-you-can-stop-doing.md) - Table of old prompting and context-management habits that newer models no longer need, with the reason.
