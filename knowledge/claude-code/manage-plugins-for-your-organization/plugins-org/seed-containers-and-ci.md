---
type: "Feature"
title: "Plugin seed directories for containers and CI"
description: "Pre-populate a plugins directory at build time and point CLAUDE_CODE_PLUGIN_SEED_DIR at it so runtime needs no cloning."
resource: "https://code.claude.com/docs/en/plugins/org"
tags: [plugins, seed, containers, ci, offline]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_PLUGIN_SEED_DIR"
  - "CLAUDE_CODE_PLUGIN_CACHE_DIR"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "GH_TOKEN"
  - "gh auth setup-git"
  - "claude plugin marketplace add"
  - "claude plugin disable"
  - "known_marketplaces.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-org"
    resource: "https://code.claude.com/docs/en/plugins/org"
    title: "Manage Claude Code plugins for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For container images and CI runners that cannot clone at runtime, a seed is a plugins directory built ahead of time. Claude Code registers the seed's marketplaces at startup and loads plugin caches from the seed in place, without cloning. A seed also serves users with no git-host account.

# How to use it

1. Build: `CLAUDE_CODE_PLUGIN_CACHE_DIR=/opt/claude-seed claude plugin marketplace add your-org/your-marketplace`, then `CLAUDE_CODE_PLUGIN_CACHE_DIR=/opt/claude-seed claude plugin install code-formatter@your-marketplace`. Layout matches `~/.claude/plugins`: `known_marketplaces.json`, `marketplaces/<name>/`, `cache/<marketplace>/<plugin>/<version>/`. The seed can be mounted at a different path than it was built at.
2. Run: set `CLAUDE_CODE_PLUGIN_SEED_DIR=/opt/claude-seed`. Several seeds are separated by `:` (Unix) or `;` (Windows); the first seed containing a marketplace or cache is used.
3. Enable: seed plugins are not enabled on their own. Set `enabledPlugins` in managed settings or repo `.claude/settings.json`.

Verify with `claude -p --output-format stream-json --verbose`: each loaded plugin's `path` in the `init` event is under the seed.

# Limits and defaults

- Seed marketplaces are read-only; Claude Code never writes to the seed and forces `autoUpdate` off for them.
- If settings declare the seed marketplace name in `extraKnownMarketplaces`, build the seed from that source and `ref`.
- To opt out of a seed plugin enabled by repo settings, use `claude plugin disable`, not removing the marketplace.
- `claude plugin marketplace update <name>` and `remove` (without `--scope`) on a seed marketplace fail naming the seed directory.
- Allowlist and blocklist still check a seed marketplace's recorded source.

# Notes

On GitHub Actions, export a token with read access as `GH_TOKEN` and run `gh auth setup-git`; the default workflow token reaches only the workflow's own repository. For fleets with no outbound git, combine a seed with `directory`/`file` sources on a shared mount and set `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` (also turns off plugin auto-update); see Proxy configuration for proxy variables.
