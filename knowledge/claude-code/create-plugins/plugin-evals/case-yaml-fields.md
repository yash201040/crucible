---
type: "Reference"
title: "case.yaml fields and workspace seeding"
description: "case.yaml adds scaffold scripts, history transcripts and read-only directories, and can hold a whole case."
resource: "https://code.claude.com/docs/en/plugin-evals"
tags: [evals, case-yaml, fixtures, scaffold]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [headless]
requires: ""
identifiers:
  - "case.yaml"
  - "context.scaffold_script"
  - "context.history_file"
  - "context.add_dirs"
  - "execution.prompt"
  - "execution:"
  - "graders"
  - "criteria"
  - "--scaffold"
  - "--no-scaffold"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugin-evals"
    resource: "https://code.claude.com/docs/en/plugin-evals"
    title: "Test plugins with evals"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`case.yaml` is an alternative or companion to `prompt.md`. It requires `schema_version: "1.1"` and `name`. At top level go `description`, `tags`, `plugins`, `runs`, `expected_outcome`; under `execution:` go `model`, `max_turns`, `timeout_seconds`, `allowed_tools`, `append_system_prompt`, `env`. When both files exist, `prompt.md` frontmatter overrides matching `case.yaml` fields, the `prompt.md` body is the prompt, and `graders/*.md` are added after graders listed in `case.yaml`.

# How to use it

| Field | Purpose |
| :- | :- |
| `context.scaffold_script` | Bash script in the case dir that runs in the empty workspace before Claude starts (fixture files, git repo). Runs only with `--scaffold`, as you, outside the sandbox, minimal environment, 120-second limit; non-zero exit fails the run (score 0, `scaffold failed`) |
| `context.history_file` | `.jsonl` transcript to resume; the case prompt becomes the next user turn |
| `context.add_dirs` | Directories inside the case dir Claude may read (read-only) |
| `execution.prompt` | The prompt when there is no `prompt.md` |
| `graders` | List of graders with `name` plus the keys a grader file takes; for `llm`, rubric in `criteria` |

Example: `schema_version: "1.1"`, `name: changelog-from-diff`, `tags: [smoke]`, `context: {scaffold_script: fixture.sh, add_dirs: [resources]}`.

# Limits and defaults

The scaffold script sees only your shell `PATH`, `HOME` set to the run's temporary home, `TMPDIR` and constants such as `TERM=dumb`; no other shell variables and no `EVAL_*`. Use it for files and git state only, since project configuration it writes is not loaded. Pass `--scaffold` only for suites you or your organization wrote.
