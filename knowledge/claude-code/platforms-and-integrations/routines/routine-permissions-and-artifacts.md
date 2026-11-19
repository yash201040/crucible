---
type: "Concept"
title: "Permissions and artifacts during scheduled runs"
description: "Cloud scheduled runs start in auto mode, may still pause for prompts, and may publish artifacts without asking under stated conditions."
resource: "https://code.claude.com/docs/en/routines"
tags: [permissions, auto-mode, unattended, artifacts, environments]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cloud]
requires: ""
identifiers:
  - "auto mode"
  - "Accept edits"
  - "ask rule"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "routines"
    resource: "https://code.claude.com/docs/en/routines"
    title: "Automate work with scheduled tasks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

You do not choose a permission mode when creating a task. A new cloud session starts in auto mode (a classifier allows or blocks actions) unless auto mode is unavailable (org turned it off or the model lacks support), in which case it keeps the mode it launched in.

# How to use it

A run still waits for an answer when an action matches an ask rule, or when repeated blocks reach auto mode's thresholds; answer by opening the run from the task's detail page. In a project, a run can continue a thread and then keeps that thread's current permission mode.

Artifacts: in auto mode, Claude publishes an artifact without asking once the classifier allows it; new artifacts are visible only to you until shared. In Accept edits mode, a new artifact publishes without asking unless it declares runtime capabilities (connector calls, file downloads). Republishing an existing artifact without asking requires all of: you can edit it and it is in your org; you own it if supporting files are included; not shared publicly; viewers of a shared one do not auto-see new versions; no force over a newer version; no capabilities declared; no reaching grant on the page. Runs started by an API or GitHub trigger always ask first. To keep a page current, give the task an artifact already published.

Environments: each task uses one cloud environment (network access, variables, setup script). The Default environment is Limited with Allow package managers. Connector traffic goes through Anthropic servers so needs no allowlist change. Blocked hosts fail with `403` or `ENOTFOUND`. Organization-shared environments are read-only in the task dialog. Environment variables are visible to anyone using the environment; store API keys as network secrets in Anthropic-hosted environments.

# Limits and defaults

"The last run" warnings under History (run did not start because the org hit its concurrent cloud session limit; environment not found; blocked by access or policy; temporary problem; repository or branch unavailable; settings not accepted; usage limit reached; failed) clear when a later run starts; the table on the page gives the fix for each.
