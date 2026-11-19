---
type: "Feature"
title: "Gateway policy for Desktop and parent settings locks"
description: "How Claude Desktop sessions receive gateway policy through parent settings, the merge opt-in, allowManaged*Only locks and what the locks do not cover."
resource: "https://code.claude.com/docs/en/claude-apps-gateway"
tags: [gateway, parent-settings, locks, security]
kind: "setting"
maturity: "unlabelled"
since: "2.1.309"
surfaces: [desktop, sdk, ide]
requires: "allowedProviders v2.1.285+; strictKnownMarketplaces v2.1.282+; managedSettings option v2.1.309+ (or TypeScript Agent SDK v0.3.309+)"
identifiers:
  - "parentSettingsBehavior"
  - "managedSourcesBehavior"
  - "allowManagedPermissionRulesOnly"
  - "allowManagedMcpServersOnly"
  - "allowManagedHooksOnly"
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "sandbox.network.allowManagedDomainsOnly"
  - "sandbox.network.allowedDomains"
  - "sandbox.filesystem.allowManagedReadPathsOnly"
  - "sandbox.filesystem.denyRead"
  - "sandbox.filesystem.allowRead"
  - "sandbox.credentials"
  - "availableModels"
  - "allowedProviders"
  - "strictKnownMarketplaces"
  - "blockedMarketplaces"
  - "strictPluginOnlyCustomization"
  - "forceLoginOrgUUID"
  - "disableAllHooks"
  - "allowedHttpHookUrls"
  - "httpHookAllowedEnvVars"
  - "disableSkillShellExecution"
  - "policyHelper"
  - "managedSettings"
  - "resolveSettings()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-apps-gateway"
    resource: "https://code.claude.com/docs/en/claude-apps-gateway"
    title: "Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Desktop runs tabs on embedded Claude Code sessions and passes them policy built from the gateway's `/user/bootstrap` configuration (model allowlist, disabled tools, egress allowlist from the policy's `cli` or `code` block, plus a `desktop` overlay). Hooks, `env` and scoped permission rules reach `/login` clients, and under `code` the Code tab when its conditions hold; they do not reach Cowork or Chat sessions. Settings passed by a launching process are parent settings; Claude Code ignores them on any machine with an admin-deployed managed source unless `parentSettingsBehavior: "merge"` is set in the selected source. `policyHelper` fleets cannot use the merge.

# How to use it

- Machines running only Claude Desktop need the opt-in; without it the egress allowlist (WebFetch domain rules and sandbox network rules) and `strictKnownMarketplaces` do not reach embedded sessions and nothing warns. Mirror the whole snippet into any source that outranks the file (plist on macOS or HKLM on Windows outrank `managed-settings.json`; gateway remote managed settings outrank both). Check the selected source via the Agent SDK `resolveSettings()` `policyOrigin` (`plist`, `hklm`, `file`).
- Once merge is on, any host process (Desktop, Agent SDK app, IDE extension) can supply parent settings, filtered to an allowlist of restrictive keys that can still grant access. Deploy all five locks plus allowlists in the same sources: `allowManagedPermissionRulesOnly`, `allowManagedMcpServersOnly`, `allowManagedHooksOnly`, `sandbox.network.allowManagedDomainsOnly`, `sandbox.filesystem.allowManagedReadPathsOnly`, with `allowedMcpServers`, `sandbox.network.allowedDomains`, `sandbox.filesystem.denyRead`/`allowRead`. Deny and ask rules are evaluated before allow rules.
- Parent-supplied `sandbox.credentials` are forwarded stripped: `deny` entries keep only path or name and mode; `mode: mask` file entries become sentinel-only whole-file masks; `envVars` mask entries not forwarded; `awsPairs` and `sigv4` restriction-only (a `sigv4` block pins `streaming`, `presigned`, `sigv4a` to `deny`).
- SDK `managedSettings` option: `disableAllHooks: true` stops user, project, local, agent-frontmatter and SDK `settings` hooks but not SDK hook callbacks or administrator hooks. Passing `hooks`, or non-empty `allowedHttpHookUrls` / `httpHookAllowedEnvVars`, is ignored (use SDK `settings`); empty lists take effect unless the admin defines `hooks` or enables a plugin; `disableSkillShellExecution: true` takes effect. On admin machines, parent settings need the administrator to let an embedding host add policy.

# Limits and defaults

- Locking with an empty managed domain list blocks all sandboxed outbound traffic; locking MCP with no `allowedMcpServers` anywhere loads every server not in `deniedMcpServers`; `allowRead` only re-allows inside `denyRead`.
- Passing the locks does not cover: `forceLoginOrgUUID` (honored from parent if managed settings set none), `allowedMcpServers` and `availableModels` and `allowedProviders` and `strictKnownMarketplaces` (honored from parent when the winning source sets none), `blockedMarketplaces` (adds to blocklists), and `strictPluginOnlyCustomization` (passes regardless and ignores the developer's own customization, including protective hooks).
- Lower sources: sandbox locks and `allowManagedPermissionRulesOnly` still block parent allow rules; the MCP lock applies from lower sources on v2.1.273+. Hooks lock needs the winning source unless `managedSourcesBehavior` is `"merge"`, which applies the strictest value of any source.
