---
type: "Release Digest"
title: "Headless, SDK and automation (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on print mode, stream-json, SDK hosts, self-hosted runner, unattended and CI use."
resource: "https://code.claude.com/docs/en/changelog"
tags: [headless, sdk, automation, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "--kill-session-after-min"
  - "/reload-plugins"
  - "/advisor"
  - "--permission-prompts none"
  - "claude plugin validate --json"
  - "CLAUDE_STREAM_IDLE_TIMEOUT_MS"
  - "claude self-hosted-runner --configure-git"
  - "--restricted"
  - "CLAUDE_CODE_RESTRICTED"
  - "--client-label"
  - "SELF_HOSTED_RUNNER_CLIENT_LABEL"
  - "--defer-shutdown-max-min"
  - "--proxy-authorization-command"
  - "--proxy-authorization-file"
  - "CLAUDE_CODE_PROJECT_DIR_NAME"
  - "modelOverrides"
  - "--base-dir"
  - "claude remote-control --continue"
  - "claude self-hosted-runner"
  - "mcp_server_errors"
  - "--forward-subagent-text"
  - "set_model"
  - "CLAUDE_CODE_FORWARD_SUBAGENT_TEXT"
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "-p"
  - "/config key=value"
  - "/goal"
  - "parentSettingsBehavior"
  - "plugin_errors"
  - "localSettings"
  - "mcp_authenticate"
  - "redirectUri"
  - "CLAUDE_CODE_FORK_SUBAGENT"
  - "claude ultrareview"
  - "--json"
  - "--output-format stream-json"
  - "TRACEPARENT"
  - "TRACESTATE"
  - "claude -p --resume"
  - "--name"
  - "/rename"
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
| 2.1.260 | 2026-09-03 | Self-hosted runner --kill-session-after-min releases a session only waiting on its user (paused, resumable) instead of killing it | `--kill-session-after-min` |
| 2.1.260 | 2026-09-03 | /reload-plugins and a text form of /advisor work in headless (-p, Agent SDK) sessions; idle CPU of -p/SDK sessions reduced | `/reload-plugins`, `/advisor` |
| 2.1.259 | 2026-09-02 | --permission-prompts none denies anything that would prompt, for unattended headless hosts, while the permission mode keeps deciding | `--permission-prompts none` |
| 2.1.259 | 2026-09-02 | claude plugin validate --json gives a machine-readable report; headless first turn starts up to 50 ms sooner once MCP connects | `claude plugin validate --json` |
| 2.1.257 | 2026-09-01 | Liveness reporting to SDK hosts while a response is held by gateway keep-alives; claude self-hosted-runner --configure-git enables push negotiation | `CLAUDE_STREAM_IDLE_TIMEOUT_MS`, `claude self-hosted-runner --configure-git` |
| 2.1.248 | 2026-08-27 | --restricted (or CLAUDE_CODE_RESTRICTED=1) removes command and code tools and WebFetch, confines file tools to the working directory, refuses bypassPermissions and ignores user, project and local settings | `--restricted`, `CLAUDE_CODE_RESTRICTED` |
| 2.1.248 | 2026-08-27 | claude self-hosted-runner --client-label (or SELF_HOSTED_RUNNER_CLIENT_LABEL) overrides the registered label (default hostname) | `--client-label`, `SELF_HOSTED_RUNNER_CLIENT_LABEL` |
| 2.1.246 | 2026-08-25 | Non-interactive sessions (-p, SDK, cloud) automatically continue a response cut off by a server error, connection loss or stall |  |
| 2.1.238 | 2026-08-20 | claude self-hosted-runner --defer-shutdown-max-min keeps serving attached sessions on SIGTERM then parks them; --proxy-authorization-command and --proxy-authorization-file for egress proxies | `--defer-shutdown-max-min`, `--proxy-authorization-command`, `--proxy-authorization-file` |
| 2.1.236 | 2026-08-19 | SIGTERM in print/SDK mode no longer records an interrupted turn; process still exits with code 143 |  |
| 2.1.234 | 2026-08-17 | CLAUDE_CODE_PROJECT_DIR_NAME lets hosts with a per-session config directory pick a short transcript directory name | `CLAUDE_CODE_PROJECT_DIR_NAME` |
| 2.1.233 | 2026-08-14 | Print mode writes a [claude-code:unrecognized_model] line to stderr for an unknown model ID; map it with modelOverrides | `modelOverrides` |
| 2.1.229 | 2026-08-12 | Server-supplied hooks supported for self-hosted runner sessions; self-hosted runner on Windows needs --base-dir; claude remote-control --continue resumes the latest Remote Control session | `--base-dir`, `claude remote-control --continue` |
| 2.1.224 | 2026-08-07 | claude self-hosted-runner turns your machines or containers into places where Claude Code web, mobile and desktop sessions run (Team and Enterprise plans) | `claude self-hosted-runner` |
| 2.1.219 | 2026-07-24 | Headless stream-json init event lists mcp_server_errors for --mcp-config entries skipped by validation; --forward-subagent-text shows depth-2+ subagents | `mcp_server_errors`, `--forward-subagent-text` |
| 2.1.212 | 2026-07-17 | Headless/SDK sessions apply a set_model control request mid-turn | `set_model` |
| 2.1.211 | 2026-07-15 | --forward-subagent-text and CLAUDE_CODE_FORWARD_SUBAGENT_TEXT include subagent text and thinking in stream-json output | `--forward-subagent-text`, `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` |
| 2.1.208 | 2026-07-14 | CLAUDE_CODE_PROCESS_WRAPPER runs every self-spawn of agent view and the background service through a required wrapper; print/SDK tool rounds up to 7x faster with many MCP tools | `CLAUDE_CODE_PROCESS_WRAPPER` |
| 2.1.183 | 2026-06-19 | Warning on stderr in print mode when the requested model is deprecated or auto-updated, including models in agent frontmatter | `-p` |
| 2.1.181 | 2026-06-17 | /config key=value sets any setting from the prompt, in interactive, -p and Remote Control | `/config key=value` |
| 2.1.144 | 2026-05-19 | SDK/headless MCP startup pre-wait overlaps startup (up to 2s faster) |  |
| 2.1.139 | 2026-05-11 | /goal works in interactive, -p and Remote Control | `/goal` |
| 2.1.133 | 2026-05-07 | parentSettingsBehavior admin key (first-wins or merge) lets SDK managedSettings join the policy merge | `parentSettingsBehavior` |
| 2.1.128 | 2026-05-04 | stream-json init.plugin_errors includes --plugin-dir load failures; SDK hosts get a localSettings suggestion for Bash prompts | `plugin_errors`, `localSettings` |
| 2.1.121 | 2026-04-28 | SDK mcp_authenticate supports redirectUri; CLAUDE_CODE_FORK_SUBAGENT=1 works in non-interactive sessions | `mcp_authenticate`, `redirectUri`, `CLAUDE_CODE_FORK_SUBAGENT` |
| 2.1.120 | 2026-04-28 | claude ultrareview [target] runs /ultrareview non-interactively from CI, findings to stdout, --json raw, exit 0 or 1 | `claude ultrareview`, `--json` |
| 2.1.111 | 2026-04-16 | Headless stream-json init event includes plugin_errors when plugins are demoted for unsatisfied dependencies | `--output-format stream-json`, `plugin_errors` |
| 2.1.110 | 2026-04-15 | SDK/headless sessions read TRACEPARENT and TRACESTATE from the environment for trace linking | `TRACEPARENT`, `TRACESTATE` |
| 2.1.101 | 2026-04-10 | claude -p --resume <name> accepts titles from /rename or --name; SDK query() cleans up subprocess and temp files on break or await using | `claude -p --resume`, `--name`, `/rename` |

# Not found in the documentation pages

These identifiers occur only in the release notes, not in the saved documentation pages:

- `claude plugin validate --json`
- `claude self-hosted-runner --configure-git`
- `/config key=value`
- `mcp_authenticate`
- `redirectUri`
