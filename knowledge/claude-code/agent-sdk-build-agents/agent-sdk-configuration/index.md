# agent-sdk-build-agents/agent-sdk-configuration

* [Change model and settings mid-session](change-config-mid-session.md) - setModel, setPermissionMode, applyFlagSettings and updateSettings let a streaming-input session change configuration while running. **[high]**
* [Choose a model and fallback chain](choose-model-and-fallback.md) - model pins a model or alias; fallbackModel switches to backups when the primary is overloaded and retries the primary each user turn. **[high]**
* [env option and working directory](environment-and-working-directory.md) - How env replaces (TypeScript) or merges (Python) the subprocess environment, and how cwd and additionalDirectories scope file access. **[high]**
* [maxTurns and maxBudgetUsd caps](limit-turns-and-spend.md) - Turn and spend caps, their result subtypes, and how single-shot and streaming input handle hitting them. **[high]**
* [Load settings files into a session](load-settings-files.md) - settingSources picks which filesystem settings load; settings passes a file path, inline JSON or object that outranks all but managed policy. **[high]**
* [Options mapped to features](option-to-feature-map.md) - Table mapping each Agent SDK option in TypeScript and Python to the feature it controls. **[high]**
* [Pass options to a session](pass-options-to-session.md) - Every query() accepts an Options (TypeScript) or ClaudeAgentOptions (Python) object; allowedTools pre-approves rather than restricts. **[high]**
