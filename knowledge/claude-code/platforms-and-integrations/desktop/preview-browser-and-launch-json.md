---
type: "Feature"
title: "App preview, Browser pane and launch.json"
description: "Claude starts dev servers in the Browser pane, auto-verifies edits, browses external sites with approvals, and is configured via .claude/launch.json."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, preview, browser, launch-json, auto-verify]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Local session for full Browser tools; SSH sessions lack the pane's tools"
identifiers:
  - ".claude/launch.json"
  - "autoVerify"
  - "runtimeExecutable"
  - "runtimeArgs"
  - "port"
  - "autoPort"
  - "program"
  - "args"
  - "url"
  - "cwd"
  - "env"
  - "name"
  - "PORT"
  - "browserExternalPageTools"
  - "disableBrowserExternalNavigation"
  - "disableRemotePreviewScripts"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude can start a dev server (frontend or backend) and open it in the Browser pane, take screenshots, inspect the DOM, click, fill forms, test API endpoints and read server logs. **Auto-verify** is on by default and checks changes after every edit. The pane is a tabbed browser (Cmd/Ctrl+Shift+B) with a clean profile; for logged-in sessions use the Claude in Chrome extension instead.

# How to use it

`.claude/launch.json` (JSON with comments) is created automatically at the root of the selected folder. Disable auto-verify with `"autoVerify": false` or the Browser pane's **Auto-verify changes** menu item.

| Field | Type | Meaning |
| - | - | - |
| `name` | string | Unique server name |
| `runtimeExecutable` + `runtimeArgs` | string, string[] | Command via package manager, e.g. `npm` `["run","dev"]` |
| `program` + `args` | string, string[] | Script run with `node` |
| `port` | number | Default 3000 |
| `cwd` | string | Relative to project root; `${workspaceFolder}` allowed |
| `env` | object | Extra variables; no secrets (file is committed) |
| `autoPort` | boolean | `true` find free port; `false` fail; unset = next free port except hardcoded-script cases |
| `url` | string | Address to open instead of `http://localhost:<port>`; localhost URL must be origin only and match `port`; alone (no command) attaches to a server you already run |

Servers should read the `PORT` environment variable; Claude rewrites `--port` or `-p` in `runtimeArgs` when moving ports. Top-level `"version": "0.0.1"`.

# Limits and defaults

- SSH sessions: no Browser tools, no auto-verify, no Dev servers menu; HTML previews of files work in SSH/WSL sessions (scripts run, web content does not load unless exported).
- External sites: classifiers review writes in Auto-capable sessions; other modes use a domain allowlist and a permission card (Allow once / Always allow / Deny). Claude will not purchase, create accounts or bypass CAPTCHAs without you.
- Managed keys: `browserExternalPageTools: "disabled"`, `disableBrowserExternalNavigation: true`, `disableRemotePreviewScripts: true` (v5.1231.0+). Values must be JSON booleans.
- Setting `autoPort` unset before Desktop v2.37337.0 prompts instead.
