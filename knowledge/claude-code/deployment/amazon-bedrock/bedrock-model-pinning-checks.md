---
type: "Feature"
title: "Bedrock model pinning and startup checks"
description: "Pin model versions on Bedrock, map versions to inference profile ARNs, and how startup checks, fallbacks and allowlists behave."
resource: "https://code.claude.com/docs/en/amazon-bedrock"
tags: [bedrock, models, pinning, fallback]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: "Amazon Bedrock"
identifiers:
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_SMALL_FAST_MODEL"
  - "modelOverrides"
  - "availableModels"
  - "enforceAvailableModels"
  - "CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY"
  - "CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK"
  - "DISABLE_PROMPT_CACHING"
  - "ENABLE_PROMPT_CACHING_1H"
  - "--model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "amazon-bedrock"
    resource: "https://code.claude.com/docs/en/amazon-bedrock"
    title: "Claude Code on Amazon Bedrock"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Without pinning, aliases resolve to Claude Code's built-in Bedrock defaults, which can lag the newest release and may not be enabled in the account. Pinning is recommended for multi-user deployments.

# How to use it

- Pin with `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`, e.g. `us.anthropic.claude-opus-4-8`, `us.anthropic.claude-sonnet-4-6`, `us.anthropic.claude-haiku-4-5-20251001-v1:0`. IDs may be inference profile IDs or application inference profile ARNs. GovCloud uses `us-gov.`.
- `ANTHROPIC_BEDROCK_REGION_PREFIX` keeps the built-in default but changes the prefix (`eu` gives `eu.anthropic.claude-opus-5-5`).
- `modelOverrides` setting maps Anthropic model IDs (e.g. `claude-opus-4-7`) to distinct application inference profile ARNs so several versions show in `/model`. Applies to `--model` and `ANTHROPIC_MODEL` from v2.1.200 (earlier passed as-is).
- Prompt caching on by default; `DISABLE_PROMPT_CACHING=1` turns it off; `ENABLE_PROMPT_CACHING_1H=1` requests 1-hour TTL (billed higher). Caching may be missing in some Bedrock regions.
- Startup checks: if a pinned model is older than the default and the newer one is invokable, a prompt offers to update the pin (writes user settings, restarts; decline remembered). No check or prompt for pins in managed settings `env` or for ARN pins. Managed-pin prompt looping fixed in v2.1.314.
- Unpinned and default unavailable: session-only fallback to earlier versions, or the default Sonnet if no Opus is available.
- Refusals can be remembered up to a day; rechecked after 10 minutes at launch. `CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY=1` disables the memory.
- `enforceAvailableModels` (managed settings) makes startup checks use only the `availableModels` list, written as the inference profile IDs including region prefix. Invoke API only; needs v2.1.287 or later.
- Mid-session model disabled: switches with message `Switched to <fallback> because <model> is not available`, unless a fallback chain is configured. Fails for pinned models, specific versions, or ARNs, and in auto mode switches only to auto-mode-supported models. `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK=1` makes rejected requests fail (also remove any fallback chain).

# Limits and defaults

| Item | Default |
|---|---|
| Primary model | Opus 5.5 (e.g. `us.anthropic.claude-opus-5-5`); before v2.1.280 it was Opus 5 |
| Small/fast (background tasks) | default Sonnet 4.5 (`us.anthropic.claude-sonnet-4-5-20250929-v1:0`), not Haiku |
| `sonnet` alias unpinned | Sonnet 4.5 |

- Starting a session with `--model`, `ANTHROPIC_MODEL` or the `model` setting makes that model the background-task model and acts as a pin for that alias; a bare alias or unknown ID (such as an ARN) does not act as a pin.
- Unpinned primary model is billed at the Opus rate.
