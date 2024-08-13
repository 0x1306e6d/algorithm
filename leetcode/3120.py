"""
    File: 3120.py
    Title: Count the Number of Special Characters I
    Difficulty: Easy
"""

from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        memo = defaultdict(int)
        ans = 0
        for c in s:
            if "A" <= c <= "Z":
                lowercase = c.lower()
                if lowercase in s:
                    ans += 1
        return ans
