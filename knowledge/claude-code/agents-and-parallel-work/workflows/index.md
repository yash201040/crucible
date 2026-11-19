# agents-and-parallel-work/workflows

* [Workflow agent stalls and automatic restarts](agent-stall-and-restart.md) - A silent agent restarts up to five times; stallMs and CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS lengthen the stall window. **[high]**
* [Approving a workflow launch](approve-workflow-launch.md) - Per-mode approval prompt for workflows and how to allow them unattended in claude -p and the Agent SDK. **[high]**
* [Asking for a workflow and ultracode](ask-for-workflow-ultracode.md) - Trigger workflows with the ultracode keyword, a direct request, or /effort ultracode for every substantive task. **[high]**
* [Dynamic workflows overview](dynamic-workflows-overview.md) - A dynamic workflow is a JavaScript script Claude writes that a runtime executes in the background to orchestrate many subagents. **[high]**
* [How a workflow runs](how-a-workflow-runs.md) - The runtime executes the script in isolation, writes it under ~/.claude/projects/, and tracks agent results for resume. **[high]**
* [Resuming and relaunching workflow runs](resume-after-pause.md) - Pause with p, relaunch stopped runs; which agents replay from saved results and which rerun; recovery after leaving the session. **[high]**
* [Bundled /deep-research workflow and progress view](run-bundled-deep-research.md) - The built-in /deep-research workflow and the /workflows progress view with its keys. **[high]**
* [Workflow runtime limits](runtime-limits-and-concurrency.md) - Concurrency, item and total-agent caps, and constraints on scripts (no input, no module loading, no direct fs). **[high]**
* [Saving, sharing and parameterizing workflows](save-and-distribute-workflows.md) - Save a run's script as /<name> in .claude/workflows/ or ~/.claude/workflows/, ship it in a plugin, and pass input via args. **[high]**
* [Turning workflows off](turn-workflows-off.md) - Disable workflows per user or organization via /config, disableWorkflows or CLAUDE_CODE_DISABLE_WORKFLOWS. **[high]**
* [Workflow cost, warnings and size guideline](workflow-cost-and-size.md) - Large workflow warning thresholds, model choice per agent and the workflowSizeGuideline setting. **[high]**
* [Prompt caching in a workflow fan-out](workflow-prompt-caching.md) - Agents with matching config share a cache prefix; a stagger hold and 5-minute default TTL apply. **[high]**
* [Workflow script format and API](workflow-script-format.md) - The meta block, agent(), pipeline(), parallel(), phase(), log(), schema validation, determinism rules and how to edit saved scripts. **[high]**
* [Workflow pause at a usage limit](workflow-usage-limit-pause.md) - When an agent hits a claude.ai usage limit the run waits for reset and continues, under conditions listed. **[high]**
