---
type: "Reference"
title: "Sandbox core settings"
description: "sandbox object keys: enabled, failIfUnavailable, autoAllowBashIfSandboxed, excludedCommands, allowUnsandboxedCommands, ripgrep, bwrapPath, socatPath, ignoreViolations."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [sandbox, bash, isolation, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.324"
surfaces: [cli, headless]
requires: "macOS, Linux or WSL2; Linux needs bubblewrap and socat"
identifiers:
  - "sandbox"
  - "sandbox.enabled"
  - "sandbox.failIfUnavailable"
  - "sandbox.autoAllowBashIfSandboxed"
  - "sandbox.excludedCommands"
  - "sandbox.allowUnsandboxedCommands"
  - "sandbox.ignoreViolations"
  - "sandbox.ripgrep"
  - "sandbox.ripgrep.command"
  - "sandbox.ripgrep.args"
  - "sandbox.bwrapPath"
  - "sandbox.socatPath"
  - "dangerouslyDisableSandbox"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
  - "USE_BUILTIN_RIPGREP"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `sandbox` object isolates Bash commands from the filesystem, network and credentials on macOS, Linux and WSL2. Default unset (no sandbox). Sub-objects `filesystem`, `network`, `credentials` have their own concepts. When managed settings set a Boolean key such as `enabled` or `failIfUnavailable` it overrides developers; array keys merge across scopes.

# How to use it

| Key | Scope | Type | Default | What it does |
| :- | :- | :- | :- | :- |
| `sandbox.enabled` | Any file (limits on project/local) | Boolean | `false` | Turn on Bash sandboxing. The `/sandbox` panel writes it to `.claude/settings.local.json`; put it in `~/.claude/settings.json` for all projects |
| `sandbox.failIfUnavailable` | Any file | Boolean | `false` | `true`: exit with an error at startup when enabled but the sandbox cannot start (unsupported platform or failed dependency check). If it passes the check then fails to initialize the session keeps running and refuses each sandboxed command. An Anthropic-hosted environment may start with a warning and not enforce filesystem or network rules |
| `sandbox.autoAllowBashIfSandboxed` | Any file | Boolean | `false` (before v2.1.324 `true`) | Run sandboxed Bash without a permission prompt; `deny` rules and content-scoped `ask` rules like `Bash(git push *)` still apply, a bare `Bash` ask rule is skipped. `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` turns auto-allow off. For managed `true`, add to the highest-ranked managed source |
| `sandbox.excludedCommands` | Any file | array of command patterns | unset | Commands run outside the sandbox; same syntax as `Bash(...)` rule content; a pattern with no wildcard is an exact match |
| `sandbox.allowUnsandboxedCommands` | Any file | Boolean | `true` | `true`: Claude can retry a blocked command with the `dangerouslyDisableSandbox` parameter. `false`: parameter ignored (strict sandbox mode, `/sandbox` Overrides tab) |
| `sandbox.ignoreViolations` | Any file | object command substring to array of violation substrings | unset | Silences reports (not enforcement). Key `*` matches every command |
| `sandbox.ripgrep` | User or managed | object `{command, args}` | unset | Own ripgrep binary inside the sandbox; default is Claude Code's binary (bundled unless `USE_BUILTIN_RIPGREP` is `0`) |
| `sandbox.bwrapPath` | Managed | absolute path string | unset | Bubblewrap outside `PATH`; relative path dropped. Linux and WSL2 only |
| `sandbox.socatPath` | Managed | absolute path string | unset | `socat` outside `PATH`. Linux and WSL2 only |

```json
{ "sandbox": { "enabled": true, "autoAllowBashIfSandboxed": true, "excludedCommands": ["docker *"] } }
```

# Limits and defaults

- `excludedCommands` takes a Bash call out of the sandbox only if entries cover every command in it. Calls stay sandboxed when they contain: `sudo`, `eval` or `xargs` start; `cd`, `pushd`, `popd`; command substitution, subshell or control-flow blocks; a redirection or heredoc (other than `2>&1`); a command name from a variable; `git clone`, `git init`, `git worktree add`, `git worktree move`, `git bundle create` with an absolute, `~` or `..` path. Excluded commands still go through the permission flow; exclusion is a convenience, not a security boundary.
- With an admin-required sandbox, entries in `.claude/settings.json` and `.claude/settings.local.json` are ignored for `excludedCommands`; managed, `--settings` and user entries still apply and no managed-only lock covers this list.
- `allowUnsandboxedCommands: false` from managed settings or `--settings` makes the sandbox admin-required; in user settings it holds against a project `true` (v2.1.285+) but does not make it admin-required. Who approves a retry depends on permission mode and allow rules.
- On a platform without sandbox support Claude Code does not start when `failIfUnavailable` is on.
