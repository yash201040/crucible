---
type: "Concept"
title: "What an eval run can access: trust and isolation"
description: "Trust prompt, flag-gated capabilities, and the isolation model: temp home, no personal config, hidden case files."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, security, isolation, trust]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "--trust-plugin"
  - "Trust this plugin directory?"
  - "--scaffold"
  - "--allow-tools"
  - "--allow-real-servers"
  - "--mocks off"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin eval` loads the target plugin's skills, hooks and agents and runs its suite on your machine as you. It is the same trust decision as `claude --plugin-dir`: only evaluate plugins you trust. The isolation limits what the agent under test reaches; it is not a boundary against the plugin's own code, and passing says nothing about safety.

# How to use it

Trust: the first run against a directory asks `Trust this plugin directory?` unless already accepted in an interactive session; in a git repository, yes trusts the whole repository (interactive sessions too). When stdin or stdout is not a terminal, or under `--json`, the run cannot ask and is refused with exit 1; pass `--trust-plugin`. A named installed or skills-directory plugin skips the prompt.

Flag-gated parts (per run): `scaffold_script` with `--scaffold`; tools beyond read-only with `--allow-tools`; real MCP servers with `--allow-real-servers` or `--mocks off`. A case's `allowed_tools` or a skill's `allowed-tools` cannot widen them.

# Limits and defaults

Isolation: each run gets a temporary home, working directory and Claude Code configuration, as a `claude -p` child with only the plugin loaded.
- Nothing personal or project-level loads: user settings, hooks, CLAUDE.md, MCP servers, other plugins, memory, skills. No `.claude/`, `CLAUDE.md` or `.mcp.json` loads from the workspace, even one a scaffold wrote; `add_dirs` grant read access only. Only an allowlist and `EVAL_*` variables reach the run.
- Managed policy settings still apply inside a run.
- The Artifact tool is off; skills that publish an artifact are graded only on output before that step.
- The eval directory is unreadable to the agent (prompt, graders, sibling cases hidden).
- No network sandbox outside shell commands: a `WebFetch(domain:...)` grant reaches that domain directly, and plugin hooks and real MCP servers can reach any host.
- If the plugin has hooks you did not write, or you start real MCP servers, treat scores as advisory unless in an isolated container or CI runner, since they run outside the sandbox and could modify files graders read.
