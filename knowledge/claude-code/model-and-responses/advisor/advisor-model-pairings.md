---
type: "Reference"
title: "Advisor model pairings and Fable consent"
description: "Which advisor models each main model accepts, aliases, version requirements, validation behavior and the Fable usage-credits consent."
resource: "https://code.claude.com/docs/en/advisor"
tags: [advisor, models, pairings, fable]
kind: "mixed"
maturity: "experimental"
since: "2.1.257"
surfaces: [cli, headless, sdk]
requires: "Fable access for Fable models"
identifiers:
  - "fable"
  - "opus"
  - "sonnet"
  - "claude-opus-5-5"
  - "claude-haiku-5-5"
  - "/model fable"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "advisor"
    resource: "https://code.claude.com/docs/en/advisor"
    title: "Escalate hard decisions with the advisor tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code ranks models by capability for the advisor role; the advisor must rank at or above the session's main model.

# How to use it

| Main model | Accepted advisors |
| - | - |
| Haiku 4.5 | Fable, Opus, Sonnet, Haiku 5.5 |
| Sonnet 4.6 | Fable, Opus, Sonnet, Haiku 5.5 |
| Opus 4.6 | Fable, Opus, Sonnet 5 or later, Haiku 5.5 |
| Sonnet 5 or Haiku 5.5 | Fable, Opus 4.7 or later, Sonnet 5 or later, Haiku 5.5 |
| Opus 4.7 or Opus 4.8 | Fable, Opus 4.7 or later, Sonnet 5.5 |
| Sonnet 5.5 | Fable, Opus 5 or later, Sonnet 5.5 |
| Opus 5 or Opus 5.5 | Fable, Opus 5 or later |
| Fable 5 | Fable 5.2, 5.1 or 5 |
| Fable 5.1 | Fable 5.2 or 5.1 |
| Fable 5.2 | Fable 5.2 |

Aliases `fable`, `opus`, `sonnet` resolve to the built-in default version of each family (advances with releases); full IDs such as `claude-opus-5-5` or `claude-haiku-5-5` also work. Haiku 4.5 can call the advisor but cannot be one.

Common pairings: Sonnet+Opus (routine work, escalate planning/failures/completion checks); Sonnet+Fable (needs Fable access); Haiku+Opus (lowest-cost main with strong planning); Opus+Opus (independent check on high-stakes work); Fable+Fable (highest capability; no Opus or Sonnet advisor is applied to a Fable main model); Sonnet+Sonnet (cheap second opinion).

# Limits and defaults

- Versions: Fable 5.2 needs v2.1.321+; Fable 5.1 v2.1.257+; Sonnet 5.5 advisor for Opus 4.7/4.8 main v2.1.287+; Haiku 5.5 as main or advisor v2.1.293+.
- Validation: Claude Code checks the pairing before sending; an advisor ranking below the main model is not attached (shown in `/advisor` output and a notification; subagents whose own model fits may still use it). If the API refuses an attached pairing, Claude Code resends without the advisor silently; a newly picked advisor then takes effect after `/clear` or `/compact` and in new sessions. Unrecognized models: advisor not attached.
- Fable consent: on some plans Fable usage bills to usage credits and needs a one-time consent. Before it, `/advisor fable` and the picker do not save Fable (pointing to `/model fable`); `claude --advisor fable` exits at launch (background session: starts without advisor); a saved Fable `advisorModel` sends requests without the advisor (interactive sessions also show a notification). Accept by running `/model fable` and choosing to continue; that saves Fable as the selected model.
