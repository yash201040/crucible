import unittest
from lru import LRUCache


class T(unittest.TestCase):
    def test_get_put(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2)
        self.assertEqual(c.get("a"), 1); self.assertEqual(c.get("b"), 2)

    def test_default(self):
        c = LRUCache(2)
        self.assertIsNone(c.get("x")); self.assertEqual(c.get("x", 7), 7)

    def test_evicts_lru(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.put("c", 3)
        self.assertIsNone(c.get("a")); self.assertEqual(c.get("c"), 3)

    def test_get_refreshes(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
        self.assertEqual(c.get("a"), 1); self.assertIsNone(c.get("b"))

    def test_put_refreshes(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.put("a", 10); c.put("c", 3)
        self.assertEqual(c.get("a"), 10); self.assertIsNone(c.get("b"))

    def test_capacity_validation(self):
        with self.assertRaises(ValueError):
            LRUCache(0)


if __name__ == "__main__":
    unittest.main()
