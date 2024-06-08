"""
    File: 266.py
    Title: Palindrome Permutation
    Difficulty: Easy
"""

from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        odd = 0
        for c in counter:
            if counter[c] % 2 == 1:
                odd += 1
        return True if odd <= 1 else False
