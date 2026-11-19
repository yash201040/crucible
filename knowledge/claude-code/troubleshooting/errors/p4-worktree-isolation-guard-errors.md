---
type: "Reference"
title: "Worktree isolation guard blocks"
description: "Blocks when a worktree-isolated session or subagent writes or runs a command through an unresolvable, network-shaped or main-checkout path."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, worktrees, isolation, bash, subagents]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.217"
surfaces: [cli]
requires: ""
identifiers:
  - "Bash"
  - "PowerShell"
  - "Monitor"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The worktree-isolation guard checks writes and command working directories in any session isolated in a worktree (interactive or background) and in worktree-isolated subagents. It resolves symlinks first and blocks an operation that could reach the shared checkout. Before v2.1.217 it compared path spellings only, so a write through a symlink or a UNC or `/net` path could land in the shared checkout.

# How to use it

| Block | Trigger | What happens |
|---|---|---|
| `This write was blocked because the path is spelled in a form that cannot be safely resolved` | Symlink storing a raw dot segment, network-share or device-namespace shape, unreadable ancestor directory | Claude retries with the direct symlink-free path; a blocked command ends `re-run the command from its direct symlink-free path`. Repeats usually mean a committed symlink whose target has `..`; edit the real path |
| `This write was blocked because the path is network-shaped` | UNC (`\\server\share`) or `/net` automount path while the checkout is local; isolating cannot unblock | Use the local plainly-spelled path |
| `This session is isolated in the worktree <path>, but this command ...` | Bash, PowerShell or Monitor command: working directory resolved to the shared checkout or a different worktree; git pointed at the main checkout; or git use cannot be verified from the text (e.g. `${!name}` indirection, `${ command; }` substitution) | Claude splits it into plain commands run from the worktree; to act on the main checkout, run it yourself outside the session |

# Notes

For a blocked file edit the conversation shows only `Error editing file`; the full text is in the transcript view (`Ctrl+O`). Blocked commands print it in their output.
