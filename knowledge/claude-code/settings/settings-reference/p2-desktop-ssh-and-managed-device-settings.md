---
type: "Reference"
title: "Desktop SSH and managed-device settings"
description: "Desktop-app keys for local-session blocking, SSH connections, SSH host allowlist and preview script control."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, desktop, ssh, managed]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Claude Desktop; versions per key"
identifiers:
  - "disableDesktopLocalSessions"
  - "disableRemotePreviewScripts"
  - "sshConfigs"
  - "sshHostAllowlist"
  - "sshHostCommands"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys only the desktop app reads; the terminal CLI ignores them.

# How to use it

| Name | Scope | Type | What it does |
| :- | :- | :- | :- |
| `disableDesktopLocalSessions` | managed | Boolean; only JSON `true` takes effect | No on-device Code sessions: user's computer (and WSL on Windows) grayed out with "Disabled by your organization"; new sessions default to first SSH connection; existing local sessions stay listed but cannot continue; SSH to other hosts and cloud sessions unaffected. Needs Claude Desktop v1.37937.0+. Pair with `sshConfigs` and `sshHostAllowlist` |
| `disableRemotePreviewScripts` | managed | Boolean; only `true` | HTML previews from SSH or WSL sessions run no scripts; external Browser pane browsing unaffected. Needs Claude Desktop v5.1231.0+ (earlier versions: use `disableBrowserExternalNavigation`). If the machine receives no other managed settings also set `parentSettingsBehavior` to `"merge"`; on Windows a managed settings file removes WSL sessions until allowed |
| `sshConfigs` | user or managed | array of `{id, name, sshHost, sshPort?, sshIdentityFile?}` | Adds SSH connections to the environment selector; managed ones cannot be edited or deleted by users, who can set their own Worktree folder |
| `sshHostAllowlist` | managed | array of hostname patterns | Limits SSH hosts: `*` any, `*.example.com` includes `example.com` and subdomains, otherwise exact match after `~/.ssh/config` resolution; case-insensitive; empty array turns SSH off; unreadable value counts as empty (except `null` = unset). Jump hosts must match too from v3.1623.0+. Needs v2.26454.0+. With `managedSourcesBehavior: "merge"` lists from every admin source combine |
| `sshHostCommands` | user or managed (managed read from one file or MDM policy on the machine; ignored in server-managed settings) | array of `{id, name, command, sshIdentityFile?, startDirectory?}` | Connections whose host is printed by a command run on your computer. `command` is a program and arguments, not shell syntax; on Windows give the full program path. Needs Desktop v3.6556.0+ (macOS, Linux) or v4.16336.0+ (Windows), signed in. Before Claude Code v2.1.307 the Edit tool refused to add it (`Unrecognized field: sshHostCommands`) |

# Notes

When an admin source exists, Claude Code ignores desktop-derived parent policy (egress allowlist, sandbox, MCP restrictions); see [parentSettingsBehavior](./p2-managed-source-and-policy-helper.md).
