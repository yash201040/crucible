import json, random, sys
sys.path.insert(0, ".")


def brute(ds, de, bookings, min_len):
    busy = [False] * (de - ds)
    for s, e in bookings:
        for t in range(max(s, ds), min(e, de)):
            busy[t - ds] = True
    out, i = [], 0
    while i < len(busy):
        if busy[i]:
            i += 1; continue
        j = i
        while j < len(busy) and not busy[j]:
            j += 1
        if j - i >= min_len:
            out.append((ds + i, ds + j))
        i = j
    return out


CASES = [
    (540, 1020, [], 1), (540, 1020, [(600, 660)], 1), (540, 1020, [(600, 660), (660, 720)], 1), (540, 1020, [(720, 780), (600, 660)], 1),
    (540, 1020, [(500, 600)], 1), (540, 1020, [(1000, 1100)], 1), (540, 1020, [(100, 200)], 1), (540, 1020, [(1100, 1200)], 1),
    (540, 1020, [(500, 1100)], 1), (540, 1020, [(600, 900), (650, 700)], 1), (540, 1020, [(600, 700), (650, 800), (790, 795)], 1),
    (540, 1020, [(540, 600), (990, 1020)], 1), (540, 1020, [(600, 660), (665, 700)], 10), (540, 1020, [(600, 660), (670, 700)], 10),
    (0, 60, [(10, 20), (20, 30), (30, 40)], 1), (0, 60, [(30, 40), (10, 20), (20, 30), (5, 12)], 5), (540, 1020, [(600, 660), (600, 660)], 1),
    (540, 1020, [(700, 800), (600, 900), (650, 660)], 30),
]
rng = random.Random(4242)
for _ in range(300):
    ds = rng.randint(0, 50); de = ds + rng.randint(1, 80)
    bs = []
    for _ in range(rng.randint(0, 7)):
        s = rng.randint(-20, 140); bs.append((s, s + rng.randint(1, 40)))
    CASES.append((ds, de, bs, rng.randint(1, 12)))
passed = total = 0
fails = []
try:
    from booking.slots import free_slots
    from booking.intervals import merge
except Exception as e:
    print(json.dumps({"passed": 0, "total": len(CASES) + 2, "fails": ["import: " + repr(e)]})); sys.exit(0)
for ds, de, bs, ml in CASES:
    total += 1
    try:
        got = [tuple(x) for x in free_slots(ds, de, list(bs), ml)]
        want = brute(ds, de, bs, ml)
        if got == want:
            passed += 1
        elif len(fails) < 12:
            fails.append(f"free_slots({ds},{de},{bs},{ml}) = {got}, want {want}")
    except Exception as e:
        if len(fails) < 12:
            fails.append(f"free_slots({ds},{de},{bs},{ml}) raised {type(e).__name__}: {e}")
for ivs, want in (([(5, 9), (1, 3), (3, 4), (8, 12)], [(1, 4), (5, 12)]), ([(1, 2)], [(1, 2)])):
    total += 1
    try:
        got = [tuple(x) for x in merge(list(ivs))]
        if got == want:
            passed += 1
        else:
            fails.append(f"merge({ivs}) = {got}, want {want}")
    except Exception as e:
        fails.append(f"merge({ivs}) raised {type(e).__name__}")
print(json.dumps({"passed": passed, "total": total, "fails": fails[:12]}))
