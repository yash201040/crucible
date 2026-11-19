import unittest
from duration import parse_duration


class T(unittest.TestCase):
    def test_valid(self):
        for text, want in [("1h30m", 5400), ("90", 90), ("0", 0), ("1.5h", 5400), (" 2m ", 120), ("1h 30m", 5400), ("1W", 604800), ("1w2d3h4m5s", 788645),
                           ("0.1h", 360), ("0.3d", 25920), ("2.25m", 135), ("1D 12H", 129600), ("0s", 0), ("007", 7), ("1.50h", 5400), ("0.05m", 3), ("10m   5s", 605)]:
            self.assertEqual(parse_duration(text), want, text)
            self.assertIs(type(parse_duration(text)), int)

    def test_invalid(self):
        for text in ["", "   ", "1 h", "30m1h", "1h1h", ".5h", "1.h", "-1h", "+5m", "1e3s", "1,000s", "1h30", "1.5", "0.5s", "1.0001m", "h", "1x", "1h30m ago", "1.2.3h"]:
            with self.assertRaises(ValueError, msg=text):
                parse_duration(text)

    def test_type(self):
        for v in (90, None, 1.5, b"1h"):
            with self.assertRaises(TypeError):
                parse_duration(v)


if __name__ == "__main__":
    unittest.main()
