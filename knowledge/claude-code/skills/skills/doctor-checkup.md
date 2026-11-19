---
type: "Feature"
title: "/doctor setup checkup"
description: "/doctor diagnoses installation, extensions, CLAUDE.md, permissions and plan usage; /doctor prompt-audit checks instruction files."
resource: "https://code.claude.com/docs/en/skills"
tags: [doctor, diagnostics, usage, claude-md]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli]
requires: "Usage check: Pro, Max, Ultra, Team or Enterprise plan"
identifiers:
  - "/doctor"
  - "/doctor prompt-audit"
  - "claude doctor"
  - "checkup"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/doctor` is a bundled skill that runs a setup checkup. Claude reports findings first and asks for confirmation before changing anything. `checkup` is an alias.

# How to use it

Areas covered:

| Area | What it checks |
| :- | :- |
| Installation health | duplicate or leftover installs, `PATH` problems, unparseable settings files, newer version on your release channel |
| Extensions | unused skills, MCP servers and plugins versus context cost; slow hooks |
| `CLAUDE.md` files | local copies of checked-in files, derivable checked-in content, always-loaded guidance Claude offers to migrate to skills or nested `CLAUDE.md` |
| Permissions | offer to make auto mode the default mode and pre-approve frequently denied read-only commands |
| Usage | on Pro, Max, Ultra, Team or Enterprise: changes `/usage` recommends, measured over the last 7 days; needs v2.1.305 or later; left out while Remote Control is connected |

- `claude doctor` in a terminal gives read-only installation diagnostics without starting a session.
- `/doctor prompt-audit` audits `CLAUDE.md` files, skills and other configuration for outdated or conflicting instructions instead of running the checkup; requires v2.1.283 or later.

# Notes

`/doctor` also estimates the skill listing's context cost (see [skill listing budget](./skill-troubleshooting.md)).
