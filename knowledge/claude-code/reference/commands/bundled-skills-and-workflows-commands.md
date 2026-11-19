---
type: "Reference"
title: "Bundled skill and workflow commands"
description: "Commands that are bundled skills or dynamic workflows: review, simplify, debug, deep research, run and verify, artifacts, design, slides and authoring."
resource: "https://code.claude.com/docs/en/commands"
tags: [slash-commands, bundled-skills, workflows, review, artifacts]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/artifact-capabilities"
  - "/artifact-diagramming"
  - "/claude-api"
  - "/claude-in-chrome"
  - "/code-review"
  - "/review"
  - "/dataviz"
  - "/debug"
  - "/deep-research"
  - "/design"
  - "/design consent"
  - "/design revoke"
  - "/design-sync"
  - "/doctor"
  - "/checkup"
  - "/fewer-permission-prompts"
  - "/loop"
  - "/proactive"
  - "/plugin-authoring"
  - "/run"
  - "/run-skill-generator"
  - "/security-review"
  - "/simplify"
  - "/slides"
  - "/ultrareview"
  - "/update-config"
  - "/verify"
  - "/workflow-authoring"
  - "/workflows"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Entries marked Skill (a prompt handed to Claude) or Workflow (a dynamic workflow fanning out subagents). The orchestration command `/batch` is described [separately](./batch-command.md).

# How to use it

| Command | Kind | What it does |
| :- | :- | :- |
| `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]` | Skill | Review the diff, PR, branch or path for correctness bugs (cleanups too depending on model and effort). `--fix` applies findings, `--comment` posts to the GitHub PR or GitLab MR (GitLab needs v2.1.257+), `ultra` runs a cloud review; `--post` with ultra on a github.com PR preselects posting (v2.1.227+). Alias `/review`; with no level the last typed `low` to `max` level is reused |
| `/review ...` | alias | Alias of `/code-review` with the same levels and flags |
| `/ultrareview [PR or branch]` | | Deep multi-agent cloud-sandbox review; alias of `/code-review ultra`. 3 free runs on Pro, Max, Ultra, then usage credits |
| `/security-review` | | Analyze the branch diff against origin's default branch for vulnerabilities; needs an `origin` remote |
| `/simplify [target]` | Skill | Four parallel review agents (reuse, simplification, efficiency, abstraction level) then apply cleanups; not a bug hunt |
| `/debug [description]` | Skill | Enable debug logging mid-session and troubleshoot from the log; off by default unless `claude --debug` |
| `/deep-research <question>` | Workflow | Fan out web searches, cross-check sources, synthesize a cited report |
| `/doctor [prompt-audit [path]]` | Skill | Setup checkup that proposes fixes applied after confirmation; `prompt-audit` needs v2.1.283+. Alias `/checkup` |
| `/fewer-permission-prompts` | Skill | Scan transcripts for common read-only Bash and MCP calls and add an allowlist to project `.claude/settings.json` |
| `/loop [interval] [prompt]` | Skill | Run a prompt repeatedly while the session is open; no interval means Claude self-paces; no prompt runs the built-in maintenance prompt or `loop.md`. Alias `/proactive` |
| `/run` | Skill | Launch and drive the project's app to see a change working |
| `/verify` | Skill | Confirm a change by building, running and observing the app |
| `/run-skill-generator` | Skill | Write a per-project skill that teaches `/run` and `/verify` to build and drive the app |
| `/update-config [request]` | Skill | Edit the matching `settings.json` for a described change (allow a command, set an env var, add a hook) |
| `/claude-api [migrate\|upgrade\|api-version\|managed-agents-onboard\|managed-agents-secure\|prompt-audit\|cost-optimize\|latency-optimize\|build-eval\|hillclimb\|preserved-thinking-migration]` | Skill | Load Claude API and Managed Agents reference; auto-activates on `anthropic` or `@anthropic-ai/sdk` imports |
| `/claude-in-chrome [task]` | Skill | Browser task through Claude in Chrome; available when Chrome integration is enabled |
| `/dataviz [request]` | Skill | Chart and dashboard design guidance with a palette validation script |
| `/design [brief]` | Skill | Draft mockups as artboards in a Claude Design artifact; v2.1.265+, needs artifacts and the Design template; Anthropic API only (unavailable on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, Claude Platform on AWS) |
| `/design consent`, `/design revoke` | | Grant or withdraw Claude access to Claude Design; type it yourself when asked |
| `/design-sync [hint]` | Skill | Convert a repo's React design system and upload it to Claude Design; first sync can take hours; uploads to the standalone claude.ai/design site, which closes by December 14, 2026; unavailable where claude.ai is not contacted |
| `/slides [brief]` | Skill | Make a Claude Slides artifact; v2.1.265+, needs artifacts and the Slides template; Anthropic API only |
| `/artifact-capabilities` | Skill | Load the runtime-capabilities reference for artifacts |
| `/artifact-diagramming` | Skill | Diagramming guidance for artifacts, inline SVG; v2.1.221+ |
| `/plugin-authoring` | Skill | Reference for writing a mod; from a built-in plugin that can be turned off in `/plugin`; v2.1.287+ |
| `/workflow-authoring` | Skill | Reference for writing dynamic workflow scripts (API, resume, patterns, examples); needs dynamic workflows enabled, v2.1.248+ |
| `/workflows` | | Open the workflow progress view to watch, pause, resume or save workflows |
