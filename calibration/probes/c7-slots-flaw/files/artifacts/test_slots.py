import unittest
from booking.slots import free_slots
from booking.intervals import merge


class T(unittest.TestCase):
    def test_back_to_back(self):
        self.assertEqual(free_slots(540, 1020, [(600, 660), (660, 720)]), [(540, 600), (720, 1020)])

    def test_unsorted(self):
        self.assertEqual(free_slots(540, 1020, [(720, 780), (600, 660)]), [(540, 600), (660, 720), (780, 1020)])

    def test_contained(self):
        self.assertEqual(free_slots(540, 1020, [(600, 900), (650, 700)]), [(540, 600), (900, 1020)])

    def test_starts_before_day(self):
        self.assertEqual(free_slots(540, 1020, [(500, 600)]), [(600, 1020)])

    def test_ends_after_day(self):
        self.assertEqual(free_slots(540, 1020, [(1000, 1100)]), [(540, 1000)])

    def test_wholly_before_day(self):
        self.assertEqual(free_slots(540, 1020, [(100, 200)]), [(540, 1020)])

    def test_min_len(self):
        self.assertEqual(free_slots(540, 1020, [(600, 660), (665, 700)], 10), [(540, 600), (700, 1020)])

    def test_merge_touching_and_unsorted(self):
        self.assertEqual(merge([(5, 9), (1, 3), (3, 4), (8, 12)]), [(1, 4), (5, 12)])


if __name__ == "__main__":
    unittest.main()
