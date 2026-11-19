---
type: "Reference"
title: "SandboxSettings, network and filesystem config"
description: "Programmatic sandbox options for sandboxed Bash: enabled, failIfUnavailable, network domains and sockets, filesystem paths, and unsandboxed fallback."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [sandbox, security, network, filesystem, isolation]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "On Linux the sandbox needs tools such as bubblewrap and socat"
identifiers:
  - "sandbox"
  - "SandboxSettings"
  - "SandboxNetworkConfig"
  - "SandboxFilesystemConfig"
  - "enabled"
  - "failIfUnavailable"
  - "autoAllowBashIfSandboxed"
  - "excludedCommands"
  - "allowUnsandboxedCommands"
  - "ignoreViolations"
  - "enableWeakerNestedSandbox"
  - "allowNestedUserNamespaces"
  - "ripgrep"
  - "allowedDomains"
  - "deniedDomains"
  - "strictAllowlist"
  - "allowManagedDomainsOnly"
  - "allowLocalBinding"
  - "allowUnixSockets"
  - "allowAllUnixSockets"
  - "httpProxyPort"
  - "socksProxyPort"
  - "allowWrite"
  - "denyWrite"
  - "denyRead"
  - "dangerouslyDisableSandbox"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Options.sandbox` configures command sandboxing for Bash programmatically.

# How to use it

| Property | Default | Notes |
| :- | :- | :- |
| `enabled` | `false` | Turn the sandbox on |
| `failIfUnavailable` | `true` | Stop at startup if enabled but cannot start; `false` falls back to unsandboxed with a stderr warning |
| `autoAllowBashIfSandboxed` | `false` | Auto-approve Bash when sandboxed; the `false` default needs v0.3.324+ |
| `excludedCommands` | `[]` | e.g. `['docker *']`; run unsandboxed automatically, no model involvement |
| `allowUnsandboxedCommands` | `true` | Model may set `dangerouslyDisableSandbox` in tool input; falls back to permissions and `canUseTool` |
| `network` | undefined | `allowedDomains` `[]`, `deniedDomains` `[]` (wins), `strictAllowlist` `false` (v2.1.219+; honored only from user, managed or CLI `--settings`), `allowManagedDomainsOnly` `false` (managed only; pass via `managedSettings`), `allowLocalBinding` `false`, `allowUnixSockets` `[]`, `allowAllUnixSockets` `false` (also Linux `AF_VSOCK`), `httpProxyPort`, `socksProxyPort` |
| `filesystem` | undefined | `allowWrite`, `denyWrite` (list absolute path to block writes to a working-dir file), `denyRead` |
| `ignoreViolations` | undefined | e.g. `{ "*": ['/etc/hosts'] }` |
| `enableWeakerNestedSandbox` | `false` | Compatibility |
| `allowNestedUserNamespaces` | `false` | Linux/WSL2 user namespaces; Claude Code v2.1.305+ |
| `ripgrep` | undefined | `{ command, args? }` |

# Limits and defaults

- If `enabled` is true and the sandbox cannot start, `query()` yields a result with `subtype: "error_during_execution"` (reason in `errors`; startup failure reason `sandbox_required_unavailable`, v0.3.314+), and a single-message query throws afterwards: wrap the loop in try.
- Network settings apply to sandboxed Bash only, not WebFetch (permission rules govern it). The built-in proxy enforces `allowedDomains` by hostname and does not inspect TLS by default, so domain fronting can bypass it; a TLS-terminating proxy is covered in the secure-deployment docs.
- Unix socket warning: allowing `/var/run/docker.sock` effectively gives full host access.
- With `permissionMode: bypassPermissions` plus `allowUnsandboxedCommands`, the model can run commands outside the sandbox without prompts (except actions no mode auto-approves), effectively escaping isolation.
