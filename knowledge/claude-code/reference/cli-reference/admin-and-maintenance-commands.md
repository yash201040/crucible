---
type: "Reference"
title: "Admin, review, import and maintenance commands"
description: "Subcommands for the gateway, remote control, self-hosted runner, auto mode, ultrareview, import, purge, plugins and doctor."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [gateway, remote-control, self-hosted, ultrareview, auto-mode]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude gateway"
  - "--config"
  - "claude auto-mode defaults"
  - "claude auto-mode config"
  - "claude auto-mode reset"
  - "--label"
  - "claude doctor"
  - "claude import [source]"
  - "claude plugin"
  - "claude plugins"
  - "claude purge [path]"
  - "claude remote-control"
  - "claude rc"
  - "claude self-hosted-runner"
  - "claude ultrareview [target]"
  - "--timeout"
  - "--post"
  - "--no-post"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Non-session subcommands for administrators and for maintenance, review and configuration tasks.

# How to use it

| Command | What it does | Version / limits |
| :- | :- | :- |
| `claude gateway --config gateway.yaml` | Start the self-hosted Claude apps gateway for SSO and policy in front of Claude Code on Bedrock, Google Cloud's Agent Platform or Microsoft Foundry; `--config` is required | |
| `claude auto-mode defaults` | Print built-in auto mode classifier rules as JSON; `--label <prefix>` filters case-insensitively. `claude auto-mode config` shows rules with your settings applied | v2.1.208+ |
| `claude auto-mode reset` | Remove the `autoMode` section from the user settings file; asks to confirm, `-y`/`--yes` skips. Managed settings and `--settings` rules still apply | v2.1.212+ |
| `claude doctor` | Read-only install and settings diagnostics without starting a session (install health, settings validation errors, Remote Control eligibility). In-session `/doctor` can apply fixes | |
| `claude import [source]` | Start an interactive session running `/import` to bring in config from other agents; accepts `--dry-run` and `--yes`. Not available on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, Claude Platform on AWS, or with feature-flag fetching off | v2.1.213+ |
| `claude plugin` (alias `claude plugins`) | Manage plugins | |
| `claude purge [path]` | Delete all local state for a project: transcripts, task lists, debug logs, file-edit history, prompt history lines, and its entry in `~/.claude.json`. Flags `--dry-run`, `-y`/`--yes`, `-i`/`--interactive`, `--all` | |
| `claude remote-control` (alias `claude rc`) | Start a Remote Control server (server mode, no local interactive session) | |
| `claude self-hosted-runner` | Register this machine or container with a self-hosted environment to host cloud sessions; subcommands `setup`, `doctor`, `orchestrator` (spawns on-demand runners) | v2.1.224+ |
| `claude ultrareview [target]` | Run ultrareview non-interactively; prints findings to stdout, exit 0 on success and 1 on failure. `--json` raw payload, `--timeout <minutes>` overrides the 45-minute default, `--post` posts findings to a github.com PR as one comment (`--no-post` is the default) | `--post`/`--no-post` v2.1.227+ |
