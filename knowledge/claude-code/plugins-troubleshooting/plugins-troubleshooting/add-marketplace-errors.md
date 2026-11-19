---
type: "Reference"
title: "Errors when adding or refreshing a marketplace"
description: "Messages, causes and fixes for failed marketplace adds and refreshes: source format, git credentials, timeouts, names, offline and GHES."
resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
tags: [plugins, troubleshooting, marketplace, git, errors]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS"
  - "CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE"
  - "CLAUDE_CODE_PLUGIN_PREFER_HTTPS"
  - "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL"
  - "CLAUDE_CODE_PLUGIN_SEED_DIR"
  - "GIT_ASKPASS"
  - "--sparse"
  - "--claudeai"
  - "Invalid marketplace source format"
  - "Invalid git URL"
  - "Git clone timed out after 120s"
  - "SSH authentication failed"
  - "HTTPS authentication failed"
  - "SSH host key is not in your known_hosts file"
  - "SSH host key has changed"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-troubleshooting"
    resource: "https://code.claude.com/docs/en/plugins/troubleshooting"
    title: "Troubleshoot plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Error entries for adding a marketplace (or a later refresh failing).

# How to use it

| Message | Cause / fix |
|---|---|
| `Marketplace "claude-plugins-official" not found` | official marketplace not registered (VS Code-only use, policy block, `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL`, retry wait); `claude plugin` shell commands never register it; run `/plugin marketplace add anthropics/claude-plugins-official` |
| `Marketplace "<name>" not found` | not added; names starting `claudeai-` are claude.ai marketplaces: `claude plugin marketplace add --claudeai <name>`; ask the sender for the source; `/plugin install <source>` form reports this instead of installing |
| `Invalid marketplace source format` / `That isn't a marketplace source` | accepted forms: GitHub `owner/repo`, `https://`/`http://` URL, `user@host:path` SSH, local path starting `./`, `../`, `/`, `~` |
| `'<source>' is not a valid GitHub owner/repo shorthand` | shorthand is GitHub-only; use full clone URL, `https://` marketplace.json URL or local path |
| `Invalid git URL` | unsupported protocol or ambiguous address; rewrite as the message says |
| `Path does not exist: <path>` / `File path must point to a .json file (marketplace.json)` | accepts a directory with `.claude-plugin/marketplace.json` or a `.json` file |
| `Marketplace file not found at <path>/.claude-plugin/marketplace.json` | no file at expected location |
| `Cannot add marketplace "<name>": Claude Code cannot install plugins from a marketplace with this name` | name must use a-z A-Z digits `.` `_` `-` and start with letter or digit; before v2.1.295 such adds were reported successful |
| `... Claude Code reserves this name ...` | names like `constructor`, `toString`, `valueOf`; before v2.1.296 it was an internal error |
| `SSH authentication failed` / `HTTPS authentication failed` (`Failed to clone marketplace repository:`) | git prompts and askpass (including `GIT_ASKPASS`) are disabled, SSH batch mode: `ssh -T git@<host>` must work without a prompt, host in `known_hosts`; HTTPS needs a stored helper credential (`gh auth login`, `gh auth setup-git`); test with `git -c core.askPass= ls-remote <url>`; `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` skips SSH for GitHub shorthand |
| `SSH host key is not in your known_hosts file` / `SSH host key has changed` | clone uses `StrictHostKeyChecking=yes`; run `ssh -T git@github.com` once or `ssh-keygen -R <host>` |
| `Command 'git' not found or is in an unsafe location` (Windows) | install Git for Windows so it is on PATH; a `git` only in the current directory is refused |
| `Git clone timed out after 120s` | default 120 s; raise `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` (e.g. `300000`); monorepos: `claude plugin marketplace add <source> --sparse <paths>`; v2.1.295+ fetches only submodules holding plugin files |
| Offline refresh keeps failing | `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1` skips re-clone (only if the checkout has `.claude-plugin/marketplace.json`); for fully offline use `CLAUDE_CODE_PLUGIN_SEED_DIR` |
| GitHub Enterprise Server add fails | policy error needs admin `hostPattern`; claude.ai GitHub access error needs a connected GHES account |

# Notes

`Marketplace "<name>" not found` and the install-line form are covered further in install-errors.
