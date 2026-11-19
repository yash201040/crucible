---
type: "Reference"
title: "Managed settings and policy startup errors"
description: "Startup failures from server-managed and file-based managed settings: load failures, approval, blocked default model, allowedProviders, unparseable documents, invalid hooks."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, managed-settings, policy, startup, enterprise]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, headless, desktop]
requires: "organization managed settings"
identifiers:
  - "deniedModels"
  - "availableModels"
  - "availableModelsMatch"
  - "allowedProviders"
  - "managed-settings.json"
  - "managed-settings.d"
  - "claude auth login"
  - "claude doctor"
  - "/status"
  - "claude plugin"
  - "claude gateway"
  - "deniedMcpServers"
  - "allowedMcpServers"
  - "disableClaudeAiConnectors"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors and warnings when organization policy (server-managed settings fetched from Anthropic, or managed settings files, macOS profiles, Windows registry) cannot load or blocks a session. Several fail closed: the session does not start. In non-interactive mode and background sessions the message is printed and the process exits with status 1.

# How to use it

| Message | Meaning | Fix |
|---|---|---|
| `Remote managed settings failed to load` (also `still loading`, `did not load`, `have now loaded`) | Eligible session could not fetch or apply server-managed settings; the line ends `using cached policy` (cached policy minus withheld env variables) or `no remote policy applied` (nothing cached, or last fetch over 24 hours ago). Cause `no setting in the server response could be applied as written` (before v2.1.282 `server returned invalid settings`). Shown interactively and in Desktop Code tab; before v2.1.248 only in the debug log | Act on the named cause (network to `api.anthropic.com`, auth via `/status`); admin fixes settings; `claude doctor` |
| `Claude Code couldn't reach Anthropic to load your organization's settings` | Session start blocked until org settings load (dialog `Claude Code can't start this session yet` retries). Fixes by cause: allow HTTPS to `api.anthropic.com/api/claude_code/policy_limits` and `api.anthropic.com/api/claude_code/settings`; `Your Claude session has expired` needs `claude auth login` | Retry now; see causes |
| `Managed settings were not approved; exiting without applying them.` | Declined the security approval dialog; not remembered | Restart and approve |
| `Your organization's managed settings need your approval, which couldn't be asked for here` | A `claude plugin` command with no keyboard and no `/dev/tty` | Run `claude` in a terminal and approve (approval stored in the configuration directory; match user and `CLAUDE_CONFIG_DIR`) |
| `Claude Code can't start: your organization's managed settings block the default model (...)` | `deniedModels` blocks the default and all its step-down fallbacks, or `availableModels` with `availableModelsMatch` `"exact"` omits it. Users cannot widen managed lists | Admin updates `availableModels` or `deniedModels` |
| `Your organization's managed settings allow Claude Code to use: ...` | `allowedProviders` excludes the session's provider or an unpinned endpoint; empty list or only unrecognized entries means no provider at all | Follow `To continue:`; admins see `Admins:` lines |
| `Managed settings document could not be parsed as a JSON object; none of its settings are in effect` | Exit 1 at startup even if another source is valid, in every mode incl. `claude doctor`. Sources: `managed-settings.json` or a `managed-settings.d` drop-in, macOS profile (`per-user` or `device-level managed preferences`), Windows registry `HKLM\SOFTWARE\Policies\ClaudeCode\Settings`. Empty `managed-settings.json` counts as `{}`. An unreadable `managed-settings.d/` gives `Managed settings drop-in directory could not be read:` | Admin fixes or removes it |
| `Unable to read managed policy settings.` | A source exists but could not be read for a reason like I/O error (not OS permission denial, which starts without that source). Exit at startup; sign-in, API requests of running sessions and `claude gateway` are refused with an `allowedProviders` variant. Before v2.1.285 only claude.ai or Console-credential sessions exited and permission denials produced it too | Admin fixes the `Detail:` line |
| `Managed settings contain invalid entries, including PreToolUse/PermissionRequest hooks that are NOT loaded` | `-p` stderr block: a hook entry (unknown `type`, declared outside `hooks`) is dropped; if the `hooks` field is listed as ignored, none from that source run. `parent managed settings` as source means the embedding application passed it. Before v2.1.300 listed under `Managed settings failed to load; policies from the failed source are NOT in effect:` | Fix or remove each entry |
| `MCP server <name> is blocked by enterprise managed policy` | See [MCP connection errors](./p3-mcp-connection-and-auth-errors.md) | |

# Limits and defaults

- Cached remote policy: not applied when the last fetch is more than 24 hours old.

# Notes

An unparseable policy document is a fail-closed condition: settings that cannot be parsed cannot be enforced.
