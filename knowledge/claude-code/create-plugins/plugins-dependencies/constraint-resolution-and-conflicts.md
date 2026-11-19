---
type: "Concept"
title: "How constraints resolve and combine"
description: "Highest matching tag wins; several plugins' ranges intersect, conflicts block installs, and auto-update honors all ranges."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, dependencies, resolution, auto-update]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin list"
  - "claude plugin prune"
  - "has conflicting version requirements"
  - "has no git tag satisfying"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A constraint such as `~2.1.0` installs from the highest `secrets-vault--v` tag satisfying it. If no tag satisfies: a plugin with its own repository fails with `Dependency "secrets-vault@your-marketplace" has no git tag satisfying`; a plugin referenced by relative path uses the marketplace's current copy and checks at load, staying disabled if outside the range (`claude plugin list` shows `Requires "secrets-vault@your-marketplace" ~2.1.0, installed 3.0.0`). A local-folder marketplace that is a git repo also resolves against its tags; a non-git folder installs current contents.

# How to use it

`claude plugin list` shows a tag-resolved dependency with a 12-character commit suffix (for example `2.1.0-8713c5b11005`). Constraint checks use the tag's version, not `plugin.json`'s. A force-moved tag is refetched on next install.

| Plugin A | Plugin B | Result |
| :- | :- | :- |
| `^2.0` | `>=2.1` | One install at highest `2.x` tag at or above `2.1.0` |
| `~2.1` | `~3.0` | Installing B fails with `has conflicting version requirements`; A and the dependency stay |
| `=2.1.0` | none | Stays at `2.1.0`; auto-update skips newer versions |

# Notes

Auto-update fetches at the highest tag satisfying every installed plugin's range; non-overlapping ranges leave it unchanged with an entry in the `/plugin` Errors tab. Uninstalling the last constraining plugin returns the dependency to tracking its marketplace entry. `claude plugin prune` removes auto-installed dependencies no plugin needs.
