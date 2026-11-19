---
type: "Feature"
title: "/run, /verify and pre-commit checks"
description: "Bundled /run, /verify and /run-skill-generator launch and confirm changes in the real app; a verify or simplify skill is run before each commit."
resource: "https://code.claude.com/docs/en/skills"
tags: [run, verify, commit, bundled-skills]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.286"
surfaces: [cli]
requires: "Pre-commit instruction: v2.1.286 or later"
identifiers:
  - "/run"
  - "/verify"
  - "/run-skill-generator"
  - "/simplify"
  - ".claude/skills/run-<name>/"
  - ".claude/skills/verify/SKILL.md"
  - "includeGitInstructions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three bundled skills confirm changes against the running app instead of tests alone.

| Skill | Purpose |
| :- | :- |
| `/run` | Launch and drive the app to see a change working |
| `/verify` | Build and run the app to confirm a change, without falling back to tests or type checks |
| `/run-skill-generator` | Record how to build and launch the project |

# How to use it

- `/run` and `/verify` need no setup; they infer launch from project type and README, `package.json` or `Makefile`. Inference is unreliable when a database, env file, graphical session or multi-step build is needed.
- `/run-skill-generator` runs the app from a clean environment, captures install commands, env vars and launch script, and commits a per-project skill at `.claude/skills/run-<name>/`. Later `/run`, `/verify` and other agents in the repo follow it. Run it once per project and again when the build or launch changes.
- `/verify` can record its own recipe to `.claude/skills/verify/SKILL.md` at the repo root (or the touched package directory in a monorepo). At the repo root the recorded skill replaces the bundled `/verify`. Claude edits it only when it steered a run wrong.

# Limits and defaults

Before-commit check (v2.1.286 or later): if a skill named `verify` or `simplify` is in place at session start, the commit instructions tell Claude to run it before each commit, except for docs or test changes. Conditions:

- Loads from enterprise, personal, project or additional-directory location, or a `.claude/commands/` file of that name. Bundled `/verify` and `/simplify`, plugin skills and claude.ai-account skills do not count.
- Claude can invoke it (not `disable-model-invocation: true`).
- `includeGitInstructions` is not turned off (turning it off removes this with all built-in commit and PR instructions).
