---
type: "Feature"
title: "claude-cli:// deep links"
description: "A claude-cli:// URL opens Claude Code in a new local terminal with a working directory and a pre-filled, unsent prompt."
resource: "https://code.claude.com/docs/en/deep-links"
tags: [deep-links, url-scheme, launch]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Handler registered by sending a prompt in an interactive session"
identifiers:
  - "claude-cli://open"
  - "q"
  - "cwd"
  - "repo"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "deep-links"
    resource: "https://code.claude.com/docs/en/deep-links"
    title: "Launch sessions from links"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude-cli://` is a custom URL scheme Claude Code registers with the OS. Clicking a link starts Claude Code in a new terminal window on the machine where you clicked, in the given directory, with the prompt in the input box. The prompt is not sent until you press Enter. The link can be hosted anywhere; the session is always local. The hosting platform must allow custom URL schemes.

# How to use it

Minimal: `claude-cli://open` (home directory, empty prompt). Parameters:

| Parameter | Description |
| --- | --- |
| `q` | Prompt text to pre-fill; URL-encode it; `%0A` for line breaks; maximum 5,000 characters |
| `cwd` | Absolute working directory. Network and UNC paths rejected, as are paths with `..` segments or invisible/bidirectional control characters |
| `repo` | GitHub `owner/name` slug resolved to a local clone Claude Code has seen; with no match the session opens in home |

Example: `claude-cli://open?repo=acme/payments&q=Investigate%20the%20failed%20deploy%20of%20payments-api.%0ACheck%20recent%20commits%20to%20main.`

# Limits and defaults

- If both `cwd` and `repo` are given, `cwd` wins and `repo` is ignored even if the path does not exist.
- A link never executes anything; it only chooses a directory and fills the prompt. A warning below the input, `Prompt from an external link`, stays until you send or clear it. Over 1,000 characters it adds the character count and tells you to scroll and review. Permission rules, `CLAUDE.md` and trust prompts apply as usual.
