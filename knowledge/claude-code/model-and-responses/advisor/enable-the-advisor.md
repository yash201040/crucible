---
type: "Feature"
title: "Enable and disable the advisor"
description: "Set the advisor with /advisor, the advisorModel setting or the --advisor flag; turn it off with /advisor off or an env var."
resource: "https://code.claude.com/docs/en/advisor"
tags: [advisor, slash-command, settings, cli-flag]
kind: "mixed"
maturity: "experimental"
since: "2.1.260"
surfaces: [cli, headless, sdk, desktop]
requires: "Main model that supports the advisor"
identifiers:
  - "/advisor"
  - "/advisor off"
  - "advisorModel"
  - "--advisor"
  - "CLAUDE_CODE_DISABLE_ADVISOR_TOOL"
  - "availableModels"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "advisor"
    resource: "https://code.claude.com/docs/en/advisor"
    title: "Escalate hard decisions with the advisor tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three ways to set the advisor model, plus ways to turn it off. After start Claude Code shows `Advisor Tool (experimental) is on and may use more tokens · /advisor`.

# How to use it

| Method | Syntax | Scope |
| - | - | - |
| `/advisor` | `/advisor` (picker) or `/advisor opus`; confirms `Advisor set to <model>` | Saved to `advisorModel` in user settings (persists, except cases the `advisorModel` settings entry lists as current-session only) |
| `advisorModel` setting | `{ "advisorModel": "opus" }` in a settings file | Persistent default |
| `--advisor` flag | `claude --advisor opus` | One session; overrides the setting; not listed in `claude --help` |

- `/advisor` also works without a terminal picker: in `-p` non-interactive mode, the Agent SDK, the desktop app and Remote Control (requires v2.1.260+). No argument prints the current advisor and accepted aliases; `/advisor <model>` sets; `/advisor off` turns off.
- Turn off: `/advisor off` or "No advisor" in the picker. `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` removes the tool entirely: `/advisor` becomes unavailable, `advisorModel` is ignored, `--advisor` is accepted with no effect.

# Limits and defaults

- `--advisor` makes Claude Code exit at launch when: the main model does not support the advisor; the requested model (such as Haiku 4.5) cannot be an advisor; the organization's `availableModels` allowlist excludes it; or Fable is requested and the usage-credits consent is pending. For a background session (agent view) it starts without the advisor instead of exiting. If the model can advise but ranks below the main model, the session starts without the advisor either way.
- A saved advisor excluded by `availableModels` is not invoked; pick an allowed one.
- A saved advisor that the current main model does not support stays saved and activates after switching (`/model`) to a compatible main model. If the API already refused it in this conversation, it stays off until `/clear` or `/compact`.
- Feature-flag fetching is needed (see [requirements](./advisor-requirements.md)).
