# Specification: parse_duration

Create `duration.py` with a function `parse_duration(text) -> int` that returns a number of seconds.

Rules
1. `text` is one or more components. A component is a non-negative decimal number followed directly by a unit:
   `w` (weeks), `d` (days), `h` (hours), `m` (minutes), `s` (seconds). Example: `"1h30m"` is 5400.
2. Units are case-insensitive. Spaces are allowed between components and around the whole text (`"1h 30m"`,
   `" 2m "`), but not between a number and its unit (`"1 h"` is invalid).
3. Units must appear in strictly descending order of size (w, d, h, m, s), each at most once: `"30m1h"` and
   `"1h1h"` are invalid.
4. A number may have a fractional part (`"1.5h"` is 5400). It must have digits on both sides of the dot:
   `".5h"` and `"1.h"` are invalid. No signs, no exponents, no thousands separators.
5. A bare non-negative integer with no unit means seconds: `"90"` is 90. A bare number cannot be fractional and
   cannot be combined with components (`"1h30"` is invalid).
6. The total must be a whole number of seconds, computed exactly; otherwise the input is invalid (`"0.5s"`,
   `"1.0001m"`).
7. Invalid text raises `ValueError`. An argument that is not a `str` raises `TypeError`.
8. The empty string and whitespace-only text are invalid.

