"""Half-open minute intervals (start, end) with start < end."""


def merge(intervals):
    """Merge overlapping intervals. Input must be sorted by start."""
    out = []
    for s, e in intervals:
        if out and s < out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], e))
        else:
            out.append((s, e))
    return out
