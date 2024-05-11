"""
    File: 380.py
    Title: Insert Delete GetRandom O(1)
    Difficulty: Medium
"""

import random


class RandomizedSet:

    def __init__(self):
        self.cache = {}

    def insert(self, val: int) -> bool:
        present = val in self.cache
        self.cache[val] = True
        return not present

    def remove(self, val: int) -> bool:
        present = val in self.cache
        if present:
            del self.cache[val]
        return present

    def getRandom(self) -> int:
        return list(self.cache.keys())[random.randint(0, len(self.cache) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
