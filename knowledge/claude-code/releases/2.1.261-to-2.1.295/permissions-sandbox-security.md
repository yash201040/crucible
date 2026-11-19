---
type: "Release Digest"
title: "Permissions, sandbox and security, 2.1.261 to 2.1.295"
description: "Release-note entries for permission modes, auto mode, sandbox, managed policy and security changes from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [permissions, auto-mode, sandbox, security, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "permissions.defaultMode"
  - "CLAUDE_CODE_AUTO_MODE_SERVER"
  - "CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT"
  - "--dangerously-skip-permissions"
  - "--permission-mode"
  - "sandbox.network.allowLocalBinding"
  - "sandbox.excludedCommands"
  - "allowUnsandboxedCommands"
  - "allowManagedDomainsOnly"
  - "allowedProviders"
  - "availableModelsMatch"
  - "deniedModels"
  - "allowClaudeInChromeWithManagedMcp"
  - "CLAUDE_CODE_DISABLE_ATTACHMENTS"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "OTEL_LOG_*"
  - "forceLoginMethod"
  - "forceLoginGatewayUrl"
  - "forceLoginOrgUUID"
  - "gatewayInternalNetworks"
  - "Skill(anthropic-skills:<name>)"
  - "Skill(claude-ai:*)"
  - "PreToolUse"
  - "pyright"
  - "ps"
  - "Bash"
  - "PowerShell"
  - "WebFetch(domain:claude.ai)"
  - "Artifact"
  - "/permissions"
  - "/insights"
  - "tool.check"
  - "GH_HOST"
  - "GH_REPO"
  - "ALLUSERSPROFILE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) about permission prompts, auto mode and its classifier, the sandbox, managed settings that limit what projects may do, and security hardening. Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | `onFailure: "block"` hooks fail closed (see hooks digest). | `onFailure` |
| 2.1.292 | 2026-10-06 | Security: PreToolUse hook approvals and auto mode no longer bypass the permission prompt for reads from network (UNC) paths. | `PreToolUse` |
| 2.1.292 | 2026-10-06 | With strict sandbox mode set in user, managed or `--settings`, an interpreter command with an env prefix like `FOO=bar python3 app.py` runs unprompted. | |
| 2.1.290 | 2026-10-05 | Bash asks before running `pyright` (no longer read-only); more forms of `ps` ask for approval. | `pyright`, `ps` |
| 2.1.290 | 2026-10-05 | `CLAUDE_CODE_DISABLE_ATTACHMENTS` can no longer be set by a repository's `.claude/settings.json` or `settings.local.json`; shell, user, managed still can. | `CLAUDE_CODE_DISABLE_ATTACHMENTS` |
| 2.1.290 | 2026-10-05 | Claude in Chrome cannot be turned on by a project's settings files; use `--chrome`, `/chrome` or user settings. | `--chrome` |
| 2.1.290 | 2026-10-05 | `/status` and doctor warn when managed settings ignore user sandbox `allowRead` paths or allowed domains; managed-settings symlink outside its folder warns. | |
| 2.1.290 | 2026-10-05 | Built-in `gh api` in cloud sessions refuses a host other than github.com in `GH_HOST` or `GH_REPO` (use `--hostname` or a full URL). | `GH_HOST`, `GH_REPO` |
| 2.1.290 | 2026-10-05 | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` also skips the startup connection warm-up. | `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` |
| 2.1.288 | 2026-10-02 | Auto mode: a conversation too long for the client-side classifier is compacted instead of prompting for or failing each tool call. | |
| 2.1.288 | 2026-10-02 | Client-side auto mode classifier ignores an `ANTHROPIC_DEFAULT_SONNET_MODEL` pin naming Sonnet 5.5 or Opus 5.5 and uses Sonnet 5. | `ANTHROPIC_DEFAULT_SONNET_MODEL` |
| 2.1.287 | 2026-10-01 | Shell writes through a repo-committed symlink onto a sensitive file or out of the tree wait for a person; whole-tool `Bash` allow rules and allowing hooks prompt for shell writes to files file tools refuse. | `Bash` |
| 2.1.287 | 2026-10-01 | Windows startup warning when denying Bash also turns off PowerShell. | |
| 2.1.285 | 2026-09-29 | `allowedProviders` managed setting limits which API providers a machine may use. | `allowedProviders` |
| 2.1.285 | 2026-09-29 | Team/Enterprise sessions (and unknown plan) withhold WebFetch until organization policy loads if it failed at startup. | |
| 2.1.285 | 2026-09-29 | Project settings cannot widen or disable an admin-required sandbox, replace the proxy behind a managed deny list, extend a strict allowlist or reopen managed read-denies. | |
| 2.1.285 | 2026-09-29 | Windows: project and local settings `env` no longer set `ALLUSERSPROFILE`, `SystemDrive`, `CommonProgramFiles` variables. | `ALLUSERSPROFILE` |
| 2.1.285 | 2026-09-29 | `/config chrome=true` directs to the panel; `/claude-api` cannot be run from Remote Control clients. | |
| 2.1.284 | 2026-09-28 | New "Yes, but ask again next time" answer to auto mode's prompt for a read outside the working directories. | |
| 2.1.284 | 2026-09-28 | Interactive terminal and VS Code sessions start in auto mode when no permission mode is configured, on every plan and provider; `permissions.defaultMode` overrides. | `permissions.defaultMode` |
| 2.1.284 | 2026-09-28 | Artifact publishing refuses a file on a network share unless on a mapped drive added with `--add-dir`; auto-memory notes neutralize invisible characters and markup-imitating tags. | `--add-dir` |
| 2.1.283 | 2026-09-25 | `availableModelsMatch` (`"exact"`) and `deniedModels` managed settings; interactive sessions on third-party providers or telemetry off start in auto mode. | `availableModelsMatch`, `deniedModels` |
| 2.1.283 | 2026-09-25 | Windows PowerShell tool no longer lets `cmd /c rd`, `rmdir`, `del`, `erase` delete drive roots or home. | `PowerShell` |
| 2.1.282 | 2026-09-24 | Auto mode uses the server-side classifier by default on a direct Anthropic API connection when telemetry is off (`CLAUDE_CODE_AUTO_MODE_SERVER=0` opts out). | `CLAUDE_CODE_AUTO_MODE_SERVER` |
| 2.1.282 | 2026-09-24 | `sandbox.excludedCommands` ignores project/local entries when managed settings or `--settings` set `allowUnsandboxedCommands: false` or managed `allowManagedDomainsOnly: true`. | `sandbox.excludedCommands`, `allowUnsandboxedCommands`, `allowManagedDomainsOnly` |
| 2.1.282 | 2026-09-24 | Project and local settings ignore OpenTelemetry variables that enable export, set endpoint or capture content (`CLAUDE_CODE_ENABLE_TELEMETRY`, `OTEL_LOG_*`). | `CLAUDE_CODE_ENABLE_TELEMETRY`, `OTEL_LOG_*` |
| 2.1.282 | 2026-09-24 | Windows/WSL: an invalid or unreadable admin policy (HKLM, `managed-settings.json`) blocks user-writable HKCU and WSL `/etc/claude-code`. | |
| 2.1.282 | 2026-09-24 | `allowClaudeInChromeWithManagedMcp` managed setting lets `claude --chrome` run alongside exclusive `managed-mcp.json`. | `allowClaudeInChromeWithManagedMcp`, `managed-mcp.json` |
| 2.1.281 | 2026-09-23 | Where classifier review runs server-side, read-only and sandboxed shell commands also wait for it and are blocked when flagged; `CLAUDE_CODE_AUTO_MODE_SERVER` applies on direct API (`0` opt out, `1` opt in). | `CLAUDE_CODE_AUTO_MODE_SERVER` |
| 2.1.281 | 2026-09-23 | Dangerous `rm` prompt in `--dangerously-skip-permissions` and auto mode waits 2 minutes then denies with a rewrite hint (`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT=1` turns off); check extended to variable-based targets. | `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`, `--dangerously-skip-permissions` |
| 2.1.281 | 2026-09-23 | Sandbox guidance on macOS points to `sandbox.network.allowLocalBinding`; `/insights` recommends auto mode with an estimate of prompts it could have handled. | `sandbox.network.allowLocalBinding`, `/insights` |
| 2.1.280 | 2026-09-22 | `PermissionRequest` hooks: agent-type hooks no longer run; `/permissions` delete confirmations default to No. | `PermissionRequest`, `/permissions` |
| 2.1.278 | 2026-09-19 | Auto mode defaults to the server-side classifier (no classifier overhead charge) for Claude API, Enterprise, Bedrock, Vertex, Foundry and gateways; `/status` gains an `Auto mode server` row. | `CLAUDE_CODE_AUTO_MODE_SERVER` |
| 2.1.277 | 2026-09-18 | Subagent results are marked as subagent output so their text cannot pass as the session's instructions; prompt invisible-Unicode characters stripped. | |
| 2.1.275 | 2026-09-17 | Claude in Chrome in auto mode skips the per-site check for classifier-approved calls. | |
| 2.1.273 | 2026-09-15 | Auto mode on Bedrock, Vertex, Foundry uses the local classifier by default (`CLAUDE_CODE_AUTO_MODE_SERVER=1` for server-side); reverted 2.1.268 Read/Edit deny checks on unanalyzable Bash lines. | `CLAUDE_CODE_AUTO_MODE_SERVER` |
| 2.1.271 | 2026-09-14 | In auto mode, `!` shell commands in skills follow default-mode rules; a subagent reports back via a classifier-reviewed hand-back call; per-command `allowed_domains` for Bash/PowerShell/Monitor. | `allowed_domains` |
| 2.1.268 | 2026-09-10 | `WebFetch` deny/ask rules no longer apply to Artifact reads/updates (use an `Artifact` rule or `WebFetch(domain:claude.ai)`); `gatewayInternalNetworks` managed setting; auto mode denial names the blocking rule. | `Artifact`, `WebFetch(domain:claude.ai)`, `gatewayInternalNetworks` |
| 2.1.261 | 2026-09-04 | Auto mode treats a link packing content into a public diagram renderer's URL as an upload; `forceLoginMethod: "gateway"` ignores leftover API key/login; dangerous-`rm` check covers positional parameters. | `forceLoginMethod` |

# Not found in the documentation pages

- `Skill(anthropic-skills:<name>)`
- `Skill(claude-ai:*)`
- `GH_REPO`
- `ALLUSERSPROFILE`
