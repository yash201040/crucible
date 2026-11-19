import unittest
from booking.slots import free_slots


class T(unittest.TestCase):
    def test_empty_day(self):
        self.assertEqual(free_slots(540, 1020, []), [(540, 1020)])

    def test_one_meeting(self):
        self.assertEqual(free_slots(540, 1020, [(600, 660)]), [(540, 600), (660, 1020)])

    def test_two_sorted(self):
        self.assertEqual(free_slots(540, 1020, [(600, 660), (720, 780)]), [(540, 600), (660, 720), (780, 1020)])


if __name__ == "__main__":
    unittest.main()
