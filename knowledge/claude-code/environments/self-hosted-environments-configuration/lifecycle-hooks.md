---
type: "Feature"
title: "Runner lifecycle hooks"
description: "checkout, post-session and command hooks in a hooks directory that replace stages of the runner's per-session pipeline."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, hooks, checkout, post-session, git]
kind: "hook"
maturity: "beta"
since: "2.1.280"
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise)"
identifiers:
  - "--hooks-dir"
  - "SELF_HOSTED_RUNNER_HOOKS_DIR"
  - "checkout"
  - "post-session"
  - "command"
  - "CLAUDE_RUNNER_REPO_URL"
  - "CLAUDE_RUNNER_REPO_REF"
  - "CLAUDE_RUNNER_CHECKOUT_PATH"
  - "CLAUDE_RUNNER_SESSION_ID"
  - "CLAUDE_RUNNER_SESSION_UUID"
  - "CLAUDE_RUNNER_API_BASE_URL"
  - "CLAUDE_RUNNER_SKIP_GIT_VERIFY"
  - "CLAUDE_RUNNER_EXIT_REASON"
  - "CLAUDE_RUNNER_WORKSPACE_PATHS"
  - "CLAUDE_RUNNER_DEBUG_LOG_PATH"
  - "--post-session-hook-timeout-sec"
  - "--kill-session-after-min"
  - "--configure-git"
  - "GIT_CONFIG_COUNT"
  - "GIT_CONFIG_KEY_n"
  - "GIT_CONFIG_VALUE_n"
  - "GIT_ALLOW_PROTOCOL"
  - "GIT_SSH_COMMAND"
  - "GIT_ASKPASS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Executable files with well-known names in a directory given by `--hooks-dir <path>` (or `SELF_HOSTED_RUNNER_HOOKS_DIR`). A missing hook falls through to built-in behavior. These run on the runner around the session and are distinct from Claude Code hooks, which run inside the session. Hooks run with the runner's privileges and session children share that UID, so mount the directory read-only or bake it into the image.

# How to use it

- **checkout**: runs per repository each time a session starts, resumes or requeues, replacing the built-in clone/fetch. Receives `CLAUDE_RUNNER_REPO_URL`, `CLAUDE_RUNNER_REPO_REF`, `CLAUDE_RUNNER_CHECKOUT_PATH` (folder `<repo-owner>-<repo>`, collisions get `-2`), session IDs, `CLAUDE_RUNNER_API_BASE_URL`, `CLAUDE_RUNNER_CLIENT_PLATFORM`, `CLAUDE_CODE_SESSION_ACCESS_TOKEN`. Must leave a working tree (detached HEAD ok) with a `.git`; for non-git sources set `CLAUDE_RUNNER_SKIP_GIT_VERIFY=1` and export results from `post-session`. No git credential is passed and `decode-token` is unavailable (no `CLAUDE_RUNNER_CLAUDE_BIN`); verify the JWT against the JWKS under `CLAUDE_RUNNER_API_BASE_URL`, or use host git auth. Failure on a push repository fails the session; on a read-only repository it is skipped with a `Skipped` step (session fails only if no repository remains).
- **post-session**: after the child exits, before teardown; your only chance to save uncommitted work (worktrees deleted at `--capacity` above one; canonical clone hard-reset at `--capacity 1`). Receives `CLAUDE_RUNNER_EXIT_REASON`, `CLAUDE_RUNNER_WORKSPACE_PATHS` (colon separated), `CLAUDE_RUNNER_DEBUG_LOG_PATH`, plus the session variables. Exit status never affects outcome. Cannot fire on abrupt termination (use a `PostToolUse` hook for periodic snapshots).
- **command**: replaces the child spawn after checkout; same environment as a wrapper; `--exec-path` wins if both are set. Always `exec` `"$CLAUDE_RUNNER_CLAUDE_BIN"` to keep version pinning.

`CLAUDE_RUNNER_EXIT_REASON` values: `completed`, `failed`, `interrupted` (released, startup timeout, server moved, archive/delete noticed by poll, draining, or `--kill-session-after-min` exceeded), `abandoned` (reserved, hook does not fire).

# Limits and defaults

- `--post-session-hook-timeout-sec` default 60 seconds, applied at every session end including shutdown.
- On v2.1.236+ an idle-after-turn or startup-timeout session is released only after the hook finishes; a session waiting on a user prompt is released first. v2.1.260+ applies this to `--kill-session-after-min`. Earlier versions always released first.
- v2.1.280+: runner fixes git settings for hook git via `GIT_CONFIG_COUNT`/`KEY_n`/`VALUE_n`: `core.hooksPath` `/dev/null`, `core.fsmonitor` empty, `GIT_ALLOW_PROTOCOL=https:http:ssh`, ignores `core.sshCommand` and `core.askPass`, fixed gpg program paths, signing only with `--configure-git`. A `[runner:git] lifecycle hooks:` startup line shows them. Credential helpers, `insteadOf` and filter drivers in session-writable config still apply, so mint hook credentials narrowly.

# Notes

Before v2.1.280 the runner set none of these git settings.
