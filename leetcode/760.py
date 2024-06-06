"""
    File: 760.py
    Title: Find Anagram Mappings
    Difficulty: Easy
"""

from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indecies = {}
        for i, n in enumerate(nums2):
            indecies[n] = i
        ans = []
        for n in nums1:
            ans.append(indecies[n])
        return ans
