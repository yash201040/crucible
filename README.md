# crucible

You type `/crucible <problem>`. It plans the work as parts, shows you the plan and its expected cost, and waits for your approval. Then every part is solved by one agent and attacked by another that never sees the solver's reasoning; code, not an agent, decides when a part is settled. At the end one agent assembles the answer from the records. A run can be stopped and continued later, and the framework improves itself from its own runs.

It is for problems where being wrong is expensive and one pass by one agent is not enough: open-ended research, a build with several components, a decision that needs its evidence checked. It is the wrong tool for a quick question.

## Read this before your first run: cost

A run starts many agent sessions, and each one uses your subscription or API budget.

| Kind of run | Agent sessions | Time |
|---|---|---|
| A narrow, checkable question | 3 | under a minute |
| A research question with a handful of parts | roughly 20 to 60 (the planner's estimate; not yet measured on a real run) | hours |
| A large build, `deep` depth (one real run) | 302 | 31 hours |

That large run used about 25 million output tokens and re-read about 4 billion cached input tokens, a large share of a top-tier weekly allowance.

What keeps this under your control:
- **You approve the plan first.** The first launch only plans. You see the parts and the estimate, and can ask for a leaner plan or cancel.
- **Every run has a ceiling**: the estimate plus headroom, or your own `--budget`. At the ceiling it wraps up with an answer from the finished work and a handoff, and can be continued later.
- **You can stop it at any time** without losing finished work.

Start with a small question at `--depth quick` to see what a run looks like on your account.

## Read this too: what the agents may do

Agents run unattended, so they are started with permission prompts off: Claude Code agents in bypass mode, Codex agents in the `workspace-write` sandbox with network access. They can run commands and write files in the directory you start from. Run crucible in a project you would let an agent work in alone, and not in a directory that holds secrets.

## Status

Version 5.5. What that rests on:

- The engine's rules are covered by a regression suite that needs no model (`node tests/run.mjs`, about 280 checks).
- The engine has done two large real runs under Claude Code (280 and 302 agents), on v4 and v5.0. The changes since then (staged retries, budget by importance, ownership of parts, closed acceptance lists) are tested in the suite and on small live probes, but **have not yet been through a large real run**. The same holds for helper sessions (v5.5): their counting, limits and closing are tested with a stand-in and on live sessions three levels deep, and whether they make a long run cheaper is not yet measured.
- The standalone runner has been run end to end on a small problem. The Codex path is written from the Codex CLI's documented flags and tested against a stand-in binary; **it has not yet been run against the real Codex CLI**. Expect to fix a detail on first use, and please report it.

## Install

Requirements: `node` 18 or later, `python3` 3.9 or later, `git`. No packages to install.

### Claude Code

Needs a Claude Code version that has the Workflow tool.

```bash
git clone <this repo> ~/.claude/skills/crucible
python3 ~/.claude/skills/crucible/scripts/crucible_run.py install
```

The second line copies the two workflow scripts to `~/.claude/workflows/`. Start a new session and type `/crucible <problem>`. For unattended runs use auto mode, or allow Bash, Write and Edit: the agents use the session's permission mode.

Recommended for long runs: start the session with `crucible-claude`, which lets more agents work at once and keeps their cache longer. See "Host settings" below.

In the skills list you will also see `crucible-engine` and `crucible-evolve`. Those are the two workflow scripts this skill installs, not separate tools; you never call them yourself.

### Codex

```bash
git clone <this repo> ~/.crucible/framework
python3 ~/.crucible/framework/scripts/crucible_run.py install --host codex
```

The second line writes the Codex front desk to `~/.agents/skills/crucible/SKILL.md`. In Codex, ask for crucible by name ("use crucible to …"). Each agent of the run is one `codex exec` session on your ChatGPT login.

By default every agent uses your Codex default model. To give harder parts a stronger model, map the role names in `~/.crucible/providers.json` and ask for the `balanced` profile:

```json
{ "codex": { "model": "<default model id>", "models": { "haiku": "<small>", "sonnet": "<medium>", "opus": "<large>", "fable": "<large>" },
             "effort": { "xhigh": "high" }, "network": true } }
```

Keep the order: the engine never lets a weaker model check a stronger one, and it relies on these names for that.

### Without either front desk

The runner works from a plain terminal, with Codex or with the `claude` CLI:

```bash
node runner/crucible-runner.mjs --args <runDir>/launch.json --provider codex --detach
node runner/crucible-runner.mjs --status <runDir>
node runner/crucible-runner.mjs --stop <runDir>
python3 scripts/crucible_run.py save <runDir>/.runner/output.json <runDir> --transcript <runDir>/.runner
```

`hosts/codex/SKILL.md` describes what goes into `launch.json`.

## Use

| You type | What happens |
|---|---|
| `/crucible <problem>` | Plan, approval, run, answer |
| `--go` | Skip the approval step |
| `--depth quick\|standard\|deep\|max` | How thorough (chosen for you if you say nothing) |
| `--budget 40` or `--budget 5%` | A ceiling in agent sessions, or as a share of a weekly allowance |
| `--profile balanced\|session\|economy\|mixed` | Which models fill the roles |
| `/crucible --stop` | Wrap up now with the best answer the finished work supports |
| `/crucible --continue <handoff.md>` | Continue a stopped or wrapped-up run; finished parts are kept |
| `/crucible --review [<run> ...]` | Improve the framework from its runs (below) |
| `/crucible --improve [repo]` | An improvement round on a product from its recorded feedback (`RSI.md`) |
| `/crucible --calibrate` | Check which models can fill the roles |

Run files go to `<project>/.crucible/runs/<time>-<name>/`. `answer.md` is for you; `crucible-handoff.md` is how to continue; the rest is the record.

## How a run works

1. **Plan.** A planner splits the problem into parts, gives every item of your success definition one owning part, rates each part's difficulty, and marks the parts the result is unusable without. A plan critic checks it. For a build, the plan must contain an early thin slice through the whole chain and a proof of the assembled result.
2. **Acceptance list.** For a part that is hard enough, an agent that will not solve it writes the tests it must pass before any work starts: a closed list, never "every flaw a checker can think of".
3. **Solve and attack.** A solver works; an attacker checks the result and its artifacts without seeing the solver's reasoning. Only a wrong behaviour or a failed listed check sends work back. A part gets at most two such rounds.
4. **If it is still open.** A referee rules on the open findings. Then one repair attempt runs alone; only if it fails do further attempts with different strategies run side by side, and they stop as soon as one survives.
5. **Review.** A panel of reviewers with different lenses tries to break the surviving result. Material flaws get one repair.
6. **Assemble.** One agent writes the answer from the records and reports each success item against its owner. The save step appends a complete, generated list of everything still open.

Cost follows difficulty: a trivial part costs three agents, a hard one many more. Budget is spent in order of importance, so the parts that come last (the assembly, the end-to-end proof) are not the ones that fall off when a run reaches its ceiling.

## How it improves itself

- `expectation.md` is the standard: the owner's own lines on what crucible is for and how they use it, each with an id. Reviews and audits measure the framework against it. Only the owner edits it; a review that changes it is undone by the save step. If you fork crucible, rewrite it as your own.

- Every run ends with one agent writing dated notes on what the framework did badly. Nothing is changed during or after a run.
- `/crucible --review` is the only place changes are made. It looks at the runs you name, or at every run made on the current version, and reads each one the way a person would after a long run: where the agent time went, whether parts went round without getting closer, what the run missed that you had to add afterwards (it reads what you typed after the result, and anything you say when asking for the review), whether the answer was a faithful merge of the records, how the run ended. `references/run-audit.md` lists the questions; the figures come from code, not from an agent.
- A change is applied only when the evidence can be opened, an independent agent has confirmed it, and the tests pass. Each change is one commit, at most five per review. `PROTECTED.md` lists what a review may never change by itself; such findings go to `PROPOSALS.md` for you.
- Every applied change names one number it should move (`references/expectations.json`). Later reviews measure that number on later runs; a change that did not move it is reworked or reverted.
- A review knows the host: it searches the knowledge bundle before proposing a mechanism of its own, and when the installed Claude Code is newer than the bundle it reads the release notes since.
- A change to a prompt is also run on small cases with a known right answer, on the engine before and after (`calibration/calibrate_rules.py`). A case that was right and turned wrong is reverted.

To undo a change: `git revert <commit>`, then `python3 scripts/crucible_run.py install`.

## Host settings that decide speed and cost

Two settings of Claude Code matter more to a long run than anything in crucible's prompts. Both are read when a session starts, so crucible can report them but not change them.

| Setting | Claude Code's default | What the first large run showed | What the launcher sets |
|---|---|---|---|
| `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`: agents of a run working at once | 16, or the number of CPUs minus two if that is less (6 on an 8-core laptop) | exactly 6 agents were alive for 78% of the 31 hours | 64 |
| `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL`: how long an agent's cached context lives | 5 minutes | 318 times a build or test run took longer, and the agent paid for its whole context again: 57% of everything written to the cache | 1 hour |

To get them, start the session you run crucible in with `crucible-claude` (`ln -s ~/.claude/skills/crucible/bin/crucible-claude ~/.local/bin/`), or put both variables in the `env` block of `~/.claude/settings.json`, which also covers sessions started from an app. A value in your settings wins over the launcher's. Sixty-four in practice lifts the cap: how many agents work at once is then decided by the plan, and that has been tested up to twelve at once, not beyond. Lower it on a machine that struggles when many agents run builds or tests at the same time. A one-hour cache write costs more than a five-minute one, so the second setting pays for agents that run long commands and costs a little for short-lived ones; by API prices it would have saved about 7% of that run's tokens.

`crucible_run.py host` prints what the current session has. The front desk mentions it once, at approval, for a plan of 30 agents or more.

**Code Mode** (Claude Code's experimental mode in which an agent writes one script that makes many tool calls) is neither required nor recommended. Tested: in a terminal session with Code Mode on, the agents of a run do work in it, and a command of eleven minutes finishes normally. On five small tasks it made no measurable difference: 15 model calls without it, 17 with it, all answers right, because agents told to work in few, large steps already put many reads, edits and commands into one shell command. Whether it helps on the long sessions of a real run is not known; every run records model calls per agent and whether Code Mode was on.

**What the host can do** is kept in `knowledge/claude-code/`: about 1,650 notes read from Claude Code's documentation, pinned to one release, in Open Knowledge Format (markdown with a header; start at `index.md` or `playbooks/how-to-use-this-bundle.md`). `experiments/` there holds every test above with its figures, and `playbooks/what-crucible-uses.md` the decision for each feature, including the ones left out: nested subagents (not available to a run's agents), agent teams, custom agent types, the advisor. `python3 scripts/crucible_okf.py refresh` says what changed in the host since the pin.

## Helpers under a solver

Claude Code gives the agents of a run no tool to start agents of their own. A solver that has a large body of files to read, a wide search to make or a long build to wait for would otherwise do all of it in its own context, and pay to re-read that context at every later step. Since v5.5 it can hand such work to a **helper**: a separate headless session, started through `scripts/crucible_helper.py`, which can start a helper of its own in turn.

A session started from a shell is outside the run, so the launcher does in code what the run cannot see:

| What could go wrong | What the launcher does |
|---|---|
| Too many sessions at once | at most four helpers work at once per level; the rest wait their turn |
| Cost outside the ceiling | all helpers of a run share one allowance, 15% of the run's ceiling, shown inside the ceiling you approve; a request past it is refused and the solver does the work itself |
| Nothing in the records | each helper leaves its task, its handoff and a record (owner, level, model, tokens, cost, session) under `<run>/helpers/`; the run's efficiency log and digest count them |
| Sessions left running | a helper is ended when its owner finishes, when its time is up (15 minutes unless the solver asks for more, 45 at most), when the session that started it is gone, and when the run is stopped or saved |
| Endless nesting | a run sets how many levels are allowed: two at standard depth, three at deep, `--helper-depth N` for another number |
| A checker leaning on a helper | only a solver or a repair may own one; any other role is refused |

The solver picks the helper's model by what the task needs, not by its level: Haiku to locate and extract, Sonnet for reading that needs judgement. What a helper hands back is unverified material: the solver re-checks every fact its result rests on and names the helper next to it, and never hands over an acceptance check. `--no-helpers` switches helpers off for a run; `crucible_helper.py status <run>` shows what they did.

Three things to know. A helper session never has Code Mode, because Claude Code gives that to terminal sessions only. It runs in the permission mode of your own settings (set `permission_mode` in `<run>/helpers/config.json` for another). And it is not covered by the workflow's waiting on a usage limit: a helper that fails on a limit is reported to its owner, which then works alone, and no helper starts for ten minutes. Helpers need the `claude` command, so the Codex front desk does not offer them.

## Your own additions

The framework names no data tool and holds nothing about your setup. If you use a paid search or data service and want every agent to follow your rules for it, or want your own flag, put it in `~/.crucible/local/`:

- `front-desk.md`: extra rules for the front desk, in plain words (for example: "when the request contains `/mytool`, pass `dataTool`, `dataRules` and `dataBudget`"). It is shown to the front desk at the start of every run.
- `local.json`: `{"paid_ledger": "<a JSONL of paid calls>", "fetch_cache": "<a cache folder>", "data_flags": ["/mytool"]}`, all optional.

## Other models

`routing.json` says which model and effort fills each role, per profile. Under Claude Code the default profile puts easy and moderate parts on a lighter model and the hard parts, planning, judging and the final answer on the strongest. `scripts/crucible_agent.py` can also run a single agent on any OpenRouter model (the `mixed` profile uses this for a second check from another model family); the key's location goes in `~/.crucible/providers.json`, never in this folder.

## Layout

```
SKILL.md                 front desk for Claude Code
hosts/codex/SKILL.md     front desk for Codex
engine/                  the two workflow scripts: the run engine and the self-review
runner/                  runs the same scripts outside Claude Code
bin/crucible-claude      starts Claude Code with the two session settings a long run profits from
bin/git-pre-commit       commit guard: no private paths, and only the owner changes expectation.md
scripts/                 bookkeeping (save, checkpoint, review pack, digests), the single-agent adapter, the launcher of helper sessions
references/              the run-audit questions, expectations, domain checks, templates
knowledge/claude-code/   what the host can do, from its documentation, pinned to one release; experiments; what crucible uses and why
calibration/             probes for models and for the engine's own prompts
tests/                   the regression suite (no model needed)
routing.json             models and effort per role
CHANGELOG.md             every change and the evidence for it
PROTECTED.md             what a self-review may never change by itself
expectation.md           what the owner expects of crucible; the standard for reviews; edited by the owner only
```

## Tests

```bash
node tests/run.mjs
```

It runs the engine against scripted agents, then the Python tests of the review pack, of the runner, of the knowledge bundle and of helper sessions (with a stand-in for the `claude` command). No model is called and it takes about two minutes.

## Working on crucible itself

This repository is the working copy: `/crucible --review` commits its changes here, one commit per change. It is public, so nothing about a problem, a client or a machine belongs in a commit. Install the guard once per clone:

```bash
ln -sf ../../bin/git-pre-commit .git/hooks/pre-commit
```

It refuses a commit that names the machine's user folder, and one that changes `expectation.md` without the owner's word. Pushing is always a deliberate step: nothing here pushes by itself.

## Licence

MIT. See `LICENSE`.
