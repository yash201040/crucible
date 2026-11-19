---
type: "Feature"
title: "Per-command allowed domains in auto mode"
description: "In auto mode, Claude lists the hosts a sandboxed command needs on the command itself and the classifier reviews them, opening them for that command only."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, auto-mode, network, classifier]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli]
requires: "auto mode with sandboxing on"
identifiers:
  - "sandbox.network.deniedDomains"
  - "sandbox.network.strictAllowlist"
  - "sandbox.network.allowManagedDomainsOnly"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In auto mode with sandboxing, each Bash, PowerShell or Monitor command in the sandbox can carry a list of extra hosts beyond the sandbox allowlist: a domain (`registry.npmjs.org`), a wildcard (`*.pythonhosted.org`) or an IP, each with optional `:port`. The classifier reviews the hosts with the command. Requires Claude Code v2.1.271 or later.

# How to use it

An approved list opens those hosts for that one command only, while it runs; nothing is added to session hosts or settings. A command carrying hosts goes to the classifier rather than being approved by a permission rule or sandbox auto-allow. If an ask rule forces a prompt, the terminal dialog lists the hosts and approving covers both.

# Limits and defaults

- Widens only what the sandbox denies by default; `deniedDomains` still block.
- When `strictAllowlist` or `allowManagedDomainsOnly` locks the allowlist, per-command lists are refused.
- While lists apply, a connection to a host no approved command listed is refused with no prompt or classifier check; the refusal names the host and Claude re-runs the command with it added.
