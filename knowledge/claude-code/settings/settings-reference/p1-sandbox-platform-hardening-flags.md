---
type: "Reference"
title: "Sandbox platform escape-hatch flags"
description: "sandbox.enableWeakerNestedSandbox, enableWeakerNetworkIsolation, allowAppleEvents and allowNestedUserNamespaces: security-reducing options for containers, macOS and Linux."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [sandbox, security, docker, macos, linux]
kind: "setting"
maturity: "unlabelled"
since: "2.1.305"
surfaces: [cli]
requires: "allowNestedUserNamespaces v2.1.305"
identifiers:
  - "sandbox.enableWeakerNestedSandbox"
  - "sandbox.enableWeakerNetworkIsolation"
  - "sandbox.allowAppleEvents"
  - "sandbox.allowNestedUserNamespaces"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four Boolean `sandbox.*` keys, each default `false`, that weaken isolation for tools that cannot run otherwise.

# How to use it

| Key | Scope | Platform | What it does |
| :- | :- | :- | :- |
| `sandbox.enableWeakerNestedSandbox` | Any file (project/local limited) | Linux, WSL2 | Run the sandbox inside an unprivileged Docker container where bubblewrap cannot mount a fresh `/proc`; the inner sandbox bind-mounts the container's `/proc`, exposing process info. Use only if the outer container isolates enough |
| `sandbox.enableWeakerNetworkIsolation` | Any file (project/local limited) | macOS | Reach the TLS trust service `com.apple.trustd.agent` so Go-based tools (`gh`, `gcloud`, `terraform`) verify certificates behind a MITM proxy with a custom CA (used with `network.httpProxyPort`); opens a possible exfiltration path. Without a MITM proxy use `excludedCommands` |
| `sandbox.allowAppleEvents` | User or managed | macOS | Let sandboxed commands send Apple Events (`open`, `osascript`; otherwise error `-600`). Removes code-execution isolation: can launch other apps unsandboxed and script running apps, subject to the macOS TCC prompt |
| `sandbox.allowNestedUserNamespaces` | User or managed | Linux, WSL2 | Allow user namespaces (Chromium/Electron sandbox, nested bubblewrap, `unshare`). Turns off a security boundary; protected paths and `credentials.files` no longer reliably stop a malicious command and auto-allow may run it without a prompt. For rootless Podman/Buildah use `excludedCommands` |

# Limits and defaults

`allowNestedUserNamespaces`: a `true` counts only from `~/.claude/settings.json`, `--settings` JSON or managed settings; ignored in project settings, and ignored from every source when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is `1`. A `false` counts from any file by precedence.
