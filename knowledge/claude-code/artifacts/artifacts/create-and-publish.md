---
type: "Feature"
title: "Create and publish an artifact"
description: "How Claude writes and publishes an artifact file, what opens, and the keys and variables that control reopening and auto-open."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, publish, auto-open]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Artifacts available (see availability)"
identifiers:
  - "Ctrl+]"
  - "CLAUDE_CODE_ARTIFACT_AUTO_OPEN"
  - "/artifacts"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Unless you name a location, Claude writes the page to an HTML or Markdown file in a temporary directory outside your project, then publishes it. The artifact stays private to you until you share it. After the first publish Claude prints the URL and your browser opens the page. Claude picks the title and a browser-tab icon; ask for a specific title or icon if wanted.

# How to use it

| Action | How |
| --- | --- |
| Reopen the session's most recent artifact | `Ctrl+]` |
| See this session's artifacts | A `⧉` pill below the prompt shows the name, or a count for several. In fullscreen rendering, click it to open the `/artifacts` list |
| Stop the browser opening | Set `CLAUDE_CODE_ARTIFACT_AUTO_OPEN=0` |

# Limits and defaults

- Remote Control: if the prompt was sent through Remote Control from claude.ai, Claude Desktop or the mobile app, no tab opens on the machine running the session. The browser opens there the next time Claude publishes from a prompt typed at the terminal.
- If Claude says it cannot publish, or writes a local HTML file without a link, artifacts are not enabled for the session. The terminal message `Artifacts need a claude.ai login` points to the errors page for sign-in.
