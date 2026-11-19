// Mock harness: runs the engine script with scripted agent answers, no model calls.
import fs from 'fs'
export async function run(enginePath, scenario, depth = 'standard', extra = {}) {
  const src = fs.readFileSync(enginePath, 'utf8').replace(/^export const meta/m, 'const meta')

const calls = [], efforts = {}, models = {}, logs = [], prompts = {}, relays = []
const scope = (id, p, deps=[], difficulty='moderate', more={}) => ({ id, title: id, statement: 's', in_scope: 'i', out_of_scope: 'o', success_criterion: 'c', verification_oracles: ['t'], domain_checks: ['d'], debunk_lenses: ['L1'], starting_angle: 'a', depends_on: deps, priority: p, difficulty, ...more })
const canon = v => (v === null || v === undefined ? 'n' : v === true ? 't' : v === false ? 'f' : typeof v === 'number' ? (Number.isInteger(v) ? String(v) : 'r' + Math.floor(v * 1000 + 0.5)) : typeof v === 'string' ? '"' + v + '"' : Array.isArray(v) ? '[' + v.map(canon).join(',') + ']' : '{' + Object.keys(v).filter(k => k !== '_ck').sort().map(k => k + ':' + canon(v[k])).join(',') + '}')
const ck = v => { const t = canon(v); let h = 0x811c9dc5; for (let i = 0; i < t.length; i++) { h ^= t.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0 } return h.toString(16).padStart(8, '0') }
async function agent(prompt, o) {
  const l = o.label; calls.push(l); efforts[l] = o.effort || '-'; models[l] = o.model || '-'
  if (/^You are a RELAY\./.test(prompt)) {   // a non-Claude route: the relay agent starts the external agent and passes its result on
    const spec = JSON.parse(prompt.match(/<<<CRUCIBLE-RELAY-\S+\n(.*)\n---PROMPT---/)[1])
    relays.push({ label: l, provider: spec.provider, model: spec.model, effort: spec.effort, relayModel: o.model, prompt })
    if (extra.relay === 'fail') return { ok: false, error: 'HTTP 402: out of credit' }
    const inner = await answer(prompt.split('---PROMPT---\n')[1], { ...o, schema: spec.schema })
    return { ok: true, result: { ...inner, _ck: extra.relay === 'corrupt' ? '00000000' : ck(inner) } }
  }
  return answer(prompt, o)
}
async function answer(prompt, o) {
  const l = o.label
  if (extra.outageAfter != null && calls.length > extra.outageAfter) { if (extra.outageMsg) throw new Error(extra.outageMsg); return null }
  if (extra.throwOn && new RegExp(extra.throwOn).test(l)) { prompts[l] = prompt; throw new Error('StructuredOutput failed 5 times') }
  const parts = l.replace(/^L\d+:/, '').split(':'); const k = parts[0]; prompts[l] = prompt
  if (k === 'planner') {
    if (scenario === 'saturate') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('s', 1), scope('n', 2)], integration_notes: 'n', shared_data: [], assumptions: [], risks: [] }
    if (scenario === 'continue') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [{ ...scope('a', 1), resume_from_round: 2, contract_path: '/tmp/run/scopes/a/contract.md', prior_state: 'best claim in round-02' }], integration_notes: 'n', shared_data: [], assumptions: [], risks: [], established: [{ id: 'done1', title: 'done one', status: 'verified', claim: 'done claim', claim_path: '/tmp/run/scopes/done1/round-02/claim.md' }] }
    if (scenario === 'resplit') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('x', 1), scope('y', 2)], integration_notes: 'n', assumptions: [], risks: [] }
    if (scenario === 'frontier') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'S', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('deep', 1, [], 'frontier')], integration_notes: 'n', assumptions: [], risks: [] }
    if (scenario === 'sched') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('a', 1, [], 'hard'), scope('lookup', 2, [], 'trivial'), scope('postcheck', 3, ['lookup'], 'trivial')], integration_notes: 'n', shared_data: [], assumptions: [], risks: [] }
    // own: a small build. skel and proof are critical; x1 and x2 are extras that do not converge; proof waits for skel only
    if (scenario === 'own') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's',
      success_items: extra.noItems ? [] : [{ id: 'S1', item: 'the tool runs end to end on a real case', owner: 'proof' }, { id: 'S2', item: 'records are readable by every step', owner: extra.badOwner ? 'nobody' : 'skel' }],
      scopes: [scope('skel', 1, [], 'easy', { owns: ['the record format handed between steps', 'the overall page structure'], critical: true }), scope('x1', 3, [], 'moderate', { owns: ['extra one'], critical: false }), scope('x2', 3, [], 'moderate', { owns: ['extra two'], critical: false }), scope('proof', 1, ['skel'], 'easy', { owns: ['the end-to-end proof'], critical: true })], integration_notes: 'n', shared_data: [], assumptions: [], risks: [] }
    // fix: one moderate part whose repair attempt settles it; stop: one hard part whose fresh attempt survives its first round
    if (scenario === 'fix') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('fix', 1), scope('lookup', 2, [], 'trivial')], integration_notes: 'n', shared_data: [], assumptions: [], risks: [] }
    if (scenario === 'stop') return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('h', 1, [], 'hard'), scope('lookup', 2, [], 'trivial')], integration_notes: 'n', shared_data: [], assumptions: [], risks: [] }
    if (scenario === 'trivial') return { problem_restatement: '1+1', deliverable: 'n', complexity_tier: 'S', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: [scope('sum', 1, [], 'trivial')], integration_notes: 'n', assumptions: [], risks: [] }
    if (scenario === 'multi') { const L2 = l.startsWith('L2:'); return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: 'exhaustive', strategy_rationale: 'r', horizon: 'multi_layer', success_definition: 's', scopes: L2 ? [scope('build', 1, [], 'hard'), scope('check', 2, ['build'], 'easy')] : [scope('research', 1, [], 'moderate'), scope('lookup', 2, [], 'trivial')], integration_notes: 'n', assumptions: [], risks: [] } }
    return { problem_restatement: 'p', deliverable: 'd', complexity_tier: 'M', strategy: scenario === 'staged' ? 'staged' : scenario === 'race' ? 'race' : 'exhaustive', strategy_rationale: 'r', horizon: 'single_pass', success_definition: 's', scopes: scenario === 'staged' ? [scope('a',1), scope('b',2,['a'])] : [scope('a',1,[],'hard'), scope('b',2,[],'hard'), scope('c',3,[],'easy'), scope('d',4)], integration_notes: 'n', shared_data: scenario === 'exhaustive' ? [{ id: 'prices', what: 'SPY daily 2010-2025', used_by: ['a','b'], source_hint: '' }, { id: 'papers', what: 'momentum papers', used_by: ['c'], source_hint: '' }] : [], assumptions: [], risks: [] }
  }
  if (k === 'fetch') return { id: parts[1], summary: parts[1] + ' fetched ok', files: ['/tmp/run/data/' + parts[1] + '/x.csv'], calls: 3, cost_usd: 0.01, gaps: [] }
  if (k === 'plan-critic') return { verdict: 'approve', issues: [] }
  if (k === 'contract') return { pinned_statement: 'p', acceptance_tests: [{ id: 't1', test: 't', threshold: extra.openContract ? 'every wrong implementation the verifier writes from the spec must make the suite raise' : 'x', kind: 'executable' }], ...(extra.openContract ? { open_classes: ['mutants of the parser: M1-M4 must be caught'], outside_control: ['the live run needs Docker: attempted and logged when it is down'] } : {}), negative_tests: ['n'], forbidden_shortcuts: ['f'], ...(extra.emptyFrozen ? { frozen_dir: '/tmp/run/c', frozen_sha256: 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', frozen_files: 0 } : {}) }
  const id = parts[1]
  const sub = (claim, status, extra={}) => ({ status, claim, assertions: ['x is y'], provenance: 'computed', evidence: [{ kind: 'executed', detail: 'd', where: 'w' }], acceptance: [], objection_responses: [], avenues: [], confidence: 0.8, ...extra })
  if (k === 'solver') { const r = +l.match(/:r(\d+)$/)[1]
    if (id === 'sum' || id === 'lookup' || id.endsWith('check')) return sub('2', 'claim')
    if (extra.emptySolver && id === 'c' && r === 1) return { status: 'progress', claim: '', assertions: [], provenance: '', evidence: [], acceptance: [], objection_responses: [], avenues: [], confidence: 0 }
    if (id === 'skel' || id === 'proof') return sub(id + ' claim', 'claim')
    if (id === 'x1' || id === 'x2' || id === 'fix' || id === 'h') return sub(id + ' claim r' + r, 'claim', { avenues: [{ avenue: 'av' + r, outcome: 'worked', why: 'w' }], objection_responses: r > 1 ? [{ id: 'o' + (r - 1), verdict: 'confirmed_fixed', evidence: 'e' }] : [] })
    if (id === 'x') return sub('x depends on y internals', 'blocked', { boundary_issues: [{ kind: 'coupled', other_scopes: ['y'], detail: 'x and y share one state machine' }] })
    if (id === 'b') return sub('nothing works', r >= 2 ? 'exhausted' : 'progress', { avenues: [{ avenue: 'x'+r, outcome: 'failed', why: 'w' }] })
    if (id === 'c') return sub('c claim', 'claim')
    if (id === 's') return sub('s claim r' + r, 'claim', { objection_responses: r > 1 ? [{ id: 'o-r' + (r - 1), verdict: 'confirmed_fixed', evidence: 'e' }] : [] })
    if (id === 'n') return sub('n claim', 'claim', extra.noteCoupling ? { boundary_issues: [{ kind: 'coupled', blocks_correctness: false, other_scopes: ['s'], detail: 'shares a helper' }] } : {})
    return sub(id + ' claim r' + r, r >= 2 ? 'claim' : 'progress', { avenues: [{ avenue: 'av'+r, outcome: 'worked', why: 'w' }] }) }
  const ok = { verdict: 'unrefuted', attack_surfaces: ['A1'], objections: [], checks_run: [{ check: 'c', executed: true, independent_method: true, result: 'r', ...(extra.inspectOnly ? { kind: 'inspected' } : {}) }], integrity_violation: '', exhaustion: { accept: false, untried_avenues: [] } }
  if (k === 'critic' || k === 'critic2') { const r = +l.match(/:r(\d+)$/)[1]
    if (extra.noneText) ok.integrity_violation = 'None found. The implementation addresses the pinned reading and contains no hardcoded answers.'
    if (extra.integrityFlag && id === 'sum') return { ...ok, integrity_ok: false, integrity_violation: 'expected values were edited' }
    if (id === 'sum' || id === 'lookup' || id.endsWith('check')) return ok
    if (id === 'skel' || id === 'proof') return ok
    const open1 = { ...ok, verdict: 'major_issues', objections: [{ id: 'o' + r, severity: 'major', blocks_acceptance: true, class: 'behaviour', issue: 'wrong result ' + r, evidence: 'e', failing_check: 'f' }] }
    if (id === 'x1' || id === 'x2') return open1
    if (id === 'fix') return r >= 3 ? ok : open1
    if (id === 'h') return r === 5 ? ok : open1
    if (extra.cls && id === 'c') return { ...ok, verdict: 'major_issues', objections: [{ id: 'm1', severity: 'major', blocks_acceptance: true, class: extra.cls, owner: 'd', issue: 'one more mutant survives', evidence: 'e', failing_check: 'f' }] }
    if (id === 'x') return { ...ok, verdict: 'major_issues', exhaustion: { accept: true, untried_avenues: [] } }
    if (id === 'b') return { ...ok, verdict: 'refuted', exhaustion: { accept: true, untried_avenues: [] } }
    if (id === 'c') return r >= 4 && !extra.allAttemptsFail ? ok : { ...ok, verdict: 'major_issues', objections: [{ id: 'o1', severity: 'major', issue: 'i', evidence: 'e', failing_check: 'f' }] }
    if (id === 's') return { ...ok, verdict: 'major_issues', objections: [{ id: 'o-r' + r, severity: 'major', blocks_acceptance: true, issue: 'new ground ' + r, evidence: 'e', failing_check: 'f' }] }
    if (id === 'n') return { ...ok, verdict: 'major_issues', objections: [{ id: 'n1', severity: 'major', blocks_acceptance: false, issue: 'incomplete', evidence: 'e', failing_check: 'f' }, { id: 'n2', severity: 'minor', blocks_acceptance: false, issue: 'wording', evidence: 'e', failing_check: 'f' }] }
    if (extra.ungatedFatal && id === 'a') return { ...ok, verdict: 'minor_issues', objections: [{ id: 'f' + r, severity: 'fatal', issue: 'core wrong', evidence: '', failing_check: '' }] }
    return { ...ok, verdict: r === 1 ? 'major_issues' : 'minor_issues', objections: r === 1 ? [{ id: 'o1', severity: 'major', issue: 'i', evidence: 'e', failing_check: 'f' }] : [{ id: 'o2', severity: 'minor', issue: 'i', evidence: 'e', failing_check: 'f' }] } }
  if (k === 'referee') { const ids = [...prompt.matchAll(/^- (\S+) \[(?:fatal|major|minor)\] at /gm)].map(m => m[1])
    return { rulings: extra.referee === 'clear' ? ids.map(i => ({ id: i, ruling: 'rejected', check_executed: true, basis: 'ran it: passes' })) : extra.referee === 'unchecked' ? ids.map(i => ({ id: i, ruling: 'rejected', check_executed: false, basis: 'looks fine' })) : ids.map(i => ({ id: i, ruling: 'upheld', check_executed: true, basis: 'ran it: fails' })), notes: '', ...(extra.referee === 'redesign' ? { repairable: false } : {}) } }
  if (k === 'debunk') return { core_verdict: id === 'd' ? 'core_refuted' : 'core_holds', core_argument: 'arg', fixable_flaws: id === 'a' ? ['typo'] : [], ...(extra.leftover && id === 'a' ? { fixable_flaws: ['typo', 'real flaw'], material_flaws: ['real flaw'] } : {}), checks_run: [], confidence: 0.7 }
  if (k === 'appeal') return { refutation_stands: true, reasoning: 'r', invalid_refutations: [] }
  if (k === 'repair') return sub(id + ' repaired', 'claim')
  if (k === 'repair-check') return extra.leftover === 'minor' ? { repaired: true, core_still_holds: true, remaining_flaws: ['a count is off by one'], remaining_material: [], note: '' }
    : extra.leftover === 'material' ? { repaired: true, core_still_holds: true, remaining_flaws: ['a count is off by one', 'wrong fixes still pass'], remaining_material: ['wrong fixes still pass'], note: '' }
    : extra.leftover === 'legacy' ? { repaired: true, core_still_holds: true, remaining_flaws: ['a count is off by one'], note: '' }
    : { repaired: true, core_still_holds: true, remaining_flaws: [], note: '' }
  if (scenario === 'resplit' && (k.startsWith('completeness'))) return calls.some(c => c.startsWith('solver:xy')) ? { task_satisfied: true, reasoning: 'r', new_scopes: [] } : { task_satisfied: false, reasoning: 'r', new_scopes: [{ ...scope('xy', 1), supersedes: ['x', 'y'] }] }
  if (k.startsWith('race-check') || k.startsWith('completeness')) return { task_satisfied: scenario === 'race' || scenario === 'multi', reasoning: 'r', new_scopes: scenario === 'exhaustive' && !calls.some(c=>c.startsWith('solver:e')) ? [scope('e', 1)] : [] }
  if (k === 'strategist') return { decision: l.endsWith('L1') ? 'next_layer' : 'stop', reasoning: 'r', next_goal: 'build it', carry_forward: 'research done' }
  if (k === 'reflector') return { findings: [{ id: 'f1', category: 'cost', title: 't', evidence: [], impact: 'i', root_cause: 'r', proposed_fix: 'p', touches_protected: false }], checked_clean: [], notes: '' }
  if (k === 'synthesizer' || k === 'final-synthesizer' || k === 'closer') return { headline: 'h', answer: 'a', contradictions: [], confidence: 'medium', human_review_items: [], report_path: 'r', report: 'internal report', success_items: [], handoff: k === 'closer' || /HANDOFF/.test(prompt) ? 'handoff text' : '' }
  throw new Error('unexpected label ' + l)
}
  const parallel = async th => Promise.all(th.map(t => t().catch(e => { logs.push('THUNK ERR ' + e); return null })))
  const pipeline = async (items, ...stages) => Promise.all(items.map(async (it, i) => { let v = it; try { for (const s of stages) v = await s(v, it, i); return v } catch (e) { logs.push('STAGE ERR ' + e); return null } }))
  const fn = new Function('args', 'budget', 'agent', 'parallel', 'pipeline', 'phase', 'log', `return (async () => { ${src} })()`)
  const res = await fn({ runDir: '/tmp/run', problem: 'p', depth, ...extra }, { total: null, spent: () => 0, remaining: () => Infinity }, agent, parallel, pipeline, () => {}, m => logs.push(m))
  return { res, calls, efforts, models, logs, prompts, relays }
}
