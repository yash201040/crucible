---
type: "Feature"
title: "Skills synced from claude.ai"
description: "Terminal sessions signed in with claude.ai download account skills to ~/.claude/skills/synced/; sync cadence, exclusions, naming and body handling."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, sync, claude-ai, namespaces]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.273"
surfaces: [cli, cloud, desktop, ide]
requires: "Sign-in with a claude.ai account via /login and feature-flag fetching"
identifiers:
  - "CLAUDE_CODE_SYNC_SKILLS"
  - "syncClaudeAiSkills"
  - "~/.claude/skills/synced/"
  - "~/.claude/skills/.trash/"
  - "anthropic-skills"
  - "/anthropic-skills:<name>"
  - "/skills"
  - "disableSkillShellExecution"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills enabled on your claude.ai account (yours, your organization's, Anthropic's such as `pdf` and `xlsx`) are downloaded in terminal sessions into `~/.claude/skills/synced/` in the background (v2.1.273 or later), then re-checked while the session runs; additions, edits and removals apply without restart. Downloads only, never uploads: local edits are not saved and a later sync can overwrite them. `/skills` lists them under `claude.ai sync`. `pdf` and `xlsx` always sync.

# How to use it

- Check cadence: about every 10 minutes while active, about every 40 minutes idle (checks within a few minutes of typing again if the last was over 10 minutes ago). Sync never delays startup; Claude waits for a skill's download only when invoking it.
- A short non-interactive run may finish before a new skill downloads. Set `CLAUDE_CODE_SYNC_SKILLS` to `1` to make a non-interactive run download and wait for the list (before v2.1.273 terminal sessions synced only in a `-p` run with this variable).
- Stop syncing: `syncClaudeAiSkills` to `false` in user settings; skills already synced move to `~/.claude/skills/.trash/` at next start. Organizations can turn off Skills on claude.ai or set the key in managed settings.
- Restart after `/login` mid-session to start syncing.

# Limits and defaults

No sync in: sessions not using a `/login` sign-in (API key, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN`, `apiKeyHelper`); sessions without feature-flag fetching (Bedrock, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`); bare mode or `--safe-mode`; sessions where managed settings lock skills to plugin sources or `--setting-sources` omits `user`. Earlier-synced skills stay on disk and load later even offline.

# Notes

- Names: invoke by `/<name>` or `/anthropic-skills:<name>`. If another command (built-in, bundled, any local or plugin skill, `.claude/commands/` file, MCP prompt) uses the short name, the synced skill runs only by its full name. Before v2.1.269 only the short name existed; v2.1.269-v2.1.280 listed all under full names; changed in v2.1.281. Comparison ignores case, spacing, invisible characters; look-alike letters from other alphabets count as different. These checks need v2.1.228.
- `anthropic-skills` namespace is reserved in every session: a folder, frontmatter `name`, commands file or saved workflow with that name does not load (startup notice). A plugin named `anthropic-skills` loads. An MCP server named `anthropic-skills` connects but its prompts are not listed as commands.
- Frontmatter: applies in every session (`allowed-tools` goes through normal permissions; ignored under `allowManagedPermissionRulesOnly`); display text is sanitized (v2.1.228 or later).
- Body: cloud sessions keep local behavior; Cowork on desktop replaces `!` lines with the `disableSkillShellExecution` placeholder; terminal and VS Code do not run `!` commands, attach `@` files, or substitute `${CLAUDE_PROJECT_DIR}` and `${CLAUDE_SESSION_ID}` (v2.1.228 or later).
- If your organization turns Skills off, downloaded skills move to `.trash/`, recoverable until the retention sweep.
