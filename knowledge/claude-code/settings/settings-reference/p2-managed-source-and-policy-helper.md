---
type: "Feature"
title: "Managed source merging and policyHelper"
description: "How managed sources combine (first-wins or merge), embedding-host parent settings, and the policyHelper that computes policy at startup."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, managed, policy, helper]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, headless, sdk, desktop]
requires: "Managed settings"
identifiers:
  - "managedSourcesBehavior"
  - "parentSettingsBehavior"
  - "policyHelper"
  - "policyHelper.path"
  - "policyHelper.timeoutMs"
  - "policyHelper.refreshIntervalMs"
  - "wslInheritsWindowsSettings"
  - "CLAUDE_CODE_VERSION"
  - "managedSettings"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed-scope keys that decide which managed sources apply, and a helper executable that emits policy.

# How to use it

| Name | Values / default | What it does |
| :- | :- | :- |
| `managedSourcesBehavior` | `"first-wins"` (default) or `"merge"`. Needs v2.1.242+ | `first-wins`: highest-priority source carrying a policy key supplies policy; lower ones add only cross-source keys. `merge`: every admin source contributes. Read from the highest-priority source carrying this key or a policy key; lower ones cannot opt in. HKCU and embedding-host parent settings take no part. Deliver it in the highest-priority source (an MDM profile on machines that never get server-managed settings); set `merge` only where lower sources are under admin control |
| `parentSettingsBehavior` | `"first-wins"` (default) or `"merge"` | `first-wins` drops settings supplied by an embedding host (Agent SDK, IDE extension) when an admin tier exists; `merge` applies them under the admin tier through a restrictive-only filter (for example Desktop delivering a gateway egress allowlist). With no admin tier the host settings apply anyway, still filtered to restrictive values |
| `wslInheritsWindowsSettings` | Boolean, default `false`. Needs v2.1.282+ | WSL reads Windows managed policy chain (HKLM and the Windows file beat `/etc/claude-code`, HKCU below); `/etc/claude-code` read only when no Windows admin document is present. Honored only in HKLM or `C:\Program Files\ClaudeCode\`. HKCU joins only if it also sets `true`. A Windows source containing only this key is not a policy source. `true`/`false` accepted with or without quotes, `null` removes it; any other value counts as a present admin document and warns. No effect on native Windows |

Merge rules by key kind: lists combine; locks take the strictest value; restriction allowlists (`availableModels`, `allowedMcpServers`, `allowedProviders`, `strictKnownMarketplaces`, `allowedChannelPlugins`, `fallbackModel` chain) are taken whole from the highest source that sets them; values taken whole (`sandbox.credentials.awsPairs`, `sandbox.ripgrep`; v2.1.257+); `managedMcpServers` combines names with the higher source's whole entry; read from highest-priority source only: `apiKeyHelper`, `awsAuthRefresh`, `awsCredentialExport`, `gcpAuthRefresh`, `otelHeadersHelper`, `proxyAuthHelper`, `parentSettingsBehavior`, `modelPicker`, `policyHelper`, `permissions.defaultMode`; `env` merges per variable under both modes; others from the highest source. `policyHelper` applies only when the top source is an MDM policy or managed file; `modelOverrides` pairs with `availableModels` (ignored from every source if a higher source sets `availableModels` without it). Gateway login keys never come from server-managed settings. Run `/status` and read the `Setting sources` line to see what combined.

# Limits and defaults

`policyHelper` (object `path`, `timeoutMs`, `refreshIntervalMs`; default unset): runs an executable before the first prompt and treats its output as the managed settings.
- Read from macOS plist, Windows HKLM or the managed settings file only; ignored in server-managed settings, HKCU and host parent settings. When server-managed settings deliver policy at launch the helper does not run; if a later fetch reports them removed, it runs then.
- Runs with no arguments and `CLAUDE_CODE_VERSION` set; stdout must be a single JSON envelope capped at 1 MiB, settings under a `managedSettings` key (a bare settings object applies nothing and reports no error). When emitted, that object is the only managed source for the run (MDM, file, HKCU ignored; no parent settings merged). Exit `0` without `managedSettings` contributes nothing.
- `path`: required, absolute normalized path without `.` or `..`; on Windows a drive-letter or UNC path ending `.exe`.
- `timeoutMs`: integer, min `1000`, default `10000`; also covers the file-existence check.
- `refreshIntervalMs`: `0` disables, otherwise at least `60000`; unset runs once at startup. A successful refresh replaces policy without restart.
- Failure (non-zero exit, timeout, no start, over 1 MiB on stdout or stderr, not a single JSON object, unrepairable schema violation, bad path): at startup Claude Code prints the reason and refuses to start, covering interactive, `claude -p`, Agent SDK, background sessions and most subcommands. Reason includes stderr (or stdout if stderr empty) after non-zero exit; after timeout only the `timeoutMs` limit. A background-refresh failure keeps the last good policy and `/status` shows the failure. `--debug` logs helper stderr. An invalid `policyHelper` value (bare path string, `timeoutMs` below minimum) is a dropped entry and no helper runs. Helpers needing outage resilience should serve from their own cache and exit `0`.
- Turn off by removing the key from its source.
