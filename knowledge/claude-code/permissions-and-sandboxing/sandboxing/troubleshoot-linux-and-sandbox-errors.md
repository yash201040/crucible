---
type: "Reference"
title: "Sandbox troubleshooting: Linux, containers, /sandbox errors"
description: "Fixes for user namespaces, bubblewrap in containers, AppArmor, the Sandbox is required refusal and /sandbox panel save errors."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, troubleshooting, linux, containers]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.305"
surfaces: [cli]
requires: "Linux or WSL2 for most entries"
identifiers:
  - "sandbox.allowNestedUserNamespaces"
  - "sandbox.enableWeakerNestedSandbox"
  - "sandbox.failIfUnavailable"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
  - "--no-sandbox"
  - "sandbox.autoAllowBashIfSandboxed"
  - "/status"
  - "/feedback"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors and fixes specific to Linux, containers, unattended-style refusals and the `/sandbox` command.

# How to use it

- **Chromium, rootless Podman, `unshare` fail** (default: sandboxed commands cannot create user namespaces): symptoms `No usable sandbox!`, `unshare: unshare failed: Operation not permitted` (with `allowAllUnixSockets` possibly `No space left on device`), Podman `cannot clone: Operation not permitted` or `read-only file system`. Fixes: Chromium/Electron `--no-sandbox`; exclude the command (e.g. `podman *`; match the test command, not the browser); or set `sandbox.allowNestedUserNamespaces: true` in `~/.claude/settings.json` (not project), requires v2.1.305+, insufficient alone for Podman or Buildah. A command beginning with `unshare` stays sandboxed whatever `excludedCommands` says. In a session with `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` set to `1`, every command is sandboxed and these settings have no effect. Warning: `allowNestedUserNamespaces` turns off a boundary; code can run outside the sandbox, and even auto-allow can run it without a prompt.
- **Bubblewrap in an unprivileged container**: `Can't mount proc on /newroot/proc: Operation not permitted`. Set `sandbox.enableWeakerNestedSandbox: true` (bind-mounts the existing `/proc`; use only when the outer container provides isolation; exposes process info).
- **Ubuntu AppArmor**: message `Ubuntu's AppArmor restriction on user namespaces stops bubblewrap here`; until fixed, commands run unsandboxed under regular permissions, or Claude Code refuses to start if `failIfUnavailable` is true. See [Linux setup](./linux-wsl2-setup.md). Check with `sysctl kernel.apparmor_restrict_unprivileged_userns` (1 = on); otherwise report with `/feedback`.
- **`Sandbox is required` refusals** (when `failIfUnavailable` set and the sandbox fails after startup): each sandboxed command is refused and the session keeps running, never falling back unsandboxed. Messages: `Sandbox is required but failed to initialize: <reason>` (take the step: `Restart to retry.` or `Fix the sandbox settings to retry`) and `Sandbox is required (sandbox.failIfUnavailable) and stopped being available in this session: <reason>` (Linux/WSL2, dependency found missing; fix and restart). Excluded commands and commands typed at `!` keep running (the latter refused in background sessions); `dangerouslyDisableSandbox` retries are ignored. In a Linux session with `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` set, excluded and typed commands are refused too. Excluded commands writing to an `allowWrite` path outside the working directory go through the regular permission flow.
- **`/sandbox` fails `Sandbox settings can't be changed here`**: `sandbox.enabled`, `sandbox.autoAllowBashIfSandboxed` or `sandbox.allowUnsandboxedCommands` is set above local settings level; the panel saves to `.claude/settings.local.json`, which cannot override higher levels. Run `/status` and read `Setting sources`: `Command line arguments` (change `--settings` content) or `Enterprise managed settings` (ask your administrator).
- **`/sandbox` prints `Sandbox settings not changed`**: could not write `.claude/settings.local.json`. For `EACCES`, `EPERM`, `EROFS` start in a writable project; for `Invalid JSON syntax in settings file` fix the JSON. Alternative: set `sandbox.enabled: true` in `~/.claude/settings.json` (regular permissions mode; add `sandbox.autoAllowBashIfSandboxed: true` for auto-allow); it takes effect at the next shell command.
