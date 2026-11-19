---
type: "Reference"
title: "Marketplace file location and reserved names"
description: "Where marketplace.json lives, how marketplace roots resolve, and which marketplace names are reserved or refused."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, reserved-names, marketplace-json, validation]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - ".claude-plugin/marketplace.json"
  - "claude-code-marketplace"
  - "claude-code-plugins"
  - "claude-plugins-official"
  - "anthropic-marketplace"
  - "anthropic-plugins"
  - "agent-skills"
  - "anthropic-agent-skills"
  - "life-sciences"
  - "knowledge-work-plugins"
  - "claude-for-legal"
  - "claude-for-financial-services"
  - "financial-services-plugins"
  - "first-party-plugins"
  - "claude-tag-plugins"
  - "claude-community"
  - "claude-plugins-community"
  - "healthcare"
  - "anthropic-plugin-directory"
  - "claude-plugin-directory"
  - "inline"
  - "builtin"
  - "skills-dir"
  - "synced"
  - "claude-plugin-test"
  - "claudeai-"
  - "extraKnownMarketplaces"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`marketplace.json` defines a plugin marketplace: its name, owner and one entry per plugin. It is saved at `.claude-plugin/marketplace.json` in the marketplace directory. The directory containing `.claude-plugin/` is the marketplace root, and every relative plugin source resolves from the root, not from `.claude-plugin/`.

# How to use it

If the file is kept elsewhere in the repo, users must declare the marketplace in `extraKnownMarketplaces` with `path` on its source, because `claude plugin marketplace add` has no option for it. Each user registers one marketplace per `name`. Unknown top-level or entry keys are ignored silently (a typo loads without error); `claude plugin validate` warns about each.

Names you cannot use:

| Group | Names / rule | Notes |
| :- | :- | :- |
| Official | `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `anthropic-agent-skills`, `life-sciences`, `knowledge-work-plugins`, `claude-for-legal`, `claude-for-financial-services`, `financial-services-plugins`, `first-party-plugins`, `claude-tag-plugins` | Reserved unless the marketplace comes from a `github` or `git` source under `github.com/anthropics/` |
| Community | `claude-community`, `claude-plugins-community`, `healthcare` | Same rule |
| Plugin directory | `anthropic-plugin-directory`, `claude-plugin-directory` | Same rule |
| Impersonation | e.g. `official-claude-plugins`, `claude-plugins-v2`, any non-ASCII name | Error `Marketplace name impersonates an official Anthropic/Claude marketplace`; control or bidirectional characters give a separate error; an already registered marketplace stops loading with its plugins |
| Other spelling | trailing dot, or a non-underscore symbol instead of a hyphen (`claude.code.plugins`) | Fails with `is another spelling of "<reserved>", a reserved marketplace name`. Needs v2.1.280 or later |
| Non-marketplace plugin sources | `inline` (`--plugin-dir`), `builtin`, `skills-dir` (auto-loaded from `.claude/skills/`), `synced` (claude.ai account), `claude-plugin-test` | `skills-dir` also appears as `{"source": "skills-dir"}` in policy lists |
| JS object members | `constructor`, `hasOwnProperty`, `isPrototypeOf`, `propertyIsEnumerable`, `toLocaleString`, `toString`, `valueOf` | Refused by `marketplace add`. Needs v2.1.296 or later |
| `claudeai-` prefix | reserved for marketplaces hosted on claude.ai | Other marketplaces refused |
| `<owner>-<repo>` download folder | a GitHub marketplace `acme/x-tools` downloads via folder `acme-x-tools` | A different marketplace named `acme-x-tools` is refused with `Can't use the marketplace name "acme-x-tools"`. Needs v2.1.290 or later |

# Notes

When a registered marketplace stops loading for an imitating name, `claude plugin list` and `/plugin` report `Claude Code refuses the marketplace name "<name>"` (named message needs v2.1.282 or later). Removing it also uninstalls its plugins and deletes their data, options and secrets. If a settings file declares it inline, rename its entry before removing the old name (steps listed in v2.1.292 or later).
