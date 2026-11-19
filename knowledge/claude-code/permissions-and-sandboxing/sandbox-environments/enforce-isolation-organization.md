---
type: "Concept"
title: "Enforcing isolation across an organization"
description: "Only the built-in Bash sandbox is enforced by Claude Code via managed settings; containers and VMs rely on device management."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, managed-settings, enterprise, enforcement]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "sandbox"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What an organization can enforce depends on the approach.

# How to use it

| Approach | Enforcement |
| :- | :- |
| Built-in Bash sandbox | The only approach Claude Code enforces itself: deliver the `sandbox` settings keys through managed settings, either an MDM-managed file or server-managed settings on Claude.ai |
| Dev containers | Commit the example dev container to repositories; a convention, not an enforcement boundary since Claude Code does not require a container. To stop use outside it, use device management or software allowlisting |
| Custom containers and VMs | Distribute Claude Code through the approved image and use device management or software allowlisting to block installs elsewhere |
