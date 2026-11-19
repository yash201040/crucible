---
type: "Concept"
title: "Keep skills discoverable"
description: "Which skills are in scope depends on the launch directory; descriptions can be cut when many skills exist; track usage via OpenTelemetry."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [skills, discovery, telemetry, plugins]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "OTEL_LOG_TOOL_DETAILS"
  - "skill_activated"
  - "skill.name"
  - "invocation_trigger"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude chooses a skill by reading every discovered skill's name and description; only the chosen skill's full content loads.

# How to use it

Skills in scope by launch point:

| Start | Skills in scope |
| :- | :- |
| Subdirectory (`packages/api/`) | That directory, every parent to the repo root, user and enterprise levels |
| Repository root | Root skills plus those from every subdirectory touched in the session (can reach hundreds) |
| After `--add-dir` | The added sibling's skills too; `additionalDirectories` does not load skills |

- Names always load, but with many skills some lose their descriptions entirely. Keep descriptions short and lead with words a request would contain.
- Skills shared by many directories (PR conventions, deploy checklist) go in the root `.claude/skills/`. For their own version history or cross-repo use, package as a plugin; plugin skills use a `plugin-name:skill-name` namespace and never collide with per-directory skills.
- To find unused skills: enable the OpenTelemetry logs exporter and set `OTEL_LOG_TOOL_DETAILS=1` so skill names are recorded verbatim. The `skill_activated` event records each invocation in `skill.name`; `invocation_trigger` records whether a command, Claude, or a nested skill invoked it.
