---
type: "Guide"
title: "Linux and WSL2 sandbox dependencies"
description: "Packages the Linux and WSL2 sandbox needs, the Dependencies tab, WSL2 notes and the AppArmor profile for Ubuntu."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, linux, wsl2, bubblewrap]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Linux or WSL2 (not WSL1)"
identifiers:
  - "bubblewrap"
  - "socat"
  - "ripgrep"
  - "@anthropic-ai/sandbox-runtime"
  - "sandbox.bwrapPath"
  - "sandbox.network.allowAllUnixSockets"
  - "/etc/apparmor.d/bwrap"
  - "kernel.apparmor_restrict_unprivileged_userns"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Linux and WSL2 the sandbox relies on `bubblewrap` (unprivileged filesystem isolation) and `socat` (relays network traffic to the sandbox proxy). Ripgrep ships with the native binary. An optional seccomp filter adds Unix domain socket blocking; install with `npm install -g @anthropic-ai/sandbox-runtime`.

# How to use it

- Ubuntu/Debian: `sudo apt-get install bubblewrap socat`. Fedora: `sudo dnf install bubblewrap socat`.
- The dependency check runs at startup, so restart Claude Code after installing. The Dependencies tab in `/sandbox` lists which of `ripgrep`, `bubblewrap`, `socat` and the seccomp filter are missing.
- WSL2: check the version with `wsl -l -v`; `Sandboxing needs WSL2` or `Sandboxing requires WSL2` means WSL1. On WSL2, launching Windows binaries (`cmd.exe`, `powershell.exe`, anything under `/mnt/c/`) goes over a Unix socket, so it follows the Unix-socket settings; set `allowAllUnixSockets` to allow these launches (it opens every Unix socket).
- Ubuntu AppArmor: if Claude Code runs `/usr/bin/bwrap` and fails with the AppArmor message, `bwrap: setting up uid map: Permission denied` or `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`, add an AppArmor profile at `/etc/apparmor.d/bwrap` (profile `bwrap /usr/bin/bwrap flags=(unconfined)` with `userns,`), then `sudo systemctl reload apparmor` and restart Claude Code. If a different `bwrap` path runs, use `sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0` instead (all programs, until reboot).

# Limits and defaults

Claude Code runs the first `bwrap` on `PATH` unless managed settings name one in `sandbox.bwrapPath`. Before v2.1.310 the AppArmor restriction was not checked at startup.
