# model-and-responses/model-config

* [Adaptive reasoning and extended thinking](adaptive-reasoning-and-thinking.md) - Which models always use adaptive reasoning, thinking toggles and env vars, and models where thinking cannot be turned off.
* [Effort levels](adjust-effort-level.md) - Per-model effort levels, resolution order, how to set them, persistence, defaults and subagent/skill effort. **[high]**
* [Alias resolution by provider](alias-resolution-by-provider.md) - Which model opus, sonnet, haiku and fable resolve to on each provider, plus the Fable gateway caveat.
* [Alias version history](alias-version-history.md) - The Claude Code version at which each model alias changed the model it resolves to.
* [Allowlist surface coverage](allowlist-surface-coverage.md) - Which delivery mechanism (server-managed vs MDM/file) reaches which surface for availableModels enforcement.
* [CLAUDE_CODE_AUTO_COMPACT_WINDOW warnings](auto-compact-window-warnings.md) - Warning texts for an unusable CLAUDE_CODE_AUTO_COMPACT_WINDOW value, the window used and the fix.
* [Automatic model fallback on flagged requests](automatic-model-fallback.md) - Content-based fallback when safety classifiers flag cybersecurity or biology requests on Fable, Opus 5.5, Sonnet 5.5 and Opus 5. **[high]**
* [Block specific models or versions](block-specific-models.md) - deniedModels and availableModelsMatch managed settings hold back newer model releases that a prefix allowlist would permit.
* [Checking your current model](checking-current-model.md) - Where to see the active model: the status line and /status.
* [Correct the window for a gateway or custom model ID](correct-window-for-custom-model-id.md) - Fix the context window Claude Code assumes for unrecognized model IDs using modelOverrides, [1m], CLAUDE_CODE_MAX_CONTEXT_TOKENS and related variables. **[high]**
* [Custom model option](custom-model-option.md) - ANTHROPIC_CUSTOM_MODEL_OPTION adds one custom entry to the /model picker without validation.
* [Default model for new sessions](default-model-for-new-sessions.md) - ANTHROPIC_DEFAULT_MODEL sets the starting model only when no flag, env, setting or org default selects one.
* [What the default option resolves to](default-model-setting.md) - The account-type default model per plan and provider, history of earlier defaults, and how org default and enforcement change it.
* [Enforce allowlist for Default and merge rules](enforce-allowlist-and-merge.md) - enforceAvailableModels extends availableModels to the Default option; controls combination and how lists merge across scopes.
* [Extended context (1M window)](extended-context.md) - Which models have the 1M window natively or via [1m], plan requirements, gateway behavior, disabling 1M, and Haiku 5.5 pricing. **[high]**
* [Fable usage credits and consent prompt](fable-usage-credits-consent.md) - Fable usage can bill to usage credits; interactive sessions show a consent prompt, unattended sessions hold it for dialogExpiry or bill without asking. **[high]**
* [Fallback model chains](fallback-model-chains.md) - Switch to up to three fallback models when the primary is overloaded or unavailable, via --fallback-model or fallbackModel. **[high]**
* [Model alias environment variables](model-alias-env-vars.md) - Env vars that map aliases to full model names, set the subagent model, and the deprecated ANTHROPIC_SMALL_FAST_MODEL. **[high]**
* [Model aliases](model-aliases.md) - Aliases accepted by the model setting (default, best, fable, sonnet, opus, haiku, [1m] variants, opusplan) and what each selects. **[high]**
* [modelOverrides setting](model-overrides-setting.md) - Map Anthropic model IDs to provider-specific IDs such as Bedrock ARNs, with precedence and managed-source rules.
* [opusplan model setting](opusplan-model-setting.md) - Hybrid alias that plans with Opus and executes with Sonnet, with 1M variant and allowlist substitution rules.
* [Organization default model](organization-default-model.md) - Enterprise admins set a default Claude Code model org-wide or per role; precedence, override option and restriction checks.
* [Organization effort limits](organization-effort-limits.md) - Caps on effort level per model and role (Enterprise) or via the maxEffortLevel managed setting on any plan or provider. **[high]**
* [Organization model restrictions](organization-model-restrictions.md) - Enterprise admins disable models in the claude.ai admin console, org-wide or per role; notices and rules per entry point.
* [Pin models for third-party deployments](pin-models-third-party.md) - Why and how to pin version-specific model IDs on Bedrock, Agent Platform, Foundry and Claude Platform on AWS, including 1M suffix rules.
* [Pinned model display and capabilities](pinned-model-display-and-capabilities.md) - _NAME, _DESCRIPTION and _SUPPORTED_CAPABILITIES companion variables for pinned models and the capability values.
* [Prompt caching environment variables](prompt-caching-env-vars.md) - DISABLE_PROMPT_CACHING variables to turn prompt caching off globally or per model tier. **[high]**
* [Restrict model selection (availableModels)](restrict-model-selection.md) - Managed allowlist of models users can select, where it applies, and how blocked selections are handled per entry point. **[high]**
* [Resumed-session model and model troubleshooting](resume-and-model-troubleshooting.md) - Which model a resumed session uses, why a new session starts on a different model, and the mistyped-model warning. **[high]**
* [Send no effort level](send-no-effort-level.md) - Set CLAUDE_CODE_EFFORT_LEVEL to auto or unset so the API default applies; how to confirm with /effort status.
* [Auto-compact window](set-auto-compact-window.md) - Control how full context can get before compaction: /autocompact, --autocompact, autoCompactWindow, CLAUDE_CODE_AUTO_COMPACT_WINDOW and defaults. **[high]**
* [Setting your model](setting-your-model.md) - Priority order for choosing a model (/model, --model, env, settings), picker keys, subagent inheritance, validation and non-interactive behavior. **[high]**
* [Ultracode](ultracode-effort.md) - A Claude Code setting (not an effort level) that makes Claude plan dynamic workflows for substantive tasks; ways to turn it on and limits. **[high]**
* [ultrathink keyword](ultrathink-keyword.md) - Including ultrathink in a prompt requests deeper reasoning for one turn, raising it to xhigh where supported.
* [Work with Fable models](work-with-fable.md) - How to select Fable 5.2, 5.1 or 5, the one-time settings move, and usage guidance for the most capable models. **[high]**
