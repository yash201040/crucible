---
type: "Limit"
title: "Auto mode fallback and block thresholds"
description: "Behavior when the classifier blocks or fails: 3 in a row or 20 total pauses auto mode; non-interactive runs keep going."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, thresholds, fallback, headless, limits]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "/permissions"
  - "/feedback"
  - "--permission-prompt-tool"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What happens when auto mode cannot approve actions.

# How to use it

- Blocked action: notification, and the action is listed in `/permissions` under the **Recently blocked** tab where it can be approved for retry.
- Repeated blocks: 3 in a row or 20 total pauses auto mode and prompting resumes; approving the prompted action resumes auto mode.
- No classifier verdict (a separate safety check refused the classifier request, or the response did not parse): action blocked without notification or **Recently blocked** entry.
- No server verdict: action denied; the turn can stop after ten consecutive no-verdict responses.
- Mode switch during a pending check: a verdict the new mode would not have requested is discarded; you are prompted, or the action is auto-denied in `dontAsk`.

# Limits and defaults

- The 3-in-a-row and 20-total thresholds are not configurable. The total counter persists for the session and resets only when its own limit triggers a fallback. Denials from a separate safety check refusing the classifier request do not count.
- A non-interactive `-p` run without `--permission-prompt-tool` has no prompt to fall back to: when a threshold is reached the action does not run, Claude keeps working, and the run is not stopped.
- Report false positives with `/feedback`; admins can configure trusted infrastructure.
