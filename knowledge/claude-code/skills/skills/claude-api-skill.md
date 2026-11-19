---
type: "Reference"
title: "/claude-api skill subcommands"
description: "The bundled /claude-api skill and its subcommands (migrate, upgrade, cost-optimize, build-eval, hillclimb and more) with minimum versions."
resource: "https://code.claude.com/docs/en/skills"
tags: [claude-api, subcommands, migration, evals]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "managed-agents-secure needs the ant CLI"
identifiers:
  - "/claude-api"
  - "/claude-api migrate"
  - "/claude-api upgrade"
  - "/claude-api api-version"
  - "/claude-api managed-agents-onboard"
  - "/claude-api managed-agents-secure"
  - "/claude-api prompt-audit"
  - "/claude-api cost-optimize"
  - "/claude-api latency-optimize"
  - "/claude-api build-eval"
  - "/claude-api hillclimb"
  - "/claude-api preserved-thinking-migration"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/claude-api` loads Claude API and Managed Agents reference material for your project's language. Claude activates it automatically when code imports `anthropic` or `@anthropic-ai/sdk`.

# How to use it

Type a subcommand after the name, for example `/claude-api migrate`. `migrate` and `managed-agents-onboard` predate v2.1.221, the oldest version the table tracks.

| Subcommand | What it does | Minimum version |
| :- | :- | :- |
| `migrate` | Update API code to a newer model | before v2.1.221 |
| `upgrade` | Upgrade the Anthropic SDK to a new major version and fix breaking changes | v2.1.236 |
| `api-version` | Update code for a newer API version and switch requests to it | v2.1.307 |
| `managed-agents-onboard` | Walk through creating a Managed Agent | before v2.1.221 |
| `managed-agents-onboard <url>` | Build the Managed Agent a page describes | v2.1.290 |
| `managed-agents-onboard <quickstart-name>` | Build a Console quickstart template such as `deep-researcher`; an unknown single word lists valid names | v2.1.290 |
| `managed-agents-secure [<agent-id>]` | Compare one Managed Agent's settings with the secure-deployment guide; needs the `ant` CLI | v2.1.304 |
| `prompt-audit` | Flag instructions written for older models in prompts, skills and tool descriptions; proposes a diff | v2.1.221 |
| `cost-optimize` | Profile API spend and propose savings (prompt caching, trimming tokens, batch, effort, model choice), one change at a time | v2.1.247 |
| `latency-optimize` | Find where time goes and propose reductions | v2.1.319 |
| `build-eval` | Build an eval set for a Claude-powered app | v2.1.259 |
| `hillclimb` | Iteratively improve the app against an existing eval | v2.1.259 |
| `preserved-thinking-migration` | Find edits that invalidate preserved thinking blocks, measure dropped reasoning, propose fixes one at a time | v2.1.282 |
