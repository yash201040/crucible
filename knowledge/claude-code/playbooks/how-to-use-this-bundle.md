---
type: "Playbook"
title: "How to use this bundle"
description: "What the bundle is for, how it is laid out, how to search it and how to keep it current."
tags: [bundle, howto]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "crucible_okf.py"
orchestration: "high"
status: "stable"
generated: { by: "claude-code/fable-5.2", at: "2026-11-20T00:00:00Z" }
sources:
  - id: "okf"
    resource: "https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md"
    title: "Open Knowledge Format 0.2"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is for

Crucible runs on a host, Claude Code. What the host can do changes every few days. This bundle is the host's own documentation, taken apart into about 1,650 notes of one feature, limit or table of names each, so that a review of crucible can ask two questions cheaply: what does the host offer that we do not use, and what changed since we last looked.

It is written in [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) 0.2: one markdown file per concept with a YAML header, an `index.md` in every folder, a `log.md` of changes. The documentation's text is not stored here, only notes on it, each with a link to its page.

# Layout

| Folder | What is in it | Who writes it |
| --- | --- | --- |
| one folder per section of the documentation's own index, then one per page | concepts read from the documentation | readers, when the documentation is read (never edited by hand) |
| [releases](/releases/) | what each range of releases added, by theme, and the names that occur only in release notes | readers |
| [release](/release/) | the pin: which release the bundle describes | the build |
| [experiments](/experiments/) | what was tested on the host, with figures | whoever ran the test |
| [playbooks](/playbooks/) | what crucible uses of the host, and why not the rest | the maintainer and reviews |

# Header fields beyond OKF's own

`kind` (env_var, setting, cli_flag, slash_command, tool, hook, frontmatter, file, api, ui, behavior, limit, mixed), `maturity` (the documentation's own label: experimental, beta, preview, research-preview, deprecated, or unlabelled), `since` (a release, where the page states one), `surfaces`, `requires`, `identifiers` (every exact name the concept covers) and `orchestration` (high, medium, low, none: how much it matters to a program that runs many agents unattended; the readers were generous with "high").

A concept read from the documentation is unverified in OKF's sense: a reader wrote it and nobody ran it. An experiment carries `verified`.

# Searching

    python3 scripts/crucible_okf.py find CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH
    python3 scripts/crucible_okf.py find cache subagent --high
    python3 scripts/crucible_okf.py list --category agents-and-parallel-work --orchestration high
    python3 scripts/crucible_okf.py list --maturity experimental
    python3 scripts/crucible_okf.py show agents-and-parallel-work/workflows/runtime-limits-and-concurrency.md

Or open any folder's `index.md`.

# Keeping it current

See [the pin](/release/pin.md). In short: `crucible_okf.py refresh` says which releases and pages are new; read the release notes first; re-read only the changed pages; run the experiments again whose subject changed.
