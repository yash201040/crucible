# agent-sdk-control-and-observability/agent-sdk-file-checkpointing

* [Checkpoint before risky operations and multiple restore points](checkpoint-patterns.md) - Two patterns: keep only the latest checkpoint UUID to revert mid-stream, or store every prompt's UUID to rewind to any turn. **[high]**
* [Checkpointing limitations](checkpointing-limitations.md) - What rewinding does not cover: Bash changes, subagent edits, other sessions, directories and remote files. **[high]**
* [Checkpointing errors and fixes](checkpointing-troubleshooting.md) - Causes and fixes for unrecognized options, missing UUIDs, no checkpoint found, rewinding not enabled and ProcessTransport errors.
* [Enable, capture UUIDs and rewind](enable-capture-and-rewind.md) - Options to enable checkpointing, receive checkpoint UUIDs, and rewind by resuming with an empty prompt or via the CLI flag. **[high]**
* [File checkpointing and rewind](how-checkpointing-works.md) - SDK backs up files before Write, Edit or NotebookEdit changes so files on disk can be rewound to the state at any prompt. **[high]**
