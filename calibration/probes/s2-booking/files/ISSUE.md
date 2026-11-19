# Bug report: wrong free slots in the booking module

`booking.slots.free_slots(day_start, day_end, bookings, min_len=1)` should return the free intervals of at least
`min_len` minutes inside the working day `[day_start, day_end)`, in ascending order, as a list of `(start, end)`
tuples. Times are integer minutes; all intervals are half-open. `bookings` is a list of `(start, end)` tuples with
`start < end`, in ANY order; bookings may overlap, touch, or lie partly or wholly outside the working day.
`min_len` is an integer >= 1.

What users see today
- With back-to-back or out-of-order meetings, some results are wrong: busy time is offered as free.
- Sometimes a slot starts before the working day or ends after it, or has its end before its start.
- A booking that ends before another one that started earlier makes later slots wrong.

Fix the module (files under `booking/`) so `free_slots` is correct for every valid input. Keep the function
signature. `booking.intervals.merge` may be changed as you see fit, but must still return merged, sorted,
non-overlapping intervals for any list of valid intervals (touching intervals are merged into one).
Three basic tests are in `test_basic.py`; they already pass and must keep passing. Check your fix by running it.
Report the checks you ran.
