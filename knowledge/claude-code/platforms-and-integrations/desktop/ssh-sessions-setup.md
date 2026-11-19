---
type: "Guide"
title: "SSH sessions: setup and requirements"
description: "Connecting Desktop to remote machines over SSH: fields, requirements, ssh config use, jump hosts, containers, port forwarding and Windows remotes."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, ssh, remote, jump-host, requirements]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Remote Linux, macOS or Windows machine with SSH server and SFTP"
identifiers:
  - "~/.ssh/config"
  - "ProxyJump"
  - "ProxyCommand"
  - "ConnectTimeout"
  - "MaxSessions"
  - "~/.claude/remote/"
  - "claude://code/new"
  - "ssh_host"
  - "ssh_port"
  - "ssh_folder"
  - "NODE_EXTRA_CA_CERTS"
  - "HTTPS_PROXY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

SSH sessions run Claude Code on a remote machine (VM, dev container, server) with Desktop as the interface. Desktop installs Claude Code on the remote automatically on first connect. Permission modes, connectors, plugins and MCP servers work.

# How to use it

New environment > SSH tab > Add SSH connection: **Name**, **SSH host** (`user@hostname` or a `~/.ssh/config` host), **SSH port** (22), **SSH key** (optional), **Worktree folder** (optional).

Remote requirements: x86_64 or arm64; glibc 2.17+ or musl; SSH server with SFTP subsystem; `~/.claude/remote/` not on a `noexec` mount, about 1 GB free; a shell that runs SSH commands; network access for Claude Code. With `MaxSessions 1`: Desktop v3.1623.0+ on macOS/Linux, OpenSSH client on Windows, or raise `MaxSessions`; prompt-free login needed.

SSH config: macOS/Linux use the OpenSSH client (v1.37937.0+, OpenSSH 7.6+) so `HostName`, `User`, `IdentityFile`, `CertificateFile`, `ProxyJump`, `ProxyCommand` apply. Windows needs v2.2553.0+, Microsoft OpenSSH 9.4+ and a non-Store install; otherwise the built-in client ignores `CertificateFile` and fails on `ProxyJump`. Desktop ignores `RemoteCommand`; reach containers with a `ProxyCommand`. Forwarding settings (`ForwardAgent`, `LocalForward`, etc.) are left off.

- **Timeout**: default 30 s (macOS/Linux v4.4212.0+ through jump host: second try with 90 s); set `ConnectTimeout` above 90 s for slow routes; remote approvals must finish within 45 s.
- **Proxy/CA on Linux remotes**: put `HTTPS_PROXY` and `NODE_EXTRA_CA_CERTS` under `env` in the remote `~/.claude/settings.json`; profile files are not read.
- **Port access**: `ssh -N -L 3000:localhost:3000 devbox`; needs `AllowTcpForwarding`.
- **MCP servers** from `~/.claude.json` or `.mcp.json` must be set up on the remote.
- **Deep link**: `claude://code/new?ssh_host=dev%40build.example.com&ssh_port=2222&ssh_folder=/srv/payments&q=...` (v2.110.0+); `ssh_host` required; always asks confirmation, never auto-sends the prompt; does not bypass `sshHostAllowlist`.

# Limits and defaults

Windows remote (v2.31226.0+, Microsoft OpenSSH Server; shells cmd.exe, PowerShell 5.1, Git Bash): terminal does not open for Windows-path folders, commands run unsandboxed, custom worktree folder ignored, forks only at first message with cmd/PowerShell shells. Side chats and terminal work over SSH; cloud move not possible. Desktop tests SSH ports by opening and closing connections (may trip fail2ban or OpenSSH 9.8+ penalties; use `PerSourcePenaltyExemptList` or `ignoreip`).
