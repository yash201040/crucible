---
type: "Reference"
title: "Admin-required sandbox and settings locks"
description: "When the sandbox becomes admin-required, which repository settings are then ignored, and which managed-only locks stop developers widening the policy."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, managed-settings, locks, security]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli]
requires: "managed settings or --settings"
identifiers:
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.network.allowManagedDomainsOnly"
  - "sandbox.allowManagedReadPathsOnly"
  - "sandbox.enableWeakerNestedSandbox"
  - "sandbox.enableWeakerNetworkIsolation"
  - "sandbox.network.allowAllUnixSockets"
  - "sandbox.network.allowLocalBinding"
  - "sandbox.allowAppleEvents"
  - "sandbox.allowNestedUserNamespaces"
  - "sandbox.network.strictAllowlist"
  - "sandbox.network.httpProxyPort"
  - "sandbox.network.socksProxyPort"
  - "sandbox.network.allowUnixSockets"
  - "sandbox.network.allowMachLookup"
  - "sandbox.ignoreViolations"
  - "sandbox.excludedCommands"
  - "sandbox.filesystem.allowWrite"
  - "sandbox.filesystem.allowRead"
  - "sandbox.autoAllowBashIfSandboxed"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When managed settings set a Boolean key such as `enabled` or `failIfUnavailable`, the managed value wins. Array keys such as `allowRead` merge across scopes, so developers can append entries unless a lock covers the key.

Keys a developer's user settings or `--settings` can turn on unless managed settings set them (repository `.claude/settings.json` too, unless admin-required): `enableWeakerNestedSandbox`, `enableWeakerNetworkIsolation`, `network.allowAllUnixSockets`, `network.allowLocalBinding`, `allowAppleEvents` (a repository cannot turn on), `allowNestedUserNamespaces` (a repository cannot turn on). Set to `false` in managed settings to block.

Managed-only locks: `allowManagedReadPathsOnly: true` (only managed `allowRead`), `allowManagedDomainsOnly` (managed domains only; with it on only managed settings can set a proxy port).

# How to use it

The sandbox is admin-required while `allowUnsandboxedCommands` is `false` in managed settings (or via `--settings` unless managed settings set it `true`), or `allowManagedDomainsOnly` is `true` in managed settings. These do not turn the sandbox on; set `enabled` too. Then settings that loosen it come only from managed settings, `--settings` and `~/.claude/settings.json`, and these are ignored in a repository's `.claude/settings.json` and `.claude/settings.local.json`:

| Repository setting | Ignored |
| - | - |
| `excludedCommands`, `ignoreViolations`, `network.allowedDomains`, `allowUnixSockets`, `allowMachLookup`, `httpProxyPort`, `socksProxyPort` | Every entry |
| `filesystem.allowWrite`, `Edit(...)` allow rules, `permissions.additionalDirectories` | Write access given to sandboxed commands (file tools still follow them) |
| `WebFetch(domain:...)` allow rules | The host added to sandbox allowlist |
| `enableWeakerNestedSandbox`, `enableWeakerNetworkIsolation`, `allowAllUnixSockets`, `allowLocalBinding` | `true` (a `false` still applies) |
| `enabled`, `failIfUnavailable` | `false`, when `~/.claude/settings.json` sets `true` |
| `filesystem.allowRead` | Entries at or under a path denied by managed, `--settings` or user settings |

Still applying from repository files: deny entries and `autoAllowBashIfSandboxed` (set it in managed settings to lock it).

Locks without admin-required (set in the named file; repository's other sandbox settings still apply):

| Setting (where) | Ignored in repository settings |
| - | - |
| `network.deniedDomains` or a `WebFetch(domain:...)` deny (managed, `--settings`) | `httpProxyPort`, `socksProxyPort` |
| `network.strictAllowlist` (managed, `--settings`, user) | Proxy ports, `allowedDomains`, `WebFetch(domain:...)` allow rules |
| `filesystem.denyRead`, a `Read(...)` deny, or a `credentials.files` entry (managed, `--settings`) | `allowRead`, `allowWrite`, `Edit(...)` allow, `additionalDirectories` at or under a denied path |

# Limits and defaults

Requires Claude Code v2.1.285 or later. From v2.1.282 to v2.1.284, the same settings made Claude Code ignore a repository's `excludedCommands` entries.
