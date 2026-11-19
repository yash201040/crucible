# Proposals for the user

Confirmed findings that `crucible-evolve` may not apply by itself (see PROTECTED.md). Newest first. Delete an entry once decided.

## 2026-11-20: lines of `expectation.md` the host tests speak to (for the owner)

Only the owner edits `expectation.md`. These are the lines that the tests of 2026-11-20 (see `knowledge/claude-code/experiments/`) bear on, with the evidence and a wording to consider. Nothing here has been applied.

1. **U8** says crucible is used "from a terminal session started with Code Mode on". Code Mode reaches a run's agents there, but saved nothing on five small tasks (15 model calls without it, 17 with it). What did matter in the records of the large run are two session settings: how many agents work at once, and how long an agent's cache lives. Consider: "I use it mostly on a Claude subscription, from a session started with the settings a long run profits from (agents at once, cache lifetime). Code Mode is optional."
2. **R11** says agents "use the host's script tool (Code Mode) where it exists". Agents told to work in few, large steps did as well with the ordinary tools. Consider: "Agents work in few, large steps, so a long run does not pay to re-read its own context at every step, and does not pay twice for it because a cache expired."
3. **R4** ends with "One looping part must not leave the run at one or two live agents for hours." The large run was held back more by the opposite: it sat at the host's cap of six agents for 78% of its time. Consider adding: "A run uses as many agents at once as its plan allows; a default of the host must not hold it back."
4. **R5** and the question of helpers under a solver (raised by the owner on 2026-11-19): no agent of a run can start helpers on this host, whatever the settings. The line can stay as it is. If a hierarchy is wanted, it is the engine that splits a part into owned parts, which keeps the ceiling of **U6** meaningful.
5. **I-section**: nothing there says a review should know the host. Consider a line: "A review knows what the host can do and what changed in it since the last review, and prefers a feature of the host to a mechanism of its own."
6. **Section 6** (the snapshot) asks the next session to establish first whether Code Mode is active for the agents of a run. Established: yes in a terminal session, no in an app, and no measurable saving so far. The open questions are now the first run on v5.4 and its figures for agents at once, cache rebuilds and model calls per agent.

## 2026-11-20: not built, and what would change that

- **Starting a run in a hidden terminal session from an app** (so that app users get Code Mode and the launcher's settings). It works in a test, but the session can hang on a prompt nobody sees, and the two settings can be had by putting them in the user's own settings. Build it if Code Mode shows a real saving on a run.
- **Helpers under a solver**. Not possible on the host today (see above).
- **A deny of the messaging tools for a run's session** (`--disallowedTools SendMessage,ListAgents`). Works; left to the user because it also binds the session's own agent, and no agent of 302 ever messaged another.
