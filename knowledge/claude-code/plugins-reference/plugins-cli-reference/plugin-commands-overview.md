---
type: "Reference"
title: "claude plugin commands: shared rules"
description: "claude plugin (alias plugins) runs from a shell or script; shared exit codes, plugin argument forms and scope values."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, cli, exit-codes, scopes]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin"
  - "claude plugins"
  - "claude plugin --help"
  - "--scope"
  - "user"
  - "project"
  - "local"
  - "managed"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin <subcommand>` runs from a shell or script, outside a session, to install and manage plugins without the `/plugin` panel. `claude plugins` is an alias. The tables on the page list commonly used options only; run `claude plugin --help` or `claude plugin <subcommand> --help` for the full set.

# How to use it

- **Exit codes**: `0` success, `1` failure. `validate` adds `2` for an unexpected error; `eval` adds codes (see [plugin eval](./plugin-eval.md)).
- **Plugin arguments**: a `<plugin>` is a plugin `name` or `name@marketplace`. Use the qualified form when two marketplaces offer the same name. `configure` takes only the qualified form.
- **Scopes**: `--scope` takes `user`, `project` or `local` and names the settings file written. `update` also takes `managed`.

Subcommands: `init` (alias `new`), `install` (`i`), `uninstall` (`remove`, `rm`), `enable`, `disable`, `update`, `list`, `details`, `configure`, `prune` (`autoremove`), `eval`, `eval init`, `tag`, `test`, `validate`, and `marketplace add|list|remove|update`.
