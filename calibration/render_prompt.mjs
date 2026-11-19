// render_prompt.mjs: print the prompt and schema the engine itself would send for one agent.
//
//   node render_prompt.mjs <engine.js> <spec.json>      -> {"prompt": ..., "schema": ..., "model": ..., "effort": ...}
//
// spec: { label, runDir, problem, depth?, plan, contract?, submission?, critic? }
//   label       the agent whose prompt is wanted: planner | plan-critic:v1 | contract:<id> | solver:<id>:r1 | critic:<id>:r1 | referee:<id>
//   plan        the plan the run works on (for label "planner" it is only what the stub planner answers)
//   contract    what the contract writer "returned"; submission: what every solver "returned"; critic: what every attacker "returned"
// The engine runs with scripted answers and no model call, exactly as in tests/mock.mjs, so a calibration probe tests
// the prompt a real run would send, not a copy of it.
import fs from 'fs'

const [enginePath, specPath] = process.argv.slice(2)
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'))
const src = fs.readFileSync(enginePath, 'utf8').replace(/^export const meta/m, 'const meta')
const seen = {}
const OK = { verdict: 'unrefuted', attack_surfaces: ['A1'], objections: [], checks_run: [{ check: 'c', kind: 'ran', executed: true, independent_method: true, result: 'r' }], integrity_ok: true, integrity_violation: '', exhaustion: { accept: false, untried_avenues: [] } }
async function agent(prompt, o) {
  seen[o.label] = { prompt, schema: o.schema, model: o.model || null, effort: o.effort || null }
  const k = o.label.replace(/^L\d+:/, '').split(':')[0]
  if (k === 'planner') return spec.plan
  if (k === 'plan-critic') return { verdict: 'approve', issues: [] }
  if (k === 'contract') return spec.contract || { pinned_statement: 'p', acceptance_tests: [], negative_tests: [], forbidden_shortcuts: [], frozen_dir: '', frozen_sha256: '' }
  if (k === 'solver' || k === 'repair') return spec.submission || { status: 'claim', claim: 'c', assertions: ['a'], provenance: 'p', evidence: [{ kind: 'executed', detail: 'd', where: 'w' }], acceptance: [], objection_responses: [], avenues: [], confidence: 0.8 }
  if (k === 'critic' || k === 'critic2') return spec.critic || OK
  if (k === 'referee') return { rulings: [], notes: '' }
  if (k === 'debunk') return { core_verdict: 'core_holds', core_argument: 'a', fixable_flaws: [], checks_run: [], confidence: 0.5 }
  if (k === 'repair-check') return { repaired: true, core_still_holds: true, remaining_flaws: [], note: '' }
  if (k === 'completeness' || k === 'race-check') return { task_satisfied: true, reasoning: 'r', new_scopes: [] }
  if (k === 'reflector') return { findings: [], checked_clean: [], notes: '' }
  if (k === 'fetch') return { id: 'x', summary: 's', files: [], calls: 0, cost_usd: 0, gaps: [] }
  return { solved: 'yes', user_answer: 'a', headline: 'h', answer: 'a', contradictions: [], confidence: 'medium', human_review_items: [], report_path: 'r', report: 'r', handoff: '' }
}
const parallel = async th => Promise.all(th.map(t => t().catch(() => null)))
const pipeline = async (items, ...stages) => Promise.all(items.map(async (it, i) => { let v = it; try { for (const s of stages) v = await s(v, it, i); return v } catch (e) { return null } }))
const fn = new Function('args', 'budget', 'agent', 'parallel', 'pipeline', 'phase', 'log', `return (async () => { ${src} })()`)
const args = { runDir: spec.runDir, problem: spec.problem, depth: spec.depth || 'standard', noReflect: true, ...(spec.label === 'planner' || spec.label.startsWith('plan-critic') ? {} : { plan: spec.plan }), ...(spec.args || {}) }
await fn(args, { total: null, spent: () => 0, remaining: () => Infinity }, agent, parallel, pipeline, () => {}, () => {})
if (!seen[spec.label]) { console.error(`the engine never called ${spec.label}; it called: ${Object.keys(seen).join(' ')}`); process.exit(1) }
process.stdout.write(JSON.stringify(seen[spec.label]))
