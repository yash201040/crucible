def lower_bound(a, x):
    """Index of the first elemnt of sorted list a that is >= x (len(a) if there is none)."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(a, x):
    """Index of the first element of sorted list a that is > x (len(a) if there is none)."""
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def count_in_range(a, lo, hi):
    """Number of elements e of sorted list a with lo <= e <= hi."""
    if hi < lo:
        return 0
    return upper_bound(a, hi) - lower_bound(a, lo)
