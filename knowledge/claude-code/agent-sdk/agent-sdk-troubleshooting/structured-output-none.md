---
type: "Concept"
title: "structured_output missing despite success"
description: "A result with subtype success can carry no structured_output; treat as failure and check for refusal or an unsatisfiable schema."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [structured-output, refusal, schema, results]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "structured_output"
  - "stop_reason"
  - "refusal"
  - "minLength"
  - "maxLength"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A result message can end with `subtype: "success"` while `structured_output` is `None` (Python) or `undefined` (TypeScript): the run completed but no validated output exists. Application code should treat this as a failure (see Error handling on the structured-outputs page).

# How to use it

Check causes:
- A request Claude declined: check the result's `stop_reason` for `"refusal"`; see the Usage Policy refusal entry in the error reference.
- A schema no output can satisfy, for example `minLength` greater than `maxLength`. If output is repeatedly missing, look for contradictory constraints, simplify the schema until outputs validate, then re-add constraints one at a time.
