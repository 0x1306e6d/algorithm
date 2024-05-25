"""
    File: 28.py
    Title: Find the Index of the First Occurrence in a String
    Difficulty: Easy
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
