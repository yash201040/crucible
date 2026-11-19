import re
from fractions import Fraction

UNITS = {"w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}
ORDER = "wdhms"


def parse_duration(text):
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    t = text.strip(" ")
    if not t:
        raise ValueError("empty")
    if re.fullmatch(r"[0-9]+", t):
        return int(t)
    total, last, pos = Fraction(0), -1, 0
    while pos < len(t):
        m = re.compile(r"([0-9]+(?:\.[0-9]+)?)([wdhmsWDHMS]) *").match(t, pos)
        if not m:
            raise ValueError("bad component")
        i = ORDER.index(m.group(2).lower())
        if i <= last:
            raise ValueError("order")
        last = i
        total += Fraction(m.group(1)) * UNITS[m.group(2).lower()]
        pos = m.end()
    if total.denominator != 1:
        raise ValueError("not whole seconds")
    return int(total)
