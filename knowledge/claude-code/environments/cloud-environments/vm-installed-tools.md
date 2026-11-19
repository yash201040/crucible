---
type: "Reference"
title: "Cloud VM image and pre-installed tools"
description: "Ubuntu 24.04 x86_64 VM with listed language runtimes, databases, Docker and Chrome; what is not pre-installed."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, vm, toolchains, installed-tools]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud]
requires: "Anthropic-hosted environment"
identifiers:
  - "check-tools"
  - "CHROME_PATH"
  - "/usr/bin/google-chrome"
  - "/opt/node20"
  - "/opt/node21"
  - "/opt/node22"
  - "service postgresql start"
  - "service redis-server start"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each Anthropic-hosted session gets a fresh Ubuntu 24.04 x86_64 VM with the repo cloned, whatever your own OS and CPU. Use x86_64 Linux builds of precompiled dependencies. Self-hosted environments provide the tools of your runner image instead.

# How to use it

| Category | Included |
| - | - |
| Python | 3.x with pip, poetry, uv, black, mypy, pytest, ruff |
| Node.js | 20, 21, 22 with npm, yarn, pnpm, bun, eslint, prettier, chromedriver |
| Ruby | 3.1, 3.2, 3.3 with gem, bundler, rbenv |
| PHP | 8.3 with Composer |
| Java | OpenJDK 21 with Maven, Gradle |
| Go, Rust | Go with modules; rustc and cargo |
| C/C++ | GCC, Clang, cmake, ninja, conan |
| Docker | docker, dockerd, docker compose |
| Databases | PostgreSQL 16, Redis 7.0 (installed, not running) |
| Browser | Chrome for Testing at `/usr/bin/google-chrome`, `CHROME_PATH` set |
| Utilities | git, gh, jq, yq, ripgrep, tmux, vim, nano |

- Ask Claude to run `check-tools` for versions (a VM shell command, not a slash command); for others use the tool's own command (`psql --version`).
- Node 22 is on `PATH`; versions live at `/opt/node20`, `/opt/node21`, `/opt/node22`; ask Claude to prepend a `bin` directory to `PATH` to switch.
- Start services by asking Claude: `service postgresql start`, `service redis-server start`, `docker compose up`.
- You get no shell into the VM; Claude runs every command.

# Limits and defaults

Bun is installed but has known proxy compatibility issues for package fetching. Toolchains such as the .NET SDK are not pre-installed even if their registries are allowlisted; use a setup script. Replacing the base image is not supported yet; layer on top or run your own image via `docker compose`. Running processes are not cached (see [environment caching](./environment-caching.md)).
