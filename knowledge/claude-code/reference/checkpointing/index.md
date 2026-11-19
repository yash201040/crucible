# reference/checkpointing

* [Checkpointing limitations](checkpointing-limitations.md) - What rewind does not track: Bash-only edits, subagent edits, external changes, mid-turn messages, symlinks and hard links. **[high]**
* [Automatic checkpoints](how-checkpoints-work.md) - Each turn-starting prompt creates a checkpoint of Claude's file edits; 100 kept per session, saved with the conversation, swept after about 30 days. **[high]**
* [Rewind menu and summarize actions](rewind-and-summarize.md) - Open with /rewind or double Esc to restore code and/or conversation, or compress context with Summarize from here or up to here.
