---
type: "Feature"
title: "/skill-doctor and skill evals"
description: "/skill-doctor reports skill context cost and usage; evaluate skills with baseline comparison, claude plugin eval or the skill-creator plugin."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, evals, cost, skill-doctor]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.252"
surfaces: [cli, headless]
requires: "/skill-doctor: not in sessions without feature-flag fetching"
identifiers:
  - "/skill-doctor"
  - "claude plugin eval"
  - "claude plugin validate"
  - "/plugin install skill-creator@claude-plugins-official"
  - "/plugin marketplace add anthropics/claude-plugins-official"
  - "/plugin marketplace update claude-plugins-official"
  - "/reload-plugins --force"
  - "evals/evals.json"
  - "grading.json"
  - "benchmark.json"
  - "tool_used: Skill"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/skill-doctor` (v2.1.252 or later) shows what each skill costs in context per turn and how often it is used, flagging never-invoked skills and where to turn them off (start with highest context cost); also lists plugins not recently used. It excludes bundled and enterprise skills. In an interactive session it opens in the `/plugin` manager's **Stats** tab; with `-p` it prints text. Not available without feature-flag fetching; over Remote Control it replies `Skill usage reports are not available on this connection.`

# How to use it

Evaluating a skill: run realistic prompts in fresh sessions with and without the skill and compare invocation and output. Turn it off for the baseline with `"off"` in `skillOverrides` (personal or project), or, for plugin skills, `claude plugin eval`.

- `claude plugin eval`: runs each prompt in an isolated session with and without the plugin, scores with graders you define or it writes, exits non-zero below a threshold so CI can gate; a `tool_used: Skill` grader measures triggering.
- `skill-creator` plugin: `/plugin install skill-creator@claude-plugins-official`; stores cases in `evals/evals.json`, spawns a subagent per test case (records tokens and duration), writes `grading.json`, aggregates `benchmark.json` (with vs without skill), runs blind A/B between versions, tunes description with should-trigger and should-not-trigger prompts, and opens an HTML review viewer. Its format is not interchangeable with `claude plugin eval`.
- `claude plugin validate .claude/skills` (or `~/.claude/skills`) finds SKILL.md files whose frontmatter does not parse; v2.1.233 or later.

# Notes

Install failures: `Marketplace "claude-plugins-official" not found` means add the marketplace; `Plugin "<name>" not found in marketplace "claude-plugins-official"` means update the catalog. After install, `/reload-plugins` runs for you; if it warns that the next message would re-read the conversation, use `/reload-plugins --force`.
