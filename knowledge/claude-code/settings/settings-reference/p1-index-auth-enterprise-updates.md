---
type: "Reference"
title: "Index: authentication, managed and update keys"
description: "Settings keys for credential helpers, login restriction, provider allowlists, managed-settings behavior, policy helper and version pinning (index rows only)."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [authentication, managed-settings, versions, enterprise]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "allowedProviders"
  - "apiKeyHelper"
  - "awsAuthRefresh"
  - "awsCredentialExport"
  - "forceLoginGatewayUrl"
  - "forceLoginMethod"
  - "forceLoginOrgUUID"
  - "gatewayInternalNetworks"
  - "gcpAuthRefresh"
  - "otelHeadersHelper"
  - "forceRemoteSettingsRefresh"
  - "managedSourcesBehavior"
  - "parentSettingsBehavior"
  - "policyHelper"
  - "policyHelper.path"
  - "policyHelper.refreshIntervalMs"
  - "policyHelper.timeoutMs"
  - "wslInheritsWindowsSettings"
  - "autoUpdatesChannel"
  - "minimumVersion"
  - "requiredMaximumVersion"
  - "requiredMinimumVersion"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Index entries from "Authentication and providers", "Enterprise and managed settings" and "Updates and versioning". Detailed sections are in other parts of the page.

# How to use it

| Key | Scope | What it does |
| :- | :- | :- |
| `apiKeyHelper` | Any file | Generate the API credential with your own command |
| `awsAuthRefresh` | Any file | Refresh expired Bedrock credentials in `.aws` with your own command |
| `awsCredentialExport` | Any file | Supply Bedrock credentials as JSON from your own command |
| `gcpAuthRefresh` | Any file | Refresh Google Cloud credentials with your own command |
| `otelHeadersHelper` | Any file | Generate rotating OpenTelemetry headers with your own command |
| `allowedProviders` | Managed | Limit which API providers a machine may use |
| `forceLoginMethod` | Any file | Restrict login to claude.ai, Claude Console or a cloud gateway |
| `forceLoginOrgUUID` | Any file | Pin claude.ai logins to an organization; only managed settings enforce it |
| `forceLoginGatewayUrl` | User or managed | Gateway URL the login screen connects to |
| `gatewayInternalNetworks` | Managed | Let `/login` reach a cloud gateway on public IPv4 space the organization uses internally |
| `forceRemoteSettingsRefresh` | Managed | Block startup until server-managed settings are freshly fetched |
| `managedSourcesBehavior` | Managed | Compose every managed source instead of using the highest-priority one |
| `parentSettingsBehavior` | Managed | Apply or drop restrictions an SDK or IDE host passes when managed settings are deployed |
| `policyHelper` | Managed | Run an executable that computes managed settings at startup |
| `policyHelper.path` | Managed | The helper executable |
| `policyHelper.refreshIntervalMs` | Managed | Re-run the helper in the background on an interval |
| `policyHelper.timeoutMs` | Managed | How long Claude Code waits for the helper |
| `wslInheritsWindowsSettings` | Managed | Have WSL read managed settings from the Windows policy chain |
| `autoUpdatesChannel` | Any file | Follow the stable release channel instead of latest |
| `minimumVersion` | Any file | Keep auto-updates from installing below a version |
| `requiredMinimumVersion` | Managed | Refuse to start on a version older than required |
| `requiredMaximumVersion` | Managed | Refuse to start on a version newer than allowed |
