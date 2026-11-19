---
type: "Feature"
title: "Share an artifact and co-edit"
description: "Audiences for sharing (organization, folder, public), view links, editor role and handling of stale copies."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, sharing, editors, public-link]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web, cli]
requires: "Team or Enterprise plan for organization sharing, folders and editor role"
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A new artifact is visible only to you. Share it from the **Share** control in the page header; the header also links to the gallery at claude.ai/code/artifacts listing every artifact you created.

# How to use it

| Audience | Notes |
| --- | --- |
| Within your organization | Team and Enterprise: specific people or everyone; viewers sign in to claude.ai as members |
| Shared folder | Team and Enterprise: move it to a folder you own or edit, from the Artifacts page at claude.ai/artifacts; folder owner and editors can change it |
| Public | Link anyone can open without sign-in; on Team and Enterprise it is off until an Owner enables it |

- Publisher identity: inside the organization your name shows in the title menu (public artifact: page header for signed-in org viewers). A public viewer who is not signed in, or is outside the organization, sees `Content is user-generated and unverified.`
- Link to a view: ask Claude for a link per tab; each is the artifact link plus an anchor such as `#overview`.
- Editors: people are viewers by default. On Team and Enterprise, switch a person's role from viewer to editor in the share dialog. An editor gives Claude the URL (or attaches from `/artifacts`) and Claude pulls current content and republishes. If an editor published while Claude holds an older copy, Claude Code refuses the stale publish and Claude merges onto the newer version and publishes again.
