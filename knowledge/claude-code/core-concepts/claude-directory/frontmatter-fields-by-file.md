---
type: "Reference"
title: "Frontmatter fields by file type"
description: "The YAML frontmatter field names accepted by skills, command files, subagents, output styles and rules."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [frontmatter, skills, subagents, rules]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "name"
  - "description"
  - "when_to_use"
  - "argument-hint"
  - "arguments"
  - "disable-model-invocation"
  - "user-invocable"
  - "allowed-tools"
  - "disallowed-tools"
  - "model"
  - "effort"
  - "context"
  - "agent"
  - "background"
  - "hooks"
  - "paths"
  - "shell"
  - "metadata"
  - "license"
  - "compatibility"
  - "tools"
  - "disallowedTools"
  - "permissionMode"
  - "maxTurns"
  - "autoCompactWindow"
  - "skills"
  - "mcpServers"
  - "memory"
  - "isolation"
  - "color"
  - "initialPrompt"
  - "omitClaudeMd"
  - "experimental"
  - "keep-coding-instructions"
  - "force-for-plugin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills, command files, subagents, output styles and rules read configuration from YAML frontmatter. Each accepts its own field set.

# How to use it

| File | Fields |
| - | - |
| `skills/<name>/SKILL.md` | `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility` |
| `commands/*.md` | The skill fields except `name` and `paths` |
| `agents/*.md` | `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `autoCompactWindow`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color`, `initialPrompt`, `omitClaudeMd`, `experimental` |
| `output-styles/*.md` | `name`, `description`, `keep-coding-instructions`, `force-for-plugin` |
| `rules/*.md` | `paths` |

# Notes

Field meanings are in the skill, subagent, output style and memory rules reference pages. Agents shipped in a plugin honor a subset of the subagent fields.
