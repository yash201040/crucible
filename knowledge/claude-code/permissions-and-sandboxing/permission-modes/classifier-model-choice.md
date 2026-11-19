---
type: "Feature"
title: "Choose the classifier model"
description: "Default classifier model rules and CLAUDE_CODE_AUTO_MODE_MODEL override, plus how to verify with the debug log."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, model, env-var, debug]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.302"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_AUTO_MODE_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "--debug-file"
  - "classifier_request_started"
  - "ignoring CLAUDE_CODE_AUTO_MODE_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Classifier requests can run on a model other than the `/model` selection. By default they go to Claude Sonnet 5 (only for calls outside the server's review when `/status` shows `Auto mode server` as `Enabled`).

First matching row replaces Sonnet 5:

| Session | Classifier model |
| - | - |
| Has an Anthropic-configured classifier model | That model (check debug log) |
| Runs on Sonnet 4.6 | Sonnet 4.6 |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` set | Its value, or Sonnet 5 if it is Sonnet 5.5 or Opus 5.5 |

If Sonnet 5 or that model is unavailable from the provider or excluded by organization model policy, the fallback is the session's model, or an Opus model in a Fable session.

# How to use it

From v2.1.302 set `CLAUDE_CODE_AUTO_MODE_MODEL` to a full model ID (cloud provider IDs work too):

```json
{ "env": { "CLAUDE_CODE_AUTO_MODE_MODEL": "claude-sonnet-4-6" } }
```

Verify: `claude --permission-mode auto --debug-file classifier-debug.log`, have Claude run `curl https://example.com`, search the log for `classifier_request_started` and read `model=`. A different model means search `ignoring CLAUDE_CODE_AUTO_MODE_MODEL` for the reason. No such line: check `/status` (`Enabled` = server reviews; `Disabled` = check not yet tested your model, make sure mode is auto, no rule matches `curl`, sandbox off).

# Limits and defaults

| Situation | Result |
| - | - |
| Debug log shows an Anthropic-configured model | That model reviews |
| You set Claude Opus 5, Sonnet 5.5, Opus 5.5, or a model your policy excludes | Default classifier model reviews |
| Provider cannot serve the model | Checks fail; every checked action denied |
| `/status` shows `Auto mode server` `Enabled` | Server reviews without your model |

First listed situation wins.
