---
type: "Reference"
title: "Sandbox approaches compared"
description: "Six isolation options from the per-command Bash sandbox to cloud sessions, with what each isolates and requires."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, isolation, containers, comparison]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "/sandbox"
  - "--cloud"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Isolation limits what a session can read, write and reach on the network. The first two approaches run on the host OS without containers; the rest put Claude Code inside a container or VM.

# How to use it

| Approach | What is isolated | Requires Docker | Setup effort |
| :- | :- | :- | :- |
| Sandboxed Bash tool | Bash, PowerShell and Monitor commands and their children | No | Minimal on macOS; low on Linux and WSL2 |
| Sandbox runtime | Whole Claude Code process incl. file tools, MCP servers, hooks | No | Low |
| Dev container | Full development environment | Yes | Medium |
| Custom container | Full development environment | Yes | Medium to high |
| Virtual machine | Full operating system | No | High |
| Cloud sessions | Full OS, hosted by Anthropic | No | None; needs a Claude subscription and a connected GitHub account to clone a GitHub repository |

Choosing:

| Goal | Start with |
| :- | :- |
| Fewer prompts in everyday work | Sandboxed Bash tool in auto-allow mode, configured with `/sandbox` |
| Unattended with `--dangerously-skip-permissions` or auto mode | Preconfigured dev container, any container or VM, or the sandbox runtime |
| Isolate MCP servers and hooks as well as Bash, no Docker | Sandbox runtime |
| Standardize across a team | Preconfigured dev container copied into the repository |
| No local setup | A cloud session |
| Native Windows host | A container or VM, or the Bash sandbox in WSL2 |

# Notes

- Only the Bash sandbox is built in; with it, built-in file tools, MCP servers and hooks still run on the host. Every other approach puts the whole process inside the boundary.
- Isolation reduces breach impact but does not remove risk: any approach with network egress can leak readable data, and a writable project mount can still be modified.
- Isolation does not change what is sent to the model: prompts and files read go to the Anthropic API or your provider either way.
