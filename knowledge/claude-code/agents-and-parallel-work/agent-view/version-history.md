---
type: "Reference"
title: "Agent view version history"
description: "Versions in which agent view flags and behaviours were added or changed, v2.1.139 to v2.1.323."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, versions, changelog]
kind: "mixed"
maturity: "research-preview"
since: "2.1.139"
surfaces: [cli]
requires: ""
identifiers:
  - "--cwd"
  - "--strict-mcp-config"
  - "worktree.bgIsolation"
  - "--agent"
  - "/model"
  - "--restricted"
  - "claude attach"
  - "claude logs"
  - "claude rm"
  - "--discard-unpushed"
  - "--force-remove-worktree"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Older Claude Code versions may differ; `claude agents` rejects flags it does not support with `unknown option`.

| Version | Change |
| :- | :- |
| v2.1.139 | Agent view introduced as a research preview |
| v2.1.141 | `claude agents --cwd` |
| v2.1.142 | `claude agents` accepts `--permission-mode`, `--model`, `--effort`, `--dangerously-skip-permissions`, `--settings`, `--add-dir`, `--plugin-dir`, `--mcp-config`, `--strict-mcp-config` |
| v2.1.143 | `worktree.bgIsolation` setting; `--allow-dangerously-skip-permissions` |
| v2.1.145 | Voice dictation in peek reply and dispatch inputs |
| v2.1.157 | `claude agents --agent`; dispatched sessions honor the `agent` setting |
| v2.1.161 | Row summaries show `done/total` for parallel work items; peek names the longest-running item |
| v2.1.172 | `/model` in dispatch input sets a session-scoped override |
| v2.1.174 | Background sessions stop inheriting gateway variables from the supervisor's launch shell |
| v2.1.191 | `--bg` with unknown `--agent` fails the launch |
| v2.1.195-v2.1.198 | Windows carry-over; `Notification` hook types `agent_needs_input`/`agent_completed`; `--bg` with `-p` rejected; draft PR by isolated sessions; `Move to background and exit`; single `←` press backgrounds; `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF`; default names for unnamed interactive sessions |
| v2.1.199-v2.1.207 | Low-memory note; `/color` carried; `←` count in footer; PR linking broadened; peek panel redesign; supervisor restarts idle sessions onto new version; `CLAUDE_CODE_EXTRA_BODY` reaches sessions; `/rename` persists across restarts |
| v2.1.208-v2.1.216 | Replies saved when service unreachable; delete keeps worktree with unpushed commits or other claimers; `/fork` copies into new background session (v2.1.212) and bare `/resume` picker; `/install-github-app` and `/mcp` allowed when attached (v2.1.213) and unattended gives Needs input (v2.1.216); `Ctrl+X` twice deletes even if stop fails; `--agent` restore on resume |
| v2.1.217-v2.1.227 | PR badge always a hyperlink; `←` confirm presses; `/status` `Session kind` row and `/fork` isolation instruction (v2.1.221); trust dialog for `claude agents` (v2.1.225); delete keeps worktree in use by another live session (v2.1.227) |
| v2.1.233-v2.1.248 | GitLab `!1234` labels; vim `Esc`; supervisor start retries (v2.1.246); `/fork` copies full conversation from a copy; `Shift+Enter` newline and `Ctrl+Enter`; branch-lock on worktree; 48-hour stopped rule; `--restricted` (v2.1.248) |
| v2.1.251-v2.1.257 | Cloud gateway forwarding (v2.1.251); `--resume --bg` same-ID or copy with `note:`; `permissions.defaultMode` for `←`-opened view; keybindings.json support; `approve message from` row for held cross-session messages; stash persistence |
| v2.1.260-v2.1.268 | `claude rm --discard-unpushed` (v2.1.260); `claude rm --force-remove-worktree` (v2.1.268); `←` confirm timing fix |
| v2.1.274-v2.1.290 | Relaunched view keeps dispatch defaults; `--setting-sources` carried (v2.1.281); workspace trust check for `claude --bg` (v2.1.281); `n:` filter and peek-reply command timing (v2.1.287); `Ctrl+F`, `Alt+↑/↓` (v2.1.288); name arguments for `claude attach`/`claude logs` and instant `/model`, `/effort`, `/rename`, `/usage` peek replies (v2.1.290) |
| v2.1.295-v2.1.323 | No auto-start of supervisor on exit and `/loop` `Ctrl+C`/`Esc` rules (v2.1.295); prompt entered while backgrounding is stopped and kept in history (v2.1.296); `--bg` parsing rule and `/effort`, `/fast` in dispatch input (v2.1.299); `Ctrl+Y` restore (v2.1.323) |
