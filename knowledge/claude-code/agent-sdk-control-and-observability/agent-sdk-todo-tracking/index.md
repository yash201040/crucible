# agent-sdk-control-and-observability/agent-sdk-todo-tracking

* [Display todo progress in real time](display-progress-in-real-time.md) - Pair TaskCreate tool_use with its tool_result by tool_use_id to read the assigned task id from tool_use_result.
* [Monitor todo changes from the stream](monitor-todo-changes.md) - Watch TaskCreate and TaskUpdate tool_use blocks to log task activity, handling repaired key names defensively.
* [Task-tracking tools and model availability](task-tools-model-availability.md) - TodoWrite and Task tools are default only on older models; how to opt in on newer ones. **[high]**
* [Todo lifecycle and when Claude creates todos](todo-lifecycle-and-creation.md) - Statuses pending, in_progress, completed, deleted, and the situations in which Claude creates todos.
