---
type: "Guide"
title: "Prepare a plugin for release"
description: "Pre-release checklist: permanent name, versioning choice, strict validation, local marketplace install, metadata, and evals."
resource: "https://code.claude.com/docs/en/plugins/publish"
tags: [plugins, release, validation, versioning]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate --strict"
  - "claude plugin marketplace add"
  - "claude plugin update"
  - "claude plugin eval"
  - "displayName"
  - "version"
  - "homepage"
  - "repository"
  - "${CLAUDE_PLUGIN_ROOT}"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-publish"
    resource: "https://code.claude.com/docs/en/plugins/publish"
    title: "Publish and distribute a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

1. **Permanent name.** Users install, enable and configure by `name@marketplace`; a rename makes it a different plugin. Use kebab-case (`claude plugin validate` warns on other forms). Set `displayName` for the label users see.
2. **Versioning.** If `version` is set in `plugin.json` and commits are pushed without changing it, `claude plugin update` prints `<name> is already at the latest version (1.0.0).` and users keep the old copy. Either bump `version` each release, or omit it in a git-hosted marketplace so the commit SHA is used.
3. **Validate.** `claude plugin validate --strict ./your-plugin` prints `✔ Validation passed`. In CI keep `--strict` (exit code 1 on warnings such as an unknown manifest field or missing `version`); drop it if you omit `version`. Validation reports component paths not starting with `./`; inside hooks and MCP configs use `${CLAUDE_PLUGIN_ROOT}/...`.
4. **Install from a local marketplace.** `claude plugin marketplace add ./path-to-marketplace`, install, start a session.
5. **Metadata.** Set `description`, `author`, `homepage` (must parse as a URL), `repository` and add a root `README.md`.
6. **Evals.** `claude plugin eval` runs test cases and scores results.
