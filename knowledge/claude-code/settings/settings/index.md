# settings/settings

* [Changing a setting: /config, files, --settings](change-a-setting.md) - Three ways to change settings (the /config menu, editing JSON, per-session --settings, flags or env vars) and when edits take effect. **[high]**
* [Confirming loaded settings and fixing errors](check-and-fix-settings.md) - /status shows loaded setting sources; Settings Error, Settings Warning, managed and ~/.claude.json failures and how -p runs treat them. **[high]**
* [Exceptions to managed settings precedence](managed-precedence-exceptions.md) - Restrictive values honored from lower scopes even over managed settings (disableClaudeAiConnectors, isolatePeerMachines, block reads/writes outside and more). **[high]**
* [Settings files and scopes](settings-files-and-scopes.md) - The four settings scopes (user, shared project, project local, managed) with file paths, who each affects, and the separate ~/.claude.json. **[high]**
* [Settings in cloud sessions](settings-in-cloud-sessions.md) - Which settings files a cloud session reads: project threads read none; single-repo sessions read shared project; user, local and device managed files are not read. **[high]**
* [Local settings file location and git handling](settings-local-file.md) - Where .claude/settings.local.json lives in a repo or worktree, how it stays out of git, and why its allow rules skip the trust step. **[high]**
* [Settings precedence and list merging](settings-precedence.md) - Order managed > command line > local > shared project > user, how lists merge, and special rules for model-list keys. **[high]**
* [Troubleshooting a setting that does not apply](troubleshoot-setting-not-applying.md) - Causes when a setting is ignored: higher level, security key, disallowed file, broken file, trust, unwritable file, or managed delivery lag. **[high]**
