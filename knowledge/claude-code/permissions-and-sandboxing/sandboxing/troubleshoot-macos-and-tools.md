---
type: "Reference"
title: "Sandbox troubleshooting: tools and macOS"
description: "Known tool incompatibilities with the sandbox (jest, Go CLIs, open/osascript, docker, clipboard, git over SSH, databases, localhost) and the settings that fix each."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, troubleshooting, macos, git]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "jest --no-watchman"
  - "sandbox.enableWeakerNetworkIsolation"
  - "sandbox.allowAppleEvents"
  - "sandbox.network.allowLocalBinding"
  - "sandbox.excludedCommands"
  - "/copy"
  - "claude doctor"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Symptom-to-fix list. If the sandbox is admin-required, save the fixes in `~/.claude/settings.json`, since project files' loosening settings are ignored. A fix adding an `excludedCommands` pattern removes the sandbox for matching commands.

# How to use it

| Symptom | Fix |
| - | - |
| Host-not-allowed error | Approve the prompt or add to `allowedDomains`; with `allowManagedDomainsOnly` there is no prompt, ask the admin |
| `jest` hangs or fails | `watchman` is incompatible: run `jest --no-watchman` |
| Go CLIs (`gh`, `gcloud`, `terraform`) fail TLS on macOS Seatbelt | Add `gh *` etc. to `excludedCommands`; with `httpProxyPort` and a MITM proxy with custom CA, set `enableWeakerNetworkIsolation: true` |
| `open`, `osascript`, browser auth fail with error `-600` (macOS) | Apple Events blocked; set `allowAppleEvents: true` in user, managed or CLI settings (ignored in project settings), which removes code-execution isolation; or add `open *` to `excludedCommands` |
| `docker` fails | Incompatible; exclude with a pattern like `docker compose *` |
| `pbcopy`, `xclip`, `wl-copy` do not update clipboard | Ask Claude to print the text, then run `/copy`; excluding the tool alone does not take the call out of the sandbox |
| `git merge`/`checkout` fails `unable to unlink old` (Linux/WSL2 ends `Read-only file system`) | File is under a protected path, a `denyWrite` entry, or outside writable dirs; approve the unsandboxed retry or run it yourself (if `allowUnsandboxedCommands` is `false`, run it yourself) |
| `Unable to create '.../index.lock'` | Started in a repo subdirectory so `.git` is outside the writable area; start from the repo (or worktree) root |
| Folder `objects`/`refs` disappears | See [protected paths](./protected-paths.md); leave something in it; move away a top-level `HEAD`, restart sessions. Before v2.1.307 deleted even with contents |
| `git` over SSH | macOS: fetch/pull/push fail even with host allowed (tunnel cannot authenticate to the proxy); switch remote to HTTPS or exclude `git fetch *`, `git pull *`, `git push *` (a call with `cd`, `git -C` or command substitution stays sandboxed; excluded git can reach any host). Linux/WSL2: works once allowed; check port 22 allowed (entry without a port covers it), corporate proxy permits 22, and key files readable (`denyRead`/`credentials` for `~/.ssh` hides them; ssh-agent socket may be blocked) |
| DB client, plain `ssh`, UDP tools fail to reach an allowed host | Tool ignores proxy variables. macOS: `Operation not permitted` or `Could not resolve host`; Linux/WSL2: `Network is unreachable` or `Temporary failure in name resolution`. Proxy-using tools instead get a prompt or a `403`. Exclude the command, optionally with an ask rule, e.g. `excludedCommands ["python scripts/load_orders.py *"]` plus `permissions.ask ["Bash(python scripts/load_orders.py *)"]` |
| Cannot reach a server on localhost | macOS: `network.allowLocalBinding: true` (also lets commands listen and reach any localhost port). Linux/WSL2: the sandbox's `localhost` is private; `allowLocalBinding` has no effect; exclude the command. An `allowedDomains` entry for `localhost` applies only to proxied connections and exposes all localhost ports; Claude Code sets `NO_PROXY` so commands connect to localhost directly |
| Allowed hostname refused `resolved to a loopback address` (e.g. `myapp.test`) | Add the IP too, with port: `["myapp.test:3000", "127.0.0.1:3000"]`; an IP with no port exposes every service on it |

# Notes

0-byte read-only placeholders: on Linux/WSL2 the sandbox creates 0-byte read-only placeholder files at not-yet-existing write-denied paths during a command. A killed session or an exit during a running background command can leave them, and later settings writes (such as saving "Yes, and don't ask again") fail. `claude doctor` lists them with the warning `Sandbox mask files left behind at write-deny paths`; delete with `rm` while no other session runs in that project. Before v2.1.257 they were left behind unflagged.
