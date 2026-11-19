---
type: "Feature"
title: "Waiting for background work at exit"
description: "A claude -p run can stay open for background commands, subagents, workflows, Monitor watches and loop wakeups, with a 10-minute idle cap."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, background-tasks, timeouts, subagents]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "--max-budget-usd"
  - "--input-format stream-json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

After Claude finishes its turn and stdin has closed, a `claude -p` run can stay open to wait for background work Claude started. Unless a background command from the main conversation is still running, Claude Code stops whatever is running after 10 minutes of continuous idle waiting by default and drops its partial result.

# How to use it

| Background work | Wait behavior |
| --- | --- |
| Background command from the main conversation (dev server, watch build) | Waits until exit or its time limit, then one more turn with the outcome; the 10-minute cap does not end the wait |
| Background subagents and workflows | Stays open until each finishes or the 10-minute cap ends the wait |
| Monitor watches | Until the watch times out (default five minutes after start) or the cap; Claude keeps responding to reports |
| Pending wakeups | Only when the prompt was passed as text, not `--input-format stream-json`: waits for each self-paced `/loop` wakeup and runs its iteration until the loop ends, even past the cap |

Set `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` to change the 10-minute cap; `0` waits without a cap. At `--max-budget-usd` Claude Code stops remaining background work instead of waiting.

# Limits and defaults

- After five seconds of waiting with stderr a terminal, a line starting `Waiting for background work to finish` goes to stderr (with `json`/`stream-json`, only when stdout is not a terminal).
- When background work starts another turn: `text` output prints each turn's result, `json` the last. Before v2.1.295 `text` printed only the last.
- A subagent's long command that moves to background at its timeout can let `-p` exit 0 before it finishes: raise `BASH_DEFAULT_TIMEOUT_MS` (e.g. 300000), and for a background subagent command over 10 minutes also raise the cap.
- MCP: `-p` does not wait for MCP work. MCP tasks on a remote server continue (resume that session to follow); results of calls moved by automatic backgrounding are lost.
