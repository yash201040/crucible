---
type: "Guide"
title: "Open a deep link from a shell or runbook"
description: "Per-OS commands to open a claude-cli:// link from scripts, and notes on embedding links in runbooks and GitHub Markdown."
resource: "https://code.claude.com/docs/en/deep-links"
tags: [deep-links, shell, runbook, automation]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Handler registered on the machine"
identifiers:
  - "open"
  - "xdg-open"
  - "Start-Process"
  - "start"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "deep-links"
    resource: "https://code.claude.com/docs/en/deep-links"
    title: "Launch sessions from links"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A script, alias or automation can open a deep link by calling the OS URL opener; it relies on the registered handler and opens a new terminal window with the prompt pre-filled (still needing Enter).

# How to use it

| OS | Command |
| --- | --- |
| macOS | `open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"` |
| Linux | `xdg-open "claude-cli://open?repo=acme/payments&q=review%20open%20PRs"` (from the `xdg-utils` package) |
| Windows PowerShell | `Start-Process "claude-cli://open?..."` |
| Windows cmd.exe | `start "" "claude-cli://open?..."` (empty title first, since `start` treats the first quoted argument as a title) |

Runbook use: a Markdown link `[label](claude-cli://open?repo=...&q=...)` in an incident runbook, alert or dashboard; encode the prompt with `encodeURIComponent`. Machines need the handler registered and the clone seen.

# Notes

GitHub-rendered Markdown (README, issues, PRs, wikis) strips non-http(s) schemes, showing only the label. Put the link in a code block so readers can paste it into a browser address bar. To run Claude without a terminal window, the docs point to non-interactive mode (`-p`).
