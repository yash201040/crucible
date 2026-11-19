---
type: "Feature"
title: "Pre-approving tools for a skill"
description: "allowed-tools grants permission for one turn; disallowed-tools removes tools; managed policies can ignore the grant."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, permissions, allowed-tools, managed-settings]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.282"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "allowed-tools"
  - "disallowed-tools"
  - "allowManagedPermissionRulesOnly"
  - "strictPluginOnlyCustomization"
  - "/status"
  - "-p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`allowed-tools` lets Claude use listed tools without prompting during the turn that invokes the skill. The grant clears on your next message (re-invoking re-applies it). It does not restrict tools: every tool stays callable and permission settings still govern unlisted tools. For whole-session approval use allow rules in permission settings.

# How to use it

`allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)`. To remove tools while a skill is active use `disallowed-tools` (also cleared on next message; cannot remove `EndConversation` while any other tool remains). To block tools everywhere use deny rules.

# Limits and defaults

- A project skill's `allowed-tools` applies even in a `-p` run in a folder you never trusted, so review skills in repos before running there.
- If managed settings list `hooks` in `strictPluginOnlyCustomization`, a personal or project skill whose frontmatter declares `hooks` loses its `allowed-tools` pre-approval (check `/status` for `Enterprise managed settings`; fix by removing `hooks` or moving the skill into a plugin).
- If managed settings set `allowManagedPermissionRulesOnly` (v2.1.282 or later), `allowed-tools` in project and personal skills and other listed sources is ignored; their tools go through managed rules and the normal prompt. `/status` lists skills whose `allowed-tools` were ignored.
