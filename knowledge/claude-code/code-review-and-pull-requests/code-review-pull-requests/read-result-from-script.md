---
type: "Guide"
title: "Read Code Review results from a script"
description: "Parse the bughunter-severity JSON comment on the check run's Details text with gh and jq to gate a merge from your own CI."
resource: "https://code.claude.com/docs/en/code-review-pull-requests"
tags: [code-review, ci, gh, automation]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "gh CLI and jq"
identifiers:
  - "bughunter-severity"
  - "gh api repos/OWNER/REPO/commits/<commit-sha>/check-runs"
  - "gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-pull-requests"
    resource: "https://code.claude.com/docs/en/code-review-pull-requests"
    title: "Read and request reviews on a pull request"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The last line of the check run's `output.text` is an HTML comment holding severity counts as JSON:

`<!-- bughunter-severity: {"nit":1,"normal":2,"pre_existing":0} -->`

`normal` is the count of Important findings. Take counts from the last line only, since earlier lines can contain file names from the PR.

# How to use it

1. List the commit's check runs and take the `id` of `Claude Code Review` (GitHub lists only the newest after a Re-run): `gh api repos/OWNER/REPO/commits/<commit-sha>/check-runs --jq '.check_runs[] | {id, name}'`.
2. Read `output.text` of `gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID`, split on newline, take last line, scan for the comment pattern and `fromjson`, with `error("no severity line")` as fallback. Keys come out alphabetical.
3. Handle in order: title starts with `Code review not repeated` (earlier Important findings still open; no severity line; read `.output.title`; fail the job to gate); title ends with `no new changes` (pass); `normal` above zero (fail to gate); line missing (no verdict, not zero findings; failed, timed-out, canceled or superseded runs have none, and some completed ones too).

# Notes

Counts include findings from earlier reviews whose threads are still open, except on a check run that kept an earlier result; under `Code review skipped — no new changes`, counts leave out earlier nits and pre-existing findings.
