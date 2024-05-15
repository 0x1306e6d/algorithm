"""
    File: 383.py
    Title: Ransom Note
    Difficulty: Easy
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = Counter(magazine)
        for c in ransomNote:
            if s[c] == 0:
                return False
            s[c] -= 1
        return True
