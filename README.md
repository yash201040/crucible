# crucible

A skill for coding agents (Claude Code and Codex) that puts one hard problem through many independent agents and gives you one direct answer, with what was checked and what was not.

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

Version 5.3. What that rests on:

- The engine's rules are covered by a regression suite that needs no model (`node tests/run.mjs`, about 260 checks).
- The engine has done two large real runs under Claude Code (280 and 302 agents), on v4 and v5.0. The changes since then (staged retries, budget by importance, ownership of parts, closed acceptance lists) are tested in the suite and on small live probes, but **have not yet been through a large real run**.
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

Optional, for cheaper long runs: put the launcher on your PATH (`ln -s ~/.claude/skills/crucible/bin/crucible-claude ~/.local/bin/`) and start the sessions in which you use crucible with `crucible-claude`. See "Code Mode" below.

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
- A change to a prompt is also run on small cases with a known right answer, on the engine before and after (`calibration/calibrate_rules.py`). A case that was right and turned wrong is reverted.

To undo a change: `git revert <commit>`, then `python3 scripts/crucible_run.py install`.

## Code Mode: fewer model calls per agent

Most of what a long run costs is re-reading: every step an agent takes re-reads everything it has read so far. In the large run above, an agent needed 69 model calls on average and re-read 13.6 million cached tokens.

Every crucible agent is therefore told to work in few, large steps. How far it can go depends on the host:

- **Claude Code with Code Mode on.** Code Mode is an experimental Claude Code feature in which an agent writes one script that makes many tool calls and returns only what it needs. Start the session with `crucible-claude` (it runs `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1 claude`) and confirm once when Claude asks. It works only in an interactive terminal session: not in `claude -p`, the Agent SDK and apps built on it, the VS Code panel, the Desktop app or cloud sessions. It needs Claude Code 2.1.323 or later and a subscription or Console account, and a session started with it can be resumed only with it. Some features are unavailable in such a session (Remote Control, Claude in Chrome, computer use). Crucible cannot switch it on from inside a session: when it is off, the front desk says so in one line and carries on.
- **Codex.** Agents ask for Codex's own code mode (`features.code_mode`, still under development in Codex). An agent that fails with it is run once more without it; `"code_mode": false` under `codex` in `~/.crucible/providers.json` turns it off.
- **Anywhere else.** Agents batch independent tool calls in one step and filter command output before reading it.

What is not known yet: Claude Code's documentation does not say whether the agents a workflow starts get the script tool when the session has it, and no run has measured the saving. Each run's efficiency log records model calls per agent and how many agents ran scripts (`crucible_run.py digest <run>`), so your first run from a Code Mode session answers both.

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
bin/crucible-claude      starts Claude Code with Code Mode on
scripts/                 bookkeeping (save, checkpoint, review pack, digests), the single-agent adapter
references/              the run-audit questions, expectations, domain checks, templates
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

It runs the engine against scripted agents, then the Python tests of the review pack and of the runner. No model is called and it takes under a minute.

## Licence

MIT. See `LICENSE`.
