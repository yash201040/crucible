#!/usr/bin/env python3
"""build_model_map.py: merge what is known about each model into references/model-map.json.

  python3 build_model_map.py <research-dir> <openrouter-models.json> <calibration-dir> [<calibration-dir> ...]

Inputs: the two research files of 2026-11-15 (B1 coding/agentic/review benchmarks, B2 intelligence/speed/price), a dump of
https://openrouter.ai/api/v1/models (prices, context), and calibration result folders. Numbers are copied, never filled
in: a missing value stays null, and every benchmark score keeps its source and source type.
"""
import json, re, sys, time
from pathlib import Path

research, or_file, cal_dirs = Path(sys.argv[1]), Path(sys.argv[2]), [Path(x) for x in sys.argv[3:]]
b1 = json.loads((research / "B1-coding-agentic-benchmarks.json").read_text())
b2 = json.loads((research / "B2-intelligence-speed-price.json").read_text())
orm = {m["id"]: m for m in json.loads(or_file.read_text())["data"]}

# name in the research files -> (OpenRouter id, Claude Code alias, Codex CLI id)
IDS = {
    "Claude Fable 5.2": ("anthropic/claude-fable-5.2", "fable", None), "Claude Opus 5.5": ("anthropic/claude-opus-5.5", "opus", None),
    "Claude Sonnet 5.5": ("anthropic/claude-sonnet-5.5", "sonnet", None), "Claude Haiku 5.5": ("anthropic/claude-haiku-5.5", "haiku", None),
    "Gemini 4 Carbon": ("google/gemini-4-carbon", None, None), "Gemini 4 Argon": ("google/gemini-4-argon", None, None), "Gemini 4 Hydrogen": ("google/gemini-4-hydrogen", None, None),
    "GPT-6.1 Sol": ("openai/gpt-6.1-sol", None, "gpt-6.1-sol"), "GPT-6.1 Terra": ("openai/gpt-6.1-terra", None, "gpt-6.1-terra"),
    "GPT-6 Astra": (None, None, "gpt-6-astra"), "GPT-6 Luna": (None, None, "gpt-6-luna"),
    "Kimi K3.1 Pro": ("moonshotai/kimi-k3.1-pro", None, None), "DeepSeek V4.1 Flash": ("deepseek/deepseek-v4.1-flash-1017", None, None),
    "Muse Ember": ("meta/muse-ember", None, None), "Muse Wonder": ("meta/muse-wonder", None, None), "Muse Spark Open": ("meta/muse-spark-open", None, None),
    "Inkling 2 Small": ("thinkingmachines/inkling-2-small", None, None), "MiniMax M3.1 Flash": ("minimax/minimax-m3.1-flash", None, None),
    "Mistral Large 4": ("mistralai/mistral-large-4-0", None, None), "Tencent HY4": ("tencent/hy4", None, None),
}
norm = lambda n: re.sub(r"[^a-z0-9.]+", "", re.sub(r"\s*(1017|0902|0813|1\.0 / full|/ full)\s*$", "", n.lower()).replace("minimax-", "minimax ").replace("-flash", " flash"))
key_of = {norm(k): k for k in IDS}

# what each model is fit for in crucible: my reading of the evidence below it (sources in the scores and in the notes file)
FIT = {
    "Claude Opus 5.5": "Planner, plan critic, completeness, strategist, synthesizer, referee; solver and attacker of hard and frontier parts. Strongest reviewer measured (Macroscope 83.9 at max effort; Qodo F1 56.8). At low effort it is below Sonnet at high (AA index 35 vs 42): do not use opus@low.",
    "Claude Sonnet 5.5": "Solver and attacker of trivial, easy and moderate parts; reflector; data fetcher. Close to Opus on agentic coding (Terminal-Bench 4.1 63.9 vs 65.8) at half the price and 1.4x the speed. In calibration: fastest of all at low and medium effort, every probe passed.",
    "Claude Haiku 5.5": "Relay agent; solver of trivial and easy parts in the economy profile. Weak on long agentic work (Terminal-Bench 4.0 39.2, vendor) and it over-flags as a fact checker (30 correct sentences flagged where Opus flagged 0, one test): never the attacker. In calibration at high effort it passed every probe but wrote about 5x the output of Sonnet and was slower.",
    "Claude Fable 5.2": "Strongest model (AA 64.6), on its own subscription meter (up to half the weekly limit on Max, then paid credits) and at twice Opus's API price. Not in any default route: use the session profile for a run that should have it everywhere.",
    "Gemini 4 Carbon": "Another family at Opus's level (AA 60.0 vs 59.1), but at high effort through OpenRouter one small review took 7.5 minutes and $0.33 (calibration, one run): too slow and dear for a routine second check. Untested at lower effort.",
    "Gemini 4 Hydrogen": "Second attacker for moderate parts in the mixed profile: another family at Sonnet's level (AA 53.9); 9 of 9 review probes right in calibration, including accepting the correct submission that tempts a reviewer to invent a stricter bar. About 40 s and $0.07 a check through OpenRouter (Sonnet: 12-18 s).",
    "GPT-6.1 Terra": "Not as an attacker here. Strong on a vendor code-review benchmark (Macroscope 82.3), but in calibration it rejected a correct submission at medium and at high effort with three to four invented blocking findings (4300-digit integers, Unicode digits, str subclasses): a reviewer that raises the bar past the contract is what makes parts loop. Fine as a solver on the probes.",
    "GPT-6.1 Sol": "Codex subscription route for solver and attacker of moderate and hard parts once the Codex CLI is installed (Terminal-Bench 4.1 60.9; $1.51 a task on AA's coding index against $44 for Fable at max).",
    "Kimi K3.1 Pro": "Not as an attacker: highest recall in one review benchmark (68.6%) with 49% precision, which means false findings and extra rounds. Possible cheap solver; its headline scores are the vendor's own.",
    "DeepSeek V4.1 Flash": "Cheapest model that passed every calibration probe ($0.04 for nine); slow per call through OpenRouter and at Haiku's level on general benchmarks (AA 32.6). A candidate for mechanical roles, not for judging.",
    "Muse Ember": "Fastest small model (736 tokens/s; 16 s a review probe) at Haiku's level (AA 36.0). A candidate for mechanical roles.",
    "GLM-5.3": "Uneven: 84.3 on one SWE-bench Pro board, 41.2 on Terminal-Bench 4.1. Not routed.",
}


def find(name):
    return key_of.get(norm(name))   # exact names only: "Claude Opus 5" is not "Claude Opus 5.5"


models = {}
for m in b2["models"]:
    e = models.setdefault(m["name"], {"name": m["name"], "vendor": m.get("vendor"), "tier": m.get("tier"), "scores": {}})
    sp = m.get("speed") or {}
    e["speed_tokens_per_s"] = sp.get("tokens_per_s")
    for b, v in (m.get("scores") or {}).items():
        e["scores"][b] = {k: v.get(k) for k in ("score", "unit", "setting", "source", "source_type", "date") if v.get(k) not in (None, "")}
for m in b1["models"]:
    name = next((n for n in models if norm(n) == norm(m["name"])), m["name"])
    e = models.setdefault(name, {"name": name, "vendor": m.get("vendor"), "tier": m.get("tier"), "scores": {}})
    for b, v in (m.get("scores") or {}).items():
        e["scores"][b] = {k: v.get(k) for k in ("score", "unit", "setting", "cost_per_task_usd", "source", "source_type", "date") if v.get(k) not in (None, "")}
    if m.get("notes"):
        e["notes"] = m["notes"]

cal = {}
for d in cal_dirs:
    f = d / "summary.json"
    if f.exists():
        for cfg, s in json.loads(f.read_text()).items():
            cal.setdefault(cfg, {})[d.name] = {k: s[k] for k in ("runs", "failed_runs", "critic_flaws_caught", "critic_clean_accepted", "critic_false_blocking", "solver_correct", "solver_false_claims", "mean_seconds", "cost_usd") if k in s}

out = []
for name, e in models.items():
    k = find(name)
    oid, alias, codex = IDS.get(k, (None, None, None)) if k else (None, None, None)
    o = orm.get(oid) if oid else None
    pr = (o or {}).get("pricing") or {}
    price = lambda x: round(float(x) * 1e6, 3) if x not in (None, "") and float(x) >= 0 else None
    row = {"name": name, "vendor": e.get("vendor"), "tier": e.get("tier"),
           "ids": {"claude_code": alias, "openrouter": oid if o else None, "codex_cli": codex},
           "price_usd_per_mtok": {"in": price(pr.get("prompt")), "out": price(pr.get("completion")), "source": "openrouter.ai/api/v1/models, 2026-11-15"} if o else None,
           "context_tokens": (o or {}).get("context_length"), "speed_tokens_per_s": e.get("speed_tokens_per_s"),
           "fit": FIT.get(k), "scores": e["scores"]}
    routes = {c: v for c, v in cal.items() if (alias and re.match(rf"^claude:{alias}@", c)) or (oid and c.startswith(f"openrouter:{oid}@"))}
    if routes:
        row["calibration"] = routes
    if e.get("notes"):
        row["notes"] = e["notes"]
    out.append(row)
rank = {"frontier": 0, "mid": 1, "fast": 2}
aa = lambda r: -(r["scores"].get("AA_Intelligence_Index", {}).get("score") or 0)
out.sort(key=lambda r: (0 if r["fit"] else 1, rank.get(r["tier"], 3), aa(r)))
doc = {
    "as_of": time.strftime("%Y-%m-%d"),
    "about": "What is known about each model that crucible could route a role to: ids per provider, price, speed, benchmark scores with their sources, the result of crucible's own calibration probes, and `fit`: the role it suits here. routing.json is the table the engine uses; this file is the evidence behind it. Regenerate with calibration/build_model_map.py after new research or a calibration.",
    "caveats": [
        "Most benchmark numbers are vendor-reported or come from aggregators (see each score's source_type); compare models only within one benchmark and one scaffold.",
        "The Artificial Analysis index and speed figures were read through an aggregator page; effort labels on that page were partly inferred.",
        "Anthropic does not publish how much of a subscription limit each model draws. The weights in routing.json follow API prices, which is a guess.",
        "Calibration probes are a floor test (12 small tasks): every model passed nearly all of them, so they show speed, cost and robustness, not which strong model is better.",
    ],
    "system_one_models": b2.get("system_one_models"),
    "subscription_economics": b2.get("subscription_economics"),
    "benchmarks": {**b2.get("benchmarks", {}), **b1.get("benchmarks", {})},
    "models": out,
}
dst = Path(__file__).resolve().parent.parent / "references" / "model-map.json"
dst.write_text(json.dumps(doc, indent=1, ensure_ascii=False))
print(f"{dst}: {len(out)} models, {sum(1 for r in out if r['fit'])} with a role fit, {sum(1 for r in out if r.get('calibration'))} calibrated, {sum(1 for r in out if r['ids']['openrouter'])} with an OpenRouter id")
