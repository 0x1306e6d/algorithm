"""
    File: 1768.py
    Title: Merge Strings Alternately
    Difficulty: Easy
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        ans = ""
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1
        if i < len(word1):
            ans += word1[i:]
        if j < len(word2):
            ans += word2[j:]
        return ans
