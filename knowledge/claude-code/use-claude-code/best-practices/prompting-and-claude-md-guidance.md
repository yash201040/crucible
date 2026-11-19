---
type: "Guide"
title: "Prompting, CLAUDE.md, rules and skills guidance"
description: "Write down only what Claude cannot see in the repo; specific prompts, interview-to-SPEC.md, short CLAUDE.md, path-scoped rules, team skills."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [claude-md, prompts, rules, skills, spec]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/init"
  - "/doctor"
  - "/doctor prompt-audit"
  - "/context all"
  - "CLAUDE.local.md"
  - ".claude/rules/"
  - "paths:"
  - ".claude/skills/<name>/SKILL.md"
  - "disable-model-invocation: true"
  - "ultrathink"
  - "be ambitious"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Guidance that most defaults already work; setup pays off for knowledge Claude cannot find in the repo (a meeting decision, a deploy process, an env var integration tests need).

# How to use it

- Test before writing something down: could Claude find it by reading the code, and would it look? If both yes, leave it out.
- Specific prompts: name the file, describe the symptom, say what "fixed" looks like. Hand over the thing itself: `@path` for a file, a pasted image, or `cat error.log | claude -p "what's going on here"`.
- `think step by step` and `be thorough` are ordinary text; effort level is the control. `be ambitious` helps with scope. `ultrathink` in a prompt gives deeper reasoning for one turn.
- Interview first: ask Claude to interview you until it can write the spec to `SPEC.md`, then start a fresh session to build from it.
- CLAUDE.md should hold: commands to confirm work, misleading code places, decisions not in the repo, anything corrected twice. `/init` generates a start; `/doctor` suggests cuts; `/doctor prompt-audit` flags outdated, dangling or contradictory instructions. Personal preferences go in `CLAUDE.local.md` (add to `.gitignore`). `/context all` confirms the file loaded.
- Path-scoped rules: `.claude/rules/api.md` with `paths:` frontmatter (e.g. `"src/api/**/*.ts"`) loads only when Claude works there.
- Team procedures go in `.claude/skills/<name>/SKILL.md`; a startable-by-Claude skill shows name and description each session and reads the full file only when needed. Use `disable-model-invocation: true` for side-effect workflows (e.g. `/release`) so only you can run them.

# Limits and defaults

Memory guide recommends staying under 200 lines in CLAUDE.md. Emphasis like IMPORTANT will not fix a missed line: shorten the file or make it a hook.
