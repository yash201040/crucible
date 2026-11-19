---
type: "Feature"
title: "/auto-mode-setup command"
description: "Drafts autoMode.environment entries from your project and recent sessions and writes them to ~/.claude/settings.json."
resource: "https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries-with-auto-mode-setup"
tags: [auto-mode, slash-command, setup, classifier]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.228"
surfaces: [cli]
requires: "Pro, Max, Ultra, Team, Enterprise or Console API key; v2.1.228+ (v2.1.233+ native Windows) on Pro/Max/Ultra/Team; v2.1.283+ on Enterprise or Console key; v2.1.304+ where feature-flag fetching is off"
identifiers:
  - "/auto-mode-setup"
  - "skillOverrides"
  - "disableBundledSkills"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-config"
    resource: "https://code.claude.com/docs/en/auto-mode-config"
    title: "Configure auto mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/auto-mode-setup` scans in the background and shows a draft you accept or discard as a whole.

# How to use it

- Always reads: this project's `CLAUDE.md`, `README.md`, config files, git remotes; your `autoMode` and `permissions.allow`; hosts, buckets and command names from commands Claude ran in recent sessions (never your messages).
- Optional scans: first word of shell-history commands; remote hosts and names of repos under your home directory.
- If entries already exist it asks to add or replace. Accepting adds `"$defaults"` to lists it extends (unless you wrote an `allow` list without it) and offers to remove `permissions.allow` rules auto mode ignores (like `Bash(*)`).
- After repeated blocks with no `autoMode.environment`, a "Teach auto mode about your environment?" dialog offers it; choose Don't show again to stop the offer. To disable command and offer: `"skillOverrides": {"auto-mode-setup": "off"}` (`disableBundledSkills` does not turn it off, since it is a built-in command).

# Limits and defaults

- Cloud session: prints `/auto-mode-setup isn't available in this environment.`
- `Unknown command: /auto-mode-setup` causes: first session after install (start a new one), outdated version, or feature-flag fetching off before v2.1.304.
