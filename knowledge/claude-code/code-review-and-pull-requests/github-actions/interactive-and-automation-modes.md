---
type: "Feature"
title: "Action interactive and automation modes"
description: "The action detects mode from the prompt input: no prompt waits for @claude, a prompt runs automatically; checks on who can trigger runs."
resource: "https://code.claude.com/docs/en/github-actions"
tags: [github-actions, modes, triggers, permissions]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless, cloud]
requires: ""
identifiers:
  - "prompt"
  - "trigger_phrase"
  - "allowed_non_write_users"
  - "allowed_bots"
  - "github_token"
  - "plugin_marketplaces"
  - "plugins"
  - "settings"
  - "claude_args"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-actions"
    resource: "https://code.claude.com/docs/en/github-actions"
    title: "Claude Code GitHub Actions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Interactive mode: workflow has no `prompt` input; Claude waits for the trigger phrase (`@claude` by default) in an issue or PR comment, PR review, or new issue body/title, and answers in a comment that it updates while working.
- Automation mode: a `prompt` input is given; Claude runs on any event (cron included) without a mention. Output goes to the run log by default; Claude can post to the issue/PR only if the prompt directs it and it has a tool that can.

# How to use it

`prompt` accepts a skill invocation. For a skill in `.claude/skills/`, run `actions/checkout` first and pass `/skill-name`. For a plugin skill, set `plugin_marketplaces` and `plugins` (`plugin-name@marketplace-name`, marketplace name from its own manifest) and pass `/plugin-name:skill-name`. Example review workflow: events `pull_request` types `opened, synchronize, ready_for_review, reopened`; `plugins: "code-review@claude-plugins-official"`; `prompt: "/code-review:code-review --comment ${{ github.repository }}/pull/${{ github.event.pull_request.number }}"`; `claude_args: '--allowedTools "mcp__github_inline_comment__create_inline_comment"'`. Without `--comment` nothing is posted. The `claude_args` line is needed because the inline-comment MCP server starts only if `--allowedTools` names it. Claude skips draft and closed PRs, ones it judges not to need review, and ones that already have a Claude comment; fork PRs on public repos get no secrets so the review runs only for same-repo branches.

# Limits and defaults

Two checks on the triggering actor run before Claude starts; failing either fails the run: write access on issue and PR events (override with `allowed_non_write_users` plus your own `github_token`; events with no user author such as `schedule` skip it), and a human actor on every event (bots rejected unless listed in `allowed_bots`; scheduled runs are attributed to the user who last changed the `cron`, so list that user if a bot).

# Notes

Plain-text prompts have no shell or GitHub API access until tools are granted via `--allowedTools` in `claude_args` or a `permissions.allow` rule in `settings`; a skill gets its `allowed-tools` frontmatter. Scheduled workflows run only from the default branch and in public repos are disabled after 60 days of repository inactivity. Example `mcp__github__list_commits,mcp__github__list_issues` for a daily report cron `0 9 * * *`.
