---
type: "Feature"
title: "Setup scripts"
description: "A Bash script run as root when a new cloud session starts, before Claude Code launches, to install tools not pre-installed."
resource: "https://code.claude.com/docs/en/cloud-environments"
tags: [cloud-sessions, setup-script, provisioning, bash]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud, desktop, mobile]
requires: "Anthropic-hosted environment"
identifiers:
  - "Setup script"
  - "Choose file"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cloud-environments"
    resource: "https://code.claude.com/docs/en/cloud-environments"
    title: "Configure cloud environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A setup script is a Bash script that runs when a new cloud session starts, before Claude Code launches. It runs as root on Ubuntu 24.04, so `apt install` and most package managers work.

# How to use it

Open the environment for editing, select the **Setup script** row, type or paste the script or use **Choose file** (replaces the box with the text of a file up to 64 KB), then **Add environment** or **Save changes**. Example:

```bash
#!/bin/bash
apt update && apt install -y shellcheck
```

# Limits and defaults

- **Exit zero**: a non-zero exit makes the session fail to start or start without what failed to install. Append `|| true` to non-critical commands.
- **Finish within about five minutes** so the cache can build; run independent installs in parallel with `&` and `wait`; move big downloads to a background SessionStart hook.
- **Network**: installs need registry access. Limited with Allow package managers covers npm, PyPI, RubyGems, crates.io; None makes installs fail.
- **Variables not set yet**: the script runs before the environment's variables are set; set needed values in the script.
- Not run when a VM is restored after idle; a change reaches an existing session only after its VM is reclaimed and rebuilt (or run commands in session / start a new one).
- Layering on the provided image works; replacing the base image is not supported.
