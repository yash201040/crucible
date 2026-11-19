---
type: "Reference"
title: "Output format options, JSON Schema support, Zod and Pydantic"
description: "outputFormat fields, the draft-07 requirement, supported schema features, format keyword handling, and generating schemas from Zod or Pydantic."
resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
tags: [agent-sdk, json-schema, zod, pydantic, draft-07]
kind: "api"
maturity: "unlabelled"
since: "2.1.205"
surfaces: [sdk]
requires: ""
identifiers:
  - "outputFormat.type"
  - "outputFormat.schema"
  - "z.toJSONSchema"
  - "target: \"draft-7\""
  - ".model_json_schema()"
  - "model_validate"
  - "safeParse"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-structured-outputs"
    resource: "https://code.claude.com/docs/en/agent-sdk/structured-outputs"
    title: "Get structured output from agents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The configuration object and schema rules for structured outputs, plus type-safe schema generation.

# How to use it

| Field | Value |
| - | - |
| `type` | `"json_schema"` |
| `schema` | a JSON Schema object; generate from Zod with `z.toJSONSchema(schema, { target: "draft-7" })` or from Pydantic with `.model_json_schema()` |

- TypeScript: define a Zod schema, convert it, then validate the result with `FeaturePlan.safeParse(message.structured_output)`.
- Python: define Pydantic models, pass `FeaturePlan.model_json_schema()`, then `FeaturePlan.model_validate(message.structured_output)`.

# Limits and defaults

- The SDK validates with JSON Schema draft-07; schemas declaring a newer version are rejected. Zod targets draft 2020-12 by default, so pass `target: "draft-7"`.
- Supported: basic types (object, array, string, number, boolean, null), `enum`, `const`, `required`, nested objects, `$ref` definitions. Full list and limitations are on the platform API structured-outputs page.
- An invalid schema fails the run at startup with an error naming the problem. Before v2.1.205 an invalid schema was silently ignored and the agent returned unstructured text.
- The `format` keyword (for example `"format": "email"`) is accepted as an annotation and not enforced by the validator. Before v2.1.205 any schema containing `format` was treated as invalid.
