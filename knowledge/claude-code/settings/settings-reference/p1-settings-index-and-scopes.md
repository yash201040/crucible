---
type: "Concept"
title: "Settings reference: scopes and index"
description: "How the settings reference is organized: each key has a scope (User, Project, Local, Managed, Any file, Global config) listed in a full key index."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, scopes, managed-settings, index]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "managed-settings.json"
  - "~/.claude.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The page lists every key Claude Code reads from a settings file, plus the short group of keys it keeps in `~/.claude.json` instead. It opens with an index table (Key, Description, Topic, Scope) and then has one section per topic, each key with scope, type, default, per-session overrides and a paste-ready JSON example.

# How to use it

Scope values used in the index:

| Scope | Meaning |
| :- | :- |
| `User` | `~/.claude/settings.json` |
| `Project` | `.claude/settings.json` |
| `Local` | `.claude/settings.local.json` |
| `Managed` | what the organization deploys (managed settings) |
| `Any file` | all four of the above |
| `Global config` | `~/.claude.json` |
| `User or managed`, `User, local, or managed` | only those files (plus `--settings` for some); a repository cannot set the key |

Topics in the index: Model and responses, Permission settings, Sandbox settings, Memory and context, Agents sessions and worktrees, Remote desktop and notifications, MCP, Plugins and skills, Hooks and automation, Authentication and providers, Enterprise and managed settings, Updates and versioning, Privacy and telemetry, Git and attribution, Interface and terminal, Tools, Global config settings.

# Notes

- Keys with scope `Managed` are ignored (with a warning) in user, project and local settings and in `--settings`.
- This part of the page covers the Model, Permission, Sandbox and Memory sections; the other topics appear here only as index rows (see the `p1-index-*` concepts).
- For choosing a file and precedence see the separate "Settings files and precedence" page.
