---
type: "Guide"
title: "Cloud session context, commands, sharing and expiry"
description: "Permission modes, supported commands, auto-compaction variables, subagents, sharing, archiving, environment expiry and what is not restored."
resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
tags: [cloud, context, sharing, expiry, subagents]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cloud, web]
requires: ""
identifiers:
  - "/compact"
  - "/context"
  - "/clear"
  - "/model"
  - "/effort"
  - "/fast"
  - "/config"
  - "/autocompact"
  - "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
  - "SearchPlugins"
  - "SuggestPluginInstall"
  - "permissions.deny"
  - "allowManagedPermissionRulesOnly"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-code-on-the-web"
    resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
    title: "Use Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Behavior of a running cloud session.

# How to use it

- Permission mode is chosen from the mode dropdown at creation and while running; a reopened expired session or a session released by an idle self-hosted runner resumes in the mode it had.
- Commands: only text-output built-ins work; terminal-only ones like `/plugin` or `/resume` do not. `/model`, `/effort`, `/color`, `/rename` take an argument (such as `/model sonnet`). `/fast` toggles fast mode if available (Claude Code v2.1.271+ in the environment). `/config` in the browser opens Settings; to change a cloud setting use an environment variable on the environment or commit to the repo's `.claude/settings.json`. `/compact [focus]`, `/context`, `/clear` all work.
- Auto-compaction: cloud sessions set `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` themselves (overrides a user value). Change the window with `CLAUDE_CODE_AUTO_COMPACT_WINDOW` in environment variables, or `/autocompact` with a token count where the variable is not set.
- Subagents work as locally; `.claude/agents/` in the repo load automatically (outside a project's threads). Agent teams are off by default; enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in environment variables.
- Plugin suggestions: Claude may show a card with an **Add** button; Add enables the plugin on the claude.ai account. Turn off by denying `SearchPlugins` and `SuggestPluginInstall` under `permissions.deny` in the repo's `.claude/settings.json` (ignored when managed settings set `allowManagedPermissionRulesOnly`; put them in managed settings then).
- Queued messages can be taken back with the X before Claude reads them.
- Sharing: Enterprise/Team visibility Private or Team (repo access verification on by default; Slack sessions auto-shared with Team); Max/Ultra/Pro visibility Private or Public (verification off by default). Archive hides from the sidebar (Archived tab at claude.ai/code/sessions, Unarchive); Delete is permanent.
- Review: **Changes** card shows lines added and removed; diff view supports inline comments and Compare against; diffs use raw git blobs (no diff drivers or textconv). A file may be missing from the list for changes not committed/pushed; ask Claude to commit and push.

# Limits and defaults

- Environment expired: sessions stop after inactivity and the VM is reclaimed; waiting on an MCP connector approval counts as inactive. Reopening from claude.ai/code provisions a fresh VM. Restored: conversation history. Not restored: running shell commands, subagents (some can be resumed), session-scoped scheduled tasks and `/loop`.
- Errors: `Session creation failed` (check status.claude.com, retry after a minute); "Your new session couldn't start" (prompt returned); "Can't rewind to this message" on self-hosted runners older than v2.1.246.
- From v2.1.274 through v2.1.289 the sign-in error text differed.
