from .intervals import merge


def free_slots(day_start, day_end, bookings, min_len=1):
    busy = merge([(max(s, day_start), min(e, day_end)) for s, e in bookings if e > day_start and s < day_end])
    slots, cursor = [], day_start
    for s, e in busy:
        if s - cursor >= min_len:
            slots.append((cursor, s))
        cursor = max(cursor, e)
    if day_end - cursor >= min_len:
        slots.append((cursor, day_end))
    return slots
