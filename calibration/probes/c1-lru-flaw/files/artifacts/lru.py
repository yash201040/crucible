from collections import OrderedDict


class LRUCache:
    """Least-recently-used cache with a fixed capacity."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._d = OrderedDict()

    def get(self, key, default=None):
        value = self._d.get(key)
        if value:
            self._d.move_to_end(key)
            return value
        return default

    def put(self, key, value):
        if key in self._d:
            self._d.move_to_end(key)
        self._d[key] = value
        if len(self._d) > self.capacity:
            self._d.popitem(last=False)

    def __len__(self):
        return len(self._d)
