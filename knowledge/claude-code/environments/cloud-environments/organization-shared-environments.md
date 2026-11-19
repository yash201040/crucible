---
type: "Feature"
title: "Organization-shared environments and Claude Tag"
description: "Owners on Team and Enterprise can share environments org-wide, set an org default, and pick the environment Claude Tag channels use."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [environments, organization, team, claude-tag]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: "Team or Enterprise plan; Owner role"
identifiers:
  - "Who can use it"
  - "claude.ai/admin-settings/claude-code"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Team and Enterprise, an Owner can make environments available to every member. Shared environments appear under an **Organization** heading in the selector after the member's **Personal** ones. A member's settings icon on a shared environment opens a read-only summary (Owners included). The Admin role cannot open the Cloud environments admin page.

# How to use it

- **Create**: Cloud environments page in admin settings (also where Owners edit and archive). Each has a name, a network access level, `.env` variables and a setup script.
- **Share a personal one**: open it for editing, use the **Who can use it** row. It keeps its ID, so sessions and scheduled tasks using it are unaffected.
- **Org default environment**: set separately at claude.ai/admin-settings/claude-code.
- **Secrets**: add a network secret on the Cloud environments page; do not put secrets in variables.
- **Claude Tag channels**: sessions use organization-level environments only (shared or self-hosted). Either set one as the org default or pin one to a channel in Claude Tag admin settings. For toolchains not pre-installed (such as .NET), an Owner creates a shared environment with a setup script.

# Limits and defaults

No organization-level allowlist exists for network domains, and no server-managed setting adds domains. A shared environment with Limited access and a fixed list is the way to give a team one standard list.
