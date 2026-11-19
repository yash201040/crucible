---
type: "Reference"
title: "What the classifier blocks by default"
description: "Default block list for auto mode, version-gated additions, and the trust boundary it assumes."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, blocklist, security, git]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli]
requires: ""
identifiers:
  - "autoMode.environment"
  - "claude auto-mode defaults"
  - "permissions.ask"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The classifier trusts the working directory and the remotes configured when the session started. A remote added or repointed in-session (`git remote add`, `git remote set-url`) is untrusted, and everything else is external until configured as trusted infrastructure via `autoMode.environment`.

# How to use it

Blocked by default (condensed):

| Group | Examples |
| :- | :- |
| Code and data egress | `curl \| bash`; sending sensitive data to external endpoints; committing/pushing secrets or widening deploy exposure (CI secret to a new destination, sourcemap/visibility settings) on any branch; pushing secrets to a known-public repo; session transcripts, credential dot-folders, shell history entering a commit/push/PR/gist/publish; links to public paste services that carry content in the URL (v2.1.261+) |
| Destructive git | `git reset --hard`, `git checkout -- .`, `git restore .`, `git clean -fd`, `git stash drop/clear`; force push; `git commit --amend` on a HEAD commit not created this session, or (v2.1.198+) already pushed (message-only reword of a Claude-made unpushed commit with nothing newly staged is allowed) |
| Infrastructure | production deploys and migrations; `terraform destroy`, `pulumi destroy`, `cdk destroy`, `terragrunt destroy`; mass cloud-storage deletion; IAM or repo permission grants; shared infrastructure; DaemonSets/admission webhooks; draining nodes; secret-manager writes; DNS or TLS changes; production feature flags; cluster writes broader than the named resource |
| Review and CI | merging a PR no human approved; approving Claude's own PR; disabling CI checks; commands-to-automation comments (`atlantis apply`, `/deploy`, `/merge`) |
| Network and shells | tunnels or reverse shells; interactive shells or port-forwards into sensitive targets; routing installs around the internal registry; flags like `--insecure` |
| Autonomy | launching agent loops without approval or sandbox (`--dangerously-skip-permissions`, `--no-sandbox`, `--yes-always`) |
| Self-protection | sending keystrokes to Claude's own tmux pane; writing session transcript `.jsonl` files under `~/.claude/projects/` (reading is allowed); deleting or weakening security tests |
| Misc | printing live credentials; Claude in Chrome actions sending content off-origin; wildcard deletes in `/tmp`/`$TMPDIR`; repointing API base URLs/webhooks to third-party hosts; changing push targets without naming them; PRs to other repos/orgs and `gh repo fork`; outbound content with sensitive details; deleting stateful resources not created in-session; recursive forced delete on an unassigned shell variable (clears when the exact path is named or the literal path is re-run) |

v2.1.257+ also blocks: requesting credentials from the instance-metadata endpoint (`169.254.169.254`) or using the machine's own service identity; reaching a public host by tunnel, reverse shell or rewritten resolver/proxy; reading host (not task) credentials such as node certificates; connecting to or scanning sibling containers, pods, VMs or the node. Where meant to be allowed, describe a Host containment entry in `autoMode.environment`.

# Notes

Several categories depend on environment entries (sensitive remote targets, protected IaC scopes) that can be narrowed. Allowed counterpart: [classifier allowed by default](./classifier-allowed-by-default.md).
