---
type: "Feature"
title: "Hooks in skill and subagent frontmatter"
description: "Hooks declared in skill or subagent frontmatter, their lifetime, trust rules, plugin-only lock and per-source hook limits."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, skills, subagents, limits]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli]
requires: ""
identifiers:
  - "hooks"
  - "once"
  - "strictPluginOnlyCustomization"
  - "registers none of its hooks"
  - "claude --debug"
  - "/debug"
  - "/hooks"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills and subagents can carry a `hooks` block in YAML frontmatter, same format as settings hooks.

- Subagent hooks run only while that subagent runs and are removed when it finishes. A `Stop` hook there is converted to `SubagentStop`.
- Skill hooks register when you or Claude invoke the skill and stay for the rest of the session, including later turns. `once: true` removes the hook after its first successful run.

# How to use it

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: '"${CLAUDE_PROJECT_DIR}"/scripts/security-check.sh'
---
```

Trust: frontmatter hooks in a project skill follow the same workspace-trust rule as settings hooks and register on invocation, even in a `-p` run in an untrusted folder. Frontmatter hooks in a project subagent run only after the workspace trust dialog is accepted for that folder; a `-p` session does not count as accepting.

# Limits and defaults

- Plugin-only lock: `strictPluginOnlyCustomization` (managed setting) can lock hooks to plugins and managed settings. Under it a skill keeps frontmatter hooks only if it is a plugin skill, bundled skill, or in the managed settings directory; hooks in your own settings files do not run. Check `/status` for `Enterprise managed settings` in `Setting sources`; fix by moving the skill into a plugin.
- Hook limit (v2.1.304+): per session, each skill source (project, personal folder, each plugin) can register at most 1,024 hooks, with matchers totaling at most 16,384 characters; a matcher with several hooks counts once per hook. Diagnose with `claude --debug` (or `/debug`), invoking the same skills in the same order, and search the debug log for `registers none of its hooks`.
- If `/hooks` lists none of a skill's hooks, check the above, then whether frontmatter parsed.
