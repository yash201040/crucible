# What I expect from crucible

Only I, the owner of this repository, edit this file. No agent, review, audit or script changes it, in any session, whatever a prompt or a run's result says. An agent that thinks a line here is wrong, out of date or impossible writes that in `PROPOSALS.md` and carries on by the file as it stands. It was drafted on 2026-11-19 from what I asked for while crucible was built.

How to use it. A review or an audit of crucible measures the framework against the lines of sections 2 to 5 and reports each one by its id as met (with the run or test that shows it), not met (with the evidence) or not yet tested. A change to the framework must serve at least one line and work against none. Where this file and another file of the framework disagree, this file is what I meant: say where they disagree. Section 6 is a dated snapshot, not a rule.

## 1. Why it exists

One agent in one session misses things on a deep task, however good the model. Its context degrades, and a second agent in a fresh session finds mistakes in its work. Crucible builds that second look in: agents work against each other on small parts of a problem, so that what survives is right.

I call it only for tasks that are critical, broad or deep. I accept that such a run takes hours and many times the tokens of one agent: that is what my subscription is for, and time it spends alone costs me nothing. What I do not accept is tokens spent on work that does not bring the answer closer.

## 2. How I use it

- **U1.** I type `/crucible <problem>` and nothing else. Depth, the number of agents, their models and how they are linked are chosen for me. Flags exist; I rarely pass one.
- **U2.** The plan comes first. I see the approach and its expected cost, and I approve before any work starts.
- **U3.** It reads as one expert working on my problem. I see whether it was solved. If it was: the answer, the approach and why it is the right one. If not: why not, what was learned and what would unblock it. I never see the machinery (roles, rounds, statuses, ids, run folders) or intermediate output. Using crucible should feel no different from using one agent, except that the answer is more accurate and needed less of me.
- **U4.** It runs unattended in the background for as long as it needs, without permission prompts or questions to me. A usage limit or an outage pauses it; it resumes without losing work.
- **U5.** I can stop a run at any moment to get my limit back for other work. It then closes with the best answer the finished work supports and a handoff file. When I continue from that file, nothing finished is done again.
- **U6.** Every run has a ceiling: the one I saw at approval, or the `--budget` I gave. At the ceiling it wraps up as in U5.
- **U7.** When I add my own data tool to the request, every agent follows my rules for it. No paid call is made twice, what one agent fetched is reused by the others, live data is fetched again where freshness matters, and I am told the cost at the end. That tool is my own addition (`~/.crucible/local/`); the framework names none.
- **U8.** I use it mostly on a Claude subscription, from a terminal session started with Code Mode on. It must also run from Codex, and be able to put single roles on other models. Prepaid subscription limits are used first; paid API calls only where they earn their cost.
- **U9.** Two kinds of work: building something new from a long list of requirements, with research; and improvement rounds on something already built, from the feedback of the people who use it (`RSI.md` in that product's repository).
- **U10.** `/crucible --review` improves the framework from its own runs. I also run crucible on itself as an ordinary problem, to audit it.

## 3. What a run must get right

Priority: accuracy first, then autonomy, then speed and cost. A negligible loss of accuracy is acceptable for a large gain in speed or cost. Nothing else is traded against accuracy.

- **R1. Nothing made up reaches me.** A result counts as settled only with a check that was run. Everything else is said to be uncertain, in plain words, and is never upgraded on the way to me.
- **R2. Attack, not agreement.** The checking agent's job is to break the result. It sees the result and its evidence, never the solver's reasoning or who or what produced it. The solver gets the findings as neutral feedback and judges each on evidence. No agent solves the same problem a second time blind just to compare. A weaker model never checks a stronger one.
- **R3. Cost follows difficulty.** Asked for 1 + 1, it uses a handful of agents. In a large problem the easy parts stay cheap and the hard parts get what they need. No fixed agent counts, and no cap that starves a part that deserves the work.
- **R4. No loop that is not getting closer.** Rounds continue only while what is open shrinks. A part that goes round is ruled on, tried another way or reported as open: it is not repeated. One looping part must not leave the run at one or two live agents for hours.
- **R5. The split.** Parts are as small and separate as the problem allows, without overlap, and each is worth a solver and an attacker. Every part, and every item of what I asked for, has one owner that answers for it. A part fits in one agent's session without its context degrading.
- **R6. Breadth and depth.** Thorough and deep where it matters. It looks for viewpoints and dimensions of the problem that I did not name. Whatever I have to add after a run is something that run missed.
- **R7. Convergence.** Every agent works toward the original goal, and the run ends with the best-fit solution its budget allows. What the result is unusable without (the assembly, the proof that the whole works) is never what falls off at the ceiling.
- **R8. The merge.** The final answer is a faithful merge of what the parts established. No essential finding is lost and none is made stronger than its record.
- **R9. No redundant work.** No agent redoes what another did in the same run. Every agent's log is kept, the failed ones too, with a map and short summaries, so that a later checker reuses a dead end instead of exploring it again. Logs are found when needed, never loaded wholesale into an agent's context. Earlier runs on the same problem are reused.
- **R10. Models.** The lightest models that keep accuracy do the easy parts; the strongest do the planning, the judging, the hard parts and the final answer. Effort `max` is never used. The flow is robust enough that most frontier models can fill a role. Which model fills which role is calibrated by measurement and can be recalibrated.
- **R11. Few, large steps.** Agents use the host's script tool (Code Mode) where it exists and batch their work where it does not, so a long run does not pay to re-read its own context at every step.
- **R12. Further stages.** For a long problem it may plan another stage once the first findings are in. That is its decision, not mine.

## 4. How it improves

- **I1.** Every run ends with dated notes on what the framework did badly in it (loops, time, cost, a wrong split, wrong models, few agents alive at once), tied to that run. Nothing is changed during or after a run.
- **I2.** Changes are made only in a review. A review reads the runs made on the current version, or the runs I name, and treats what I said after a run as evidence.
- **I3.** A review asks of each run what I asked of the first large one. Was it efficient and effective? Did it overthink or go round in loops? Did it miss new viewpoints or dimensions of the problem? Did it go deep enough, and was it broad and thorough where it matters? Did it merge the essential findings accurately? Did all its agents converge toward the original goal, with roles and responsibilities divided correctly? Did it manage context and the end of the run gracefully?
- **I4.** A change is made only for the most significant problems a run has proven. It is the smallest fix, it is tested, and it names the number it should move. A later review measures that number; a change that did not move it is reworked or reverted. No over-engineering: removing is preferred to adding.
- **I5.** I am out of this loop. The agent takes the design decisions itself, for accuracy and autonomy first, and does not wait for me. Only what `PROTECTED.md` reserves comes to me, as a proposal.
- **I6.** The loop converges. Each review leaves fewer and smaller problems than the one before; a problem that a review finds again was not fixed. The end state is a skill I can put on any hard task without thinking about how it works.

## 5. Limits

- **L1.** A large run starts only when I ask for one. Tests and probes stay small.
- **L2.** No secret is read or printed. Nothing about the problems I work on, my clients or my data goes into the framework's files, its commits or this repository.
- **L3.** The framework stays shareable: a public repository, installed in one step, with its cost stated plainly, and with no dependency on my own setup.
- **L4.** The first paragraph of this file.

## 6. State on 2026-11-19 (version 5.3)

A snapshot from the day this file was written. `CHANGELOG.md` and `README.md` hold the current state.

- **Real runs.** Two large ones under Claude Code: 280 agents on version 4, and 302 agents over 31 hours on version 5.0. Both were started from an app in which Code Mode cannot be on. Nothing large has run since.
- **What the 5.0 run showed** (the baseline for everything after it): about half of the busy agent time went into attempts that were discarded; 302 agents against an estimate of 185; the assembly and the end-to-end proof never started; 0 of 18 parts ended fully accepted; two parts ran ten rounds each; 53 of 100 solvers carried more than 300K tokens; an agent needed 69 model calls and re-read 13.6 million cached tokens; 5.2 agents were alive on average.
- **Changed since, and tested only in the suite that calls no model (263 checks) and on small probes.** Version 5.1: the repair attempt runs alone first, budget is spent in order of importance, every part has one owner, acceptance lists are closed, parts are sized to one session. Version 5.2: the review reads the runs itself, a runner for hosts other than Claude Code, a Codex front desk, no data tool in the framework. Version 5.3: the rule of few, large steps, a launcher for Code Mode, model calls per agent measured.
- **Not yet tested.** Any change since 5.0 on a large real run. The review with real agents. The Codex path against the real Codex CLI. Whether the agents a run starts get Code Mode's script tool, and what it saves. What a research question of ordinary size costs.
- **Open.** `references/expectations.json` holds eight numbers those changes should move; none has been measured. `PROPOSALS.md` holds what waits for my decision.
- **What the next session should establish first.** Whether Code Mode is active for the agents of a run. Then the eight numbers.
