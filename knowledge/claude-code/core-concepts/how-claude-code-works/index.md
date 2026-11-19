# core-concepts/how-claude-code-works

* [The agentic loop](agentic-loop.md) - Claude works in three blended phases (gather context, take action, verify) using models and tools, and the user can interrupt at any point.
* [Built-in tool categories](built-in-tool-categories.md) - The five categories of built-in tools and what Claude can do with each, plus tools for orchestration.
* [Checkpoints and permission modes](checkpoints-and-permission-modes.md) - File snapshots before edits (Esc twice to rewind) and the four permission modes cycled with Shift+Tab, including Auto as the starting mode. **[high]**
* [Context window and compaction](context-window-and-compaction.md) - What fills the context window, automatic compaction into a summary, how to steer it, the thrashing stop, and attribution settings. **[high]**
* [Execution environments and interfaces](environments-and-interfaces.md) - Local, cloud and Remote Control execution environments and the interfaces that reach the same agentic loop.
* [Sessions, resume and fork](sessions-resume-fork.md) - Conversations are stored as local JSONL; resume reuses the session ID, fork copies history into a new ID; worktrees give parallel sessions. **[high]**
* [What Claude can access](what-claude-can-access.md) - The project files, terminal, git state, CLAUDE.md, auto memory and extensions available when claude runs in a directory.
* [Working effectively: steer, delegate, get help](working-effectively-tips.md) - Interrupting with Esc, queueing messages, delegating with context, and the /init and /doctor helper commands.
