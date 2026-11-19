#!/usr/bin/env node
// crucible-runner.mjs: run a crucible workflow script (engine/crucible-engine.js, engine/crucible-evolve.js) outside
// Claude Code's Workflow tool. The script is the same file; this runner supplies what the Workflow tool supplies:
// agent(), parallel(), pipeline(), phase(), log(), a cap on agents alive at once, and a cache so a relaunch of the same
// run replays every finished agent. Each agent is one headless CLI call (`codex exec`, `claude -p`, or an OpenRouter
// model) made through scripts/crucible_agent.py, which returns JSON checked against the agent's reply format.
//
//   node crucible-runner.mjs --args <args.json> [--engine <script.js>] [--provider codex|claude|openrouter] [--jobs 4]
//                            [--timeout 7200] [--retries 1] [--cwd <dir>] [--state <dir>] [--detach]
//   node crucible-runner.mjs --status <runDir | state dir>      is it running, how far is it, where is the result
//   node crucible-runner.mjs --stop <runDir | state dir>        stop it; finished agents are kept for a relaunch
//
//   args.json   the args object the script takes (for the engine: runDir, problem, context, depth, routing, planOnly, ...)
//   state       default <runDir>/.runner (for the evolve script: <historyPack>/.runner). It holds journal.jsonl (what every
//               agent returned; also the replay cache), agent-<id>.jsonl (time and tokens), prompts/, progress.log, and
//               output.json when the script returns. `crucible_run.py save <state>/output.json <runDir> --transcript <state>`
//               reads it exactly as it reads a Workflow run.
// No dependency beyond Node 18+ and Python 3.9+.
import fs from 'fs'
import path from 'path'
import crypto from 'crypto'
import { spawn } from 'child_process'
import { fileURLToPath } from 'url'

const HERE = path.dirname(fileURLToPath(import.meta.url))
const AGENT = path.join(HERE, '..', 'scripts', 'crucible_agent.py')
// tests replace the agent command with a stand-in: CRUCIBLE_AGENT_CMD='["python3","/path/stub.py"]'
const AGENT_CMD = process.env.CRUCIBLE_AGENT_CMD ? JSON.parse(process.env.CRUCIBLE_AGENT_CMD) : ['python3', AGENT]
const argv = process.argv.slice(2)
const opt = (name, dflt) => { const i = argv.indexOf(name); return i >= 0 && i + 1 < argv.length ? argv[i + 1] : dflt }
const has = name => argv.includes(name)
const stateOf = p => { const d = path.resolve(p); return path.basename(d) === '.runner' || fs.existsSync(path.join(d, 'journal.jsonl')) ? d : path.join(d, '.runner') }
const alive = pid => { try { process.kill(pid, 0); return true } catch { return false } }
const readPid = st => { try { return Number(fs.readFileSync(path.join(st, 'runner.pid'), 'utf8').trim()) || null } catch { return null } }
const jsonl = f => fs.existsSync(f) ? fs.readFileSync(f, 'utf8').split('\n').filter(Boolean).map(l => { try { return JSON.parse(l) } catch { return null } }).filter(Boolean) : []

if (has('--status') || has('--stop')) {
  const st = stateOf(opt(has('--status') ? '--status' : '--stop'))
  const pid = readPid(st), running = !!pid && alive(pid)
  if (has('--stop')) {
    if (running) process.kill(pid, 'SIGTERM')
    console.log(JSON.stringify({ state: st, stopped: running, note: running ? 'stopping: agents that were mid-flight are lost, finished ones are kept' : 'no runner is running for this run' }))
    process.exit(0)
  }
  const j = jsonl(path.join(st, 'journal.jsonl'))
  const started = j.filter(e => e.type === 'started'), done = j.filter(e => e.type === 'result')
  const open = new Set(started.map(e => e.agentId)); done.forEach(e => open.delete(e.agentId))
  const log = fs.existsSync(path.join(st, 'progress.log')) ? fs.readFileSync(path.join(st, 'progress.log'), 'utf8').trim().split('\n') : []
  const out = path.join(st, 'output.json')
  const finished = fs.existsSync(out) && (!pid || !running)
  console.log(JSON.stringify({ state: st, running, finished, output: finished ? out : null, agents: { started: started.length, returned: done.filter(e => e.result !== null).length, failed: done.filter(e => e.result === null).length, alive: running ? started.filter(e => open.has(e.agentId)).map(e => e.label) : [] },
    last: log.slice(-8), note: finished ? 'finished: save it with crucible_run.py save <output> <runDir> --transcript <state>' : running ? 'still running' : (started.length ? 'not running and not finished: it was stopped or it failed (see runner.log); relaunch with the same args to continue from the finished agents' : 'not started') }, null, 1))
  process.exit(0)
}

const argsFile = opt('--args')
if (!argsFile) { console.error('usage: crucible-runner.mjs --args <args.json> [--engine <script.js>] [--provider codex|claude|openrouter] [--jobs 4] [--detach]   |   --status <runDir>   |   --stop <runDir>'); process.exit(2) }
const ARGS = JSON.parse(fs.readFileSync(argsFile, 'utf8'))
const ENGINE = path.resolve(opt('--engine', path.join(HERE, '..', 'engine', 'crucible-engine.js')))
const PROVIDER = opt('--provider', 'claude')
const JOBS = Math.max(1, Number(opt('--jobs', 4)))
const TIMEOUT = Number(opt('--timeout', 7200))
const RETRIES = Number(opt('--retries', 1))
const CWD = path.resolve(opt('--cwd', process.cwd()))
const STATE = path.resolve(opt('--state', path.join(ARGS.runDir || ARGS.historyPack || '.', '.runner')))
fs.mkdirSync(path.join(STATE, 'prompts'), { recursive: true })

if (has('--detach')) {   // start the same command in the background and return at once
  const old = readPid(STATE)
  if (old && alive(old)) { console.log(JSON.stringify({ error: `a runner is already running for this run (pid ${old}); stop it first with --stop` })); process.exit(1) }
  const logFd = fs.openSync(path.join(STATE, 'runner.log'), 'a')
  const child = spawn(process.execPath, [fileURLToPath(import.meta.url), ...argv.filter(a => a !== '--detach')], { detached: true, stdio: ['ignore', logFd, logFd], cwd: CWD })
  child.unref()
  console.log(JSON.stringify({ started: true, pid: child.pid, state: STATE, log: path.join(STATE, 'runner.log'), status: `node ${fileURLToPath(import.meta.url)} --status ${STATE}` }))
  process.exit(0)
}

fs.writeFileSync(path.join(STATE, 'runner.pid'), String(process.pid))
try { fs.rmSync(path.join(STATE, 'output.json'), { force: true }) } catch {}
const JOURNAL = path.join(STATE, 'journal.jsonl')
const journal = e => fs.appendFileSync(JOURNAL, JSON.stringify(e) + '\n')
const progress = m => { const line = `${new Date().toISOString().slice(0, 19)}Z ${m}`; fs.appendFileSync(path.join(STATE, 'progress.log'), line + '\n'); console.error(line) }

// replay cache: an agent whose prompt and options are unchanged since an earlier launch returns what it returned then
const sha = s => crypto.createHash('sha256').update(s).digest('hex')
const stable = v => Array.isArray(v) ? `[${v.map(stable).join(',')}]` : v && typeof v === 'object' ? `{${Object.keys(v).sort().map(k => JSON.stringify(k) + ':' + stable(v[k])).join(',')}}` : JSON.stringify(v === undefined ? null : v)
const cache = new Map()
{ const labelOf = {}
  for (const e of jsonl(JOURNAL)) {
    if (e.type === 'started') labelOf[e.agentId] = e
    if (e.type === 'result' && e.result !== null && e.result !== undefined && e.key) cache.set(e.key, e.result) } }
let seq = jsonl(JOURNAL).filter(e => e.type === 'started').length, live = 0, replayed = 0, ran = 0, failed = 0, PHASE = ''
const waiting = []
const acquire = () => live < JOBS ? (live++, Promise.resolve()) : new Promise(r => waiting.push(r))
const release = () => { const next = waiting.shift(); if (next) next(); else live-- }
const children = new Set()

function runOnce(id, o, promptFile, schemaFile) {
  return new Promise(resolve => {
    const out = path.join(STATE, 'prompts', `${id}.out.json`)
    const a = [...AGENT_CMD.slice(1), 'run', '--provider', PROVIDER, '--prompt-file', promptFile, '--cwd', CWD, '--timeout', String(TIMEOUT), '--out', out]
    if (o.model) a.push('--model', o.model)
    if (o.effort) a.push('--effort', o.effort)
    if (schemaFile) a.push('--schema-file', schemaFile)
    const c = spawn(AGENT_CMD[0], a, { stdio: ['ignore', 'ignore', 'pipe'], cwd: CWD })
    children.add(c)
    let err = ''
    c.stderr.on('data', d => { err = (err + d).slice(-2000) })
    c.on('close', () => { children.delete(c)
      let r = null
      try { r = JSON.parse(fs.readFileSync(out, 'utf8')) } catch {}
      resolve(r || { ok: false, kind: 'provider', error: `the agent process returned nothing${err ? ': ' + err.replace(/\s+/g, ' ').slice(-300) : ''}` }) })
    c.on('error', e => { children.delete(c); resolve({ ok: false, kind: 'setup', error: String(e.message || e) }) })
  })
}

async function agent(prompt, o = {}) {
  const key = sha(prompt + '\0' + stable(o))
  if (cache.has(key)) { replayed++; return JSON.parse(JSON.stringify(cache.get(key))) }
  await acquire()
  try {
    const id = `r${String(++seq).padStart(4, '0')}-${key.slice(0, 8)}`
    const label = o.label || id
    journal({ type: 'started', key, agentId: id, label, phase: o.phase || PHASE })
    const promptFile = path.join(STATE, 'prompts', `${id}.txt`)
    fs.writeFileSync(promptFile, prompt)
    let schemaFile = null
    if (o.schema) { schemaFile = path.join(STATE, 'prompts', `${id}.schema.json`); fs.writeFileSync(schemaFile, JSON.stringify(o.schema)) }
    const t0 = new Date()
    let r = null, tries = 0, usage = { in: 0, out: 0 }
    do {
      r = await runOnce(id, o, promptFile, schemaFile); tries++
      if (r.usage) { usage.in += r.usage.in || 0; usage.out += r.usage.out || 0 }
    } while (!r.ok && (r.kind === 'schema' || r.kind === 'provider') && tries <= RETRIES)
    // time and tokens, in the shape crucible_run.py reads from a Claude Code agent transcript. The token counts are totals
    // over the agent's whole session ("aggregate"), so they say nothing about the largest context it carried.
    fs.writeFileSync(path.join(STATE, `agent-${id}.jsonl`), JSON.stringify({ type: 'user', timestamp: t0.toISOString() }) + '\n'
      + JSON.stringify({ type: 'assistant', timestamp: new Date().toISOString(), aggregate: true, message: { id, model: r.model || o.model || PROVIDER, content: [], usage: { input_tokens: usage.in, output_tokens: usage.out } } }) + '\n')
    if (!r.ok) {
      failed++
      journal({ type: 'result', key, agentId: id, result: null, error: String(r.error || '').slice(0, 600), kind: r.kind })
      progress(`${label}: failed (${r.kind}): ${String(r.error || '').replace(/\s+/g, ' ').slice(0, 200)}`)
      throw new Error(String(r.error || 'agent failed'))     // the engine reads the message: a usage limit pauses the run
    }
    let result = r.result
    if (result && typeof result === 'object') { result = { ...result }; delete result._ck }
    journal({ type: 'result', key, agentId: id, result })
    cache.set(key, result); ran++
    progress(`${label}: returned in ${Math.round((Date.now() - t0) / 1000)} s`)
    return result
  } finally { release() }
}
const parallel = async thunks => Promise.all(thunks.map(t => Promise.resolve().then(t).catch(() => null)))
const pipeline = async (items, ...stages) => Promise.all(items.map(async (it, i) => { let v = it; try { for (const s of stages) v = await s(v, it, i); return v } catch { return null } }))
const phase = title => { PHASE = title; progress(`== ${title}`) }
const log = m => progress(String(m))
const budget = { total: null, spent: () => 0, remaining: () => Infinity }
const workflow = async () => { throw new Error('workflow() is not available in the standalone runner') }

let stopping = false
for (const sig of ['SIGTERM', 'SIGINT']) process.on(sig, () => { if (stopping) return; stopping = true
  progress(`stopped (${sig}): ${children.size} agent(s) were mid-flight and are lost; finished ones are kept`)
  for (const c of children) { try { c.kill('SIGTERM') } catch {} }
  try { fs.rmSync(path.join(STATE, 'runner.pid'), { force: true }) } catch {}
  process.exit(130) })

const src = fs.readFileSync(ENGINE, 'utf8').replace(/^export const meta/m, 'const meta')
const fn = new Function('args', 'budget', 'agent', 'parallel', 'pipeline', 'phase', 'log', 'workflow', `return (async () => { ${src}\n })()`)
progress(`runner: ${path.basename(ENGINE)} with ${PROVIDER} agents, up to ${JOBS} at once; ${cache.size} finished agent(s) from earlier launches can be replayed`)
let result, error = null
try { result = await fn(ARGS, budget, agent, parallel, pipeline, phase, log, workflow) } catch (e) { error = String((e && e.stack) || e) }
try { fs.rmSync(path.join(STATE, 'runner.pid'), { force: true }) } catch {}
if (error) { progress(`the script failed: ${error.split('\n')[0]}`); console.error(error); process.exit(1) }
const OUT = path.join(STATE, 'output.json')
fs.writeFileSync(OUT, JSON.stringify({ result, transcriptDir: STATE }))
progress(`finished: ${ran} agent(s) ran, ${replayed} replayed, ${failed} failed; result in ${OUT}`)
console.log(JSON.stringify({ output: OUT, state: STATE, ran, replayed, failed }))
process.exit(0)
