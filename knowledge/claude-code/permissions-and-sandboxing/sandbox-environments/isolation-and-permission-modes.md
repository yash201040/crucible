---
type: "Concept"
title: "Isolation for unattended runs"
description: "Run --dangerously-skip-permissions only inside a container, VM or sandbox runtime; auto mode's classifier is not an isolation boundary."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, unattended, permission-modes, bypass]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--dangerously-skip-permissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Permission modes decide whether a tool call runs and whether you are prompted. Isolation restricts what a command can access once it runs. When a mode lets actions run without asking, the isolation boundary limits what they can reach.

# How to use it

- With `--dangerously-skip-permissions` the actions no mode auto-approves still apply, but nothing else catches mistakes. Always run such sessions inside a container, a VM or the sandbox runtime so file tools, MCP servers and hooks are inside the boundary.
- Auto mode swaps the prompt for a classifier that reviews actions. The classifier is a per-action control, not an isolation boundary: an outer boundary adds defense in depth but is not required the way it is for `--dangerously-skip-permissions`.
- The sandboxed Bash tool alone constrains only shell commands, so it is not sufficient for fully unattended runs in either mode. It can be layered inside a container or VM.

# Limits and defaults

On Linux and macOS, Claude Code refuses to start with `--dangerously-skip-permissions` when running as root. Run the container, VM or sandbox runtime as a non-root user.
