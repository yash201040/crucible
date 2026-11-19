---
type: "Guide"
title: "Create your first plugin"
description: "Minimal steps to build, validate and run a one-skill plugin with --plugin-dir, including the manifest fields."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, walkthrough, manifest, validate]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate"
  - "claude --plugin-dir"
  - "name"
  - "description"
  - "version"
  - "author"
  - "disable-model-invocation"
  - "/plugin-dev:create-plugin"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

1. `mkdir -p my-first-plugin/.claude-plugin`.
2. Write `.claude-plugin/plugin.json`: `name` (required; becomes the prefix on every skill and agent; no spaces), `description` (shown in `/plugin`), `version` (optional; setting it pins users until changed), `author` (`name` required inside; `email`, `url` optional).
3. Add `skills/hello/SKILL.md` with frontmatter `name`, `description`, and `disable-model-invocation: true` (Claude does not run the skill on its own; remove the line to allow it).
4. `claude plugin validate ./my-first-plugin` prints the manifest path and `✔ Validation passed`, or `✘ Validation failed` with the field to fix.
5. `claude --plugin-dir ./my-first-plugin`, then run `/my-first-plugin:hello`.

The plugin loads only in sessions started with `--plugin-dir`.

# Notes

- Only `plugin.json` goes inside `.claude-plugin/`; components saved there do not load. The plugin root is the plugin directory, not `~/.claude/` (a `~/.claude/.mcp.json` does not load).
- Anthropic's `plugin-dev` plugin (from `claude-plugins-official`) adds skills and agents for authoring; `/plugin-dev:create-plugin <description>` walks through design, creation and validation.
