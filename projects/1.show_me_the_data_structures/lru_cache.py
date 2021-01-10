"""
Least Recently Used Cache

In case of a cache hit, your get() operation should return the appropriate value
In case of a cache miss, your get() should return -1.

While putting an element in the cache, your set() operation must insert the element
    If the cache is full;
    * you must write code that removes the least recently used entry first
    * then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5
"""
import pytest
from collections import OrderedDict


class LRU_Cache(OrderedDict):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent
        try:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            raise KeyError("cache has a capacity of 0, please reset")
        # Set the value if the key is not present in the cache
        # If the cache is at capacity remove the oldest item
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.cache.popitem(False)  # remove oldest item (left to right)
            self.cache[key] = value


our_cache = LRU_Cache(5)


our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


assert our_cache.get(1) == 1
assert our_cache.get(2) == 2
assert our_cache.get(9) == -1  # 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

assert (
    our_cache.get(3) == -1
)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# edge case
test_cache = LRU_Cache(0)


def test_cache_exception():
    """test that exception is raised for capacity of 0"""
    with pytest.raises(Exception):
        assert test_cache.set(1, 23)  # cache has capacity of zero
