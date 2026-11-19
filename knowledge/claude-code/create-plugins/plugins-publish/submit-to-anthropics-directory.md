---
type: "Guide"
title: "Submit to Anthropic's directory"
description: "Submit a validated plugin from the developer portal on a paid claude.ai plan; it reaches Claude Code as <name>@synced."
resource: "https://code.claude.com/docs/en/plugins/publish"
tags: [plugins, directory, submission, claude-ai]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web, cli]
requires: "Paid claude.ai plan (Pro, Max, Ultra; Team or Enterprise Owner, or Enterprise Directory permission)"
identifiers:
  - "claude plugin validate ./your-plugin --strict"
  - "claude-plugins-official"
  - "<name>@synced"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-publish"
    resource: "https://code.claude.com/docs/en/plugins/publish"
    title: "Publish and distribute a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Anthropic's directory (claude.ai/directory) is the catalog on claude.ai and Cowork; one listing reaches claude.ai, Cowork and Claude Code. Submit at the developer portal claude.ai/directory/manage. The official marketplace `claude-plugins-official` does not take submissions through the portal; ask an Anthropic partner contact.

# How to use it

1. Confirm eligibility: a paid claude.ai plan. Pro, Max, Ultra submit from their own account; Team and Enterprise Owners can submit; on Enterprise an Owner can grant the **Directory** permission to other members via a custom role under **Organization settings > Roles**.
2. Validate locally with `claude plugin validate ./your-plugin --strict`. The portal applies extra directory rules the CLI does not check.
3. Check which components load where; some are Claude Code-only and do not load on claude.ai or Cowork.
4. Submit in the portal. Review, update and connector submission details are documented on claude.com.

# Notes

A person who installs from the directory has it on their account and Claude Code loads it as `<name>@synced`.
