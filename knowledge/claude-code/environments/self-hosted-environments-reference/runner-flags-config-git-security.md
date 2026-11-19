---
type: "Reference"
title: "Runner CLI flags: secrets, git, security and logs"
description: "Runner flags for the environment secret, git handling, repo-settings guard, host config snapshot, proxy auth, auto mode lists and logging."
resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
tags: [self-hosted, runner, cli-flags, security, git]
kind: "cli_flag"
maturity: "beta"
since: ""
surfaces: [cloud, cli]
requires: ""
identifiers:
  - "--configure-git"
  - "--confine-repo-settings"
  - "SELF_HOSTED_RUNNER_CONFINE_REPO_SETTINGS"
  - "--debug-token-dir"
  - "SELF_HOSTED_RUNNER_DEBUG_TOKEN_DIR"
  - "--environment-secret-file"
  - "SELF_HOSTED_RUNNER_ENVIRONMENT_SECRET"
  - "--pool-secret-file"
  - "SELF_HOSTED_RUNNER_POOL_SECRET"
  - "--exec-path"
  - "SELF_HOSTED_RUNNER_EXEC_PATH"
  - "--git-host-rewrite"
  - "--git-ssh-rewrite"
  - "--hooks-dir"
  - "SELF_HOSTED_RUNNER_HOOKS_DIR"
  - "--host-config-snapshot"
  - "SELF_HOSTED_RUNNER_HOST_CONFIG_SNAPSHOT"
  - "--lock-to-account"
  - "SELF_HOSTED_RUNNER_LOCK_TO_ACCOUNT"
  - "--log-file"
  - "SELF_HOSTED_RUNNER_LOG_FILE"
  - "--proxy-authorization-command"
  - "SELF_HOSTED_RUNNER_PROXY_AUTHORIZATION_COMMAND"
  - "--proxy-authorization-file"
  - "SELF_HOSTED_RUNNER_PROXY_AUTHORIZATION_FILE"
  - "--push-outcome-on-release"
  - "SELF_HOSTED_RUNNER_PUSH_OUTCOME_ON_RELEASE"
  - "--remove-session-state"
  - "SELF_HOSTED_RUNNER_REMOVE_SESSION_STATE"
  - "--server-auto-mode-lists"
  - "SELF_HOSTED_RUNNER_SERVER_AUTO_MODE_LISTS"
  - "--trust-workspace"
  - "SELF_HOSTED_RUNNER_TRUST_WORKSPACE"
  - "--use-anthropic-git-proxy"
  - "CLAUDE_RUNNER_USE_GIT_PROXY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-reference"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-reference"
    title: "Self-hosted environments reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The remaining runner flags (see [lifecycle flags](./runner-flags-lifecycle.md)).

# How to use it

| Flag | Env var | Default | What it does |
| :- | :- | :- | :- |
| `--configure-git` | `SELF_HOSTED_RUNNER_CONFIGURE_GIT=1` | off | Global git identity, Anthropic commit signing, push negotiation (v2.1.257+), `Co-authored-by:` hooks |
| `--confine-repo-settings <mode>` | `SELF_HOSTED_RUNNER_CONFINE_REPO_SETTINGS` | `warn` | `warn`, `enforce`, `off`; flags repo settings granting access outside the workspace, setting env, or overriding sandbox/hooks posture (`sandbox.enabled: false`, `disableAllHooks`) |
| `--debug-token-dir <path>` | `SELF_HOSTED_RUNNER_DEBUG_TOKEN_DIR` | unset | Writes live tokens to disk; debug only |
| `--environment-secret-file <path>` | `SELF_HOSTED_RUNNER_ENVIRONMENT_SECRET` | required | File with the environment secret (or single-use work-order JWT for orchestrator-spawned runners). The env var carries the secret value itself, not a path. Deprecated `--pool-secret-file` / `SELF_HOSTED_RUNNER_POOL_SECRET` still work with a stderr notice; preview builds older than 2.1.216 only know those |
| `--exec-path <path>` | `SELF_HOSTED_RUNNER_EXEC_PATH` | own binary | Binary or wrapper script spawned per session |
| `--git-host-rewrite <from>=<to>` | none | unset | Rewrite clone host; repeatable; flag only |
| `--git-ssh-rewrite <host>` | none | unset | Clone over SSH (`git@<host>:`); repeatable; flag only |
| `--hooks-dir <path>` | `SELF_HOSTED_RUNNER_HOOKS_DIR` | unset | Lifecycle hook scripts |
| `--host-config-snapshot <mode>` | `SELF_HOSTED_RUNNER_HOST_CONFIG_SNAPSHOT` | `disk` | `disk` copies startup snapshot under `--base-dir` and verifies files against an in-memory digest (modified file fails session and runner refuses sessions until restart); `memory` caps at 64 MiB; falls back to memory if disk write fails; v2.1.271+ |
| `--lock-to-account <id>` | `SELF_HOSTED_RUNNER_LOCK_TO_ACCOUNT` | unset | Pre-lock to an email or `user_...` ID; never serves Claude Tag channel sessions |
| `--log-file <path>` | `SELF_HOSTED_RUNNER_LOG_FILE` | unset | Mirror logs to a `0600` file; needed for `doctor` to tail |
| `--proxy-authorization-command <command>` | `SELF_HOSTED_RUNNER_PROXY_AUTHORIZATION_COMMAND` | unset | Header from command stdout; needs HTTPS_PROXY/HTTP_PROXY; v2.1.238+ |
| `--proxy-authorization-file <path>` | `SELF_HOSTED_RUNNER_PROXY_AUTHORIZATION_FILE` | unset | Header from file; mutually exclusive with the command flag; v2.1.238+ |
| `--push-outcome-on-release` | `SELF_HOSTED_RUNNER_PUSH_OUTCOME_ON_RELEASE` | off | Best-effort push of outcome branches to `origin` on runner-initiated end; +30 s shutdown; git 2.29+ to resume |
| `--remove-session-state [bool]` | `SELF_HOSTED_RUNNER_REMOVE_SESSION_STATE` | off | Delete `<base-dir>/_sessions/` entries at session end (also drops failed-session debug logs); v2.1.268+ |
| `--server-auto-mode-lists <mode>` | `SELF_HOSTED_RUNNER_SERVER_AUTO_MODE_LISTS` | `no-allow` | `all`, `no-allow`, `none`; v2.1.295+ |
| `--trust-workspace [bool]` | `SELF_HOSTED_RUNNER_TRUST_WORKSPACE` | on | Honor repo-committed `permissions.allow` and `additionalDirectories`; false drops them (repo `sandbox.*` still applies) |
| `--use-anthropic-git-proxy` | `CLAUDE_RUNNER_USE_GIT_PROXY=1` | off | Anthropic-managed git for github.com; needs `--capacity 1`, git 2.32+, v2.1.267+; supersedes rewrite flags |

# Notes

Auto mode lists: the control plane may send three classifier lists with a session: `environment` (can allow more or less), `soft_deny` (blocks unless user asked or `allow` excepts), `allow` (exceptions to soft_deny). `no-allow` applies environment and soft_deny; `all` applies all three; `none` applies none (and drops soft_deny restrictions). No runner setting makes the control plane send lists; use `--log-level debug` to see `the server asked this runner to apply` or `the server did not ask this runner to apply the auto mode lists it sends`.
