# create-plugins/plugins-cli-hints

* [Emitting a claude-code-hint tag](emit-claude-code-hint.md) - A CLI or SDK writes a one-line claude-code-hint tag to stderr, gated on CLAUDECODE or CLAUDE_CODE_CHILD_SESSION, to prompt a plugin install.
* [Hint tag format and when the prompt appears](hint-format-and-prompt-conditions.md) - Required v, type and value attributes, and the conditions and frequency limits that must all pass for the prompt to show.
* [Plugin recommendation dialog](plugin-recommendation-dialog.md) - The dialog users see for a hint and the effect of each answer, including a 30-second timeout counting as No.
