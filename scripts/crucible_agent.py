#!/usr/bin/env python3
"""crucible_agent.py: run ONE agent on any provider and return JSON that matches a schema.

Providers
  claude      Claude Code headless (`claude -p`), on the Claude subscription login
  codex       Codex CLI headless (`codex exec`), on the ChatGPT login            (written from the Codex CLI's documented flags and
              checked against a stand-in binary in tests/test_runner.py; not yet run against the real CLI)
  openrouter  any OpenRouter model, through the small tool loop in this file (read_file, write_file, run_bash)

Commands
  run    --provider P [--model M] [--effort E] --prompt-file F [--schema-file S] [--cwd D] [--timeout SEC]
         [--max-turns N] [--lean] [--no-tools] [--out FILE]        run one agent, print one JSON line
  relay  --marker TAG [--session ID] [--wait SEC]                  used by a relay agent inside a crucible run: finds the
         spec and prompt that the engine put in the relay agent's own transcript, runs the agent detached, waits
  wait   --job DIR [--wait SEC]                                     keep waiting for a relay job
  check                                                             which providers can be used here (no secrets printed)
  ck     --file F                                                   checksum of a JSON file (same function as the engine)

The OpenRouter key is read from $OPENROUTER_API_KEY, else from the file named in ~/.crucible/providers.json
({"openrouter": {"key_file": "/path/to/env", "key_var": "OPENROUTER_API_KEY"}}). It is never printed, logged or
passed to a tool: shell commands the model runs get a scrubbed environment and cannot read the key file. More paths
those commands must never read go in the same file: {"secret_paths": ["/path", "~/path"]}.
"""
import json, math, os, re, shutil, subprocess, sys, tempfile, time, urllib.error, urllib.request
from pathlib import Path

HOME = Path.home()
PROVIDERS_FILE = HOME / ".crucible" / "providers.json"
OR_URL = "https://openrouter.ai/api/v1/chat/completions"
EFFORTS = ("low", "medium", "high", "xhigh")


# ───────────────────────── JSON helpers (shared contract with the engine) ─────────────────────────
def _canon(v) -> str:
    """Canonical text of a JSON value. The engine has the same function in JavaScript (canon): keep them equal."""
    if v is None:
        return "n"
    if v is True:
        return "t"
    if v is False:
        return "f"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):   # same arithmetic as the engine: whole numbers as integers, others to three decimals
        return str(int(v)) if v == int(v) else "r" + str(math.floor(v * 1000 + 0.5))
    if isinstance(v, str):
        return '"' + v + '"'
    if isinstance(v, list):
        return "[" + ",".join(_canon(x) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ",".join(k + ":" + _canon(v[k]) for k in sorted(v) if k != "_ck") + "}"
    return "?"


def checksum(v) -> str:
    """FNV-1a (32 bit) over the UTF-16 code units of the canonical text: detects a relay that altered the result."""
    h = 0x811C9DC5
    b = _canon(v).encode("utf-16-le", "surrogatepass")
    for i in range(0, len(b), 2):
        h ^= b[i] | (b[i + 1] << 8)
        h = (h * 16777619) & 0xFFFFFFFF
    return format(h, "08x")


def extract_json(text: str):
    """The JSON object in a model reply: the whole text, a fenced block, or the first balanced {...}."""
    if isinstance(text, (dict, list)):
        return text
    t = (text or "").strip()
    for cand in [t] + re.findall(r"```(?:json)?\s*(.*?)```", t, re.S):
        try:
            return json.loads(cand)
        except Exception:
            pass
    start = t.find("{")
    while start >= 0:
        depth, instr, esc = 0, False, False
        for i in range(start, len(t)):
            c = t[i]
            if instr:
                esc = (c == "\\") and not esc
                if c == '"' and not esc:
                    instr = False
                if c != "\\":
                    esc = False
                continue
            if c == '"':
                instr = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(t[start:i + 1])
                    except Exception:
                        break
        start = t.find("{", start + 1)
    return None


def validate(v, s, path="$") -> list:
    """Errors of value v against JSON schema s (the subset crucible uses: type, properties, required, enum, items,
    minimum, maximum, minItems)."""
    errs = []
    if not isinstance(s, dict):
        return errs
    t = s.get("type")
    ok = {"object": isinstance(v, dict), "array": isinstance(v, list), "string": isinstance(v, str), "boolean": isinstance(v, bool),
          "integer": isinstance(v, int) and not isinstance(v, bool), "number": isinstance(v, (int, float)) and not isinstance(v, bool)}.get(t, True)
    if not ok:
        return [f"{path}: expected {t}, got {type(v).__name__}"]
    if "enum" in s and v not in s["enum"]:
        errs.append(f"{path}: {v!r} is not one of {s['enum']}")
    if t in ("number", "integer"):
        if "minimum" in s and v < s["minimum"]:
            errs.append(f"{path}: below minimum {s['minimum']}")
        if "maximum" in s and v > s["maximum"]:
            errs.append(f"{path}: above maximum {s['maximum']}")
    if t == "object":
        for k in s.get("required", []):
            if k not in v:
                errs.append(f"{path}.{k}: required field missing")
        for k, sub in (s.get("properties") or {}).items():
            if k in v:
                errs += validate(v[k], sub, f"{path}.{k}")
    if t == "array":
        if len(v) < s.get("minItems", 0):
            errs.append(f"{path}: needs at least {s['minItems']} item(s)")
        for i, x in enumerate(v):
            errs += validate(x, s.get("items") or {}, f"{path}[{i}]")
    return errs[:20]


def schema_hint(schema) -> str:
    return ("\n\nFINAL ANSWER FORMAT: when the work is done, reply with ONE JSON object and nothing else (no prose, no code fence). "
            "It must match this JSON Schema exactly (all required fields, exact enum values):\n" + json.dumps(schema))


# ───────────────────────── secrets ─────────────────────────
def _key_file():
    try:
        cfg = json.loads(PROVIDERS_FILE.read_text()).get("openrouter", {})
        return cfg.get("key_file"), cfg.get("key_var", "OPENROUTER_API_KEY")
    except Exception:
        return None, "OPENROUTER_API_KEY"


def openrouter_key():
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        return k.strip()
    f, var = _key_file()
    if f and Path(f).is_file():
        for line in Path(f).read_text(errors="replace").splitlines():
            m = re.match(rf"^\s*(?:export\s+)?{re.escape(var)}\s*=\s*(.*)$", line)
            if m:
                return m.group(1).strip().strip("'\"")
    return None


SECRET_DIRS = [".ssh", ".treg", ".codex", ".cursor", ".aws", ".gnupg", ".config/gh", ".config/infisical", "Library/Keychains"]
SECRET_FILES = [".claude.json", ".netrc", ".npmrc"]


def _secret_paths():
    ps = [str(HOME / d) for d in SECRET_DIRS] + [str(HOME / f) for f in SECRET_FILES] + [str(PROVIDERS_FILE)]
    try:      # this machine's own additions: {"secret_paths": ["/path", "~/path"]} in ~/.crucible/providers.json
        ps += [str(Path(x).expanduser()) for x in json.loads(PROVIDERS_FILE.read_text()).get("secret_paths") or []]
    except Exception:
        pass
    f, _ = _key_file()
    if f:
        ps.append(str(Path(f).resolve()))
    return ps


def _is_secret(p: Path) -> bool:
    s = str(p.resolve())
    return any(s == x or s.startswith(x.rstrip("/") + "/") for x in _secret_paths()) or p.name in (".env",) or p.name.startswith(".env.")


# ───────────────────────── tool loop for OpenRouter models ─────────────────────────
TOOLS = [
    {"type": "function", "function": {"name": "read_file", "description": "Read a text file. Returns up to `limit` lines starting at line `offset` (1-based).",
        "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "offset": {"type": "integer"}, "limit": {"type": "integer"}}, "required": ["path"]}}},
    {"type": "function", "function": {"name": "write_file", "description": "Create or overwrite a text file (parent folders are created). Only inside the working directory or a temp folder.",
        "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "content": {"type": "string"}}, "required": ["path", "content"]}}},
    {"type": "function", "function": {"name": "run_bash", "description": "Run a shell command in the working directory and return its exit code, stdout and stderr. Use it to run code, tests and checks.",
        "parameters": {"type": "object", "properties": {"command": {"type": "string"}, "timeout_s": {"type": "integer", "description": "default 120, max 600"}}, "required": ["command"]}}},
]


def _sandbox_profile(write_roots) -> str:
    deny_read = " ".join(f'(subpath "{p}")' if Path(p).is_dir() or not Path(p).suffix else f'(literal "{p}")' for p in _secret_paths())
    allow_w = " ".join(f'(subpath "{p}")' for p in write_roots)
    return (f'(version 1)(allow default)(deny file-read* {deny_read})(deny file-write*)'
            f'(allow file-write* {allow_w} (literal "/dev/null") (literal "/dev/tty") (literal "/dev/stdout") (literal "/dev/stderr") (regex #"^/dev/fd/") (regex #"^/dev/ttys"))')


def _clean_env(cwd):
    keep = {k: os.environ[k] for k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR", "USER", "SHELL", "TERM") if k in os.environ}
    keep["PWD"] = str(cwd)
    return keep


def _tool(name, a, cwd: Path, roots):
    try:
        if name == "read_file":
            p = Path(a["path"]).expanduser()
            p = p if p.is_absolute() else cwd / p
            if _is_secret(p):
                return "refused: that path is not readable by agents"
            lines = p.read_text(errors="replace").splitlines()
            o, n = max(1, int(a.get("offset") or 1)), int(a.get("limit") or 400)
            out = "\n".join(f"{i}\t{l}" for i, l in enumerate(lines[o - 1:o - 1 + n], o))
            return out[:60000] + (f"\n[{len(lines)} lines in file]" if len(lines) > o - 1 + n else "")
        if name == "write_file":
            p = Path(a["path"]).expanduser()
            p = (p if p.is_absolute() else cwd / p).resolve()
            if not any(str(p).startswith(str(r) + "/") for r in roots):
                return f"refused: writes are allowed only under {', '.join(map(str, roots))}"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(a.get("content", ""))
            return f"wrote {p} ({len(a.get('content', ''))} chars)"
        if name == "run_bash":
            t = min(600, max(5, int(a.get("timeout_s") or 120)))
            cmd = ["/bin/bash", "-c", a["command"]]
            if shutil.which("sandbox-exec"):
                cmd = ["sandbox-exec", "-p", _sandbox_profile(roots)] + cmd
            try:
                r = subprocess.run(cmd, cwd=str(cwd), env=_clean_env(cwd), capture_output=True, text=True, timeout=t, stdin=subprocess.DEVNULL)
                out = f"exit {r.returncode}\n--- stdout ---\n{r.stdout[-16000:]}\n--- stderr ---\n{r.stderr[-6000:]}"
            except subprocess.TimeoutExpired:
                out = f"timed out after {t}s"
            return out
        return f"unknown tool {name}"
    except Exception as e:
        return f"tool error: {type(e).__name__}: {e}"


def _ssl_ctx():
    """A verifying TLS context. python.org builds on macOS ship without a CA bundle: use certifi or the system file."""
    import ssl
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        pass
    for f in ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt"):
        if Path(f).is_file():
            return ssl.create_default_context(cafile=f)
    return ssl.create_default_context()


def _post(body, key, timeout):
    req = urllib.request.Request(OR_URL, data=json.dumps(body).encode(), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "X-Title": "crucible"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx()) as r:
                return json.loads(r.read().decode()), None
        except urllib.error.HTTPError as e:
            txt = e.read().decode(errors="replace")[:600]
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(4 * (attempt + 1)); continue
            return None, f"HTTP {e.code}: {txt}"
        except Exception as e:
            if attempt < 2:
                time.sleep(3); continue
            return None, f"{type(e).__name__}: {e}"
    return None, "no answer"


def run_openrouter(model, effort, prompt, schema, cwd: Path, timeout, max_turns, tools=True, extra_roots=()):
    key = openrouter_key()
    if not key:
        return {"ok": False, "error": "no_key: set OPENROUTER_API_KEY or ~/.crucible/providers.json", "kind": "setup"}
    roots = [cwd.resolve()] + [Path(p).resolve() for p in extra_roots] + [Path(p).resolve() for p in ("/tmp", "/private/tmp", tempfile.gettempdir())]
    sys_msg = ("You are an autonomous agent working in the directory " + str(cwd) + ". Use the tools to read files, write files and run commands; "
               "check your work by running it. Do not ask questions: nobody can answer. Never claim a check passed unless you ran it and saw it pass.")
    msgs = [{"role": "system", "content": sys_msg}, {"role": "user", "content": prompt + (schema_hint(schema) if schema else "")}]
    usage = {"in": 0, "out": 0, "cost_usd": 0.0}
    t0, turns, fixes, served = time.time(), 0, 0, None
    while True:
        if time.time() - t0 > timeout:
            return {"ok": False, "error": f"timeout after {timeout}s", "kind": "timeout", "usage": usage, "turns": turns}
        if turns >= max_turns:
            return {"ok": False, "error": f"no final answer within {max_turns} turns", "kind": "turns", "usage": usage, "turns": turns}
        body = {"model": model, "messages": msgs, "usage": {"include": True}, "max_tokens": 16000, "provider": {"data_collection": "deny"}}
        if effort:
            body["reasoning"] = {"effort": effort}
        if tools:
            body["tools"] = TOOLS
        resp, err = _post(body, key, min(900, max(60, timeout - (time.time() - t0))))
        if err and "data_collection" in body.get("provider", {}) and re.search(r"No endpoints found|data policy", err, re.I):
            return {"ok": False, "error": "no provider of this model accepts the no-training data policy: " + err[:200], "kind": "policy", "usage": usage, "turns": turns}
        if err:
            return {"ok": False, "error": err, "kind": "provider", "usage": usage, "turns": turns}
        if resp.get("error"):
            return {"ok": False, "error": json.dumps(resp["error"])[:600], "kind": "provider", "usage": usage, "turns": turns}
        u = resp.get("usage") or {}
        usage["in"] += u.get("prompt_tokens") or 0
        usage["out"] += u.get("completion_tokens") or 0
        usage["cost_usd"] += float(u.get("cost") or 0)
        served = resp.get("provider") or served
        turns += 1
        ch = (resp.get("choices") or [{}])[0]
        m = ch.get("message") or {}
        calls = m.get("tool_calls") or []
        keep = {"role": "assistant", "content": m.get("content") or ""}
        if calls:
            keep["tool_calls"] = calls
        if m.get("reasoning_details"):
            keep["reasoning_details"] = m["reasoning_details"]  # some providers need their reasoning blocks sent back
        msgs.append(keep)
        if calls:
            for c in calls:
                fn = (c.get("function") or {})
                try:
                    args = json.loads(fn.get("arguments") or "{}")
                except Exception:
                    args = None
                out = _tool(fn.get("name"), args, cwd, roots) if isinstance(args, dict) else "tool error: arguments were not valid JSON"
                msgs.append({"role": "tool", "tool_call_id": c.get("id"), "content": out})
            continue
        text = m.get("content") or ""
        if not schema:
            return {"ok": True, "result": text, "usage": usage, "turns": turns, "served_by": served}
        obj = extract_json(text)
        errs = ["the reply was not a JSON object"] if not isinstance(obj, dict) else validate(obj, schema)
        if not errs:
            return {"ok": True, "result": obj, "usage": usage, "turns": turns, "served_by": served, "schema_fixes": fixes}
        if fixes >= 2:
            return {"ok": False, "error": "schema: " + "; ".join(errs[:6]), "kind": "schema", "usage": usage, "turns": turns, "raw": text[:2000]}
        fixes += 1
        msgs.append({"role": "user", "content": ("Your reply was empty. " if not text.strip() else "Your final answer did not match the required format: " + "; ".join(errs[:10]) + ". ")
                     + "Reply again with ONLY the corrected JSON object."})


# ───────────────────────── Claude Code and Codex CLIs ─────────────────────────
def run_claude(model, effort, prompt, schema, cwd: Path, timeout, lean=False, tools=True):
    exe = shutil.which("claude")
    if not exe:
        return {"ok": False, "error": "claude CLI not found", "kind": "setup"}
    cmd = [exe, "-p", "--output-format", "json", "--no-session-persistence", "--permission-mode", "bypassPermissions"]
    if model:      # none: the CLI's own default model
        cmd += ["--model", model]
    if effort:
        cmd += ["--effort", effort]
    if schema:
        cmd += ["--json-schema", json.dumps(schema)]
    if lean:   # no CLAUDE.md, hooks, MCP servers or skills: for probes and roles that need none of them
        cmd += ["--safe-mode"]
    if not tools:
        cmd += ["--tools", ""]
    # Code Mode works only in an interactive terminal session; asked for here it only prints a warning
    env = {k: v for k, v in os.environ.items() if k not in ("OPENROUTER_API_KEY", "CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "CLAUDE_CODE_EXPERIMENTAL_CODE_MODE")}
    try:
        r = subprocess.run(cmd, input=prompt, cwd=str(cwd), env=env, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout after {timeout}s", "kind": "timeout"}
    try:
        d = json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else {}
    except Exception:
        d = {}
    if isinstance(d, list):   # --verbose style array: the last element is the result
        d = next((x for x in reversed(d) if isinstance(x, dict) and x.get("type") == "result"), {})
    u = d.get("usage") or {}
    usage = {"in": (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0),
             "out": u.get("output_tokens") or 0, "cost_usd": float(d.get("total_cost_usd") or 0)}
    if r.returncode or d.get("is_error") or not d:
        msg = (d.get("result") if isinstance(d.get("result"), str) else "") or r.stderr.strip()[-400:] or r.stdout.strip()[-400:]
        kind = "limit" if re.search(r"usage limit|weekly limit|hit your .{0,24}limit|rate.?limit|overloaded", msg, re.I) else "provider"
        return {"ok": False, "error": f"claude exit {r.returncode}: {msg}"[:600], "kind": kind, "usage": usage, "turns": d.get("num_turns")}
    out = {"usage": usage, "turns": d.get("num_turns"), "api_seconds": round((d.get("duration_api_ms") or 0) / 1000, 1)}
    if not schema:
        return {"ok": True, "result": d.get("result", ""), **out}
    obj = d.get("structured_output")
    if not isinstance(obj, dict):
        obj = extract_json(d.get("result") or "")
    errs = ["no JSON object in the reply"] if not isinstance(obj, dict) else validate(obj, schema)
    if errs:
        return {"ok": False, "error": "schema: " + "; ".join(errs[:6]), "kind": "schema", "raw": str(d.get("result"))[:2000], **out}
    return {"ok": True, "result": obj, **out}


CLAUDE_NAMES = ("haiku", "sonnet", "opus", "fable")


def codex_config() -> dict:
    """~/.crucible/providers.json -> "codex": {"model": "<default model id>", "models": {"sonnet": "<id>", "opus": "<id>", ...},
    "effort": {"xhigh": "high"}, "network": true, "code_mode": true, "args": ["..."]}. All optional: with nothing set, every
    agent runs on the Codex CLI's own default model, with network access inside its workspace sandbox and with Codex's code
    mode asked for (the model writes one script that calls its tools; under development in Codex, so an agent that fails
    with it is run once more without it)."""
    try:
        return json.loads(PROVIDERS_FILE.read_text()).get("codex") or {}
    except Exception:
        return {}


def codex_cmd(exe, model, effort, schema_file, last_file, cfg, code_mode=None) -> list:
    """The `codex exec` command for one agent. A role name from the routing table (sonnet, opus, ...) is not a Codex model:
    it is looked up in the user's map, else the default model is used."""
    if model in CLAUDE_NAMES or not model:
        model = (cfg.get("models") or {}).get(model) or cfg.get("model")
    cmd = [exe, "exec", "--sandbox", "workspace-write", "--skip-git-repo-check", "--ephemeral", "--json", "-o", str(last_file)]
    if model:
        cmd += ["-m", model]
    effort = (cfg.get("effort") or {}).get(effort, effort)
    if effort:
        cmd += ["-c", f'model_reasoning_effort="{effort}"']
    if cfg.get("network", True):      # research needs the web; set "network": false to keep agents offline
        cmd += ["-c", "sandbox_workspace_write.network_access=true"]
    if cfg.get("code_mode", True) if code_mode is None else code_mode:
        cmd += ["-c", "features.code_mode=true"]
    if schema_file:
        cmd += ["--output-schema", str(schema_file)]
    return cmd + [str(a) for a in cfg.get("args") or []]


def _codex_usage(stdout: str) -> dict:
    """Token usage from the JSONL events of `codex exec --json` (the turn.completed events carry it)."""
    u = {"in": 0, "out": 0, "cost_usd": 0.0}
    for line in stdout.splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        x = e.get("usage") if isinstance(e, dict) else None
        if isinstance(x, dict):
            u["in"] += (x.get("input_tokens") or 0)
            u["out"] += (x.get("output_tokens") or 0)
    return u


KEEP = ("type", "properties", "required", "items", "enum", "description")


def strict_schema(s, optional=False):
    """The schema in the strict form OpenAI's structured output asks for: every object closed (additionalProperties false)
    with all its properties required, an optional property allowed to be null instead, and only the plain keywords kept
    (limits such as minimum or minItems are checked here afterwards, against the original schema)."""
    if not isinstance(s, dict):
        return s
    out = {k: v for k, v in s.items() if k in KEEP}
    t = out.get("type")
    if t == "object":
        props, req = s.get("properties") or {}, set(s.get("required") or [])
        out["properties"] = {k: strict_schema(v, k not in req) for k, v in props.items()}
        out["required"] = list(props)
        out["additionalProperties"] = False
    elif t == "array":
        out["items"] = strict_schema(s.get("items") or {"type": "string"})
    if optional and isinstance(t, str):
        out["type"] = [t, "null"]
        if "enum" in out:
            out["enum"] = list(out["enum"]) + [None]
    return out


def drop_nulls(v, s):
    """Undo strict_schema on a reply: an optional property the model set to null is left out again."""
    if isinstance(v, dict) and isinstance(s, dict) and s.get("type") == "object":
        req, props = set(s.get("required") or []), s.get("properties") or {}
        return {k: drop_nulls(x, props.get(k)) for k, x in v.items() if not (x is None and k not in req)}
    if isinstance(v, list) and isinstance(s, dict):
        return [drop_nulls(x, s.get("items")) for x in v]
    return v


def run_codex(model, effort, prompt, schema, cwd: Path, timeout, _plain=False, _code_mode=None):
    """Per the Codex CLI's documented flags (read 2026-11-15 and again 2026-11-19). The reply format is sent as a strict
    schema; if the CLI or the API refuses it, the agent runs once more with the format written into the prompt."""
    exe = shutil.which("codex")
    if not exe:
        return {"ok": False, "error": "codex CLI not found (install it and run `codex login`)", "kind": "setup"}
    tmp = Path(tempfile.mkdtemp(prefix="crucible-codex-"))
    native = bool(schema) and not _plain
    if native:
        (tmp / "schema.json").write_text(json.dumps(strict_schema(schema)))
    cfg = codex_config()
    code_mode = cfg.get("code_mode", True) if _code_mode is None else _code_mode
    cmd = codex_cmd(exe, model, effort, tmp / "schema.json" if native else None, tmp / "last.txt", cfg, code_mode)
    try:
        r = subprocess.run(cmd + [prompt + (schema_hint(schema) if schema and not native else "")], cwd=str(cwd), capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout after {timeout}s", "kind": "timeout"}
    text = (tmp / "last.txt").read_text(errors="replace") if (tmp / "last.txt").exists() else ""
    usage = _codex_usage(r.stdout or "")
    if r.returncode or not text.strip():
        msg = (r.stderr.strip() or r.stdout.strip())[-400:]
        if native and re.search(r"schema|response_format|text\.format|additionalProperties", msg, re.I):
            return run_codex(model, effort, prompt, schema, cwd, timeout, _plain=True, _code_mode=code_mode)
        if code_mode and not re.search(r"usage limit|rate.?limit|quota", msg, re.I):   # an under-development feature must not cost an agent
            out = run_codex(model, effort, prompt, schema, cwd, timeout, _plain=_plain, _code_mode=False)
            out["code_mode"] = "failed with it, ran without"
            return out
        return {"ok": False, "error": f"codex exit {r.returncode}: {msg}", "kind": "limit" if re.search(r"usage limit|rate.?limit|quota", msg, re.I) else "provider", "usage": usage}
    if not schema:
        return {"ok": True, "result": text, "usage": usage}
    obj = extract_json(text)
    obj = drop_nulls(obj, schema) if isinstance(obj, dict) else obj
    errs = ["no JSON object in the reply"] if not isinstance(obj, dict) else validate(obj, schema)
    return {"ok": False, "error": "schema: " + "; ".join(errs[:6]), "kind": "schema", "raw": text[:2000], "usage": usage} if errs else {"ok": True, "result": obj, "usage": usage}


def run_agent(provider, model, effort, prompt, schema=None, cwd=None, timeout=1800, max_turns=60, lean=False, tools=True, extra_roots=()):
    cwd = Path(cwd or os.getcwd())
    t0 = time.time()
    if provider == "claude":
        out = run_claude(model, effort, prompt, schema, cwd, timeout, lean, tools)
    elif provider == "codex":
        out = run_codex(model, effort, prompt, schema, cwd, timeout)
    elif provider == "openrouter":
        out = run_openrouter(model, effort, prompt, schema, cwd, timeout, max_turns, tools, extra_roots)
    else:
        out = {"ok": False, "error": f"unknown provider {provider}", "kind": "setup"}
    out.update({"provider": provider, "model": model, "effort": effort, "seconds": round(time.time() - t0, 1)})
    if out.get("ok") and isinstance(out.get("result"), dict):
        out["result"]["_ck"] = checksum(out["result"])
    return out


# ───────────────────────── relay: an external agent inside a crucible (Claude Code) run ─────────────────────────
def _find_spec(marker, session):
    """The engine puts <<<MARKER {spec json} ---PROMPT--- prompt MARKER>>> into the relay agent's first message; that
    message is in the relay agent's own transcript on disk."""
    base = HOME / ".claude" / "projects"
    files = sorted(base.glob(f"*/{session or '*'}/subagents/**/agent-*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)[:400]
    for f in files:
        try:
            with f.open(errors="replace") as fh:
                head = [next(fh, "") for _ in range(6)]
        except Exception:
            continue
        for line in head:
            if marker not in line:
                continue
            try:
                m = json.loads(line).get("message") or {}
            except Exception:
                continue
            c = m.get("content")
            text = c if isinstance(c, str) else "\n".join(b.get("text", "") for b in c or [] if isinstance(b, dict))
            mm = re.search(re.escape(f"<<<{marker}") + r"\n(.*?)\n---PROMPT---\n(.*)\n" + re.escape(f"{marker}>>>"), text, re.S)
            if mm:
                return json.loads(mm.group(1)), mm.group(2)
    return None, None


def _job_wait(job: Path, wait):
    t0 = time.time()
    while time.time() - t0 < wait:
        f = job / "result.json"
        if f.exists():
            try:
                out = json.loads(f.read_text())
            except Exception:
                time.sleep(1); continue
            if out.get("ok"):
                print(json.dumps({"result": out["result"], "meta": {k: out.get(k) for k in ("provider", "model", "effort", "seconds", "usage", "turns")}}))
            else:
                print(json.dumps({"failed": True, "error": out.get("error"), "kind": out.get("kind")}))
            return 0
        time.sleep(3)
    print(json.dumps({"pending": True, "wait": f'python3 "{__file__}" wait --job "{job}" --wait {int(wait)}'}))
    return 0


def relay(marker, session, wait):
    spec, prompt = _find_spec(marker, session)
    if not spec:
        print(json.dumps({"failed": True, "error": f"no spec with marker {marker} in this session's agent transcripts", "kind": "setup"}))
        return 0
    job = Path(spec.get("runDir") or tempfile.gettempdir()) / "agents" / (re.sub(r"[^A-Za-z0-9._-]+", "_", spec.get("label") or marker) + "-" + checksum(prompt))
    job.mkdir(parents=True, exist_ok=True)
    if not (job / "result.json").exists() and not (job / "started").exists():   # idempotent: a replayed relay reuses the job
        (job / "started").write_text(time.strftime("%Y-%m-%dT%H:%M:%S"))
        (job / "prompt.txt").write_text(prompt)
        (job / "schema.json").write_text(json.dumps(spec.get("schema") or {}))
        cmd = [sys.executable, __file__, "run", "--provider", spec["provider"], "--model", spec["model"], "--prompt-file", str(job / "prompt.txt"),
               "--schema-file", str(job / "schema.json"), "--cwd", spec.get("runDir") or os.getcwd(), "--timeout", str(spec.get("timeout") or 2400), "--out", str(job / "result.json")]
        if spec.get("effort"):
            cmd += ["--effort", spec["effort"]]
        with (job / "log.txt").open("w") as lg:
            subprocess.Popen(cmd, stdout=lg, stderr=lg, stdin=subprocess.DEVNULL, start_new_session=True)
    return _job_wait(job, wait)


def check():
    f, var = _key_file()
    print(json.dumps({"claude": bool(shutil.which("claude")), "codex": bool(shutil.which("codex")),
                      "openrouter": bool(openrouter_key()), "openrouter_key_source": "env" if os.environ.get("OPENROUTER_API_KEY") else (f"file ({var})" if f else None),
                      "sandbox": bool(shutil.which("sandbox-exec"))}, indent=1))
    return 0


def main(argv):
    if not argv:
        print(__doc__); return 2
    cmd, o, flags = argv[0], {}, set()
    i = 1
    while i < len(argv):
        if argv[i] in ("--lean", "--no-tools"):
            flags.add(argv[i]); i += 1
        elif argv[i].startswith("--") and i + 1 < len(argv):
            o[argv[i]] = argv[i + 1]; i += 2
        else:
            i += 1
    if cmd == "check":
        return check()
    if cmd == "ck":
        print(checksum(json.loads(Path(o["--file"]).read_text()))); return 0
    if cmd == "relay":
        return relay(o["--marker"], o.get("--session"), float(o.get("--wait", 570)))
    if cmd == "wait":
        return _job_wait(Path(o["--job"]), float(o.get("--wait", 570)))
    if cmd == "run":
        prompt = Path(o["--prompt-file"]).read_text() if o.get("--prompt-file") else sys.stdin.read()
        schema = json.loads(Path(o["--schema-file"]).read_text()) if o.get("--schema-file") else None
        out = run_agent(o["--provider"], o.get("--model"), o.get("--effort"), prompt, schema or None, o.get("--cwd"), int(o.get("--timeout", 1800)),
                        int(o.get("--max-turns", 60)), "--lean" in flags, "--no-tools" not in flags)
        text = json.dumps(out)
        if o.get("--out"):
            tmp = Path(o["--out"] + ".tmp"); tmp.write_text(text); tmp.replace(o["--out"])
        print(text)
        return 0 if out.get("ok") else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
