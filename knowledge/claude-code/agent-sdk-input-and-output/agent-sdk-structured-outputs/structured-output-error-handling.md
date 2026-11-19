---
type: "Limit"
title: "Structured output errors and retries"
description: "error_max_structured_output_retries, success-without-output cases, model-fallback retraction and tips for avoiding failures."
resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
tags: [agent-sdk, structured-output, errors, retries]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "error_max_structured_output_retries"
  - "is_error"
  - "errors"
  - "success"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-structured-outputs"
    resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
    title: "Get structured output from agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Generation can fail when the agent cannot produce valid JSON for the schema: schema too complex, ambiguous task, or retry limit hit while fixing validation errors. It can also fail without validation failure: a model fallback can retract an already-completed output mid-stream, and if no retry replaces it the run ends with the same error. Check the `errors` list on the error result to tell the causes apart.

# How to use it

| Subtype | Meaning |
| - | - |
| `success` | the run ended without an error subtype |
| `error_max_structured_output_retries` | no valid output remained after multiple attempts (validation failures, or a fallback retraction with no successful retry) |

`success` alone does not mean an answer exists. Treat the result as a failure when `is_error` is `true` (for example the final request ended in an API error or a refusal; do not use `structured_output` then) or when `structured_output` is absent (see troubleshooting "structured_output is None but the result says success"). Connection or process failures yield no result message.

# Notes

Tips: keep schemas focused (deep nesting with many required fields is harder), make fields optional when the task may lack the data, and use clear prompts.
