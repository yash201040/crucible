---
type: "Feature"
title: "Install and manage plugins from the shell"
description: "Non-interactive claude plugin install, enable, disable, uninstall, update, with --scope, --marketplace and --yes."
resource: "https://code.claude.com/docs/en/plugins/install"
tags: [plugins, cli, headless, scripting]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin install"
  - "claude plugin enable"
  - "claude plugin disable"
  - "claude plugin uninstall"
  - "claude plugin update"
  - "claude plugin prune"
  - "claude plugin details"
  - "--scope"
  - "--marketplace"
  - "--yes"
  - "CLAUDE_CODE_PLUGIN_PREFER_HTTPS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-install"
    resource: "https://code.claude.com/docs/en/plugins/install"
    title: "Install and manage plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin ...` commands install and manage plugins without starting a session, for example from a setup script. They change the same settings as the `/plugin` panel.

# How to use it

```bash
claude plugin install formatter@your-org --scope project
claude plugin disable formatter@your-org
claude plugin enable formatter@your-org
claude plugin uninstall formatter@your-org --scope project
claude plugin install deploy-helper --marketplace your-org/plugins
claude plugin update <plugin>@<marketplace>
```

- `install` prints `Successfully installed plugin: formatter@your-org (scope: project)`. Default scope is user; `--scope project` or `--scope local` changes it. `install` and `uninstall` default to user scope; `enable` and `disable` act on the most specific scope that already lists the plugin.
- Plugins installed this way load at the next start or after `/reload-plugins` in an open session.
- On a machine where nobody has opened an interactive session, the official marketplace is not registered; a script installing from it first runs `claude plugin marketplace add anthropics/claude-plugins-official`.
- A plugin with a `command` source asks the user to accept its command; a script passes `--yes` to accept.
- **`--marketplace <source>`** adds and installs in one step (give the plugin name without `@marketplace`). Shell form needs v2.1.292 or later and adds the marketplace with no confirmation, under the same organization policy checks as `marketplace add`, declared in user settings even with `--scope project`; prints `Successfully added marketplace: <name> (declared in user settings)`. In a session, `/plugin install deploy-helper --marketplace your-org/plugins` needs v2.1.275 or later, the source cannot contain spaces, and an unadded marketplace asks for confirmation first.
- `claude plugin prune` removes auto-installed dependencies left after uninstall.
- `claude plugin details <name>` shows the `Always-on` token cost of an installed plugin and per-component rows.

# Notes

Private marketplaces clone with git credentials on the machine and never prompt: HTTPS uses credential helpers (git prompts and askpass, including `GIT_ASKPASS`, are off); SSH needs the host in `known_hosts` and a passphrase-free key (`GIT_SSH_COMMAND`, `GIT_SSH`, `core.sshCommand` are honored); GitHub `owner/repo` checks whether SSH authenticates to github.com and falls back to HTTPS; set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` to always use HTTPS. The same credentials apply to `/plugin install`, `/plugin marketplace update` and `claude plugin update`.
