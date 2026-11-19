from .intervals import merge


def free_slots(day_start, day_end, bookings, min_len=1):
    """Free (start, end) slots of at least min_len minutes inside [day_start, day_end), given booked intervals."""
    busy = merge(bookings)
    slots, cursor = [], day_start
    for s, e in busy:
        if s - cursor >= min_len:
            slots.append((cursor, s))
        cursor = max(cursor, e)
    if day_end - cursor >= min_len:
        slots.append((cursor, day_end))
    return slots
