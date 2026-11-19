---
type: "Reference"
title: "Workflow script format and API"
description: "The meta block, agent(), pipeline(), parallel(), phase(), log(), schema validation, determinism rules and how to edit saved scripts."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, script, api, schema, editing]
kind: "api"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "export const meta"
  - "agent()"
  - "pipeline()"
  - "parallel()"
  - "phase()"
  - "log()"
  - "args"
  - "schema"
  - "label"
  - "stallMs"
  - "phases"
  - "MAX_STRUCTURED_OUTPUT_RETRIES"
  - "/workflow-authoring"
  - "/reload-skills"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A saved script has `export const meta = { name, description }` first, then a plain-JavaScript body with top-level `await`.

# How to use it

| Name | Purpose |
| :- | :- |
| `agent(prompt, opts)` | Spawn one subagent; options seen: `schema`, `label`, `stallMs` |
| `pipeline(list, fn)` | One agent task per item |
| `parallel(tasks)` | Run agent tasks at the same time, wait for all |
| `phase(title)` | Group following agents under a title in the progress view |
| `log(msg)` | Show a message above the phases |
| `args` | Global holding invocation input |

- `agent()` resolves to `null` if stopped mid-run or on an unrecoverable API error; `pipeline()` keeps each `null` in its result array (hence `.filter(Boolean)`), including slots of agents that stalled on all attempts.
- `schema`: the subagent returns JSON matching it. Checked before starting: a provable self-contradiction (e.g. a `required` key excluded by `additionalProperties: false`) fails the call with an error and the subagent never starts. Output failing validation after five attempts fails the call with the last validation failure; change the count with `MAX_STRUCTURED_OUTPUT_RETRIES`.
- In auto mode the prompt a script passes to `agent()` is marked as script-computed text, not a request from you, when the classifier reviews the subagent's actions.

# Limits and defaults

Editing a saved script: edit the `.js` file or ask Claude. First run `/workflow-authoring` (bundled skill, v2.1.248 or later) to load the authoring reference. Reload with `/reload-skills`, then run `/<name>`.
- `meta` must stay the first statement and a plain object literal with `name` and `description`; any non-literal (variable, call, spread) drops `/<name>` from autocomplete.
- A syntax error is reported at run time.
- If `phases` is listed in `meta`, each entry must equal a `phase()` title; an unlisted title gets its own group.
- `Date.now()`, `Math.random()` and no-argument `new Date()` throw inside the script so a relaunch repeats the same `agent()` calls; pass timestamps through `args`.
- `import()` makes the script fail before the run starts.
- Example prompts on the page: audit many files, loop until a check passes, migrate files each in an isolated copy, per-file review then one summary, multi-source research, repeat rounds until the list stops growing.
