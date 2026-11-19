---
type: "Release Digest"
title: "Sessions, context and memory, 2.1.261 to 2.1.295"
description: "Release-note entries for resume, background sessions, compaction, send-now, AGENTS.md, auto-memory and Remote Control sessions from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [sessions, resume, memory, context, compaction, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/resume"
  - "claude --resume"
  - "--continue"
  - "/autocompact"
  - "/memory"
  - "/recap"
  - "/btw"
  - "/rewind"
  - "/tasks"
  - "/loop"
  - "ctrl+enter"
  - "ctrl+x ctrl+s"
  - "AGENTS.md"
  - "CLAUDE.md"
  - "MEMORY.md"
  - "/config"
  - "claude --desktop"
  - "claude --remote-control"
  - "/remote-control"
  - "claude purge"
  - "claude project purge"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN"
  - "--system-prompt-snapshot"
  - "__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__"
  - "claude auth status --json"
  - "configDirectory"
  - "/focus"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) about session resume and continuation, queued and send-now messages, compaction and context, CLAUDE.md/AGENTS.md loading and auto-memory. Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | Large-file upload failure with no reason: Claude reports it instead of shrinking the file. | |
| 2.1.292 | 2026-10-06 | Ctrl+C draft recovery: a cleared prompt stays reachable with Up after a slash command or sent message. | |
| 2.1.290 | 2026-10-05 | Resuming large sessions keeps timers, input and rendering responsive while the transcript loads. | |
| 2.1.288 | 2026-10-02 | Pressing Up on an empty prompt after Ctrl+C restores the draft, including pasted text and images; `claude project purge` renamed `claude purge` (old name works with notice); `/autocompact` saved per model. | `claude purge`, `claude project purge`, `/autocompact` |
| 2.1.287 | 2026-10-01 | `/memory` left/right arrows flip settings such as Auto-memory. | `/memory` |
| 2.1.285 | 2026-09-29 | Auto-memory can no longer be turned on from a background session or a session started by Claude Code's own tools (turning off still works). | `/memory` |
| 2.1.285 | 2026-09-29 | `/resume` and `claude --resume <id> "prompt"` on a background-running session open it and send the prompt as its next turn; `claude --desktop` opens the desktop app on the current directory or on a session with `--continue` / `--resume <id>`. | `/resume`, `claude --resume`, `claude --desktop` |
| 2.1.284 | 2026-09-28 | `/recap` declines when relayed from a chat thread, routine or webhook. | `/recap` |
| 2.1.284 | 2026-09-28 | Auto-memory loading neutralizes invisible characters and Claude-markup-imitating tags in `MEMORY.md` and recalled notes; Ultracode now a separate toggle. | `MEMORY.md` |
| 2.1.283 | 2026-09-25 | Compaction spinner timer starts at compaction begin and counts summary tokens as they stream. | |
| 2.1.282 | 2026-09-24 | Resume of very large sessions faster. | |
| 2.1.281 | 2026-09-23 | Send now (ctrl+enter or ctrl+x ctrl+s) moves running tools to the background instead of cancelling the turn; AGENTS.md support extended to Bedrock, Vertex, Foundry, gateways and telemetry-disabled sessions; "Prompt is too long" recovery summarizes an oversized first prompt separately. | `ctrl+enter`, `ctrl+x ctrl+s`, `AGENTS.md` |
| 2.1.281 | 2026-09-23 | After resuming in a new process, the auto-mode classifier can reuse its prompt cache; large CLAUDE.md startup notice counts instruction files together. | |
| 2.1.277 | 2026-09-18 | In a project with no CLAUDE.md, Claude Code reads AGENTS.md; change under "Project instructions" in `/config`. | `AGENTS.md`, `/config` |
| 2.1.275 | 2026-09-17 | Send-now key (ctrl+enter, ctrl+x ctrl+s) interrupts the current turn and sends all queued messages at once. | `ctrl+enter` |
| 2.1.274 | 2026-09-17 | Visible warning when memory usage is critical. | |
| 2.1.273 | 2026-09-15 | Fork a `--remote-control` session from the Claude app as a background session. | `claude --remote-control` |
| 2.1.269 | 2026-09-11 | `/focus` spinner tip (view of prompt, work summary, response). | `/focus` |
| 2.1.268 | 2026-09-10 | `--continue` / `--resume` show the conversation immediately instead of waiting for SessionStart hooks and skip re-reading the whole transcript on first message; `claude auth status --json` gains `configDirectory`; MEMORY.md truncation warning states lines cut. | `--continue`, `claude auth status --json`, `configDirectory` |
| 2.1.267 | 2026-09-09 | `--system-prompt-snapshot off` renders the system prompt fresh on every request instead of reusing the recorded prompt. | `--system-prompt-snapshot` |
| 2.1.265 | 2026-09-08 | Resume of long sessions that read many files is faster. | |
| 2.1.261 | 2026-09-04 | `/context` local token estimate when counting API is unavailable. | `/context` |

# Not found in the documentation pages

- `claude auth status --json`
