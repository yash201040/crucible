---
type: "Limit"
title: "Sandbox limitations and scope"
description: "Security limits of the sandbox (TLS, Unix sockets, domain fronting, Apple Events, user namespaces) and how computer use, subagents and mods relate to it."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, limitations, security, subagents]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox.network.tlsTerminate"
  - "sandbox.network.allowUnixSockets"
  - "sandbox.enableWeakerNestedSandbox"
  - "sandbox.allowAppleEvents"
  - "sandbox.network.allowMachLookup"
  - "sandbox.allowNestedUserNamespaces"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The docs say sandboxing reduces risk but is not a complete isolation boundary.

# Limits and defaults

- **Network filtering**: by default the proxy does not terminate or inspect TLS; allowing broad domains such as `github.com` can create exfiltration paths, and domain fronting may reach hosts outside the allowlist because the decision uses the client-supplied hostname. For stronger guarantees use a custom TLS-terminating proxy with its CA installed in the sandbox.
- **Unix sockets**: `allowUnixSockets` can grant access to system services (e.g. `/var/run/docker.sock` is effectively host access).
- **Filesystem escalation**: broad write permissions to `$PATH` directories, system config or shell config files (`.bashrc`, `.zshrc`) can lead to code execution in other contexts.
- **Linux strength**: `enableWeakerNestedSandbox` (for Docker without privileged namespaces) considerably weakens security.
- **macOS**: `allowAppleEvents` removes code-execution isolation (user, managed or CLI settings only); services listed in `network.allowMachLookup` are reachable outside the sandbox and unconfined.
- **User namespaces**: `allowNestedUserNamespaces: true` turns off a boundary.
- Effective sandboxing needs both filesystem and network isolation: without network isolation a compromised agent could exfiltrate files; without filesystem isolation it could backdoor system resources.

# Notes

Scope:
- Computer use runs on your real desktop, gated by per-app permission prompts.
- Subagents run in the same process as the parent and use the same sandbox configuration; their Bash commands are sandboxed when the parent has sandboxing enabled.
- Background sessions run in their own process; Bash commands are sandboxed when their settings enable it.
- To cover everything outside the sandbox, run Claude Code (local mode) inside the sandbox runtime with a host allowlist, or in the dev container with its firewall script; for the background service see the corporate-launcher page.
- Mods and processes they start run outside the sandbox.
