---
type: "Release Digest"
title: "Apps, UI and other, 2.1.296 to 2.1.328"
description: "Release-note changes to VS Code, Desktop, cloud sessions, Remote Control, Claude Tag, Code Review, Chrome and terminal UI between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [vscode, desktop, cloud-sessions, claude-tag, code-review, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [ide, desktop, web, cloud]
requires: ""
identifiers:
  - "/code-review"
  - "/simplify"
  - "/bug"
  - "/chrome"
  - "/install-github-app"
  - "/ide"
  - "/design-sync"
  - "/design-login"
  - "/voice"
  - "/diff"
  - "/schedule"
  - "/ultrareview"
  - "@claude review"
  - "@claude review stop"
  - "Claude Tag"
  - "Code Mode"
  - "claudeCode.promptSuggestions"
  - "claudeCode.attachSelection"
  - "claudeCode.toggleDictation"
  - "claude-vscode.toggleDictation"
  - "Compliance API"
  - "OSC 7501"
  - "Ctrl+O"
  - "/remote-control"
  - "claude remote-control"
  - "/artifacts"
  - "/stickers"
  - "/powerup"
  - "/scroll-speed"
  - "/autocompact"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | /code-review on most models reports only bugs and CLAUDE.md violations, marks findings Important, Pre-existing or Nit and ends with a suggested fix; /simplify handles reuse and efficiency cleanups. | `/code-review`, `/simplify` |
| 2.1.328 | 2026-11-19 | /bug asks Yes or No before sending; computer use approval dialog shows each app's access level. | `/bug` |
| 2.1.328 | 2026-11-19 | VS Code notice when a message from another session is held, linking to the settings file that can allow it. | |
| 2.1.327 | 2026-11-17 | VS Code adds Claude Code: Add to Chat to the Explorer right-click menu; /install-github-app confirms before changing a repository; Chrome refuses uploading some credential files. | `/install-github-app` |
| 2.1.326 | 2026-11-16 | Added Ctrl+O to show hidden startup notices; VS Code claudeCode.promptSuggestions setting turns prompt suggestions off; /usage in fullscreen shows plan limit bars first. | `Ctrl+O`, `claudeCode.promptSuggestions` |
| 2.1.326 | 2026-11-16 | Program Status Protocol (OSC 7501) reports list background commands, monitors and MCP tasks and show a waiting session as working; Remote Control replies stream to the phone or browser as written. | `OSC 7501` |
| 2.1.325 | 2026-11-13 | VS Code prompt suggestions with Tab to accept, off via promptSuggestionEnabled false; Console sign-in that creates no API key. | `promptSuggestionEnabled` |
| 2.1.325 | 2026-11-13 | Remote Control /resume and /teleport disconnect first when the connected session has a share link; Claude Tag artifact link card fix. | |
| 2.1.323 | 2026-11-12 | Claude Tag sessions started in Slack added to the Compliance API on Enterprise plans, in beta; Code Review admin CSV export of review costs by repository and period. | `Compliance API` |
| 2.1.323 | 2026-11-12 | VS Code shows live output of a running Bash or PowerShell command and a trust prompt before the first session in an untrusted folder; cloud sessions got scheduled-task failure notification and a No repository option for self-hosted environments. | |
| 2.1.323 | 2026-11-12 | /stickers says the pack is all claimed; claude.ai chats and Cowork tasks scan a plugin file for secret keys before sending. | `/stickers` |
| 2.1.321 | 2026-11-09 | "Upgrade to Max or Ultra" wording; /model picker puts More models below every other row; VS Code warns when both an auth token and an API key are set. | |
| 2.1.319 | 2026-11-06 | Claude Tag admin Models row; Code Review: unlinking a GitHub organization also turns off its All repositories setting. | |
| 2.1.318 | 2026-11-04 | Cloud sessions: No repository option on Anthropic-hosted environments; Chrome names for the built-in Chromium. | |
| 2.1.317 | 2026-11-03 | Cloud sessions link card and /schedule warning for unrequested connectors; check before a web or shell call sends the account email to the network; /design-sync stops early when the design system moved. | `/schedule`, `/design-sync` |
| 2.1.316 | 2026-10-31 | VS Code: sign-in to a Claude apps gateway from the chat panel; ultrathink at xhigh effort in VS Code; Code Review findings-by-severity card; cloud sessions form card. | |
| 2.1.314 | 2026-10-30 | Cloud sessions from web, desktop and mobile start even when a setup script exits with an error; Include completed button on Scheduled tasks page. | |
| 2.1.312 | 2026-10-27 | Cloud routine model picker gains effort level; click to send a queued message in fullscreen. | |
| 2.1.311 | 2026-10-26 | Claude Tag Skills analytics view; VS Code code-block syntax coloring; Code Review retries a review whose session fails to start once. | |
| 2.1.310 | 2026-10-23 | Cloud sessions and Remote Control permissions added to Enterprise custom roles; Code Review admin Try again banner. | |
| 2.1.307 | 2026-10-21 | Code Review: @claude review stop (also off, pause) ends an @claude review always subscription; VS Code dictation stop notice. | `@claude review stop` |
| 2.1.304 | 2026-10-19 | Code Review levels Quick, Standard (default) and Deep per organization or repository; option to review every repository of a GitHub organization; VS Code draws mods on Bedrock, Vertex, Foundry, gateways and telemetry-off sessions. | |
| 2.1.302 | 2026-10-16 | /design-sync and /design-login notice that standalone Claude Design closes by December 14, 2026; Claude Tag admin settings reorganized into four tabs. | `/design-sync`, `/design-login` |
| 2.1.301 | 2026-10-15 | VS Code LaTeX math rendering; vim mode gains the percent bracket motion. | |
| 2.1.300 | 2026-10-14 | Claude Tag supports Slack Connect channels (off by default), Allow once or Deny cards and Slack voice clips; VS Code claudeCode.attachSelection setting. | `claudeCode.attachSelection` |
| 2.1.299 | 2026-10-14 | Claude Tag can delete a canvas it created; Claude in Slack joins channels over 100 members quietly; deleting a self-hosted environment turns off its routines at once. | |
| 2.1.296 | 2026-10-09 | Claude Tag memory file editing on the Activity page; Claude Desktop Code tab behind a gateway shows the reason a session cannot start. | |
