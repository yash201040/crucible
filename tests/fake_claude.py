#!/usr/bin/env python3
"""A stand-in for the `claude` command, for tests/test_helper.py. It reads the prompt on stdin like `claude -p` and
acts on a directive in the task text, so the launcher's counting, limits and closing can be tested with no model.

  FAKE:ok            answer at once            FAKE:sleep=<s>     answer after <s> seconds
  FAKE:fail          exit 1                    FAKE:limit         fail with a usage-limit message
  FAKE:turns         stop at the turn limit    FAKE:notes         write notes, then hang
  FAKE:child         start a process of its own, write its pid, then hang (is it killed with the session?)
  FAKE:nest=<task>   start a helper of its own with <task> as its task, and hand back what that printed
"""
import json, os, re, subprocess, sys, time

argv = sys.argv[1:]
flag = lambda name: argv[argv.index(name) + 1] if name in argv else None
prompt = sys.stdin.read()
task = prompt.split("TASK (written by your owner):", 1)[-1].split("\nRules:", 1)[0]
m = re.search(r"Change no file outside (.+?)/ unless", prompt)
mydir = m.group(1) if m else "."
model = {"haiku": "claude-haiku-5-5", "sonnet": "claude-sonnet-5-5", "opus": "claude-opus-5-5"}.get(flag("--model"), "claude-opus-5-5")
usd = float((re.search(r"FAKE:usd=([\d.]+)", task) or [0, "1.42"])[1])


def out(result, subtype="success", is_error=False):
    print(json.dumps({"type": "result", "subtype": subtype, "is_error": is_error, "result": result, "num_turns": 3, "session_id": flag("--session-id"),
                      "total_cost_usd": usd, "modelUsage": {model: {"inputTokens": 10, "outputTokens": 1000, "cacheReadInputTokens": 200000,
                                                                     "cacheCreationInputTokens": 30000, "costUSD": usd}}}))


inner = ""
if "FAKE:nest=" in task:
    task, inner = task.split("FAKE:nest=", 1)
    task += "FAKE:nest"
with open(os.path.join(mydir, "fake-argv.json"), "w") as f:
    json.dump({"argv": argv, "env": {k: v for k, v in os.environ.items() if k.startswith("CRUCIBLE_HELPER_") or k == "CLAUDECODE"}}, f)

if (s := re.search(r"FAKE:sleep=([\d.]+)", task)):
    time.sleep(float(s.group(1)))
if "FAKE:fail" in task:
    sys.stderr.write("something broke\n"); sys.exit(1)
if "FAKE:limit" in task:
    out("You have hit your usage limit. It resets at 5pm.", "error_during_execution", True); sys.exit(1)
if "FAKE:turns" in task:
    out("", "error_max_turns", True); sys.exit(1)
if "FAKE:notes" in task:
    open(os.path.join(mydir, "notes.md"), "w").write("found so far: A at file.py:3 (cited)\n")
    time.sleep(600)
if "FAKE:child" in task:
    p = subprocess.Popen(["sleep", "600"])
    open(os.path.join(mydir, "child.pid"), "w").write(str(p.pid))
    time.sleep(600)
if inner:
    sub = os.path.join(mydir, "sub-task.md")
    open(sub, "w").write("A task for a helper one level further down, long enough to be accepted. " + inner.strip())
    cmd = re.search(r"run `(.+?) run --task-file", prompt)
    if not cmd:
        out("I was told to do all of the work myself (no helper command in my rules)."); sys.exit(0)
    r = subprocess.run(cmd.group(1).split() + ["run", "--task-file", sub, "--model", "haiku"], capture_output=True, text=True)
    out("NESTED:\n" + r.stdout); sys.exit(0)
out("1. Answer: done.\n2. Findings: X at a.py:1 (cited).\n3. Not done: nothing.\n4. Files: none.")
