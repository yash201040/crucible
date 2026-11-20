# Bundle Update Log

## 2026-11-20
* **Creation**: Added [helper sessions, counted and closed](/experiments/helper-sessions-counted-and-closed.md): the launcher that makes nesting safe to use, its live tests, and what solvers did with it. The playbook now lists nested helpers as used.
* **Correction**: Nesting is possible after all, through a child session started from the shell: added [the test](/experiments/nesting-through-a-child-session.md) and corrected [the earlier one](/experiments/workflow-agents-cannot-start-helpers.md), whose finding is only that an agent of a workflow has no helper tool.
* **Update**: [Code Mode](/experiments/code-mode-reaches-workflow-agents.md) now records that a headless session never has it, and that a terminal session gets it from the user's settings alone.
* **Creation**: Added seven experiments on workflows, Code Mode, the cap on agents at once, the agents' cache lifetime, agent types and context growth, starting with [nesting](/experiments/workflow-agents-cannot-start-helpers.md).
* **Creation**: Added two more on [long commands](/experiments/long-command-in-code-mode.md) and [messaging tools](/experiments/deny-messaging-tools-for-a-run.md).
* **Creation**: Added the playbooks [what crucible uses](/playbooks/what-crucible-uses.md) and [how to use this bundle](/playbooks/how-to-use-this-bundle.md).

## 2026-11-19
* **Initialization**: Built from the Claude Code documentation as of release 2.1.328: 205 pages read by 49 readers into about 1,630 concepts, plus digests of the release notes from 2.1.101 to 2.1.328 in three ranges. See [the pin](/release/pin.md).
* **Method**: The documentation's own index gave the folders. Pages were grouped by section, each group read in full by one reader (Sonnet 5.5) that wrote concepts with exact names, defaults, limits and release numbers, in its own words. Reference sections were read closely; administration, gateways, error lists and app pages as a survey. Every page has at least one concept; names that occur only in release notes are listed in each digest.
