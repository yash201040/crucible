---
type: "Reference"
title: "Python SandboxSettings"
description: "Programmatic sandbox configuration for Bash commands: enable flags, network rules, unsandboxed fallback and platform notes."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [sandbox, network, security, permissions, python]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Platform sandbox support; on Linux bubblewrap and socat"
identifiers:
  - "SandboxSettings"
  - "enabled"
  - "autoAllowBashIfSandboxed"
  - "excludedCommands"
  - "allowUnsandboxedCommands"
  - "network"
  - "ignoreViolations"
  - "enableWeakerNestedSandbox"
  - "failIfUnavailable"
  - "filesystem"
  - "denyWrite"
  - "SandboxNetworkConfig"
  - "allowedDomains"
  - "deniedDomains"
  - "allowManagedDomainsOnly"
  - "allowUnixSockets"
  - "allowAllUnixSockets"
  - "allowLocalBinding"
  - "allowMachLookup"
  - "httpProxyPort"
  - "socksProxyPort"
  - "SandboxIgnoreViolations"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`ClaudeAgentOptions(sandbox=SandboxSettings)` configures command sandboxing for Bash. The network settings apply to sandboxed Bash only; they do not restrict WebFetch, which uses permission rules.

# How to use it

| Property | Default | What it does |
| :- | :- | :- |
| `enabled` | `False` | turn sandbox on |
| `autoAllowBashIfSandboxed` | `False` (default needs Python SDK 0.2.182+) | auto-approve Bash when sandboxed |
| `excludedCommands` | `[]` | commands that bypass the sandbox with no model involvement, such as `["docker *"]` |
| `allowUnsandboxedCommands` | `True` | model may set `dangerouslyDisableSandbox`; falls back to permissions and `can_use_tool` |
| `network` | `None` | `SandboxNetworkConfig` |
| `ignoreViolations` | `None` | dict of command-part (or `*`) to text lists hidden from the violation report; the access is still blocked |
| `enableWeakerNestedSandbox` | `False` | weaker nested sandbox for compatibility |
| `failIfUnavailable` | (forwarded, not declared) | `True` raises `ResultError` when the sandbox cannot start |
| `filesystem` | (forwarded) | for example `{"denyWrite": ["/abs/path/.env"]}` blocks sandboxed writes to those absolute paths |

`SandboxNetworkConfig`: `allowedDomains` `[]`, `deniedDomains` `[]` (wins over allowed), `allowManagedDomainsOnly` `False` (managed settings only; no effect via SDK options), `allowUnixSockets` `[]` (macOS only, ignored on Linux), `allowAllUnixSockets` `False` (also Linux VM sockets `AF_VSOCK`), `allowLocalBinding` `False`, `allowMachLookup` `[]` (macOS only, trailing wildcard), `httpProxyPort`, `socksProxyPort` (`None`).

# Limits and defaults

- If `enabled` is `True` but the sandbox cannot start, commands run unsandboxed with a stderr warning by default. This differs from the TypeScript SDK, where `failIfUnavailable` defaults to `true`.
- The proxy filters by hostname and does not inspect TLS by default, so domain fronting can bypass the allowlist; a TLS-terminating proxy can be configured.
- `allowUnixSockets` for something like `/var/run/docker.sock` effectively grants full host access.
- `bypassPermissions` together with `allowUnsandboxedCommands` lets the model run commands outside the sandbox without prompts (apart from actions no mode auto-approves).
