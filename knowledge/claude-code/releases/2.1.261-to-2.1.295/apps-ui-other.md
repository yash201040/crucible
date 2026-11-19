---
type: "Release Digest"
title: "Apps, UI and other, 2.1.261 to 2.1.295"
description: "Release-note entries for VS Code, Claude Tag, Code Review, artifacts, Claude in Chrome, terminal UI and screen reader changes from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [vscode, claude-tag, code-review, artifacts, ui, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [ide, web, cli]
requires: ""
identifiers:
  - "/copy"
  - "/artifacts"
  - "/focus"
  - "/status"
  - "/help"
  - "/hooks"
  - "/export"
  - "/plan"
  - "/chrome"
  - "/sandbox"
  - "/desktop"
  - "/mobile"
  - "/web-setup"
  - "/autofix-pr"
  - "/ultrareview"
  - "/insights"
  - "/code-review"
  - "--max-findings"
  - "claudeCode.scrollToBottomOnSend"
  - "claudeCode.lockEditorGroups"
  - "claudeCode.preferredLocation"
  - "claudeCode.environmentVariables"
  - "!fast"
  - "!fork"
  - "!restart"
  - "!status"
  - "REVIEW.md"
  - "OSC 7501"
  - "ctrl+o"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Selected release-note rows (bug fixes removed) about surfaces and interface: VS Code extension, Claude Tag in Slack, Code Review, the Artifact tool and terminal UI. Only rows that add a command, flag or limit are listed.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | Program Status Protocol (OSC 7501) support: terminals can show working, waiting or done. | `OSC 7501` |
| 2.1.295 | 2026-10-08 | Artifact pages without a background show on white; artifact permission prompts with telemetry disabled match other installs. | |
| 2.1.293 | 2026-10-07 | Artifacts: Claude pins libraries to exact versions two weeks old or older. | |
| 2.1.292 | 2026-10-06 | Artifact tool listing shows artifact count and lists up to 200 (was 50); Code Review analytics gain totals and per-repository breakdown. | |
| 2.1.290 | 2026-10-05 | Claude Tag: `!fast` / `!fast off` switch a Slack thread to fast mode; channel instructions limit 8,192 characters. | `!fast` |
| 2.1.288 | 2026-10-02 | `--max-findings <n>\|all` for `/code-review` (reused until `--max-findings default`). | `--max-findings` |
| 2.1.287 | 2026-10-01 | `/config` ‹ › cycling, PgUp/PgDn paging; mod-based "You should know" side agent. | `/config` |
| 2.1.286 | 2026-09-30 | VS Code bookmarks, question rows, option previews; `/hooks` opens on one grouped list; `/ultrareview` browser link removed. | `/hooks` |
| 2.1.285 | 2026-09-29 | `/ultrareview` on macOS/Linux needs git 2.31+ to upload a local repo; symbolic refs omitted. | `/ultrareview` |
| 2.1.284 | 2026-09-28 | `/artifacts` filter tabs All, Mine, Shared; Claude Tag model family choices such as "Opus (latest)". | `/artifacts` |
| 2.1.283 | 2026-09-25 | Artifact watching: an automatically armed watch ends after 3.5 hours without activity; Claude Tag "Channels Claude can search" setting. | |
| 2.1.280 | 2026-09-22 | VS Code adds Status, Sandbox, Claude in Chrome dialogs and typed `/export`, `/skills`, `/plan`. | `/export`, `/plan`, `/sandbox`, `/chrome` |
| 2.1.277 | 2026-09-18 | VS Code `/logout`, `/tasks`, `/copy`; `/ultrareview` refuses in non-interactive sessions without a base branch. | `/copy` |
| 2.1.275 | 2026-09-17 | VS Code accept/reject buttons per change; Claude Tag attach conditions for access bundles. | |
| 2.1.274 | 2026-09-17 | VS Code `claudeCode.lockEditorGroups`; Claude Tag Guests setting. | `claudeCode.lockEditorGroups` |
| 2.1.271 | 2026-09-14 | Artifacts: a session can watch up to 10 artifacts (was 5); Markdown files published as artifacts render as styled pages; `/mobile` single QR code. | `/mobile` |
| 2.1.269 | 2026-09-11 | VS Code agent map, Hooks dialog, Permission rules dialog; `/diff` opens fully rendered. | |
| 2.1.268 | 2026-09-10 | Browser-tab icons for published artifacts. | |
| 2.1.265 | 2026-09-08 | VS Code archives sessions inactive for 14 days by default ("Archive inactive sessions"). | |
| 2.1.261 | 2026-09-04 | VS Code "Build a custom style" walkthrough, MCP server Add/Remove form, fold button on prompts. | |
