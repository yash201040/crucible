---
type: "Guide"
title: "Writing eval cases and graders by hand"
description: "Case directory layout, a manual prompt.md plus two graders, and habits that keep scores stable."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, cases, graders, authoring]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "evals/"
  - "evals/<case>/prompt.md"
  - "evals/<case>/case.yaml"
  - "evals/<case>/graders/<name>.md"
  - "evals/results/"
  - "--judge-model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A case is a directory under the eval directory containing a `prompt.md`, a `case.yaml`, or both. Every case needs at least one grader (a `graders/<name>.md` file or a `graders:` entry in `case.yaml`) or it fails to load. Nest cases under a non-case directory to group them; anything inside a case directory belongs to that case. Add `results/` to `.gitignore`.

# How to use it

`claude plugin eval init --bare first-case` writes a placeholder `prompt.md` and `graders/criteria.md` and runs nothing. In `prompt.md`, frontmatter such as `max_turns: 10` and `allowed_tools: [Read, Glob, Grep, Skill]` plus a body phrased as a user would type it (not naming the skill). Each run starts in an empty working directory, so put needed content in the prompt or seed it with [case.yaml context](./case-yaml-fields.md). `@path` mentions in the body are not expanded into attachments; grant a tool in `allowed_tools` instead.

Example graders: `type: llm` with a PASS/FAIL rubric body; `type: tool_used`, `tool: Skill`, `input_match: '"skill"\s*:\s*"(?:[\w-]+:)?your-skill-name"'` (passes if the skill was invoked, namespaced form included).

Stable signals:
- Grade long output with `regex` over the file contents; keep `llm` graders for short output with concrete PASS/FAIL conditions.
- Give each case one grader on the result and one on the steps (`tool_used` or `tool_order`).
- If `tool_used: Skill` passes but `Δ` is negative, suspect the judge: rerun with `--judge-model sonnet` and tighten the rubric.
- To check a build or test passed, have the prompt write the outcome to a file, grade the file, and assert the command ran with `tool_used` whose `input_match` names it.

# Limits and defaults

There are no custom-code graders. The default judge for `llm` and `baseline` graders is the model used for background tasks; `--judge-model sonnet` or a full model ID overrides it.
