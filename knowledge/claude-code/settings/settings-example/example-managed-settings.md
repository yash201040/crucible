---
type: "Guide"
title: "Example: organization managed-settings.json"
description: "A managed-settings.json showing login pinning, model limits, permission denies, managed-only rules, MCP and marketplace allowlists, sandbox, version floor."
resource: "https://code.claude.com/docs/en/settings-example"
tags: [settings, example, managed-settings, sandbox, mcp]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "availableModels"
  - "enforceAvailableModels"
  - "permissions.deny"
  - "permissions.disableBypassPermissionsMode"
  - "allowManagedPermissionRulesOnly"
  - "allowedMcpServers"
  - "allowManagedMcpServersOnly"
  - "strictKnownMarketplaces"
  - "sandbox.enabled"
  - "sandbox.failIfUnavailable"
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.network.allowedDomains"
  - "sandbox.network.allowManagedDomainsOnly"
  - "requiredMinimumVersion"
  - "cleanupPeriodDays"
  - "companyAnnouncements"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-example"
    resource: "https://code.claude.com/docs/en/settings-example"
    title: "Example settings files"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `managed-settings.json` illustrating managed keys, one plausible value each; not a recommended policy. Deploy as the file, or the same JSON through MDM or server-managed settings. One deployed file applies to every machine or account it reaches; deploy a different file or profile per group, or on an Enterprise plan give a group its own configuration in server-managed settings.

# How to use it

| Key | Example | Effect |
| :- | :- | :- |
| `forceLoginMethod` | `"claudeai"` | only claude.ai logins |
| `forceLoginOrgUUID` | `["xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"]` | only that organization (replace the placeholder) |
| `availableModels` | `["opus", "sonnet"]` | restrict models |
| `enforceAvailableModels` | `true` | the Default option obeys the list too |
| `permissions.deny` | `Bash(curl *)`, `Read(./.env)`, `Read(./secrets/**)` | deny on every machine |
| `permissions.disableBypassPermissionsMode` | `"disable"` | removes bypass-permissions mode |
| `allowManagedPermissionRulesOnly` | `true` | ignore permission rules from user, project, local |
| `allowedMcpServers` | `[{"serverUrl": "https://api.githubcopilot.com/*"}]` | match MCP servers by URL, not name; non-matching user-added servers do not load, including every stdio server when the list has only URL entries |
| `allowManagedMcpServersOnly` | `true` | managed MCP list is the only allowlist |
| `strictKnownMarketplaces` | `[{"source": "github", "repo": "acme-corp/approved-plugins"}]` | plugins only from this marketplace |
| `sandbox.enabled` | `true` | sandbox every command |
| `sandbox.failIfUnavailable` | `true` | refuse to start where sandbox cannot run (except in an Anthropic-hosted environment) |
| `sandbox.allowUnsandboxedCommands` | `false` | no unsandboxed retry |
| `sandbox.network.allowedDomains` | `["registry.npmjs.org", "github.com"]` | fixed network allowlist |
| `sandbox.network.allowManagedDomainsOnly` | `true` | users cannot add domains |
| `requiredMinimumVersion` | `"2.1.150"` | refuse to start on older versions |
| `cleanupPeriodDays` | `7` | delete transcripts and local data after 7 days |
| `companyAnnouncements` | `["Welcome to Acme Corp! ..."]` | startup message |
