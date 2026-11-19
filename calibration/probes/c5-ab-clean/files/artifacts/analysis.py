import csv, math

rows = list(csv.DictReader(open("events.csv")))


def ztest(x1, n1, x2, n2):
    p1, p2, p = x1 / n1, x2 / n2, (x1 + x2) / (n1 + n2)
    z = (p2 - p1) / math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    return z, math.erfc(abs(z) / math.sqrt(2))

users = {"A": set(), "B": set()}
buyers = {"A": set(), "B": set()}
for r in rows:
    users[r["variant"]].add(r["user_id"])
    if r["purchased"] == "1":
        buyers[r["variant"]].add(r["user_id"])

na, nb = len(users["A"]), len(users["B"])
xa, xb = len(buyers["A"]), len(buyers["B"])
z, p = ztest(xa, na, xb, nb)
print(f"A: {xa}/{na} = {xa / na:.4f}")
print(f"B: {xb}/{nb} = {xb / nb:.4f}")
print(f"relative lift = {(xb / nb) / (xa / na) - 1:+.4f}")
print(f"z = {z:.3f}, p = {p:.5f}")
