"""
    File: 3.py
    Title: Longest Substring Without Repeating Characters
    Difficulty: Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        longest = 0
        start = 0
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = i
            else:
                if chars[c] >= start:
                    longest = max(longest, i - start)
                    start = chars[c] + 1
                chars[c] = i
        return max(longest, len(s) - start)
