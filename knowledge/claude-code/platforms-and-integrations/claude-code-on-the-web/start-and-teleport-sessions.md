---
type: "Feature"
title: "Start cloud sessions with --cloud and teleport back"
description: "claude --cloud creates cloud sessions from the terminal, local repos can be bundled and uploaded, and --teleport pulls a session into the terminal."
resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
tags: [cloud, teleport, parallel, upload]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, cloud]
requires: "claude.ai sign-in (claude auth login); same account; not third-party providers"
identifiers:
  - "--cloud"
  - "--remote"
  - "--teleport"
  - "/teleport"
  - "/tp"
  - "/tasks"
  - "CCR_FORCE_BUNDLE"
  - "worktree.sparsePaths"
  - "--permission-mode plan"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-code-on-the-web"
    resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
    title: "Use Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude --cloud "<task>"` creates a new cloud session for the current repository; the VM clones the GitHub remote at the current branch (not the local checkout), so push first. It works with one repository at a time. `--remote` is a deprecated alias. Each `--cloud` command creates an independent session, so several can run in parallel. The CLI shows a setup checklist and queues messages typed during provisioning. Handoff from CLI is one-way: `--teleport` pulls cloud to terminal, but a terminal session cannot be pushed to the cloud (the Desktop app can, from its Open in menu). `--remote-control` is unrelated.

# How to use it

```bash
claude --cloud "Fix the authentication bug in src/auth/login.ts"
CCR_FORCE_BUNDLE=1 claude --cloud "Run the test suite and fix any failures"
claude --teleport            # picker
claude --teleport <session-id>
```

Teleport alternatives: `/teleport` or `/tp` in a session; `/tasks` then `t`; Open in > Terminal on claude.ai/code; `/teleport` inside the cloud session prints the command. `--resume` does not list cloud sessions. Teleport loads the conversation and branch; compacted history is not copied; the terminal copy stays local (use `/remote-control` to keep steering). Plan locally with `claude --permission-mode plan`, commit the plan and push, then run `--cloud`.

| Teleport requirement | Detail |
| - | - |
| Clean git state | stash prompt if uncommitted changes |
| Correct repository | same repo, not a fork; SSH host aliases ask to confirm |
| Branch available | must be pushed |
| Same account | same claude.ai account |

# Limits and defaults

- Local repo upload (no remote, or GitHub App not installed): bundle includes history across all branches plus uncommitted changes to tracked files. On macOS, Linux and WSL, uncommitted changes to credential-like files (`.env`, `*.tfvars`, `id_rsa`, `*.pem`) and git-filter (Git LFS) files are left out with a `Left on this machine:` notice; native Windows uploads tracked changes as they are.
- Bundle must be a git repo with at least one commit and under 100 MB (fallback to current branch, then a single squashed snapshot; fails if still too large). Untracked files are excluded. Needs git 2.31+ on macOS/Linux/WSL; unsupported layouts (submodule, `--separate-git-dir`, `--shared`, `--reference`, `core.worktree`, reftable, sparse-checkout worktrees incl. `worktree.sparsePaths`, git config includes inside the tree) fail with `Not uploading this working tree:`. Partial clones via `git clone --filter` upload as a snapshot without history.
- Teleport fetch never waits for terminal input (passwords, passphrases, new SSH host prompts fail).
- `Branch <name> is not on GitHub`: session still starts from a pushed commit or default branch.
