import json, sys
sys.path.insert(0, ".")
OK = [("1h30m", 5400), ("90", 90), ("0", 0), ("1.5h", 5400), (" 2m ", 120), ("1h 30m", 5400), ("1W", 604800), ("1w2d3h4m5s", 788645),
      ("0.1h", 360), ("0.3d", 25920), ("2.25m", 135), ("1D 12H", 129600), ("0s", 0), ("007", 7), ("1.50h", 5400), ("0.05m", 3), ("10m   5s", 605),
      ("0.7h", 2520), ("1.1h", 3960)]
BAD = ["", "   ", "1 h", "30m1h", "1h1h", ".5h", "1.h", "-1h", "+5m", "1e3s", "1,000s", "1h30", "1.5", "0.5s", "1.0001m", "h", "1x", "1h30m ago", "1.2.3h", "1h30m5"]
passed = total = 0
fails = []
try:
    from duration import parse_duration
except Exception as e:
    print(json.dumps({"passed": 0, "total": len(OK) + len(BAD) + 2, "fails": ["import: " + repr(e)]})); sys.exit(0)
for s, want in OK:
    total += 1
    try:
        got = parse_duration(s)
        if got == want and isinstance(got, int) and not isinstance(got, bool):
            passed += 1
        else:
            fails.append(f"{s!r}: got {got!r}, want {want}")
    except Exception as e:
        fails.append(f"{s!r}: raised {type(e).__name__}, want {want}")
for s in BAD:
    total += 1
    try:
        got = parse_duration(s); fails.append(f"{s!r}: got {got!r}, want ValueError")
    except ValueError:
        passed += 1
    except Exception as e:
        fails.append(f"{s!r}: raised {type(e).__name__}, want ValueError")
for v in (90, None):
    total += 1
    try:
        parse_duration(v); fails.append(f"{v!r}: no TypeError")
    except TypeError:
        passed += 1
    except Exception as e:
        fails.append(f"{v!r}: raised {type(e).__name__}, want TypeError")
print(json.dumps({"passed": passed, "total": total, "fails": fails[:12]}))
