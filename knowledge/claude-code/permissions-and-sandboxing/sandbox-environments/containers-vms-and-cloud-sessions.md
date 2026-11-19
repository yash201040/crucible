---
type: "Concept"
title: "Dev containers, custom containers, VMs and cloud sessions"
description: "Container, VM and cloud isolation options for running Claude Code, including the example dev container with a default-deny firewall."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, devcontainer, docker, vm, cloud]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: "Docker for dev and custom containers; Claude subscription for cloud sessions"
identifiers:
  - "--cloud"
  - "enableWeakerNestedSandbox"
  - "--dangerously-skip-permissions"
  - ".devcontainer/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- **Dev container**: Claude Code inside a Docker container managed by VS Code or a compatible editor, project mounted in; define your own in a `.devcontainer/` directory. The claude-code repository publishes an example with a default-deny iptables firewall; copy it, then adjust the firewall allowlist, base image and pinned Claude Code version. Because the firewall blocks unapproved egress, such a configuration supports `--dangerously-skip-permissions` for unattended work.
- **Custom container**: any Docker or OCI image with your own network policies, volumes and seccomp profiles; the common path for organizations with container infrastructure or CI runners. Managed sandbox and remote execution services can host it. Review what is mounted writable, which credentials are reachable, and the egress policy. The built-in Bash sandbox can be layered inside; unprivileged containers need `enableWeakerNestedSandbox`.
- **Virtual machine**: strongest separation, own kernel (cloud instances, local hypervisors, microVMs such as Firecracker). Docker Sandboxes is a free standalone Docker product giving a microVM with its own Docker daemon and workspace sync; it does not require Docker Desktop.
- **Cloud session**: an isolated Anthropic-managed VM. A network proxy enforces a default allowlist and a separate proxy holds your GitHub token outside the sandbox, issuing scoped credentials inside. Sessions routed to a self-hosted environment run on infrastructure you provision, where isolation, egress control and git credentials are your responsibility.

# Limits and defaults

Cloud sessions need a Claude subscription and, for a GitHub repository, a connected GitHub account. Launching from the CLI with `--cloud` needs no GitHub account if Claude Code bundles and uploads the local repository.
