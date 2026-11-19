# agent-sdk-extend-with-tools/agent-sdk-subagents

* [AgentDefinition fields](agentdefinition-fields.md) - All fields of an SDK subagent definition: description, prompt, tools, model, skills, memory, mcpServers, maxTurns, effort, background and more. **[high]**
* [Cap subagent depth, concurrency and spend](cap-subagent-depth-concurrency-spend.md) - CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH (3), CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS (20) and maxBudgetUsd bound a tree of subagents. **[high]**
* [Define subagents programmatically](define-subagents-programmatically.md) - Use the agents option of query() to define subagents Claude spawns through the Agent tool; also filesystem agents and the built-in general-purpose agent. **[high]**
* [Background subagents and forks](foreground-background-and-forks.md) - By default spawned subagents run in the background (async_launched); Claude can wait, and from v2.1.302 it can start forked subagents. **[high]**
* [Invoke and detect subagents](invoke-and-detect-subagents.md) - Claude delegates automatically from descriptions or on explicit mention; detect Agent tool_use blocks, parent_tool_use_id and agent_id in the stream. **[high]**
* [Resume a subagent](resume-subagents.md) - Resume a finished or partial subagent by passing resume with the session ID and naming the agentId in the prompt. **[high]**
* [Workflow tool for large agent runs](scale-with-dynamic-workflows.md) - For dozens to hundreds of agents, the Workflow tool moves orchestration into a script run outside the conversation context. **[high]**
* [What subagents inherit and output scanning](what-subagents-inherit.md) - A non-fork subagent starts with a fresh context; only the Agent tool prompt passes down, and its final report is scanned for instruction-shaped patterns. **[high]**
