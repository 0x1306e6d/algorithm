"""
    File: 242.py
    Title: Valid Anagram
    Difficulty: Easy
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
