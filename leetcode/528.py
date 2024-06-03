"""
    File: 528.py
    Title: Random Pick with Weight
    Difficulty: Medium
"""

import random
from typing import List


def bisect_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.weights.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = random.random() * self.total
        return bisect_left(self.weights, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
