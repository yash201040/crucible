---
type: "Feature"
title: "Plugin executables in bin/"
description: "Files in the plugin bin/ directory are put on the Bash tool's PATH while the plugin is enabled."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, bin, path, executables]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "bin/"
  - "chmod +x"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`bin/` at the plugin root ships a command-line tool. While the plugin is enabled its files are on the `PATH` of the Bash tool's shell, so Claude (or a skill's instructions) can run them as bare commands without installation. Commands run with the PowerShell tool outside the sandbox also find them; sandboxed PowerShell does not.

# How to use it

Add an executable script (for example `bin/hello-plugin`), `chmod +x` it, load the plugin, and ask Claude to run it.

# Limits and defaults

- Plugin `bin/` entries come after the user's own `PATH` entries, so a plugin cannot shadow `git`, `ls` or other system commands.
- Claude.ai and Cowork do not install a plugin that has a top-level `bin/` directory, including via claude.ai organization settings.
