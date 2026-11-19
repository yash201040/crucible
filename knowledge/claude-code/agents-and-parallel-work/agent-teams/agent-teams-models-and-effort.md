---
type: "Feature"
title: "Choosing teammate models"
description: "Order in which Claude Code picks a teammate's model, the CLAUDE_CODE_SUBAGENT_MODEL(_FORCE) variables, availableModels substitution and effort inheritance."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, model, effort, availablemodels]
kind: "mixed"
maturity: "experimental"
since: "2.1.257"
surfaces: [cli]
requires: "CLAUDE_CODE_SUBAGENT_MODEL_FORCE needs v2.1.257 or later"
identifiers:
  - "CLAUDE_CODE_SUBAGENT_MODEL"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "availableModels"
  - "teammateDefaultModel"
  - "agent.spawn"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude decides how many teammates to spawn, or you name a number and a model in the prompt ("Spawn 4 teammates ... Use Sonnet for each teammate").

# How to use it

Model selection, first that applies:

1. The model the spawn prompt names for that teammate.
2. For a teammate spawned from a subagent definition, the definition's `model` (`inherit` selects the lead's model).
3. `CLAUDE_CODE_SUBAGENT_MODEL`, when set to anything other than `inherit`.
4. The lead's current model.

- An installed mod that sets a model in its `agent.spawn` hook has that model used in place of the first source.
- With `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`, sources 1 and 2 do not apply: every teammate uses `CLAUDE_CODE_SUBAGENT_MODEL` (if not `inherit`), else the lead's model. Requires v2.1.257 or later.
- Before v2.1.251, `CLAUDE_CODE_SUBAGENT_MODEL` came first in this order.
- `teammateDefaultModel` was removed in v2.1.234; a leftover value is ignored. Name the model in the prompt instead.

# Limits and defaults

- The chosen model is checked against the organization's `availableModels` allowlist. A blocked family alias such as `opus` runs on the newest permitted version of that family on the Anthropic API and Claude Platform on AWS. Any other blocked value (including an alias on providers with provider-specific model IDs, or a family with no permitted version) falls back to the lead's model; if `CLAUDE_CODE_SUBAGENT_MODEL` is set, that is tried first under the same rules.
- A teammate on the lead's model inherits the lead's effort level by default. For split-pane teammates this applies from v2.1.186; earlier versions did not pass the lead's session effort. For a teammate on another model see "Effort level of subagents and teammates" in model-config.
- A teammate's model and fast mode are fixed when it spawns.
