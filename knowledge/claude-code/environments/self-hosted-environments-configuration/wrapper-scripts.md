---
type: "Feature"
title: "Runner wrapper scripts"
description: "A script the runner starts in place of the Claude Code binary for each session, with a documented environment and fd rules."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, wrapper, credentials, runner, environment]
kind: "mixed"
maturity: "beta"
since: "2.1.229"
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise); runner host on Linux or macOS"
identifiers:
  - "--exec-path"
  - "SELF_HOSTED_RUNNER_EXEC_PATH"
  - "CLAUDE_RUNNER_CLAUDE_BIN"
  - "CLAUDE_CODE_SESSION_ACCESS_TOKEN"
  - "CCR_SESSION_ACCOUNT_EMAIL"
  - "CLAUDE_RUNNER_CLIENT_PLATFORM"
  - "CLAUDE_CODE_REMOTE_SESSION_ID"
  - "CLAUDE_CODE_REMOTE_SESSION_UUID"
  - "CLAUDE_CODE_REMOTE_SLACK_THREAD_URL"
  - "CLAUDE_CODE_REMOTE_SLACK_THREAD_TS"
  - "CLAUDE_CODE_REMOTE_SLACK_CHANNEL_ID"
  - "CLAUDE_SESSION_INGRESS_TOKEN_FILE"
  - "CLAUDE_CONFIG_DIR"
  - "CLAUDE_CODE_REMOTE_MCP_CONFIG"
  - "CLAUDE_CODE_REMOTE"
  - "CLAUDE_CODE_ENVIRONMENT_KIND"
  - "ANTHROPIC_BASE_URL"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "CLAUDE_RUNNER_ALIVE_EVERY_MS"
  - "--remove-session-state"
  - "--system-prompt-file"
  - "--append-system-prompt-file"
  - "--append-system-prompt"
  - "decode-token"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A wrapper script is started by the runner in place of the Claude Code binary every time a session starts, resumes or is requeued. Use it for per-session credentials scoped to the creator, environment secrets, language toolchains, or resource limits. End it with `exec "$CLAUDE_RUNNER_CLAUDE_BIN" "$@"` so signals and exit codes propagate.

# How to use it

`claude self-hosted-runner --environment-secret-file /etc/claude/environment-secret --base-dir '<writable-dir>' --exec-path /etc/claude/session-wrapper.sh` (or env `SELF_HOSTED_RUNNER_EXEC_PATH`).

| Variable | What it holds |
| :- | :- |
| `CLAUDE_CODE_SESSION_ACCESS_TOKEN` | Session JWT (prefix `sk-ant-cc-`), `act` claim names the creator; only the initial value, refreshes arrive on stdin |
| `CCR_SESSION_ACCOUNT_EMAIL` | Creator email from unverified `act.email`; label-only, PII, can be unset |
| `CLAUDE_RUNNER_CLIENT_PLATFORM` | Surface such as `web_claude_ai`, `desktop_app`, `ios`, `claude_code_cli`, `scheduled_trigger`; analytics only, v2.1.229+ |
| `CLAUDE_RUNNER_CLAUDE_BIN` | Absolute path to the runner's own binary |
| `CLAUDE_CODE_REMOTE_SESSION_ID` / `_UUID` | Session ID in `cse_...` form / UUID form |
| `CLAUDE_CODE_REMOTE_SLACK_THREAD_URL`, `_THREAD_TS`, `_CHANNEL_ID` | Claude Tag Slack thread info; each can be unset independently |
| `CLAUDE_SESSION_INGRESS_TOKEN_FILE` | File with current JWT, kept fresh; carry over if rebuilding env or attachment downloads break |
| `CLAUDE_CONFIG_DIR` | Per-session config dir under `<base-dir>/_sessions/` (kept unless `--remove-session-state`) |
| `CLAUDE_CODE_REMOTE_MCP_CONFIG`, `CLAUDE_CODE_REMOTE`, `CLAUDE_CODE_ENVIRONMENT_KIND` | Carry all three if rebuilding env; v2.1.299+ |
| `ANTHROPIC_BASE_URL` | Delivered per session; do not override |
| `CLAUDE_CODE_OAUTH_TOKEN` | Inference token, about 30 minute lifetime, rotated over stdin; treat as bearer credential |
| `CLAUDE_RUNNER_ALIVE_EVERY_MS` | Child liveness interval; carry over, v2.1.309+ |

- Use `decode-token` (`"$CLAUDE_RUNNER_CLAUDE_BIN" self-hosted-runner decode-token`) to read JWT claims (argument, `CLAUDE_CODE_SESSION_ACCESS_TOKEN`, or stdin). Key credentials on `act.sub` (`user:` for humans; `agent:` for service identities), use `jq -re`. Email gating should verify the token.
- Under `set -u` expand potentially unset variables with a default (`"${VAR:-}"`). Quote all arguments; never substitute values into `eval` or `sh -c` strings.
- Permission mode and tools: append after `"$@"`, e.g. `--permission-mode auto`, `--allowed-tools "Bash(bazel *) mcp__internal__*"` (list flags accumulate), `--disallowed-tools`, `--mcp-config <file>`.

# Limits and defaults

- stdin is the runner's control channel; fd 3 carries activity signals (idle and startup timeouts); fd 4 and 5 are reserved from v2.1.309 (use 6 to 9). Backgrounding the child with a bare `&` severs stdin and every API call fails with `401 authentication_error` after about 30 minutes; save stdin with `exec 9<&0` and re-attach `<&9`.
- stderr tail is posted to the session on non-zero exit: no secrets, no `set -x`.
- System prompts arrive as `--system-prompt-file` / `--append-system-prompt-file` (v2.1.281+; earlier inline text). Appended file flag replaces the server's; on v2.1.283+ pass only your own text via `--append-system-prompt` (both used). v2.1.281/282 error `Cannot use both --append-system-prompt and --append-system-prompt-file`. A single Linux argument is limited to 128 KB (`Argument list too long`, exit 126).

# Notes

Wrappers run on the runner host and see more of the environment than lifecycle hooks do.
