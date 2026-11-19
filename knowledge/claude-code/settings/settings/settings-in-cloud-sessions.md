---
type: "Reference"
title: "Settings in cloud sessions"
description: "Which settings files a cloud session reads: project threads read none; single-repo sessions read shared project; user, local and device managed files are not read."
resource: "https://code.claude.com/docs/en/settings"
tags: [settings, cloud, managed-settings, environments]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud, web]
requires: ""
identifiers:
  - "enabledPlugins"
  - "extraKnownMarketplaces"
  - ".claude/settings.json"
  - "/config"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings"
    resource: "https://code.claude.com/docs/en/settings"
    title: "Settings files and precedence"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A cloud session runs in a cloud environment on a fresh clone, not on your machine, so fewer settings reach it.

# How to use it

| Source | In a cloud session |
| :- | :- |
| Cloud threads in a project | none of a repo's `.claude/settings.json` permission rules, hooks or `env` apply, however many repos |
| Shared project `.claude/settings.json`, one repo outside project threads | read (part of the clone); commit a setting there to apply it |
| Shared project, several repos (Anthropic-hosted) | session starts above the clones; reads only `enabledPlugins` and `extraKnownMarketplaces` from each repo's file, not permission rules, hooks, `env` or other keys; those plugins still do not load in cloud sessions. Self-hosted environments have their own rule |
| User `~/.claude/settings.json` and project local | not read |
| Managed file or MDM profile on your device | does not reach; server-managed settings do (surface coverage lists which cloud sessions); a self-hosted environment also reads the managed file in its runner image |
| `/config` | in the browser at claude.ai/code opens your claude.ai settings page instead; set an environment variable on the cloud environment, or commit the key to the repo's `.claude/settings.json` (single repo, outside project threads) |

# Notes

Other items (CLAUDE.md, skills, MCP servers, plugins, credentials) are listed on the cloud environments page.
