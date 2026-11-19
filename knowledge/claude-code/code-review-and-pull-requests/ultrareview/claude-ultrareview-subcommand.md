---
type: "Reference"
title: "claude ultrareview subcommand for CI"
description: "Non-interactive ultrareview that blocks until findings print to stdout, with flags and exit codes 0, 1 and 130."
resource: "https://code.claude.com/docs/en/ultrareview"
tags: [headless, ci, subcommand, exit-codes]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli, headless]
requires: "claude.ai auth and usage-credits configuration as /code-review ultra"
identifiers:
  - "claude ultrareview"
  - "--json"
  - "--timeout"
  - "--post"
  - "--no-post"
  - "--trust-workspace"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "ultrareview"
    resource: "https://code.claude.com/docs/en/ultrareview"
    title: "Find bugs with ultrareview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude ultrareview` starts the same review as `/code-review ultra` from CI or a script, blocks until the remote review finishes, and prints findings to stdout. Progress goes to stderr so stdout stays parseable. `claude -p '/code-review ultra'` does not return findings: it launches the cloud review and exits without waiting (and stops without launching if it would bill usage credits). Use the subcommand in scripts.

# How to use it

```bash
claude ultrareview
claude ultrareview 1234
claude ultrareview origin/main
claude ultrareview 1234 --trust-workspace
```

| Flag | What it does |
| - | - |
| `--json` | print raw `bugs.json` payload instead of formatted findings |
| `--timeout <minutes>` | max wait for the review; default 45 |
| `--post` | post findings to the PR as one comment (v2.1.227+) |
| `--no-post` | default; do not post (v2.1.227+) |
| `--trust-workspace` | trust the current folder for this run only, no value; put the PR number or base before it (v2.1.309+) |

Exit codes: 0 completed (with or without findings); 1 failed to launch, stopped, cloud session errored, timeout, or folder not trusted (including answering n, Enter or Ctrl-C at the trust question); 130 Ctrl-C while launching, waiting or posting.

# Limits and defaults

- Running the subcommand is the consent for the whole-repository fallback and the billing/terms prompt. If Claude runs it for you (for example via Bash), the whole-repository review is refused.
- When it cannot ask `Trust <folder>? [y/N]` (CI, output to file) it exits with `Error: Workspace not trusted`; add `--trust-workspace`. Trust only code you trust: git and Claude Code can run programs named in git config and project settings. To review an untrusted PR, run it from a trusted branch; the PR is cloned in the cloud.
- If the subcommand exits before findings arrive they never reach the terminal; the cloud review may keep running; rerunning starts a new review (uses a free run or bills credits).
- With `--post`, failure, stop or timeout posts nothing; if the comment fails, the reason goes to stderr and findings stay on stdout.
- For automatic PR reviews without a CLI step, the separate Code Review integration posts inline PR comments.
