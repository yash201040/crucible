---
type: "Reference"
title: "Vertex per-model region overrides"
description: "VERTEX_REGION_CLAUDE_* variables that override the Google Cloud Agent Platform region for one Claude model."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [vertex, region, models, google-cloud]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Google Cloud's Agent Platform"
identifiers:
  - "VERTEX_REGION_CLAUDE_3_5_HAIKU"
  - "VERTEX_REGION_CLAUDE_3_5_SONNET"
  - "VERTEX_REGION_CLAUDE_3_7_SONNET"
  - "VERTEX_REGION_CLAUDE_4_0_OPUS"
  - "VERTEX_REGION_CLAUDE_4_0_SONNET"
  - "VERTEX_REGION_CLAUDE_4_1_OPUS"
  - "VERTEX_REGION_CLAUDE_4_5_OPUS"
  - "VERTEX_REGION_CLAUDE_4_5_SONNET"
  - "VERTEX_REGION_CLAUDE_4_6_OPUS"
  - "VERTEX_REGION_CLAUDE_4_6_SONNET"
  - "VERTEX_REGION_CLAUDE_4_7_OPUS"
  - "VERTEX_REGION_CLAUDE_4_8_OPUS"
  - "VERTEX_REGION_CLAUDE_5_5_OPUS"
  - "VERTEX_REGION_CLAUDE_5_5_SONNET"
  - "VERTEX_REGION_CLAUDE_5_OPUS"
  - "VERTEX_REGION_CLAUDE_5_SONNET"
  - "VERTEX_REGION_CLAUDE_FABLE_5"
  - "VERTEX_REGION_CLAUDE_FABLE_5_1"
  - "VERTEX_REGION_CLAUDE_FABLE_5_2"
  - "VERTEX_REGION_CLAUDE_HAIKU_4_5"
  - "VERTEX_REGION_CLAUDE_HAIKU_5_5"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

One variable per Claude model that overrides the region used on Google Cloud's Agent Platform.

# How to use it

| Variable | Model | Added in |
| :- | :- | :- |
| `VERTEX_REGION_CLAUDE_3_5_HAIKU` | Claude 3.5 Haiku | |
| `VERTEX_REGION_CLAUDE_3_5_SONNET` | Claude 3.5 Sonnet | |
| `VERTEX_REGION_CLAUDE_3_7_SONNET` | Claude 3.7 Sonnet | |
| `VERTEX_REGION_CLAUDE_4_0_OPUS` | Claude Opus 4 | |
| `VERTEX_REGION_CLAUDE_4_0_SONNET` | Claude Sonnet 4 | |
| `VERTEX_REGION_CLAUDE_4_1_OPUS` | Claude Opus 4.1 | |
| `VERTEX_REGION_CLAUDE_4_5_OPUS` | Claude Opus 4.5 | |
| `VERTEX_REGION_CLAUDE_4_5_SONNET` | Claude Sonnet 4.5 | |
| `VERTEX_REGION_CLAUDE_4_6_OPUS` | Claude Opus 4.6 | |
| `VERTEX_REGION_CLAUDE_4_6_SONNET` | Claude Sonnet 4.6 | |
| `VERTEX_REGION_CLAUDE_4_7_OPUS` | Claude Opus 4.7 | |
| `VERTEX_REGION_CLAUDE_4_8_OPUS` | Claude Opus 4.8 | |
| `VERTEX_REGION_CLAUDE_5_5_OPUS` | Claude Opus 5.5 | v2.1.280 |
| `VERTEX_REGION_CLAUDE_5_5_SONNET` | Claude Sonnet 5.5 | v2.1.284 |
| `VERTEX_REGION_CLAUDE_5_OPUS` | Claude Opus 5 | v2.1.219 |
| `VERTEX_REGION_CLAUDE_5_SONNET` | Claude Sonnet 5 | v2.1.197 |
| `VERTEX_REGION_CLAUDE_FABLE_5` | Claude Fable 5 | v2.1.170 |
| `VERTEX_REGION_CLAUDE_FABLE_5_1` | Claude Fable 5.1 | v2.1.257 |
| `VERTEX_REGION_CLAUDE_FABLE_5_2` | Claude Fable 5.2 | v2.1.321 |
| `VERTEX_REGION_CLAUDE_HAIKU_4_5` | Claude Haiku 4.5 | |
| `VERTEX_REGION_CLAUDE_HAIKU_5_5` | Claude Haiku 5.5 | v2.1.293 |
