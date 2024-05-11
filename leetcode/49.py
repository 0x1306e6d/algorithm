"""
    File: 49.py
    Title: Group Anagrams
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        ans = []
        for k in anagrams:
            ans.append(anagrams[k])
        return ans
