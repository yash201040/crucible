---
type: "Reference"
title: "Refusing to use a worktree and resume messages"
description: "The Refusing to use <path> as an isolation worktree error, its recoveries, and resume messages in interactive, -p and SDK runs including startup_failure_reason."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, errors, resume, sdk, stream-json]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.274"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "Refusing to use <path> as an isolation worktree"
  - "launch from the parent checkout"
  - "Run the resume from the project checkout"
  - "it cannot be resumed or re-entered"
  - "it contains the protected checkout"
  - "its recorded path"
  - "Your worktree <path> no longer exists"
  - "Could not verify your worktree <path> this time"
  - "Did not re-enter your worktree <path>"
  - "Could not re-enter your worktree <path>"
  - "Error: cannot resume into worktree <path>: ...This session was not started."
  - "Error: could not verify worktree <path> for this resume, so the resume was aborted..."
  - "Notice: the worktree <path> for this session no longer exists..."
  - "--output-format stream-json"
  - "error_during_execution"
  - "startup_failure_reason"
  - "worktree_unverified"
  - "worktree_resume_refused"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Refusing to use <path> as an isolation worktree` means Claude Code checked the directory's git identity before adopting it as a session's or subagent's isolated checkout and declined (creating, entering or reusing). Usually the git metadata resolves into the main checkout (`.git` file pointing at the main `.git`, or a `core.worktree` redirect), where `git reset --hard` would hit the main checkout; also refused when a `.git` entry cannot be read. The refused directory is left in place.

# How to use it

Recoveries by message ending:

| Message says | Action |
| :- | :- |
| `launch from the parent checkout` / `Run the resume from the project checkout` | Launch from the main checkout; no recreation needed |
| `it cannot be resumed or re-entered` | Recreate it (work stays on disk); resuming from the parent checkout also works |
| `it contains the protected checkout` | Refused directory is a parent of the main checkout (e.g. home); do not delete; change the worktree path (hook output or `EnterWorktree` target) |
| `the protected checkout <path> has a .git entry that could not be examined` / `has git metadata that could not be resolved` | Problem is the main checkout's metadata (permissions, git `dubious ownership`); repair it and retry; do not delete the worktree. Before v2.1.302 with git 2.56+ a stray `.git` file (bad `gitdir:` path) also caused this: update Claude Code or delete that file |
| `its recorded path` | Restore access to the path; otherwise recreate at a local path (network-path worktrees are not resumed) |
| Any other ending | Follow the message (e.g. remove a `core.worktree` redirect); address the named cause before deleting; salvage changes first |

Interactive resume messages: `Your worktree <path> no longer exists` (continues without isolation, binding cleared); `Could not verify your worktree <path> this time` (transient; binding kept, resume again); `Did not re-enter your worktree <path>` (refused as unsafe; binding cleared; includes the specific refusal); `Could not re-enter your worktree <path>` (cannot vouch from launch location; binding kept). If you suppress transcript writes, the clear is not recorded and the message says it will re-check later.

# Limits and defaults

- In `-p` mode and Agent SDK resumes, every refusal except a gone worktree stops the resume with a stderr error instead of continuing without isolation. Shapes: `Error: cannot resume into worktree <path>: ...This session was not started.` (for Did not re-enter; the binding is cleared before exit, so the next resume continues without isolation; before v2.1.260 the clear was not written and retries kept failing; with transcript writes suppressed the error says the command will be refused again and names `--fork-session` and a new conversation); `Error: could not verify worktree <path> for this resume, so the resume was aborted...`; `Error: ...The worktree binding is kept.`; and for a gone worktree `Notice: the worktree <path> for this session no longer exists...` (continues).
- With `--output-format stream-json` the refusal also arrives on stdout as a `result` message with subtype `error_during_execution` whose `errors` array has the same text (before v2.1.260 no `result` message). `startup_failure_reason` is `worktree_unverified` for the could-not-verify error and `worktree_resume_refused` for the cannot-resume and binding-is-kept errors (field absent before v2.1.274).
