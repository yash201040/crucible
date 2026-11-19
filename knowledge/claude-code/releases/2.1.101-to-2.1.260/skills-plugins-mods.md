---
type: "Release Digest"
title: "Skills, plugins and extensions (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on skills, plugins, marketplaces, bundled skills and slash commands."
resource: "https://code.claude.com/docs/en/changelog"
tags: [skills, plugins, marketplaces, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "/reload-plugins"
  - "claude plugin validate --json"
  - "claude-api"
  - "workflow-authoring"
  - "/claude-api cost-optimize"
  - "plugin_id_hash"
  - "enabled_via"
  - "name@synced"
  - "/claude-api upgrade"
  - "headersHelper"
  - "claude plugin install"
  - "claude plugin update"
  - "claude plugin validate"
  - "additionalMarketplaces"
  - "allowedMarketplaces"
  - "extraKnownMarketplaces"
  - "strictKnownMarketplaces"
  - "blockedMarketplaces"
  - "command"
  - "mode: link"
  - "archive"
  - "/review"
  - "/code-review"
  - "disable-model-invocation"
  - "skills"
  - "prompt-audit"
  - "/deep-research"
  - "dataviz"
  - "/verify"
  - "pluginConfigs"
  - "/doctor"
  - "/checkup"
  - "/dataviz"
  - "renames"
  - "display-name"
  - "default-enabled"
  - "fallback"
  - "metadata"
  - "disableBundledSkills"
  - "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS"
  - "--safe-mode"
  - "CLAUDE_CODE_SAFE_MODE"
  - "/plugin list"
  - "--enabled"
  - "--disabled"
  - "claude plugin init"
  - "defaultEnabled"
  - "skipLfs"
  - "/reload-skills"
  - "disallowed-tools"
  - "pluginSuggestionMarketplaces"
  - "--scope"
  - "claude plugin disable"
  - "claude plugin enable"
  - "SKILL.md"
  - "CLAUDE_CODE_PLUGIN_PREFER_HTTPS"
  - "claude plugin details"
  - "--plugin-url"
  - "skillOverrides"
  - "experimental"
  - "--plugin-dir"
  - "claude plugin prune"
  - "--prune"
  - "${CLAUDE_EFFORT}"
  - "/ultrareview"
  - "claude plugin tag"
  - "/less-permission-prompts"
  - "/skills"
  - "Skill"
  - "monitors"
  - "/team-onboarding"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.260 | 2026-09-03 | /reload-plugins added to headless sessions; claude plugin validate --json; bundled claude-api skill samples use current model IDs | `/reload-plugins`, `claude plugin validate --json`, `claude-api` |
| 2.1.259 | 2026-09-02 | claude plugin validate --json machine-readable report | `claude plugin validate --json` |
| 2.1.248 | 2026-08-27 | Workflow-writing reference moved into bundled workflow-authoring skill | `workflow-authoring` |
| 2.1.247 | 2026-08-26 | /claude-api cost-optimize profiles API spend; /claude-api skill gains Admin API coverage | `/claude-api cost-optimize` |
| 2.1.246 | 2026-08-25 | OTel plugin events: plugin_id_hash reflects the real marketplace; enabled_via is admin-install for admin-installed plugins | `plugin_id_hash`, `enabled_via` |
| 2.1.239 | 2026-08-21 | Cloud sessions show claude.ai-synced plugins as name@synced; /claude-api upgrade migrates Python anthropic 0.x to 1.x | `name@synced`, `/claude-api upgrade` |
| 2.1.238 | 2026-08-20 | Plugin marketplace headersHelper mints HTTP headers for catalog and archive fetches; catalog-entry helper runs only at install or update after the command is shown (claude plugin install/update ask y/N or -y) | `headersHelper`, `claude plugin install`, `claude plugin update` |
| 2.1.237 | 2026-08-20 | Built-in Concise output style |  |
| 2.1.233 | 2026-08-14 | claude plugin validate checks a bare .claude/skills directory for unparsable SKILL.md frontmatter | `claude plugin validate` |
| 2.1.232 | 2026-08-13 | additionalMarketplaces and allowedMarketplaces accepted as aliases for extraKnownMarketplaces and strictKnownMarketplaces; bare gitlab.com repo URLs work as marketplaces; /plugin install refreshes the marketplace first | `additionalMarketplaces`, `allowedMarketplaces`, `extraKnownMarketplaces`, `strictKnownMarketplaces`, `blockedMarketplaces` |
| 2.1.229 | 2026-08-12 | Plugin marketplace command sources: a local command prints the plugin directory, re-resolved each session; mode link uses it in place | `command`, `mode: link` |
| 2.1.228 | 2026-08-11 | Skills synced from claude.ai no longer shadow local commands, descriptions are sanitized and bodies do not run ! commands or expand @ files |  |
| 2.1.224 | 2026-08-07 | archive plugin source installs a zip over HTTPS with optional SHA-256 pinning | `archive` |
| 2.1.223 | 2026-08-06 | Owner wildcard entries owner/* for strictKnownMarketplaces and blockedMarketplaces | `strictKnownMarketplaces`, `blockedMarketplaces` |
| 2.1.223 | 2026-08-06 | /review is now an alias of /code-review; /code-review with no level reuses the last level | `/review`, `/code-review` |
| 2.1.222 | 2026-08-04 | Refusal when Claude invokes a skill with disable-model-invocation tells it to ask you; ultraplan feature removed | `disable-model-invocation` |
| 2.1.221 | 2026-08-04 | claude plugin validate warns on names Claude Desktop would reject; plugins accept . as a skills path; /plugin installs activate immediately when safe; prompt-audit subcommand in claude-api skill | `skills`, `prompt-audit` |
| 2.1.218 | 2026-07-22 | /code-review runs as a background subagent; /deep-research starts only when invoked manually; frontmatter booleans accept yes, no, on, off, 1, 0 | `/code-review`, `/deep-research` |
| 2.1.216 | 2026-07-20 | Bundled dataviz skill palette reordered | `dataviz` |
| 2.1.215 | 2026-07-19 | Claude no longer runs /verify and /code-review on its own | `/verify`, `/code-review` |
| 2.1.207 | 2026-07-11 | Plugin option values (pluginConfigs) read only from user, --settings and managed settings, not project settings | `pluginConfigs` |
| 2.1.205 | 2026-07-08 | /doctor is a full setup checkup (alias /checkup); Claude Browser reserved as MCP server name | `/doctor`, `/checkup` |
| 2.1.202 | 2026-07-06 | /review <pr> back to a fast single pass; /code-review <level> <pr#> is the multi-agent review | `/review`, `/code-review` |
| 2.1.199 | 2026-07-02 | Stacked slash-skill invocations load up to 5 leading skills |  |
| 2.1.198 | 2026-07-01 | /dataviz skill added | `/dataviz` |
| 2.1.193 | 2026-06-25 | Plugin auto-rename follows marketplace renames maps | `renames` |
| 2.1.186 | 2026-06-22 | claude mcp login/logout; Skills section in /plugin Installed tab; skill frontmatter display-name, default-enabled, fallback and metadata.* accept kebab, snake and camel case; malformed SKILL.md frontmatter loads body with empty metadata | `display-name`, `default-enabled`, `fallback`, `metadata` |
| 2.1.178 | 2026-06-15 | Skills in nested .claude/skills load when working on files there, named dir:name on a clash |  |
| 2.1.169 | 2026-06-08 | disableBundledSkills setting and CLAUDE_CODE_DISABLE_BUNDLED_SKILLS hide bundled skills, workflows and built-in slash commands from the model; --safe-mode disables customizations | `disableBundledSkills`, `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS`, `--safe-mode`, `CLAUDE_CODE_SAFE_MODE` |
| 2.1.163 | 2026-06-04 | /plugin list with --enabled and --disabled; skills escape \$ for a literal dollar before a digit | `/plugin list`, `--enabled`, `--disabled` |
| 2.1.157 | 2026-05-29 | claude plugin init <name> scaffolds a plugin; plugins in .claude/skills load automatically | `claude plugin init` |
| 2.1.154 | 2026-05-28 | Plugins can declare defaultEnabled: false in plugin.json or a marketplace entry | `defaultEnabled` |
| 2.1.153 | 2026-05-28 | skipLfs option on github/git plugin marketplace sources | `skipLfs` |
| 2.1.152 | 2026-05-27 | /reload-skills re-scans skill directories; skills and slash commands accept disallowed-tools frontmatter; pluginSuggestionMarketplaces managed setting; claude plugin marketplace remove --scope | `/reload-skills`, `disallowed-tools`, `pluginSuggestionMarketplaces`, `--scope` |
| 2.1.143 | 2026-05-15 | claude plugin disable refuses when another enabled plugin depends on it, enable force-enables dependencies; /plugin browse shows projected context cost | `claude plugin disable`, `claude plugin enable` |
| 2.1.142 | 2026-05-14 | Plugins with a root-level SKILL.md and no skills/ directory surface as a skill; claude plugin details shows LSP servers | `SKILL.md` |
| 2.1.141 | 2026-05-13 | CLAUDE_CODE_PLUGIN_PREFER_HTTPS clones GitHub plugin sources over HTTPS | `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` |
| 2.1.139 | 2026-05-11 | claude plugin details <name> shows component inventory and projected per-session token cost | `claude plugin details` |
| 2.1.129 | 2026-05-06 | --plugin-url fetches a plugin zip for the session; plugin manifests declare themes and monitors under experimental; skillOverrides setting works (off, user-invocable-only, name-only) | `--plugin-url`, `skillOverrides`, `experimental` |
| 2.1.128 | 2026-05-04 | --plugin-dir accepts .zip archives | `--plugin-dir` |
| 2.1.121 | 2026-04-28 | claude plugin prune removes orphaned auto-installed dependencies (plugin uninstall --prune) | `claude plugin prune`, `--prune` |
| 2.1.120 | 2026-04-28 | Skills can reference ${CLAUDE_EFFORT}; claude plugin validate accepts $schema, version, description | `${CLAUDE_EFFORT}` |
| 2.1.120 | 2026-04-28 | claude ultrareview subcommand and /ultrareview run multi-agent cloud code review | `/ultrareview` |
| 2.1.118 | 2026-04-23 | Custom themes from /theme and plugin themes/ directory; claude plugin tag creates release git tags | `claude plugin tag` |
| 2.1.111 | 2026-04-16 | /less-permission-prompts skill scans transcripts for read-only Bash and MCP calls and proposes an allowlist; /ultrareview added; /skills sorts by token count with t | `/less-permission-prompts`, `/ultrareview`, `/skills` |
| 2.1.108 | 2026-04-14 | Model can invoke built-in slash commands like /init, /review, /security-review via the Skill tool; /undo alias for /rewind | `Skill` |
| 2.1.105 | 2026-04-13 | Plugin monitors manifest key arms background monitors at session start or on skill invoke; skill description listing cap raised from 250 to 1,536 characters | `monitors` |
| 2.1.101 | 2026-04-10 | /team-onboarding generates a teammate ramp-up guide; plugin update warns when marketplace could not refresh | `/team-onboarding` |

# Not found in the documentation pages

These identifiers occur only in the release notes, not in the saved documentation pages:

- `claude plugin validate --json`
- `/claude-api cost-optimize`
- `/claude-api upgrade`
- `mode: link`
- `default-enabled`
- `/less-permission-prompts`
