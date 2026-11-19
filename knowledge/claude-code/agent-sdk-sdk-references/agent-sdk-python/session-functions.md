---
type: "Reference"
title: "Python session management functions"
description: "Synchronous helpers to list, read, rename, tag and fork stored sessions, plus the SDKSessionInfo shape."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [python, sessions, fork, resume, tags]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "list_sessions"
  - "get_session_messages"
  - "get_session_info"
  - "rename_session"
  - "tag_session"
  - "fork_session"
  - "SDKSessionInfo"
  - "SessionMessage"
  - "ForkSessionResult"
  - "include_worktrees"
  - "up_to_message_id"
  - "parent_tool_use_id"
  - "parent_agent_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Module-level synchronous functions in `claude_agent_sdk` for inspecting and managing past sessions without starting a query.

# How to use it

| Function | Signature (key params) | Behavior |
| :- | :- | :- |
| `list_sessions` | `directory=None, limit=None, offset=0, include_worktrees=True` | sorted by `last_modified` descending; omit `directory` to list all projects; with a git repo directory includes all worktree paths |
| `get_session_messages` | `session_id, directory=None, limit=None, offset=0` | returns `SessionMessage` list |
| `get_session_info` | `session_id, directory=None` | one `SDKSessionInfo` or `None`, without scanning the project dir |
| `rename_session` | `session_id, title, directory=None` | appends a custom-title entry; latest wins |
| `tag_session` | `session_id, tag, directory=None` | `None` clears the tag; tag is Unicode-sanitized; latest wins |
| `fork_session` | `session_id, directory=None, up_to_message_id=None, title=None` | copies the transcript to a new session; returns `ForkSessionResult` whose `session_id` is passed as `resume` |

`SDKSessionInfo` fields: `session_id`, `summary`, `last_modified` (ms since epoch), `file_size` (`None` for remote storage backends), `custom_title`, `first_prompt`, `git_branch`, `cwd`, `tag`, `created_at`.

`SessionMessage` fields: `type` (`"user"` or `"assistant"`), `uuid`, `session_id`, `message`, `parent_tool_use_id` (spawning `Agent` tool-use id for subagent messages), `parent_agent_id` (parent subagent id for nested subagents; needs Python Agent SDK 0.2.140+).

# Limits and defaults

- `rename_session` and `tag_session` raise `ValueError` for a non-UUID id or empty title/tag, and `FileNotFoundError` if the session is not found.
- `fork_session` raises `ValueError` for invalid UUIDs, an empty session or an `up_to_message_id` that matches nothing, and `FileNotFoundError` if not found. Default fork title is the original's title followed by `(fork)`.
- A fork does not carry the original's file checkpoints, so it cannot be rewound to earlier checkpoints.
