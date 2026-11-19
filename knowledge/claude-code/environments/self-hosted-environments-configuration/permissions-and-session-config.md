---
type: "Concept"
title: "Permissions and per-session config assembly"
description: "How the runner builds each session's config from a host snapshot, pins permission mode, and handles repository settings and managed settings."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, permissions, config, auto-mode, managed-settings]
kind: "mixed"
maturity: "beta"
since: "2.1.229"
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise)"
identifiers:
  - "--permission-mode auto"
  - "--allowed-tools"
  - "--disallowed-tools"
  - "SELF_HOSTED_RUNNER_HOST_CONFIG_DIR"
  - "forceRemoteSettingsRefresh"
  - "managed-settings.json"
  - "disableAllHooks"
  - "allowManagedHooksOnly"
  - "--confine-repo-settings"
  - "--trust-workspace"
  - "defaultMode"
  - "CLAUDE_PROJECT_DIR"
  - "enabledPlugins"
  - "extraKnownMarketplaces"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A self-hosted session has no terminal, so an unanswered permission prompt stalls the turn until the user answers in the UI. The control plane sends the tool list and permission rules; the default pre-approves routine tool calls including `Bash`, and cloud sessions pre-approve file edits in every mode.

# How to use it

- Pin auto mode from a wrapper or `command` hook: `exec "$CLAUDE_RUNNER_CLAUDE_BIN" "$@" --permission-mode auto` (last flag wins). It applies only until a client sets a mode. Do this only with default-deny network egress and the hardening section in place. A classifier model reviews actions in auto mode; ask rules still prompt and deny rules always block.
- Pre-approve with `--allowed-tools "Bash(bazel *) Bash(yarn *) mcp__internal__*"` after `"$@"`; list flags accumulate; `--disallowed-tools` denies.
- Config assembly: each session gets its own config dir seeded from a snapshot of the host `~/.claude/` taken once at startup (`settings.json`, `CLAUDE.md`, hooks, agents, commands, skills); restart the runner to apply changes. `SELF_HOSTED_RUNNER_HOST_CONFIG_DIR` changes the source; `projects/` is left out. Managed settings are read from the standard system path in the image.
- Control-plane-supplied Claude Code hooks (v2.1.229+) are installed alongside yours under `hooks/.ccr-launcher/` and a separate `--settings` file; they run `python3` (install it in the image); `disableAllHooks` stops them.
- Account skills are downloaded for a person's own sessions but not for scheduled task runs or Bedrock/Agent Platform sessions. Auto memory is off by default outside Claude Tag sessions; use `CLAUDE.md`.
- `forceRemoteSettingsRefresh: true` in the image's `managed-settings.json` stops sessions that fail to fetch server-managed settings (error `Your organization requires remote managed settings to load, but they could not be loaded.`). Leave it out for Claude Tag channel environments (the API refuses their fetch).

# Limits and defaults

- Multi-repo sessions: with `--capacity 1` and the built-in checkout, the session starts in the first repository and only its `.claude/settings.json` and `.mcp.json` apply; with higher capacity or a `checkout` hook, none apply and `$CLAUDE_PROJECT_DIR` is the per-session directory. In a project thread no repository settings, `.mcp.json` or skills load. Each repo's `CLAUDE.md` always loads; `enabledPlugins` and `extraKnownMarketplaces` are read from each repo.
- Do not commit a bare `Edit`, `Write` or `NotebookEdit` in a repository `permissions.allow`; the write-scope confine guard flags it, and `--confine-repo-settings enforce` refuses the session. Scope to `Edit(/**)`.
- `defaultMode` of `auto` is honored only from image-wide or user-level settings.
