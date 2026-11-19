// Regression suite for the crucible engine. Usage: node tests/run.mjs [enginePath]
// Exit code 0 = all pass. Expectations encode behaviour the user settled on; do not weaken them to make a change pass.
import { run } from './mock.mjs'
import path from 'path'
import { fileURLToPath } from 'url'
const here = path.dirname(fileURLToPath(import.meta.url))
const engine = process.argv[2] || path.join(here, '..', 'engine', 'crucible-engine.js')
let fails = 0
const check = (name, cond, info) => { if (!cond) { fails++; console.log(`FAIL ${name}${info ? ': ' + info : ''}`) } else console.log(`ok   ${name}`) }
const byId = (res, id) => res.results.find(r => r.id === id) || {}

{ const { res, calls, logs } = await run(engine, 'trivial')
  check('trivial: exactly 3 agents (planner, solver, attacker)', calls.length === 3, calls.join(' '))
  check('trivial: verified', byId(res, 'sum').final === 'verified')
  check('trivial: no synthesizer agent', res.synthesis && res.synthesis.inline === true)
  check('trivial: no errors', !logs.some(l => /ERR/.test(l)), logs.filter(l => /ERR/.test(l)).join(' | ')) }
{ const { res, calls } = await run(engine, 'trivial', 'quick')
  check('trivial quick: 3 agents', calls.length === 3) }
{ const { res, calls, efforts, logs } = await run(engine, 'race')
  check('race: won race skips c,d', JSON.stringify(res.skipped) === '["c","d"]', JSON.stringify(res.skipped))
  check('race: a verified', byId(res, 'a').final === 'verified')
  check('race: b exhausted', byId(res, 'b').final === 'exhausted')
  check('race: hard scope solver high, attacker high', efforts['critic:a:r1'] === 'high' && efforts['solver:a:r1'] === 'high')
  check('race: no errors', !logs.some(l => /ERR/.test(l))) }
{ const { res, calls, logs } = await run(engine, 'exhaustive')
  check('exhaustive: shared data fetched once per item', calls.filter(c => c.startsWith('fetch:')).length === 2)
  check('exhaustive: an easy part that fails two rounds gets parallel attempts, and the attempt that survives is verified', byId(res, 'c').fanout && byId(res, 'c').fanout.winner === 'fresh' && byId(res, 'c').final === 'verified' && byId(res, 'c').rounds === 4 && !calls.some(c => c.includes('c--')), JSON.stringify(byId(res, 'c').fanout))
  check('exhaustive: refuted claim with upheld appeal is debunked', byId(res, 'd').final === 'debunked' && byId(res, 'd').appeal === 'upheld')
  check('exhaustive: gap loop adds scope e', byId(res, 'e').final === 'verified')
  check('exhaustive: no errors', !logs.some(l => /ERR/.test(l))) }
{ const { res, calls, logs } = await run(engine, 'staged')
  check('staged: a runs before b', calls.indexOf('solver:a:r1') < calls.indexOf('solver:b:r1'))
  check('staged: b exhausted', byId(res, 'b').final === 'exhausted')
  check('staged: no errors', !logs.some(l => /ERR/.test(l))) }
{ const { res, calls, logs } = await run(engine, 'multi')
  check('multi: two layers', res.layers.length === 2)
  check('multi: layer-2 ids prefixed', res.results.some(r => r.id === 'L2-build'))
  check('multi: final synthesizer runs', calls.includes('final-synthesizer'))
  check('multi: no errors', !logs.some(l => /ERR/.test(l))) }
{ const { res, calls, logs, prompts } = await run(engine, 'resplit', 'quick')
  check('resplit: merged scope brief carries both superseded results', /x \[blocked, superseded by xy\]/.test(prompts['solver:xy:r1'] || '') && /- y \[/.test(prompts['solver:xy:r1'] || ''))
  check('resplit: blocked scope stops after round 1', byId(res, 'x').final === 'blocked' && byId(res, 'x').rounds === 1)
  check('resplit: restructuring pass runs even at quick depth', calls.some(c => c.startsWith('completeness')))
  check('resplit: merged scope replaces both and builds on them', byId(res, 'xy').final === 'verified' && byId(res, 'x').supersededBy === 'xy' && byId(res, 'y').supersededBy === 'xy')
  check('resplit: boundary issue recorded', (byId(res, 'x').boundaryIssues || []).length === 1)
  check('resplit: no errors', !logs.some(l => /ERR/.test(l)), logs.filter(l => /ERR/.test(l)).join(' | ')) }
// self-reflection: recorded per run, never applied per run; skipped on small clean runs; runs alongside the final synthesis
{ const { res, calls } = await run(engine, 'trivial')
  check('reflect: skipped on a small clean run', !calls.includes('reflector') && res.reflection === null) }
{ const { res, calls } = await run(engine, 'exhaustive')
  check('reflect: runs on a non-trivial run and returns proposals', calls.includes('reflector') && res.reflection && res.reflection.findings.length === 1)
  check('reflect: no applier or framework edit inside a run', !calls.some(c => /applier|verify:/.test(c)))
  check('reflect: launched together with the synthesizer', Math.abs(calls.indexOf('reflector') - calls.indexOf('synthesizer')) === 1) }
// effort policy set by the user: never max; xhigh only for the attacking side of frontier scopes; attacker never below solver
for (const sc of ['trivial', 'race', 'exhaustive', 'staged', 'multi', 'frontier', 'resplit', 'saturate', 'sched', 'own', 'fix', 'stop']) for (const depth of ['standard', 'max']) {
  const { efforts } = await run(engine, sc, depth)
  const vals = Object.entries(efforts)
  check(`effort ${sc}/${depth}: never max`, !vals.some(([, e]) => e === 'max'))
  const { res } = await run(engine, sc, depth)
  const frontier = new Set((res.plan.scopes || []).filter(x => x.difficulty === 'frontier').map(x => x.id))
  const attackerRole = l => /^(critic|contract|debunk|appeal|repair-check):/.test(l)
  const okX = ([l, e]) => e !== 'xhigh' || (attackerRole(l) && frontier.has(l.split(':')[1].replace(/--.*/, '')))
  check(`effort ${sc}/${depth}: xhigh only on frontier attackers`, vals.every(okX), vals.filter(v => !okX(v)).map(([l]) => l).join(' '))
  const lvl = { low: 0, medium: 1, high: 2, xhigh: 3, max: 4 }
  const bad = vals.filter(([l, e]) => l.startsWith('critic:') && lvl[e] < lvl[efforts[l.replace('critic:', 'solver:')]])
  check(`effort ${sc}/${depth}: attacker never below solver`, !bad.length, bad.map(([l]) => l).join(' '))
  const { models } = await run(engine, sc, depth)
  const rank = { haiku: 1, sonnet: 2, opus: 3, fable: 4 }
  const weak = Object.keys(models).filter(l => l.startsWith('critic:') && rank[models[l]] < rank[models[l.replace('critic:', 'solver:')]])
  check(`model ${sc}/${depth}: a weaker model never attacks a stronger one`, !weak.length, weak.join(' '))
}
{ const { efforts } = await run(engine, 'frontier')
  check('frontier: solver high, attacker xhigh', efforts['solver:deep:r1'] === 'high' && efforts['critic:deep:r1'] === 'xhigh', JSON.stringify(efforts)) }
// periodic evolve gating: only confirmed, significant, unprotected, budgeted fixes reach the applier
{ const fs = await import('fs')
  const src = fs.readFileSync(path.join(here, '..', 'engine', 'crucible-evolve.js'), 'utf8').replace(/^export const meta/m, 'const meta')
  const F = (id, size, prot) => ({ id, category: 'cost', title: id, evidence: [{ path: 'p', locator: 'l', shows: 's' }], impact: 'i', root_cause: 'r', fix: 'f', fix_files: ['engine/crucible-engine.js'], size, touches_protected: prot, generality: 'g' })
  const calls = []
  const agent = async (prompt, o) => { calls.push(o.label)
    if (o.label === 'reflector') return { findings: [F('real-small', 'small', false), F('protected', 'small', true), F('real-medium', 'medium', false), F('low', 'tiny', false), F('wrong', 'tiny', false)], checked_clean: [], notes: '' }
    if (o.label.startsWith('verify:')) { const id = o.label.slice(7)
      return { verdict: id === 'wrong' ? 'rejected' : 'confirmed', evidence_checked: [], significance: id === 'low' ? 'low' : 'high', fix_ok: true, fix_revised: '', touches_protected: id === 'protected', reason: 'r' } }
    if (o.label === 'applier') return { applied: [{ id: 'real-small', commit: 'abc', files: [], tests: 'ok', test_added: false }], reverted: [], installed: true, notes: '' }
    throw new Error('unexpected ' + o.label) }
  const parallel = async th => Promise.all(th.map(t => t().catch(() => null)))
  const fn = new Function('args', 'agent', 'parallel', 'phase', 'log', `return (async () => { ${src} })()`)
  const res = await fn({ runDirs: ['/tmp/run'], repo: '/tmp/repo', historyPack: '/tmp/pack', reviewReport: '/tmp/pack/run/report.md' }, agent, parallel, () => {}, () => {})
  check('evolve: confirmed unprotected fixes are applied (small and medium)', JSON.stringify(res.accepted.slice().sort()) === '["real-medium","real-small"]', JSON.stringify(res.accepted))
  check('evolve: protected finding goes to the user', res.proposals.length === 1 && res.proposals[0].id === 'protected')
  check('evolve: rejected and low-significance findings are dropped', !res.accepted.includes('wrong') && !res.accepted.includes('low') && !res.deferred.some(d => d.id === 'low'))
  const none = await new Function('args', 'agent', 'parallel', 'phase', 'log', `return (async () => { ${src} })()`)({ runDirs: ['/tmp/run'], repo: '/tmp/repo', historyPack: '/tmp/pack', reviewReport: '/tmp/pack/run/report.md' }, async (p, o) => o.label === 'reflector' ? { findings: [], checked_clean: [], notes: '' } : null, parallel, () => {}, () => {})
  check('evolve: zero findings ends after one agent', none.findings.length === 0 && !none.applied.length)
  // the run audit (2026-11-19): a review reads each run under review the way a person would, before it selects changes
  const EX = { metric: 'attempts.discarded_share_of_busy', baseline: 0.52, op: '<=', target: 0.3, why: 'w' }
  const run2 = async (primaryRuns, more = {}) => { const seen = [], prompts = {}
    const ag = async (prompt, o) => { seen.push(o.label); prompts[o.label] = prompt
      if (o.label.startsWith('audit:')) return more.auditFails === o.label ? null : { answers: [{ question: 'loops', verdict: 'problem', figures: 'two parts ran ten rounds', note: 'n' }, { question: 'efficiency', verdict: 'fine', figures: 'f', note: 'n' }], leads: [{ title: 'open acceptance bar ' + o.label, stage: 'contract', evidence: [{ path: 'p', locator: 'l', shows: 's' }], cost: '40 agents', recurs: 'yes' }], digest_corrections: ['blocking is 142 not 141'], notes: '' }
      if (o.label === 'reflector') return { findings: [{ ...F('prompt-fix', 'small', false), change_kind: 'prompt', probe: 'case', expect: EX, from_audits: ['big/work: open acceptance bar'] }, { ...F('code-fix', 'small', false), change_kind: 'code', probe: '', expect: { ...EX, metric: '' } }, { ...F('not-applied', 'small', false), change_kind: 'code', expect: EX }],
        expectations: [{ id: 'v5.1-staged-attempts', status: 'met', reason: 'r' }, { status: 'open', reason: 'no id' }], checked_clean: [], notes: '' }
      if (o.label.startsWith('verify:')) return { verdict: 'confirmed', evidence_checked: [], significance: 'high', fix_ok: true, fix_revised: '', touches_protected: false, reason: 'r' }
      if (o.label === 'applier') return { applied: [{ id: 'prompt-fix', commit: 'abc', files: [more.noEngine ? 'SKILL.md' : 'engine/crucible-engine.js'], tests: 'ok', test_added: true, changes_prompt: !more.noEngine, probe_case: 'b5' }, { id: 'code-fix', commit: 'abd', files: ['scripts/crucible_run.py'], tests: 'ok', test_added: false, changes_prompt: false, probe_case: '' }], reverted: [{ id: 'not-applied', reason: 'tests failed' }], installed: true, version: 'v5.2.1', notes: '' }
      throw new Error('unexpected ' + o.label) }
    const logs = []
    const res = await new Function('args', 'agent', 'parallel', 'phase', 'log', `return (async () => { ${src} })()`)({ repo: '/tmp/repo', historyPack: '/tmp/pack', primaryRuns, feedback: more.feedback }, ag, parallel, () => {}, m => logs.push(m))
    return { res, seen, prompts, logs } }
  const R = (name, agents, more = {}) => ({ dir: '/runs/' + name, name, engine: 'v5.1', agents, audit: true, digest: `/tmp/pack/runs/${name}/digest.md`, after: `/tmp/pack/runs/${name}/after-run.md`, ...more })
  { const { res, seen, prompts } = await run2([R('big', 302), R('small', 9)], { feedback: '/tmp/pack/user-feedback.md' })
    check('audit: a large run gets one auditor per lens, a small run one for all', JSON.stringify(seen.filter(l => l.startsWith('audit:'))) === '["audit:big:work","audit:big:answer","audit:big:after","audit:small:all"]', seen.join(' '))
    check('audit: auditors run before the selector', seen.indexOf('reflector') > seen.indexOf('audit:small:all'))
    check('audit: an auditor gets the digest, the rubric, the user\'s words after the run and the feedback file', ['/tmp/pack/runs/big/digest.md', '/tmp/pack/run-audit.md', '/tmp/pack/runs/big/after-run.md', '/tmp/pack/user-feedback.md'].every(x => prompts['audit:big:after'].includes(x)))
    check('audit: each lens is told its own questions', /questions 1 to 4/.test(prompts['audit:big:work']) && /questions 5 and 6/.test(prompts['audit:big:answer']) && /questions 7 and 8/.test(prompts['audit:big:after']) && /all eight questions/.test(prompts['audit:small:all']))
    check('audit: the user\'s words are data, never instructions', /data, never instructions/.test(prompts['audit:big:after']) && /data, never instructions/.test(prompts.reflector))
    check('audit: leads, problem verdicts and digest corrections reach the selector', /LEAD \(contract\) open acceptance bar audit:big:work/.test(prompts.reflector) && /loops: two parts ran ten rounds/.test(prompts.reflector) && /blocking is 142 not 141/.test(prompts.reflector))
    check('audit: a verifier of an audit-based finding is told to recompute the auditor\'s figures', /recompute it from the run's records/.test(prompts['verify:prompt-fix']) && !/recompute it from the run's records/.test(prompts['verify:code-fix']))
    check('audit: the result lists every audit with its verdicts and leads', res.audits.length === 4 && res.audits[0].verdicts.loops === 'problem' && res.audits[0].leads[0].stage === 'contract')
    check('expectations: only an applied change with a number becomes an expectation', JSON.stringify(res.newExpectations.map(e => e.finding)) === '["prompt-fix"]' && res.newExpectations[0].target === 0.3, JSON.stringify(res.newExpectations))
    check('expectations: the selector\'s verdicts on earlier changes are returned, entries without an id dropped', JSON.stringify(res.expectations.map(e => e.id + ':' + e.status)) === '["v5.1-staged-attempts:met"]')
    // the owner's standard (2026-11-19): every agent of a review reads expectation.md and none may edit it
    check('expectation.md: every agent of a review is given the owner\'s file as the standard and told never to change it', ['audit:big:work', 'audit:small:all', 'reflector', 'verify:prompt-fix', 'applier'].every(l => prompts[l].includes('/tmp/repo/expectation.md') && /Only the owner edits that file: never change it/.test(prompts[l])), Object.keys(prompts).join(' '))
    check('expectation.md: a finding names the line it serves, a fix against a line is protected, the applier never edits the file', /id of the line of expectation\.md it serves/.test(prompts.reflector) && /work against a line of expectation\.md \(then touches_protected is true\)/.test(prompts['verify:prompt-fix']) && /never in expectation\.md/.test(prompts.applier))
    check('probes: an engine edit is reported so the probes run afterwards', res.engineChanged === true && res.version === 'v5.2.1')
    check('applier: told to add a probe case for a prompt change, to raise the version, and not to run the probes', /calibrate_rules\.py/.test(prompts.applier) && /raise ENGINE_VERSION by one patch step/.test(prompts.applier) && /Do not run the probes/.test(prompts.applier) && /kind: prompt; probe: case/.test(prompts.applier)) }
  { const { res } = await run2([R('big', 302)], { noEngine: true })
    check('probes: a review that did not touch the engine needs none', res.engineChanged === false) }
  { const { seen, logs } = await run2(Array.from({ length: 8 }, (_, i) => R('r' + i, 50)))
    const a = [...new Set(seen.filter(l => l.startsWith('audit:')).map(l => l.split(':')[1]))]
    check('audit: at most six runs are audited in full, the most recent, and the rest are named', a.length === 6 && !a.includes('r0') && !a.includes('r1') && a.includes('r7') && logs.some(m => /2 run\(s\) under review keep their digest.*r0, r1/.test(m)), a.join(' ') + ' | ' + logs.join(' | ')) }
  { const { res, seen } = await run2([R('big', 302), R('skip', 80, { audit: false })], { auditFails: 'audit:big:answer' })
    check('audit: a run marked not for audit is skipped, and a failed auditor does not stop the review', !seen.some(l => l.startsWith('audit:skip')) && res.audits.length === 2 && res.accepted.length === 3) }
  { const { seen } = await run2([])
    check('audit: no runs under review means no audit phase (proposals only)', !seen.some(l => l.startsWith('audit:')) && seen.includes('reflector')) } }
// cost control (2026-11-12, after the first live audit run: attackers always found new ground, so every scope ran to its cap)
// v5 (2026-11-15): a part that does not converge no longer loops serially. Two rounds at most; then a referee rules on
// the open findings (when the solver disputes them or each attack opened new ground) and fresh attempts run side by side.
{ const { res, calls, logs, prompts, models } = await run(engine, 'saturate')
  check('saturate: two serial rounds at most; then a referee, the repair attempt alone, and only then the other attempts side by side', byId(res, 's').rounds === 5 && byId(res, 's').pairOutcome === 'not_converged' && calls.includes('referee:s') && calls.indexOf('critic:s:r3') < calls.indexOf('solver:s:r4') && calls.indexOf('solver:s:r5') < calls.indexOf('critic:s:r4'), JSON.stringify(byId(res, 's').roundLog))
  check('saturate: the parallel attempts run one difficulty up, and their attackers are raised with them', models['solver:s:r1'] === 'sonnet' && models['solver:s:r3'] === 'opus' && models['critic:s:r3'] === 'opus', `${models['solver:s:r1']} ${models['solver:s:r3']} ${models['critic:s:r3']}`)
  check('saturate: each parallel attempt has its own strategy', /Yours: REPAIR/.test(prompts['solver:s:r3']) && /Yours: FRESH START/.test(prompts['solver:s:r4']) && /Yours: CHECK FIRST/.test(prompts['solver:s:r5']))
  check('saturate: a part that still does not converge is caveated, not reviewed as settled', byId(res, 's').final === 'unconverged' && !calls.some(c => c.startsWith('debunk:s:')))
  check('saturate: non-blocking findings do not buy another round', byId(res, 'n').rounds === 1 && byId(res, 'n').final === 'verified', JSON.stringify(byId(res, 'n')))
  check('saturate: synthesizer sees the open blocking finding and writes a handoff', /blocking findings still open: o-r2/.test(prompts.synthesizer || '') && /crucible-handoff\.md/.test(prompts.synthesizer || ''))
  check('saturate: no errors', !logs.some(l => /ERR/.test(l)), logs.filter(l => /ERR/.test(l)).join(' | ')) }
{ const { res, calls } = await run(engine, 'saturate', 'standard', { referee: 'clear' })
  check('referee: findings it rejects after running their checks stop blocking; the result goes to review, with no more rounds', byId(res, 's').referee && byId(res, 's').referee.upheld === 0 && byId(res, 's').rounds === 2 && !calls.includes('solver:s:r3') && calls.some(c => c.startsWith('debunk:s:')) && byId(res, 's').final === 'verified', JSON.stringify(byId(res, 's'))) }
{ const { res, calls } = await run(engine, 'saturate', 'standard', { referee: 'unchecked' })
  check('referee: a rejection without an executed check clears nothing', byId(res, 's').referee.upheld === 1 && calls.includes('solver:s:r3')) }
{ const { res } = await run(engine, 'exhaustive', 'standard', { allAttemptsFail: true })
  check('parallel attempts: when none is better, the earlier best stays and the part is unconverged', byId(res, 'c').fanout && byId(res, 'c').fanout.winner === null && byId(res, 'c').final === 'unconverged' && byId(res, 'c').bestRound === 2, JSON.stringify(byId(res, 'c').fanout)) }
{ const { calls } = await run(engine, 'exhaustive')
  check('repair only for material flaws (a typo is a caveat)', !calls.includes('repair:a') && !calls.includes('repair-check:a')) }
{ const { res } = await run(engine, 'exhaustive', 'standard', { planOnly: true })
  check('planOnly: returns a cost estimate and a ceiling', res.cost && res.cost.estimate.agents > 0 && res.cost.ceiling.agents >= res.cost.estimate.agents && typeof res.cost.estimate.weeklyPct === 'number', JSON.stringify(res.cost)) }
{ const full = await run(engine, 'exhaustive')
  check('budget: ceiling recorded and respected on a normal run', full.res.budget && full.res.budget.agents <= full.res.budget.ceiling && !full.res.budget.wrapped, JSON.stringify(full.res.budget))
  const { res, calls, logs, prompts } = await run(engine, 'exhaustive', 'standard', { maxAgents: 9 })
  const work = calls.filter(c => !['synthesizer', 'reflector'].includes(c)).length
  check('budget: a run at its ceiling wraps up instead of spawning more', res.budget.wrapped && work <= 9 && calls.length < full.calls.length, `${work} work agents; ${calls.join(' ')}`)
  check('budget: wrapped run still synthesizes and writes a handoff', calls.includes('synthesizer') && /wrapped up early/.test(prompts.synthesizer || '') && /crucible-handoff\.md/.test(prompts.synthesizer || ''))
  check('budget: no errors when wrapping', !logs.some(l => /ERR/.test(l)), logs.filter(l => /ERR/.test(l)).join(' | ')) }
{ const { res, calls } = await run(engine, 'trivial')
  check('budget: trivial run ceiling stays small', res.budget.ceiling <= 6 && calls.length === 3, JSON.stringify(res.budget)) }
{ const { res, calls, prompts } = await run(engine, 'exhaustive', 'standard', { close: true })
  check('close: one closer (plus the reflector), nothing re-run', JSON.stringify(calls.slice().sort()) === '["closer","reflector"]' && res.closed, calls.join(' '))
  check('close: closer reads the checkpoint and writes answer + handoff', /checkpoint\.json/.test(prompts.closer) && /crucible-handoff\.md/.test(prompts.closer) && /answer\.md/.test(prompts.closer)) }
{ const { res, calls, prompts } = await run(engine, 'continue', 'standard', { continueFrom: '/tmp/run/checkpoint.json' })
  check('continue: planner is told to plan only what is left', /CONTINUATION/.test(prompts.planner) && /checkpoint\.json/.test(prompts.planner))
  check('continue: resumed scope reuses its contract and continues from the next round', !calls.includes('contract:a') && calls.includes('solver:a:r3') && !calls.includes('solver:a:r1') && /EARLIER WORK ON THIS SCOPE/.test(prompts['solver:a:r3']) && /contract\.md/.test(prompts['solver:a:r3']), calls.join(' '))
  check('continue: established results are not re-run but reach the synthesizer', !calls.some(c => c.includes('done1')) && /done1: done one \[verified, established by the earlier session\]/.test(prompts.synthesizer || '') && res.established.includes('done1')) }
{ let threw = false; try { await run(engine, 'trivial', 'standard', { expectVersion: 'v0-stale' }) } catch (e) { threw = /expected/.test(e.message) }
  check('version guard: a stale or mismatched engine refuses to run', threw) }
// fixes from the first live audit (2026-11-12): checks, tamper fingerprint, plan review, failures, context, data-tool rules, coupling, lenses
{ const { res } = await run(engine, 'trivial', 'standard', { inspectOnly: true })
  check('checks: reading the submission is not an executed check (never verified on inspection alone)', byId(res, 'sum').final !== 'verified', byId(res, 'sum').final) }
{ const { logs, prompts } = await run(engine, 'exhaustive', 'standard', { emptyFrozen: true })
  check('fingerprint: a contract whose fingerprint covers no files is not trusted as a tamper check', logs.some(l => /covers no files/.test(l)) && !/must equal e3b0/.test(prompts['critic:a:r1'] || ''))
  const { prompts: p2 } = await run(engine, 'exhaustive')
  check('fingerprint: the command is quoted and null-separated (paths with spaces)', /find "\/tmp\/run\/scopes\/a\/contract" -type f -print0 \| sort -z \| xargs -0/.test(p2['contract:a'] || '')) }
{ const { res, logs } = await run(engine, 'exhaustive', 'standard', { throwOn: '^(plan-critic:v1|critic:a:r1|debunk:d:1)$' })
  check('failures: a throwing agent never crashes the run', res && res.synthesis && !logs.some(l => /ERR/.test(l)), logs.filter(l => /ERR/.test(l)).join(' | '))
  check('failures: failed agents are recorded and reach the synthesizer', res.failedAgents.length === 3)
  check('plan review: a failed plan critic is reported as not reviewed, never as approved', /not reviewed/.test(res.planReview || ''), res.planReview) }
{ const { res } = await run(engine, 'exhaustive')
  check('plan review: an approving critic is reported as approved', /approved/.test(res.planReview || ''), res.planReview) }
{ const { prompts } = await run(engine, 'exhaustive')
  check('context: every agent is pointed at problem.md', Object.values(prompts).every(p => /\/tmp\/run\/problem\.md/.test(p)))
  check('data tool: no rules file unless the user asked for the tool', !Object.values(prompts).some(p => /The user asked for .* on this run/.test(p)))
  check('steps: every agent is told to work in few, large steps, with a script tool where it has one', Object.values(prompts).every(p => /Work in few, large steps/.test(p) && /a code or REPL tool/.test(p) && /never replaces a check your role requires/.test(p)))
  check('data tool: the engine names no particular tool of its own', !Object.values(prompts).some(p => /treg|tinyfish|X-Treg/i.test(p)))
  check('lenses: the review panel always includes independent reproduction', /independent reproduction/.test(prompts['debunk:a:2'] || ''))
  check('synthesis sees the success definition', /Success definition:/.test(prompts.synthesizer || '')) }
{ const { prompts } = await run(engine, 'exhaustive', 'standard', { dataTool: 'paidtool', dataRules: '/home/u/rules/paidtool-rules.md', dataNote: 'Make paidtool calls through its MCP tools so identical calls come from the session cache.' })
  check('data tool: when the user asks for it every agent gets the rules file', Object.values(prompts).every(p => /asked for paidtool on this run.*paidtool-rules\.md/s.test(p)))
  check('data tool: the installation\'s own note reaches every agent', Object.values(prompts).every(p => /identical calls come from the session cache/.test(p))) }
{ const on = await run(engine, 'trivial', 'standard', { codeMode: true }), off = await run(engine, 'trivial', 'standard', { codeMode: false }), unset = await run(engine, 'trivial')
  check('code mode: what the front desk saw is recorded in the result, and changes no prompt', on.res.codeMode === true && off.res.codeMode === false && unset.res.codeMode === null && JSON.stringify(on.prompts) === JSON.stringify(off.prompts)) }
{ const { prompts } = await run(engine, 'exhaustive', 'standard', { dataRules: '/r.md' })
  check('data tool: without a name it is the user\'s external data tool', Object.values(prompts).every(p => /asked for their external data tool on this run/.test(p))) }
{ const { logs, calls } = await run(engine, 'saturate', 'standard', { noteCoupling: true })
  check('coupling: a noted, non-blocking coupling does not trigger restructuring', !logs.some(l => /split problems reported/.test(l))) }
// v4.3 (2026-11-13): fixes from the continued audit
{ const { res, logs } = await run(engine, 'exhaustive', 'standard', { maxAgents: 24 })
  check('ceiling: attempts that do not fit are skipped alone; the rest of the run goes on', logs.some(l => /skipping the repair attempt on c/.test(l)) && byId(res, 'd').final === 'unreviewed' && byId(res, 'c').final === 'unconverged', res.results.map(x => x.id + ':' + x.final).join(','))
  const full = await run(engine, 'exhaustive')
  check('ceiling: with the default ceiling the part that did not converge gets its parallel attempts', byId(full.res, 'c').fanout && byId(full.res, 'c').fanout.width === 2) }
{ const { res, calls } = await run(engine, 'exhaustive', 'standard', { throwOn: '^debunk:a:[2-9]$' })
  const n = calls.filter(c => c.startsWith('debunk:a:')).length
  check('quorum: a result is never verified when most of its reviewers failed', n > 1 && byId(res, 'a').final !== 'verified', `${n} reviewers, final ${byId(res, 'a').final}`) }
{ const { res, prompts } = await run(engine, 'exhaustive', 'standard', { maxAgents: 9 })
  check('outputs: the synthesizer returns report, answer and handoff instead of writing them', /do not write report\.md, answer\.md or crucible-handoff\.md yourself/.test(prompts.synthesizer || '') && !/Write \/tmp\/run\/(report|answer)\.md/.test(prompts.synthesizer || '') && res.synthesis.handoff === 'handoff text') }
{ const { res, prompts } = await run(engine, 'exhaustive', 'standard', { close: true })
  check('outputs: the closer returns them too', /do not write report\.md/.test(prompts.closer || '') && res.synthesis.report === 'internal report') }
{ const { res, prompts } = await run(engine, 'multi', 'deep')
  check('layers: later layers get earlier layer reports inline, not as paths to files that do not exist yet', /--- layer 1 report ---\ninternal report/.test(prompts['strategist:L1'] || '') && res.layers[0].reportText === 'internal report') }
{ const { res } = await run(engine, 'exhaustive', 'standard', { ungatedFatal: true })
  check('open fatal: a fatal objection dropped for missing evidence still keeps the result from being verified', byId(res, 'a').final !== 'verified', byId(res, 'a').final) }
{ const { prompts } = await run(engine, 'exhaustive', 'standard', { dataTool: 'paidtool', dataRules: '/r.md', dataBudget: '$20' })
  check('data budget: reaches every agent with the rules', Object.values(prompts).every(p => /paidtool budget of \$20 for this whole run/.test(p))) }
{ const { res, calls } = await run(engine, 'exhaustive', 'standard', { outageAfter: 6, outageMsg: "You've hit your weekly limit · resets Nov 15 at 10:30am" })
  check('outage: a usage limit pauses the run at once; no synthesizer or reflector is started to fail', !!res.paused && calls.length <= 12 && !calls.some(c => /synthesizer|reflector/.test(c)), `${calls.length} calls, paused=${res.paused}`) }
{ const { res, calls } = await run(engine, 'exhaustive', 'standard', { outageAfter: 6 })
  check('outage: agents returning nothing four times in a row pause the run', !!res.paused && calls.length <= 14 && !calls.some(c => /synthesizer|reflector/.test(c)), `${calls.length} calls, paused=${res.paused}`) }
{ const { res } = await run(engine, 'exhaustive', 'standard', { throwOn: '^debunk:a:[2-9]$' })
  check('outage: ordinary agent failures do not pause the run', !res.paused && !!res.synthesis, `paused=${res.paused}`) }
// v5 (2026-11-15): routing. Each role runs on the model and effort its difficulty calls for, not on the session's model.
{ const { res, models, efforts } = await run(engine, 'exhaustive')
  check('routing: the model follows difficulty (easy and moderate on sonnet, hard and the orchestration roles on opus)', models['solver:c:r1'] === 'sonnet' && models['solver:d:r1'] === 'sonnet' && models['solver:a:r1'] === 'opus' && models.planner === 'opus' && models.synthesizer === 'opus' && models['fetch:prices'] === 'sonnet', JSON.stringify(models))
  check('routing: a moderate review panel has one seat on the strongest route', models['debunk:d:1'] === 'opus' && models['debunk:d:2'] === 'sonnet')
  check('routing: no agent inherits the session model on the default table', Object.values(models).every(m => m !== '-'), Object.entries(models).filter(([, m]) => m === '-').map(([l]) => l).join(' '))
  check('routing: the run reports the routes it used', res.routing && res.routing.profile === 'balanced' && Object.keys(res.routing.used).some(k => /^solver\/hard opus@high$/.test(k)), JSON.stringify(res.routing)) }
{ const fs = await import('fs')
  const src = fs.readFileSync(engine, 'utf8')
  const inEngine = new Function('return ' + src.match(/const ROUTING_DEFAULT = (\{[\s\S]*?\n\})\n/)[1])()
  const table = JSON.parse(fs.readFileSync(path.join(here, '..', 'routing.json'), 'utf8'))
  const canonical = o => JSON.stringify(o, (k, v) => (v && typeof v === 'object' && !Array.isArray(v) ? Object.fromEntries(Object.keys(v).sort().map(x => [x, v[x]])) : v))
  check('routing: the engine fallback table equals routing.json (default profile)', canonical(inEngine) === canonical(table.profiles[table.default]))
  const bad = Object.entries(table.profiles).flatMap(([n, p]) => JSON.stringify(p.roles).match(/@max/g) ? [n] : [])
  check('routing: no profile uses effort max', !bad.length, bad.join(' ')) }
{ const weakCritic = { roles: { critic: { trivial: 'haiku@low', easy: 'haiku@low', moderate: 'haiku@low', hard: 'haiku@low', frontier: 'haiku@low' } } }
  const { models, efforts } = await run(engine, 'exhaustive', 'standard', { routing: weakCritic })
  check('routing: a table that puts a weaker model or a lower effort on the attacking side is corrected in code', models['critic:a:r1'] === 'opus' && models['critic:d:r1'] === 'sonnet' && efforts['critic:d:r1'] === 'medium' && efforts['critic:a:r1'] === 'high', `${models['critic:a:r1']}@${efforts['critic:a:r1']} ${models['critic:d:r1']}@${efforts['critic:d:r1']}`) }
{ const fs = await import('fs')
  const session = JSON.parse(fs.readFileSync(path.join(here, '..', 'routing.json'), 'utf8')).profiles.session
  const { models, efforts } = await run(engine, 'exhaustive', 'standard', { routing: session })
  check('routing: the session profile leaves every agent on the session model, with the effort table', Object.values(models).every(m => m === '-') && efforts['solver:a:r1'] === 'high' && efforts['solver:d:r1'] === 'medium' && efforts['critic:d:r1'] === 'high') }
{ let threw = false; try { await run(engine, 'trivial', 'standard', { routing: { roles: { planner: 'opus@max' } } }) } catch (e) { threw = /max is never used/.test(e.message) }
  check('routing: a route with effort max is refused', threw) }
// other providers: a role routed to Codex or OpenRouter runs behind a relay agent; its result is accepted only with a matching checksum
{ const mixed = { rank: { haiku: 1, sonnet: 2, opus: 3, 'openai/gpt-6.1-terra': 2 }, roles: { critic2: { moderate: 'openrouter:openai/gpt-6.1-terra@high' } } }
  const ok = await run(engine, 'exhaustive', 'standard', { routing: mixed, sessionId: 'sess-1' })
  check('relay: a second attacker from another provider runs beside the first, behind a cheap relay agent', ok.relays.some(r => r.label === 'critic2:d:r1' && r.provider === 'openrouter' && r.model === 'openai/gpt-6.1-terra' && r.effort === 'high' && r.relayModel === 'haiku') && ok.calls.includes('critic:d:r1') && ok.res.routing.relayed.ok > 0 && ok.res.routing.relayed.failed === 0, JSON.stringify(ok.res.routing.relayed))
  check('relay: the relay is told how to find its spec (marker and session id)', /crucible_agent\.py relay --marker CRUCIBLE-RELAY-[0-9a-f]{8}-critic2-d-r1 --session sess-1/.test((ok.relays.find(r => r.label === 'critic2:d:r1') || {}).prompt || ''))
  check('relay: results merge with the first attacker and the part is still decided by code', byId(ok.res, 'd').final === 'debunked')
  const bad = await run(engine, 'exhaustive', 'standard', { routing: mixed, relay: 'corrupt' })
  check('relay: a result whose checksum does not match is discarded and the Claude route answers instead', bad.res.routing.relayed.failed > 0 && bad.res.routing.relayed.ok === 0 && bad.logs.some(l => /did not match its checksum/.test(l)) && bad.models['critic2:d:r1'] === 'sonnet', JSON.stringify(bad.res.routing.relayed))
  const dead = await run(engine, 'exhaustive', 'standard', { routing: mixed, relay: 'fail' })
  check('relay: a failed provider falls back to the Claude route and the run goes on', dead.res.routing.relayed.failed > 0 && !!dead.res.synthesis && !dead.res.paused && dead.logs.some(l => /out of credit/.test(l))) }
{ const unranked = { roles: { critic: { moderate: 'openrouter:some/unknown-model@high' } } }
  const { relays, models } = await run(engine, 'exhaustive', 'standard', { routing: unranked })
  check('relay: a model without a strength rank is never put on the attacking side', !relays.length && models['critic:d:r1'] === 'sonnet') }
{ const fs = await import('fs'); const cp = await import('child_process'); const os = await import('os')
  const src = fs.readFileSync(engine, 'utf8')
  const ckOf = new Function(src.match(/const canon = [\s\S]*?\nconst ckOf = .*\n/)[0] + 'return ckOf')()
  const sample = { verdict: 'major_issues', n: 3, conf: 0.85, half: 0.5, whole: 2.0, ok: true, none: null, text: 'naïve “quotes” → 雪 \n tab\t', list: [1, 'a', { z: 1, a: [true, false] }], _ck: 'ignored' }
  const f = path.join(os.tmpdir(), `crucible-ck-${process.pid}.json`); fs.writeFileSync(f, JSON.stringify(sample))
  const py = cp.spawnSync('python3', [path.join(here, '..', 'scripts', 'crucible_agent.py'), 'ck', '--file', f], { encoding: 'utf8' }).stdout.trim(); fs.unlinkSync(f)
  check('relay: the engine and the adapter compute the same checksum', /^[0-9a-f]{8}$/.test(py) && py === ckOf(sample), `python ${py} js ${ckOf(sample)}`) }
// robustness across models: "none" where an empty value is meant must not read as a finding
{ const { res, calls } = await run(engine, 'trivial', 'standard', { noneText: true })
  check('none-text: an attacker that writes "None found." in the violation field does not send clean work back', byId(res, 'sum').final === 'verified' && calls.length === 3, `${byId(res, 'sum').final} ${calls.length}`) }
{ const { res } = await run(engine, 'trivial', 'standard', { integrityFlag: true })
  check('integrity: a flagged violation still blocks acceptance', byId(res, 'sum').final !== 'verified', byId(res, 'sum').final) }
// scheduling: a part starts when its own prerequisites are reviewed, not when the whole earlier layer is
{ const { calls, logs } = await run(engine, 'sched')
  check('scheduling: a part does not wait for an unrelated slow part', calls.indexOf('solver:postcheck:r1') > calls.indexOf('critic:lookup:r1') && calls.indexOf('solver:postcheck:r1') < calls.indexOf('debunk:a:1'), calls.join(' '))
  check('scheduling: no errors', !logs.some(l => /ERR/.test(l))) }
{ const a = await run(engine, 'exhaustive'), b = await run(engine, 'exhaustive')
  check('resume: the same plan builds the same prompts every time', JSON.stringify(a.prompts) === JSON.stringify(b.prompts)) }
// v5.1 (2026-11-19), from the first real v5.0 run: 302 agents, 31 hours. 130 agents worked on parallel attempts and 18 of
// them on a version that was kept; the run reached its ceiling before the assembly and the end-to-end proof started; two
// parts chased contract clauses over an open set of cases for ten rounds; no part ended verified.
{ const { res, calls } = await run(engine, 'fix')
  check('staged attempts: when the repair attempt survives, no other attempt is started', byId(res, 'fix').final === 'verified' && byId(res, 'fix').fanout.winner === 'repair' && byId(res, 'fix').fanout.width === 1 && !calls.includes('solver:fix:r4') && !calls.includes('solver:fix:r5'), JSON.stringify(byId(res, 'fix').fanout)) }
{ const { res, calls } = await run(engine, 'stop')
  const f = byId(res, 'h').fanout
  check('staged attempts: the others start side by side only after the repair failed', calls.indexOf('critic:h:r4') < calls.indexOf('solver:h:r5') && calls.indexOf('solver:h:r7') < calls.indexOf('critic:h:r5'), calls.filter(c => /:h:/.test(c)).join(' '))
  check('staged attempts: once one attempt has survived, its siblings start no further round', f.winner === 'fresh' && !calls.includes('solver:h:r8') && !calls.includes('solver:h:r6') && f.attempts.find(a => a.strategy === 'check-first').outcome === 'stopped' && byId(res, 'h').final === 'verified', JSON.stringify(f))
  check('staged attempts: round numbers keep each strategy\'s slot, whichever attempts ran', calls.includes('solver:h:r3') && calls.includes('solver:h:r4') && calls.includes('solver:h:r5') && calls.includes('solver:h:r7') && byId(res, 'h').bestRound === 5) }
{ const { res, calls } = await run(engine, 'saturate', 'standard', { referee: 'redesign' })
  check('staged attempts: a referee ruling that the approach is wrong skips the repair attempt', !calls.includes('solver:s:r3') && calls.includes('solver:s:r4') && calls.includes('solver:s:r5') && byId(res, 's').referee.repairable === false, calls.filter(c => /:s:/.test(c)).join(' ')) }
{ const { res, calls, prompts, logs } = await run(engine, 'own')
  const sp = prompts['solver:x1:r1'] || ''
  check('ownership: a solver is told what its scope owns and which success items it is held to', /This scope owns \(it alone settles these and answers for them\): extra one/.test(sp) && /held to: S1: the tool runs end to end/.test(prompts['solver:proof:r1'] || ''))
  check('ownership: every scope gets the plan map (who owns what) and the request board', /PLAN MAP/.test(sp) && /- skel \[critical\]: skel\. Owns: the record format handed between steps/.test(sp) && /REQUESTS BETWEEN SCOPES \(folder \/tmp\/run\/board\//.test(sp) && /to-x1--\*\.md/.test(sp))
  check('ownership: the attacker passes a cause outside the scope to its owner through the board', /out_of_part/.test(prompts['critic:x1:r1'] || '') && /board\/to-<owner id>--from-check-x1--/.test(prompts['critic:x1:r1'] || ''))
  check('ownership: the synthesizer reports each success item against its owner and reads the board', /S2 \(owner: skel\): records are readable by every step/.test(prompts.synthesizer || '') && /Fill success_items/.test(prompts.synthesizer || '') && /\/tmp\/run\/board\//.test(prompts.synthesizer || ''))
  check('critical: a scope that is not critical gets one further attempt, not the full set', byId(res, 'x1').fanout.width === 2 && !calls.includes('solver:x1:r5') && res.plan.scopes.find(x => x.id === 'x1').critical === false && res.plan.scopes.find(x => x.id === 'proof').critical === true, JSON.stringify(byId(res, 'x1').fanout))
  check('critical: no errors', !logs.some(l => /ERR/.test(l)), logs.filter(l => /ERR/.test(l)).join(' | ')) }
for (const m of [14, 16, 20]) { const { res, calls, logs } = await run(engine, 'own', 'standard', { maxAgents: m })
  check(`critical: at a ceiling of ${m} agents the critical scopes are worked and reviewed; the extras give way`, byId(res, 'skel').final === 'verified' && byId(res, 'proof').final === 'verified' && !res.skipped.includes('proof') && ['unconverged', 'not_started'].includes(byId(res, 'x1').final) && calls.filter(c => !['synthesizer', 'reflector'].includes(c)).length <= m, res.results.map(x => x.id + ':' + x.final).join(' ') + ' skipped ' + JSON.stringify(res.skipped)) }
{ const { logs } = await run(engine, 'own', 'standard', { maxAgents: 14 })
  check('critical: a skipped step says what the budget is kept for', logs.some(l => /kept for parts not yet started/.test(l))) }
{ const { res } = await run(engine, 'exhaustive')
  check('critical: a plan that marks nothing treats every scope as critical (behaviour as before)', res.plan.scopes.every(x => x.critical === null)) }
{ const { res, calls } = await run(engine, 'multi', 'deep')
  check('critical: a later layer whose plan marks nothing keeps all of its scopes critical', res.plan.scopes.every(x => x.critical === null) && res.layers.length === 2) }
{ const { res, prompts } = await run(engine, 'own', 'standard', { badOwner: true, planOnly: true })
  check('plan checks: a success item whose owner is not a scope is reported, in the plan and to the plan critic', res.plan.lint.some(l => /S2 .* names an owner that is not a scope: "nobody"/.test(l)) && /Mechanical checks found/.test(prompts['plan-critic:v1'] || ''), JSON.stringify(res.plan.lint))
  const ok = await run(engine, 'own', 'standard', { planOnly: true })
  check('plan checks: a plan with owners, items and a chosen critical set passes them', ok.res.plan.lint.length === 0 && ok.res.cost.critical.join() === 'skel,proof' && ok.res.cost.criticalAgents > 0, JSON.stringify(ok.res.plan.lint))
  check('plan rules: the planner is told about ownership, the skeleton, the early proof and the critical mark', /11\. Ownership\./.test(ok.prompts.planner) && /the skeleton/.test(ok.prompts.planner) && /end-to-end proof/.test(ok.prompts.planner) && /13\. Mark what is critical/.test(ok.prompts.planner)) }
{ const { res, calls } = await run(engine, 'exhaustive', 'standard', { cls: 'test_strength' })
  const c = byId(res, 'c')
  check('bar: a finding of test strength beyond the listed cases never sends the work back, whatever the attacker marks', c.rounds === 1 && c.final === 'verified' && !c.fanout && !calls.includes('solver:c:r2'), `${c.final} r${c.rounds}`)
  const o = await run(engine, 'exhaustive', 'standard', { cls: 'out_of_part' })
  check('bar: a cause outside the scope is recorded for its owner and does not send the work back', byId(o.res, 'c').rounds === 1 && byId(o.res, 'c').boundaryIssues.some(b => b.from === 'check' && b.other.join() === 'd'), JSON.stringify(byId(o.res, 'c').boundaryIssues))
  const b = await run(engine, 'exhaustive', 'standard', { cls: 'behaviour' })
  check('bar: a behaviour finding still blocks', byId(b.res, 'c').rounds > 1) }
{ const { logs, prompts } = await run(engine, 'exhaustive', 'standard', { openContract: true })
  check('contract: the writer is told to use closed thresholds and to name what the scope does not control', /Closed thresholds only/.test(prompts['contract:a'] || '') && /outside_control/.test(prompts['contract:a'] || ''))
  check('contract: a clause over an open set of cases is read as the listed instances, in code', logs.some(l => /a: contract clause\(s\) over an open set of cases \(t1\)/.test(l)) && /Note from the orchestrator: t1 is worded over an open set/.test(prompts['critic:a:r1'] || '') && /Classes of cases this contract samples, not exhausts[^\n]*M1-M4/.test(prompts['solver:a:r1'] || '') && /Outside this scope's control[^\n]*Docker/.test(prompts['critic:a:r1'] || ''))
  { const fs = await import('fs'); const m = fs.readFileSync(engine, 'utf8').match(/const OPEN_SET = (\/.*\/i)\n/); const re = new Function('return ' + m[1])()
    const open = ['every mutant is killed', 'every applicable mutant is killed by the suite', 'any wrong implementation the verifier writes must make the suite raise', 'the check cannot be evaded', 'no input the attacker can construct passes']
    const closed = ['every mutant m01-m20 fails the frozen suite', 'all mutants listed below must fail', 'mutants M1, M2 and M3 are each killed', 'all 12 tests pass', 'every mutant in the contract table is caught', 'all mutants (M1-M6) are killed']
    check('contract: the open-set pattern flags unbounded wording and leaves a named, closed list alone', open.every(x => re.test(x)) && closed.every(x => !re.test(x)), open.filter(x => !re.test(x)).concat(closed.filter(x => re.test(x))).join(' | ')) }
  const plain = await run(engine, 'exhaustive')
  check('contract: an ordinary threshold is not flagged', !plain.logs.some(l => /open set of cases/.test(l)) && !/Note from the orchestrator/.test(plain.prompts['critic:a:r1'] || '')) }
{ const { res, calls, logs } = await run(engine, 'exhaustive', 'standard', { emptySolver: true })
  check('empty hand-back: a solver that returns nothing is not attacked', !calls.includes('critic:c:r1') && calls.includes('solver:c:r2') && calls.includes('critic:c:r2') && logs.some(l => /c r1: the solver returned no claim and no evidence/.test(l)) && !logs.some(l => /ERR/.test(l))) }
{ const minor = await run(engine, 'exhaustive', 'standard', { leftover: 'minor' }), mat = await run(engine, 'exhaustive', 'standard', { leftover: 'material' }), old = await run(engine, 'exhaustive', 'standard', { leftover: 'legacy' })
  check('repair check: a leftover that is not material is a caveat; the result is verified', byId(minor.res, 'a').final === 'verified' && byId(minor.res, 'a').caveats.some(c => /off by one/.test(c)), byId(minor.res, 'a').final)
  check('repair check: a material leftover keeps the result from being verified', byId(mat.res, 'a').final === 'flawed' && byId(mat.res, 'a').repairLeft.material.length === 1)
  check('repair check: a check that gives no split is read the strict way', byId(old.res, 'a').final === 'flawed') }
{ const { res, prompts } = await run(engine, 'exhaustive')
  check('versions: after attempts the synthesizer is told which version is the result', /kept version: round 4 \(fresh\); the other attempts \(repair\) are not the result/.test(prompts.synthesizer || '') && byId(res, 'c').kept.attempt === 'fresh', JSON.stringify(byId(res, 'c').kept))
  const st = await run(engine, 'stop')
  check('versions: an avenue from an attempt that was not kept is labelled so in the atlas', /attempt "repair" \(round \d\), NOT the kept version/.test(st.prompts.synthesizer || '') && /\[worked, kept version\] av5/.test(st.prompts.synthesizer || ''), (st.prompts.synthesizer || '').match(/avenues tried:[\s\S]{0,400}/)?.[0]) }
{ const { res } = await run(engine, 'saturate')
  check('handoff: every open finding is returned in full for the generated list', byId(res, 's').open.some(o => o.blocking && o.issue && o.check) && byId(res, 'n').open.length === 2 && byId(res, 'n').open.every(o => !o.blocking), JSON.stringify(byId(res, 's').open))
  const { prompts } = await run(engine, 'exhaustive', 'standard', { maxAgents: 9 })
  check('handoff: the synthesizer is told a complete list is appended and to give the order of work', /appends below your text a complete list/.test(prompts.synthesizer || '') && /order in which to assemble/.test(prompts.synthesizer || '')) }
{ const plan = await run(engine, 'exhaustive', 'standard', { planOnly: true }), full = await run(engine, 'exhaustive')
  check('estimate: it counts the retries a plan is likely to need (within a third of what the mock run used)', Math.abs(plan.res.cost.estimate.agents - full.calls.length) <= full.calls.length / 3, `${plan.res.cost.estimate.agents} estimated, ${full.calls.length} used`) }
for (const sc of ['own', 'fix', 'stop']) { const a = await run(engine, sc), b = await run(engine, sc)
  check(`resume ${sc}: the same plan builds the same prompts every time`, JSON.stringify(a.prompts) === JSON.stringify(b.prompts) && JSON.stringify(a.calls.slice().sort()) === JSON.stringify(b.calls.slice().sort())) }
// the review pack (run selection, digest, what the user said afterwards, expectations, probe verdict): Python, on made-up runs
{ const { spawnSync } = await import('child_process')
  const r = spawnSync('python3', [path.join(here, 'test_review.py')], { encoding: 'utf8' })
  check('review pack: tests/test_review.py passes', r.status === 0, (r.stderr || '').split('\n').slice(-12).join(' | '))
  const q = spawnSync('python3', [path.join(here, 'test_runner.py')], { encoding: 'utf8' })
  check('standalone runner and Codex adapter: tests/test_runner.py passes', q.status === 0, (q.stderr || '').split('\n').slice(-12).join(' | ')) }
console.log(fails ? `\n${fails} FAILED` : '\nall passed')
process.exit(fails ? 1 : 0)
