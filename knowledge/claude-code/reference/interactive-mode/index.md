# reference/interactive-mode

* [Background Bash commands](background-bash-commands.md) - Run shell commands asynchronously with task IDs, output files, cleanup rules and memory-pressure stops. **[high]**
* [Side questions with /btw](btw-side-questions.md) - Ask a tool-less question answered from current context without adding to conversation history.
* [Command history and reverse search](command-history.md) - Per-directory prompt history, recovery of cleared drafts, and Ctrl+R search.
* [Review changes with /diff](diff-review-panel.md) - The /diff command opens a diff panel (fullscreen) or dialog (classic) built from the cc-plugin-diff built-in mod.
* [Emoji shortcodes](emoji-shortcodes.md) - Typing :name: inserts an emoji; a suggestion popup appears after two characters.
* [General keyboard shortcuts](general-controls-shortcuts.md) - Keys for interrupting, backgrounding, stashing, switching model or mode, and sending queued messages in the interactive prompt.
* [Multiline, quick commands, transcript viewer, voice keys](input-modes-and-viewer-shortcuts.md) - Ways to enter multiline input, the prefix characters at prompt start, transcript viewer keys and the dictation key.
* [Invisible character removal in prompts](invisible-characters-in-prompts.md) - Claude Code strips tag characters, bidi controls and zero-width characters from prompts on Enter.
* [PR status badge, GitLab MR badge and issue links](pr-and-issue-links.md) - Footer PR or MR badge with review-state color, and clickable owner/repo#123 issue references.
* [Prompt suggestions](prompt-suggestions.md) - Grayed-out next-prompt suggestions, when they are skipped, cost, print-mode emission and how to disable them.
* [Queue messages while Claude works](queue-messages-while-working.md) - Messages typed during a turn are queued; rules for when they are sent, taken back or moved to a background session.
* [Session recap and /recap](session-recap.md) - A one-line recap shown when you return to an idle terminal, and an on-demand /recap command.
* [Shell mode with the ! prefix](shell-mode-bang-prefix.md) - Run a shell command directly from the prompt, add its output to context and have Claude respond.
* [Spell checking in the prompt](spell-checking.md) - Optional underlining of misspelled words using aspell, hunspell or ispell, configured with the spellcheck setting.
* [Task list (Claude's checklist)](task-list.md) - Claude's to-do checklist toggled with Ctrl+T, shared across sessions with CLAUDE_CODE_TASK_LIST_ID. **[high]**
* [Text editing shortcuts and word boundaries](text-editing-shortcuts.md) - Readline-style editing keys in the prompt and how word boundaries are defined for them.
* [Wait for a usage limit to reset (auto-continue)](usage-limit-auto-continue.md) - Claude Code waits in the open session when a claude.ai usage limit hits and continues the task after reset. **[high]**
* [Vim editor mode](vim-editor-mode.md) - Vim-style editing in the prompt: modes, motions, operators, text objects, visual mode and INSERT remaps.
* [You should know suggestions (built-in mod)](you-should-know-mod.md) - An off-by-default built-in mod where a side agent flags one thing you may have missed, with its cost and controls.
