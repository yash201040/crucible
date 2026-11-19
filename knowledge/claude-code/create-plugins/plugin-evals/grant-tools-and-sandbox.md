---
type: "Feature"
title: "Granting tools to eval runs and the shell sandbox"
description: "Runs never prompt; only read-only tools plus --allow-tools grants exist, and any Bash grant requires an OS sandbox."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, permissions, sandbox, tools]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: "Sandbox backend (WSL2 on Windows; bubblewrap and socat on Linux) when granting Bash"
identifiers:
  - "--allow-tools"
  - "Bash(npm test *)"
  - "WebFetch(domain:example.com)"
  - "not granted"
  - "sandbox.enabled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs never stop to ask for permission. Built-in tools needing a grant you did not give (`Bash`, `Write`, `Edit`, `WebFetch`, `WebSearch`) are removed from the session. Read-only tools allowed when the case lists them in `allowed_tools`: `Read`, `Glob`, `Grep`, `NotebookRead`, `Skill`, `AskUserQuestion`, `Agent`, `TodoWrite`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate`, `TaskStop`. A tool a case asked for but was not granted is listed as `not granted` in progress output.

# How to use it

`claude plugin eval . --allow-tools Write Edit "Bash(npm test *)"`. The grant applies to every case in the run. Mocked MCP tools need no grant; real plugin MCP tools need the server started plus a grant by name. A case's `allowed_tools` and a skill's `allowed-tools` frontmatter cannot widen any grant.

# Limits and defaults

- Granting `Bash` in any form runs every command under the OS-level sandbox: writes confined to the run workspace, home directory and Claude Code configuration unreadable, network limited to domains granted via `--allow-tools "WebFetch(domain:example.com)"`. With no sandbox backend, each run is refused (a run error, usually score 0). Native Windows has none: use WSL2; on Linux install `bubblewrap` and `socat`.
- On a managed machine, a `sandbox` key in managed settings can cause the refusal. Error starts `A shell tool (Bash or PowerShell) was granted but this machine cannot confine it (no sandbox backend on this platform, or it is not installed)` and ends with `this machine's managed settings:` plus the key (e.g. `sandbox.enabled is false`); read it from the `NOTES` column or the JSON `error` field.
