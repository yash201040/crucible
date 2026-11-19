---
type: "Release Digest"
title: "Apps, UI and other surfaces (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on Remote Control, Claude apps gateway, Chrome, VS Code, fullscreen UI and other surfaces."
resource: "https://code.claude.com/docs/en/changelog"
tags: [apps, ui, remote-control, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/diff"
  - "oidc.scope_on_refresh"
  - "/radio"
  - "/login"
  - "/chrome"
  - "/scroll-speed"
  - "claudeCode.enableReopenClosedSessionShortcut"
  - "/ultraplan"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.260 | 2026-09-03 | /diff panel in fullscreen shows uncommitted changes; ctrl+l clears transcript view; Claude apps gateway oidc.scope_on_refresh and desktop policy keys | `/diff`, `oidc.scope_on_refresh` |
| 2.1.259 | 2026-09-02 | GitLab glab mr commands show MR !N badge; /install-github-app points GitLab users to CI/CD docs |  |
| 2.1.257 | 2026-09-01 | VS Code model pill, session list sections, Archive session replacing Delete |  |
| 2.1.251 | 2026-08-28 | /radio on Bedrock, Vertex, Foundry and telemetry-off; VS Code Remote Control footer pill | `/radio` |
| 2.1.243 | 2026-08-25 | Keyless Console sign-in under /login | `/login` |
| 2.1.239 | 2026-08-21 | Fullscreen renderer offered on Bedrock, Vertex, Foundry |  |
| 2.1.237 | 2026-08-20 | Built-in Concise output style |  |
| 2.1.234 | 2026-08-17 | GitLab MR badge in footer and statusline; Remote Control account-switch stops session |  |
| 2.1.224 | 2026-08-07 | Remote Control archives stale server session after compaction or resume |  |
| 2.1.221 | 2026-08-04 | VS Code Focus view (Ctrl+Alt+F); Claude in Chrome closes tabs it opens |  |
| 2.1.198 | 2026-07-01 | Claude in Chrome generally available |  |
| 2.1.154 | 2026-05-28 | Claude in Chrome browser picker via /chrome | `/chrome` |
| 2.1.139 | 2026-05-11 | VS Code reopen closed tab Cmd/Ctrl+Shift+T (claudeCode.enableReopenClosedSessionShortcut); /scroll-speed | `/scroll-speed`, `claudeCode.enableReopenClosedSessionShortcut` |
| 2.1.101 | 2026-04-10 | Remote-session features such as /ultraplan auto-create a default cloud environment | `/ultraplan` |
