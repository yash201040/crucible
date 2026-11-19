---
type: "Guide"
title: "Claude Code in a dev container"
description: "Install Claude Code via the Dev Container Feature, sign in, and persist authentication and settings across rebuilds with a volume and CLAUDE_CONFIG_DIR."
resource: "https://code.claude.com/docs/en/devcontainer"
tags: [devcontainer, install, persistence, codespaces]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: "Docker and an editor supporting the Dev Containers spec"
identifiers:
  - ".devcontainer/devcontainer.json"
  - "ghcr.io/anthropics/devcontainer-features/claude-code:1.0"
  - "ghcr.io/devcontainers/features/node:1"
  - "CLAUDE_CONFIG_DIR"
  - "containerEnv"
  - "mounts"
  - "${devcontainerId}"
  - "ANTHROPIC_API_KEY"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "claude setup-token"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "devcontainer"
    resource: "https://code.claude.com/docs/en/devcontainer"
    title: "Development containers"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A dev container gives every engineer an identical isolated environment; commands Claude runs execute inside the container while edits to bind-mounted project files appear on the host. Works with VS Code, GitHub Codespaces, JetBrains IDEs, Cursor.

# How to use it

- Add the feature to `.devcontainer/devcontainer.json`: `"features": {"ghcr.io/anthropics/devcontainer-features/claude-code:1.0": {}}` (example image `mcr.microsoft.com/devcontainers/base:ubuntu`). The `:1.0` tag pins the install script, not Claude Code; the feature installs the latest release and Claude Code auto-updates. It also adds the VS Code extension in VS Code/Codespaces. If it fails with `Failed to install Node.js and npm`, add `ghcr.io/devcontainers/features/node:1` above it. Then rebuild (VS Code: **Dev Containers: Rebuild Container**) and run `claude`.
- Sign-in: Anthropic uses a browser (if none opens or a `localhost` error appears, use the login URL and paste the code). Bedrock, Google Cloud's Agent Platform and Foundry use cloud credentials with no browser; pass them via `containerEnv`, a Codespaces secret or workload identity rather than mounting credential files.
- Persist: the home directory is discarded on rebuild. Mount a named volume at `~/.claude` and set `CLAUDE_CONFIG_DIR` to the same path so `.claude.json` lands inside, e.g. `"mounts": ["source=claude-code-config,target=/home/node/.claude,type=volume"]` with `"containerEnv": {"CLAUDE_CONFIG_DIR": "/home/node/.claude"}` (replace `/home/node` with the `remoteUser` home). Use `${devcontainerId}` in the source name to isolate per project. Without `CLAUDE_CONFIG_DIR`, first-launch setup repeats each rebuild.
- Codespaces: `~/.claude` survives stop/start but not rebuild; to carry auth across codespaces store `ANTHROPIC_API_KEY` or a `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token` as a Codespaces secret.

# Limits and defaults

Warning from the docs: with `--dangerously-skip-permissions`, a dev container does not stop a malicious project from exfiltrating anything inside it, including `~/.claude` credentials. Use only with trusted repositories and avoid mounting `~/.ssh` or cloud credential files.
