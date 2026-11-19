---
type: "Reference"
title: "Subagent, fork and agent team variables"
description: "Variables for subagent concurrency, nesting depth, default model, built-in agent removal, fork mode, stall timeout and agent teams."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [subagents, limits, concurrency, agent-teams]
kind: "env_var"
maturity: "experimental"
since: "2.1.217"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS"
  - "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH"
  - "CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION"
  - "CLAUDE_CODE_SUBAGENT_MODEL"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS"
  - "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS"
  - "CLAUDE_CODE_FORK_SUBAGENT"
  - "CLAUDE_CODE_FORWARD_SUBAGENT_TEXT"
  - "CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS"
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Limits and defaults for subagents. Only `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` carries the docs' "experimental" label (agent teams, disabled by default); the rest are unlabelled.

# How to use it

| Variable | Default | What it does |
| :- | :- | :- |
| `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | 20 | Subagents running in one session before the Agent tool refuses another. Positive whole number, plain digits; anything else ignored, so it adjusts but cannot disable the cap. Requires v2.1.217+. |
| `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | 3 | Subagent layers below the main conversation; a third-layer subagent cannot spawn further; `1` turns nesting off. In v2.1.217-v2.1.218 the default was 1; v2.1.219 raised it to 3. Plain digits; cannot be removed. Requires v2.1.217+. |
| `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` | was 200 | Removed in v2.1.224, now a no-op. Spawning past the cap used to fail with `Subagent spawn limit reached`. Concurrent and depth limits still apply. |
| `CLAUDE_CODE_SUBAGENT_MODEL` | unset | Default model (alias like `haiku` or full name) for subagents, agent team teammates and workflow agents not assigned a model otherwise. A model Claude passes at spawn and an agent definition's `model` field (including `inherit`) take precedence. `inherit` equals unset. Before v2.1.251 it overrode both. |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` | off | `1` forces one model onto subagents, teammates and workflow agents. Requires v2.1.257+. |
| `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS` | off | `1` disables all built-in subagent types (Explore, Plan) in non-interactive mode (`-p`) only; also removes `general-purpose`, so an Agent call without `subagent_type` fails with `subagent_type is required`. |
| `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS` | off | `1` disables built-in Explore and Plan subagents; plan mode reads files directly. Custom subagents named `Explore` or `Plan` unaffected. Requires v2.1.198+. |
| `CLAUDE_CODE_FORK_SUBAGENT` | on | Fork mode lets Claude start forks itself; while on, Claude cannot wait for a subagent in interactive terminal, VS Code or desktop sessions on your machine. `0` turns it off. |
| `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` | off | `1` emits subagent text and thinking blocks in `claude -p --output-format stream-json`; same as `--forward-subagent-text`. Unlike the flag it is ignored (no error) outside that mode. Requires v2.1.211+. |
| `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` | 600000 | Stall timeout for subagents; also covers workflow agents from v2.1.286. If `CLAUDE_STREAM_IDLE_TIMEOUT_MS` is raised while the stream watchdog is on, the default rises with it. |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | off | `1` enables agent teams (experimental, disabled by default). |
