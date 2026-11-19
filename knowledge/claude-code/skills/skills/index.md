# skills/skills

* [Bundled skills](bundled-skills.md) - Prompt-based skills shipped with Claude Code (/doctor, /code-review, /batch, /debug, /loop, /claude-api) and how to turn them off.
* [/claude-api skill subcommands](claude-api-skill.md) - The bundled /claude-api skill and its subcommands (migrate, upgrade, cost-optimize, build-eval, hillclimb and more) with minimum versions.
* [Control who invokes a skill](control-skill-invocation.md) - disable-model-invocation and user-invocable decide whether you, Claude, or both can run a skill and when its description is in context. **[high]**
* [Skills in Cowork and cloud sessions](cowork-cloud-skills.md) - Cowork and cloud sessions, including cloud scheduled tasks, do not read ~/.claude/skills/; they load claude.ai account skills. **[high]**
* [Create your first skill](create-first-skill.md) - Minimal SKILL.md in ~/.claude/skills/<name>/ with frontmatter and an injected git diff, invoked by /name or automatically.
* [/doctor setup checkup](doctor-checkup.md) - /doctor diagnoses installation, extensions, CLAUDE.md, permissions and plan usage; /doctor prompt-audit checks instruction files.
* [Dynamic context injection (! commands)](dynamic-context-injection.md) - !`cmd` and ```! blocks run shell commands before Claude sees the skill; failures abort the invocation; disableSkillShellExecution turns it off. **[high]**
* [Run a skill in a subagent (context: fork)](fork-skill-in-subagent.md) - context: fork starts an isolated subagent of type agent with the skill as its prompt; runs in background by default. **[high]**
* [Frontmatter portability outside Claude Code](frontmatter-outside-claude-code.md) - claude.ai uploads, the Skills API and package_skill.py accept only six frontmatter fields and fail hard on others.
* [Live skill edits and removing skills](live-change-and-removal.md) - Skill directories are watched for changes (except bare mode); /reload-skills for new top-level dirs; how to remove each kind of skill.
* [Pre-approving tools for a skill](pre-approve-tools-for-skill.md) - allowed-tools grants permission for one turn; disallowed-tools removes tools; managed policies can ignore the grant. **[high]**
* [Restricting Claude's skill access](restrict-skill-access.md) - Deny the Skill tool or use Skill(name) allow and deny permission rules, including alias, nested and synced-skill matching. **[high]**
* [/run, /verify and pre-commit checks](run-and-verify-skills.md) - Bundled /run, /verify and /run-skill-generator launch and confirm changes in the real app; a verify or simplify skill is run before each commit. **[high]**
* [Sharing skills](sharing-skills.md) - Distribute skills via committed project .claude/skills/, plugins, or managed settings.
* [Passing arguments and stacking skills](skill-arguments-and-stacking.md) - Skills take arguments from the user or Claude; at the terminal up to six skills can be stacked in one message, but -p and the SDK load only the first. **[high]**
* [Skill content lifecycle and compaction](skill-content-lifecycle.md) - Invoked skill content stays in context, is not re-read, and is re-attached after compaction within 5,000 tokens each and 25,000 combined. **[high]**
* [Skill discovery in subdirectories and added dirs](skill-discovery-added-dirs.md) - How project skills load from parent, nested, worktree and --add-dir directories, and how same-named skills get prefixed. **[high]**
* [/skill-doctor and skill evals](skill-doctor-and-evals.md) - /skill-doctor reports skill context cost and usage; evaluate skills with baseline comparison, claude plugin eval or the skill-creator plugin. **[high]**
* [Skill frontmatter fields](skill-frontmatter-fields.md) - Every SKILL.md frontmatter field (name, description, allowed-tools, model, effort, context, hooks, paths, shell and more) with semantics. **[high]**
* [Where skills live](skill-locations.md) - Skill locations (enterprise, personal, project, nested, added directory, plugin, claude.ai) with paths and what each loads in, plus folder rules. **[high]**
* [Resolving skills that share a name](skill-name-resolution.md) - Precedence table for same-named skills across enterprise, personal, project, bundled, built-in, plugin, added-directory and synced sources.
* [Skill command names and invalid characters](skill-name-rules.md) - How the invoked command name derives from file layout and frontmatter name, and which characters make Claude Code refuse a name.
* [skillOverrides setting](skill-overrides-setting.md) - Set a skill to on, name-only, user-invocable-only or off from settings without editing SKILL.md. **[high]**
* [Skill string substitutions](skill-string-substitutions.md) - $ARGUMENTS, $N, $name and ${CLAUDE_*} placeholders available inside skill content and allowed-tools rules. **[high]**
* [Supporting files in a skill](skill-supporting-files.md) - A skill directory can hold reference files and scripts loaded on demand; keep SKILL.md under 500 lines.
* [Skill troubleshooting and listing budget](skill-troubleshooting.md) - Fix skills that do not trigger, trigger too often, stop being followed, have truncated descriptions or vanished; listing budget settings. **[high]**
* [Skills synced from claude.ai](synced-claude-ai-skills.md) - Terminal sessions signed in with claude.ai download account skills to ~/.claude/skills/synced/; sync cadence, exclusions, naming and body handling. **[high]**
