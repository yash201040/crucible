---
type: "Release Digest"
title: "Permissions, sandbox and security (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on permission rules and modes, auto mode, sandbox settings and hardening."
resource: "https://code.claude.com/docs/en/changelog"
tags: [permissions, sandbox, auto-mode, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "Read"
  - "claudeMd"
  - "sandbox.allowUnsandboxedCommands"
  - "permissions.blockReadsOutsideWorkingDirectories"
  - "defaultMode"
  - "managedSourcesBehavior"
  - "sandbox.credentials.awsPairs"
  - "sandbox.ripgrep"
  - "additionalDirectories"
  - "--add-dir"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_TMPDIR"
  - "/permissions"
  - "Monitor"
  - "/add-dir"
  - "sandbox.bwrapPath"
  - "sandbox.socatPath"
  - "extract"
  - "onExtractNoMatch"
  - "maskClaims"
  - "awsPairs"
  - "sigv4"
  - "network.tlsTerminate"
  - "mode: mask"
  - "sandbox.network.strictAllowlist"
  - "sandbox.filesystem.disabled"
  - "claude auto-mode reset"
  - "--yes"
  - "--dangerously-skip-permissions"
  - "CLAUDE_CODE_ENABLE_AUTO_MODE"
  - "disableAutoMode"
  - "autoMode"
  - "--permission-mode manual"
  - "autoMode.classifyAllShell"
  - "sandbox.credentials"
  - "sandbox.allowAppleEvents"
  - "Agent(model:opus)"
  - "SendMessage"
  - "acceptEdits"
  - "autoMode.hard_deny"
  - "allowManagedDomainsOnly"
  - "allowManagedReadPathsOnly"
  - "blockedMarketplaces"
  - "autoMode.allow"
  - "autoMode.soft_deny"
  - "autoMode.environment"
  - "wslInheritsWindowsSettings"
  - "sandbox.network.deniedDomains"
  - "--enable-auto-mode"
  - "CLAUDE_CODE_CERT_STORE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.260 | 2026-09-03 | Reverted the 2.1.259 change applying Read() deny rules to Bash arguments; permission rules with text after the closing parenthesis are reported as invalid; managed CLAUDE.md (claudeMd) no longer triggers the approval dialog | `Read`, `claudeMd` |
| 2.1.260 | 2026-09-03 | Commands typed at the ! bash-mode prompt run outside the sandbox even with sandbox.allowUnsandboxedCommands false | `sandbox.allowUnsandboxedCommands` |
| 2.1.257 | 2026-09-01 | Auto mode Containment Escape rule stops auto-approving cloud metadata credential fetches, egress evasion and cross-tenant reach; permissions.blockReadsOutsideWorkingDirectories option on first outside read | `permissions.blockReadsOutsideWorkingDirectories` |
| 2.1.257 | 2026-09-01 | defaultMode bypassPermissions in project settings is ignored (use user, managed settings or --permission-mode); managedSourcesBehavior merge takes sandbox.credentials.awsPairs and sandbox.ripgrep whole; --add-dir, /add-dir and additionalDirectories refuse network paths | `defaultMode`, `managedSourcesBehavior`, `sandbox.credentials.awsPairs`, `sandbox.ripgrep`, `additionalDirectories`, `--add-dir` |
| 2.1.251 | 2026-08-28 | Server-managed settings that weaken sandbox isolation or terminate TLS need approval; ANTHROPIC_CUSTOM_HEADERS credential or routing headers from managed or project settings need approval; project env cannot set CLAUDE_CONFIG_DIR, CLAUDE_CODE_TMPDIR, TMPDIR, TMP, TEMP | `ANTHROPIC_CUSTOM_HEADERS`, `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_TMPDIR` |
| 2.1.251 | 2026-08-28 | Claude in Chrome browser actions always pass Claude Code permission checks |  |
| 2.1.248 | 2026-08-27 | Managed settings: timeout, MCP startup-mode and stream-watchdog env vars no longer trigger the approval prompt |  |
| 2.1.246 | 2026-08-25 | Startup warning for Bash allow rules with a wildcard before the subcommand such as Bash(git * main); Auto mode tab in /permissions | `/permissions` |
| 2.1.236 | 2026-08-19 | macOS sandbox wildcard read-deny rules take precedence inside allowed read regions; auto mode sets aside Monitor allow rules and its git status check resists status.showUntrackedFiles=no | `Monitor` |
| 2.1.234 | 2026-08-17 | Windows NT-namespace paths rejected in remote file reads, session restore, CLAUDE.md includes, workflow scripts, uploads; /permissions and /add-dir open mid-turn | `/permissions`, `/add-dir` |
| 2.1.233 | 2026-08-14 | Reverted 2.1.232 Bash permission changes for Cygwin symlinks and input redirections |  |
| 2.1.232 | 2026-08-13 | Bash input redirections (< file) permission-checked on all platforms; GitLab token families redacted; sandbox.ripgrep honored only from user, managed and --settings; Linux sandbox protected-path bypass hardened; cross-session socket directory hardened | `sandbox.ripgrep`, `sandbox.bwrapPath`, `sandbox.socatPath` |
| 2.1.229 | 2026-08-12 | Sandbox network domain lists bracket IPv6 literals; ambiguous spellings fail closed and are flagged by /doctor |  |
| 2.1.224 | 2026-08-07 | Sandbox credential masking: extract, onExtractNoMatch, decode jwt with maskClaims, awsPairs and sigv4 re-signing; need network.tlsTerminate and honored only from user, managed or --settings | `extract`, `onExtractNoMatch`, `maskClaims`, `awsPairs`, `sigv4`, `network.tlsTerminate` |
| 2.1.221 | 2026-08-04 | Sandbox credential files mode mask on Linux and WSL (deny on macOS); auto-mode permission checks reuse cached prefix | `mode: mask` |
| 2.1.219 | 2026-07-24 | sandbox.network.strictAllowlist denies non-allowlisted hosts for sandboxed commands without prompting | `sandbox.network.strictAllowlist` |
| 2.1.218 | 2026-07-22 | Plan mode with auto lets the classifier judge Bash the analyzer cannot prove read-only; dangerous-rm, background-& and suspicious Windows path checks go to the auto-mode classifier |  |
| 2.1.216 | 2026-07-20 | sandbox.filesystem.disabled skips filesystem isolation but keeps network egress control; /rewind no longer follows symlinks or hard links | `sandbox.filesystem.disabled` |
| 2.1.214 | 2026-07-18 | docker commands with daemon-redirect flags prompt; file -m and -f need permission; deny and ask rules keep any-depth dir/** matching |  |
| 2.1.212 | 2026-07-17 | claude auto-mode reset restores default auto mode configuration (--yes skips confirmation) | `claude auto-mode reset`, `--yes` |
| 2.1.211 | 2026-07-15 | Always-allow rules save at the repository root so worktree approvals persist |  |
| 2.1.210 | 2026-07-14 | Startup warning for Write(path), NotebookEdit(path), Glob(path) rules (use Edit or Read) |  |
| 2.1.208 | 2026-07-14 | Catastrophic removals with command substitution prompt even under --dangerously-skip-permissions and auto mode | `--dangerously-skip-permissions` |
| 2.1.207 | 2026-07-11 | Auto mode needs no CLAUDE_CODE_ENABLE_AUTO_MODE on Bedrock, Vertex, Foundry (disableAutoMode disables); autoMode no longer read from .claude/settings.local.json | `CLAUDE_CODE_ENABLE_AUTO_MODE`, `disableAutoMode`, `autoMode` |
| 2.1.205 | 2026-07-08 | Auto mode blocks transcript tampering and asks before rm -rf on an unresolved variable; background task notifications state no human input occurred |  |
| 2.1.200 | 2026-07-03 | default permission mode renamed Manual; --permission-mode manual and defaultMode manual accepted | `--permission-mode manual`, `defaultMode` |
| 2.1.193 | 2026-06-25 | autoMode.classifyAllShell routes all Bash/PowerShell through the classifier; denial reasons in transcript and /permissions | `autoMode.classifyAllShell` |
| 2.1.187 | 2026-06-23 | sandbox.credentials blocks sandboxed commands from reading credential files and secret env vars | `sandbox.credentials` |
| 2.1.183 | 2026-06-19 | Auto mode blocks git reset --hard, checkout -- ., clean -fd, stash drop, commit --amend of others' commits, terraform/pulumi/cdk destroy unless asked |  |
| 2.1.181 | 2026-06-17 | sandbox.allowAppleEvents lets sandboxed macOS commands send Apple Events | `sandbox.allowAppleEvents` |
| 2.1.178 | 2026-06-15 | Tool(param:value) permission rule syntax matches tool input parameters, e.g. Agent(model:opus) | `Agent(model:opus)` |
| 2.1.166 | 2026-06-06 | Messages relayed via SendMessage carry no user authority; deny rules accept glob tool names ("*" denies all) | `SendMessage` |
| 2.1.160 | 2026-06-02 | Prompt before writing shell startup files and ~/.config/git/; acceptEdits prompts before build-tool config files like .npmrc | `acceptEdits` |
| 2.1.158 | 2026-05-30 | Auto mode available on Bedrock, Vertex, Foundry for Opus 4.7 and 4.8 with CLAUDE_CODE_ENABLE_AUTO_MODE=1 | `CLAUDE_CODE_ENABLE_AUTO_MODE` |
| 2.1.152 | 2026-05-27 | Auto mode no longer requires opt-in consent |  |
| 2.1.136 | 2026-05-08 | settings.autoMode.hard_deny rules block unconditionally | `autoMode.hard_deny` |
| 2.1.133 | 2026-05-07 | sandbox.bwrapPath and sandbox.socatPath managed settings for custom binaries (Linux/WSL) | `sandbox.bwrapPath`, `sandbox.socatPath` |
| 2.1.126 | 2026-05-01 | --dangerously-skip-permissions bypasses prompts for .claude/, .git/, .vscode/ and shell config writes (catastrophic removals still prompt); allowManagedDomainsOnly and allowManagedReadPathsOnly security fix | `allowManagedDomainsOnly`, `allowManagedReadPathsOnly` |
| 2.1.121 | 2026-04-28 | --dangerously-skip-permissions no longer prompts for .claude/skills, agents, commands writes |  |
| 2.1.119 | 2026-04-23 | PowerShell commands auto-approvable; blockedMarketplaces enforces hostPattern and pathPattern | `blockedMarketplaces` |
| 2.1.118 | 2026-04-23 | autoMode.allow, soft_deny, environment accept $defaults to extend built-ins; wslInheritsWindowsSettings policy key | `autoMode.allow`, `autoMode.soft_deny`, `autoMode.environment`, `wslInheritsWindowsSettings` |
| 2.1.113 | 2026-04-17 | sandbox.network.deniedDomains; deny rules match commands wrapped in env, sudo, watch, ionice, setsid; Bash(find:*) allow no longer approves -exec or -delete | `sandbox.network.deniedDomains` |
| 2.1.111 | 2026-04-16 | Auto mode for Max on Opus 4.7 and no --enable-auto-mode needed; read-only globs and cd project-dir && no longer prompt | `--enable-auto-mode` |
| 2.1.101 | 2026-04-10 | OS CA certificate store trusted by default (CLAUDE_CODE_CERT_STORE=bundled for bundled CAs only) | `CLAUDE_CODE_CERT_STORE` |
