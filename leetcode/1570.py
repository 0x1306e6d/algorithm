"""
    File: 1570.py
    Title: Dot Product of Two Sparse Vectors
    Difficulty: Medium
"""

from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {}
        for i, num in enumerate(nums):
            if num == 0:
                continue
            self.values[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        ans = 0
        for i in self.values:
            if i not in vec.values:
                continue
            ans += self.values[i] * vec.values[i]
        return ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
