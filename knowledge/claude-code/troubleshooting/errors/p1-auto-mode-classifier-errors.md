---
type: "Reference"
title: "Auto mode classifier errors and denials"
description: "Messages when auto mode cannot judge an action: classifier unavailable, unparseable, safety-filtered, too long, no server verdict, and what unattended runs do."
resource: "https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action"
tags: [auto-mode, classifier, permissions, headless, errors]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.280"
surfaces: [cli, headless]
requires: "Auto mode"
identifiers:
  - "CLAUDE_CODE_AUTO_MODE_SERVER=0"
  - "CLAUDE_CODE_AUTO_MODE_MODEL"
  - "--permission-prompt-tool"
  - "--debug"
  - "Agent aborted: auto mode classifier request refused by the safety safeguard in headless mode"
  - "Agent aborted: auto mode classifier transcript exceeded context window in headless mode"
  - "Auto mode classifier transcript exceeded context window"
  - "Auto mode is unavailable — the server returned no safety verdict for the last 10 responses"
  - "The server-side auto mode classifier gave no verdict"
  - "was not reviewed and did not run"
  - "a hook changed this call's input after auto mode reviewed it"
  - "Not run · auto mode's check had no usable answer"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Auto mode uses a classifier model to approve or deny actions. When it cannot produce a decision the action is not auto-approved. Message depends on the failure.

# How to use it

| Failure | Message and behavior |
| :- | :- |
| Classifier model unavailable | `<model> is temporarily unavailable, so auto mode cannot determine the safety of <tool> right now.` Category in parentheses when known: `(rate-limited)`, `(overloaded)`, `(server error)`, `(timed out)`, `(connection failed)`. Interactive sessions show a dim `Not run · auto mode's check had no usable answer` row (Ctrl+O opens the transcript viewer). On Amazon Bedrock it repeats until the account can invoke the model. A refreshed OAuth token is retried once (before v2.1.216 every check failed). Check `CLAUDE_CODE_AUTO_MODE_MODEL` if it names a model your provider does not serve. |
| Unparseable classifier response | `Auto mode could not evaluate this action and is blocking it for safety — run with --debug for details`; retry. |
| API safety check blocked the classifier request | Same prefix plus a note that it is not about the action; retrying will not help. Does not count toward auto mode pause thresholds (before v2.1.225 it did). In `-p` runs the run continues: a background subagent without `--input-format stream-json` gets an error result `Agent aborted: auto mode classifier request refused by the safety safeguard in headless mode`; elsewhere the denial goes back to Claude. |
| Conversation too long for classifier | `Auto mode classifier transcript exceeded context window — falling back to manual approval`. Interactive: normal permission prompt. Background subagent in `-p` without `--input-format stream-json`: error result `Agent aborted: auto mode classifier transcript exceeded context window in headless mode`, run continues. Other `-p` runs without `--permission-prompt-tool`: action does not run, run continues. Also `<tool> was not reviewed and did not run: ...` while Claude Code tries to compact first. |
| Server-side review: no verdict | `The server-side auto mode classifier gave no verdict (timed out), so ...`. After 10 responses in a row with no verdict, the turn stops with `Auto mode is unavailable — the server returned no safety verdict for the last 10 responses`; `-p` runs end with an execution error (stderr in text output); a subagent stops early. Sending a message resets the count. Spinner may show `Auto mode check unavailable` with Esc to interrupt. |
| Hook or mod changed input after review | `a hook changed this call's input after auto mode reviewed it`; sibling calls may be denied as changed or unconfirmed. Disable the hook or mod, or switch to Manual mode. Not counted toward the ten. |

# Limits and defaults

Set `CLAUDE_CODE_AUTO_MODE_SERVER=0` before start to use Claude Code's own classifier requests instead of server-side review (before v2.1.281 it was not read on a direct Anthropic API connection). Before v2.1.280 no-verdict denials were immediate and never stopped the turn; before v2.1.302 a too-long conversation was not compacted on a direct API connection; before v2.1.229 messages named no category; before v2.1.296 the message was a red error.
