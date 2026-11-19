import random
import unittest
from search import lower_bound, upper_bound, count_in_range


class T(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lower_bound([], 3), 0); self.assertEqual(upper_bound([], 3), 0); self.assertEqual(count_in_range([], 0, 9), 0)

    def test_lower_basic(self):
        a = [1, 3, 3, 5, 8]
        self.assertEqual([lower_bound(a, x) for x in (0, 1, 2, 3, 4, 8, 9)], [0, 0, 1, 1, 3, 4, 5])

    def test_upper_basic(self):
        a = [1, 3, 3, 5, 8]
        self.assertEqual([upper_bound(a, x) for x in (0, 1, 2, 3, 4, 8, 9)], [0, 1, 1, 3, 3, 5, 5])

    def test_all_equal(self):
        a = [4] * 7
        self.assertEqual((lower_bound(a, 4), upper_bound(a, 4)), (0, 7))

    def test_count_basic(self):
        a = [1, 3, 3, 5, 8]
        self.assertEqual(count_in_range(a, 3, 5), 3); self.assertEqual(count_in_range(a, 2, 2), 0); self.assertEqual(count_in_range(a, -5, 50), 5)

    def test_count_inverted(self):
        self.assertEqual(count_in_range([1, 2, 3], 3, 1), 0)

    def test_floats(self):
        a = [-2.5, 0.0, 0.5, 0.5, 7.25]
        self.assertEqual(count_in_range(a, 0.5, 0.5), 2); self.assertEqual(lower_bound(a, 0.1), 2)

    def test_single(self):
        self.assertEqual((lower_bound([5], 5), upper_bound([5], 5), count_in_range([5], 5, 5)), (0, 1, 1))

    def test_random_against_brute_force(self):
        rng = random.Random(20261115)
        for _ in range(2000):
            a = sorted(rng.randint(-20, 20) for _ in range(rng.randint(0, 30)))
            x, y = rng.randint(-25, 25), rng.randint(-25, 25)
            self.assertEqual(lower_bound(a, x), sum(1 for e in a if e < x))
            self.assertEqual(upper_bound(a, x), sum(1 for e in a if e <= x))
            self.assertEqual(count_in_range(a, x, y), sum(1 for e in a if x <= e <= y))


if __name__ == "__main__":
    unittest.main()
