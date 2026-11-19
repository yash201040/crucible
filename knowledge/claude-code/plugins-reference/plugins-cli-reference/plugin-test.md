---
type: "Feature"
title: "claude plugin test"
description: "Runs every *.test.ts and *.test.tsx file under a mod's directory with no session, sign-in or network; exits 1 on failure."
resource: "https://code.claude.com/docs/en/plugins/cli-reference"
tags: [plugins, mods, testing, ci]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin test"
  - ".test.ts"
  - ".test.tsx"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-cli-reference"
    resource: "https://code.claude.com/docs/en/plugins/cli-reference"
    title: "Plugin commands reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin test [directory]` runs the tests for a mod (a plugin whose code registers event handlers). `[directory]` defaults to the current directory. It runs every file under it whose name ends in `.test.ts` or `.test.tsx` and exits with status 1 when a test fails. It needs no session, sign-in or network. It has no session form (not available as a `/plugin` subcommand).

# How to use it

`claude plugin test ./first-mod`. See [Write and run a mod test](../../mods/plugins-mods-test/write-a-mod-test.md).
