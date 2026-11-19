---
type: "Guide"
title: "Host a marketplace and grant private access"
description: "Host options and add commands, git credential behavior for private marketplaces, shared directories, symlinks, organization sync and users without git accounts."
resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
tags: [marketplace, hosting, git, credentials, private]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, cloud]
requires: "Organization sync needs a Team or Enterprise plan"
identifiers:
  - "/plugin marketplace add"
  - "--scope project"
  - "CLAUDE_CODE_PLUGIN_PREFER_HTTPS"
  - "CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE"
  - "GIT_ASKPASS"
  - "GITHUB_TOKEN"
  - "GH_TOKEN"
  - "sha256"
  - "bin/"
  - "ssh -T git@github.com"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-host-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/host-marketplace"
    title: "Host and maintain a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hosting means putting `marketplace.json` where others can add it. Four hosts: GitHub (`/plugin marketplace add your-org/your-marketplace`), another git host (full URL; `owner/repo` always means github.com), a hosted `marketplace.json` URL (HTTPS only, no git needed), or a shared-filesystem directory. Append `#<ref>` to pin a branch or tag (`your-org/your-marketplace#stable`). To register for everyone in a repo, run `claude plugin marketplace add ... --scope project` once and commit the written `.claude/settings.json`.

# How to use it

- URL-hosted marketplaces download only the `marketplace.json`, so relative-path entries fail at install (`its marketplace entry path does not stay inside the marketplace directory`). Use `github`, `archive` etc. sources, or host in a git repo.
- Shared directory: relative-path plugins are read in place; edits show on next session or `/reload-plugins`, no version bump.
- Git LFS: clones never download LFS content, so LFS files arrive as pointers.
- Symlinks inside a plugin dir when cached: target within plugin kept as relative symlink; target elsewhere in the same marketplace is dereferenced (content copied); target outside the marketplace is skipped. Local-path and default `copy`-mode `command` installs keep only symlinks within the plugin.
- Organization sync (Organization settings > Plugins & skills on claude.ai): uses the org's GitHub/GitLab connection, no user credentials. Stricter: repo must be private or internal on github.com/gitlab.com, only some source types accepted, and a plugin with a top-level `bin/` is rejected (`Plugin contains a top-level bin/ directory`); use `scripts/` and `${CLAUDE_PLUGIN_ROOT}/scripts/<name>`.
- Private access: Claude Code runs `git` on the user's machine with prompts off and no token of its own. GitHub `owner/repo` probes `ssh -T git@github.com` and clones over SSH, else HTTPS (set `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` to skip the probe). `git@host:path.git` is SSH, `https://` is HTTPS. SSH needs a passphrase-free usable key and host in `known_hosts`. HTTPS keeps the credential helper but forbids prompts and ignores `GIT_ASKPASS`; use `gh auth login` and `gh auth setup-git`.
- Users without git accounts: `archive` sources (pin `sha256`), public git repos via `https://` URL, shared directories. Installs from `/plugin` and plugin updates do not fall back to HTTPS the way `claude plugin install` does, so keep the `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` instruction.

# Limits and defaults

Background auto-update of a private marketplace uses the user's credential helpers and never prompts. If the check finds new commits or cannot reach or authenticate, Claude Code re-clones and replaces the checkout; if that clone fails the old one stays. Setting `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1` keeps the checkout instead of re-cloning. `GITHUB_TOKEN` alone does not authenticate; it works only through a helper that reads it.

# Notes

Rollout roles: owner (repo, add command), admin (`extraKnownMarketplaces`, `enabledPlugins`, `autoUpdate`), each person (read access). Marketplace cannot do: restrict others, install/enable plugins itself, show different entries per user, mark deprecated, carry git credentials.
