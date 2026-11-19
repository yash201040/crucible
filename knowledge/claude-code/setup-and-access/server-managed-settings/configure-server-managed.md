---
type: "Guide"
title: "Configuring server-managed settings"
description: "Owner setup in the claude.ai admin console, requirements, verification, per-group configurations and limitations."
resource: "https://code.claude.com/docs/en/server-managed-settings"
tags: [server-managed, admin-console, groups, enterprise]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli, desktop]
requires: "Claude for Teams or Enterprise; Owner or Primary Owner role; network access to api.anthropic.com; group configurations need Enterprise"
identifiers:
  - "claude doctor"
  - "Managed settings (remote)"
  - "/status"
  - "/permissions"
  - "managedMcpServers"
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "policyHelper"
  - "wslInheritsWindowsSettings"
  - "availableModels"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "server-managed-settings"
    resource: "https://code.claude.com/docs/en/server-managed-settings"
    title: "Configure server-managed settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Owners edit JSON in Organization settings > Claude Code > Managed settings (claude.ai/admin-settings/claude-code). Clients fetch it at startup and hourly. All `settings.json` keys work (hooks, `env`, managed-only keys, `autoMode`) except those restricted to OS-level delivery. The editor validates against the published schema (which can lag); a warning relabels Save as **Update with errors** or **Add with errors** but still saves.

# How to use it

- Verify: user restarts Claude Code; `/status` shows `Enterprise managed settings` with `remote`; `/permissions` shows effective rules; `claude doctor` line `Managed settings (remote)` (v2.1.248+) reports loaded, none configured, fetch failed (cause, whether cache applies) or skipped (reason).
- Group configurations (Enterprise only; not yet available with HIPAA): each group exists via SCIM or as a custom group. Steps: add a configuration per group, set the "Everyone else" catch-all, drag to rank, check effective settings per member, switch to group-based mode (banner). A member gets only the highest-ranked group configuration; configurations do not merge, so each must hold every setting. Without a catch-all, others get no server-managed settings. Group `availableModels` limits hold only in local sessions; cloud and remote Cowork use the catch-all (or the organization-wide configuration).
- Access: Primary Owner and Owner.

# Limits and defaults

- Team plan: one uniform org-wide configuration.
- `managed-mcp.json` cannot be distributed; use `allowedMcpServers`/`deniedMcpServers`, or `managedMcpServers` on v2.1.259+ (http and sse only, no exclusive control). A file at the system path is read separately and still applies.
- OS-level-only keys such as `policyHelper` and `wslInheritsWindowsSettings` are not honored here.
- Audit log events for settings changes are via the compliance API or export (contact account team).
