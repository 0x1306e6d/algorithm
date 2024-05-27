"""
    File: 438.py
    Title: Find All Anagrams in a String
    Difficulty: Medium
"""

from typing import List


def chardict():
    d = {}
    for c in range(ord("a"), ord("z") + 1):
        d[chr(c)] = 0
    return d


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens, lenp = len(s), len(p)
        if lens < lenp:
            return []

        target = chardict()
        for c in p:
            target[c] += 1

        ans = []
        window = chardict()
        for i in range(lens):
            if i >= lenp:
                j = i - lenp
                window[s[j]] -= 1
            window[s[i]] += 1
            if window == target:
                ans.append(i - lenp + 1)
        return ans
