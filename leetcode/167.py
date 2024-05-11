"""
    File: 167.py
    Title: Two Sum II - Input Array Is Sorted
    Difficulty: Medium
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            s = numbers[i] + numbers[j]
            if s > target:
                j -= 1
            else:
                i += 1
        return [i + 1, j + 1]
