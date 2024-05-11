"""
    File: 5.py
    Title: Longest Palindromic Substring
    Difficulty: Medium
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [[False] * len(s) for _ in range(len(s))]
        longest = ""
        for i in range(len(s)):
            memo[i][i] = True
            if len(longest) == 0:
                longest = s[i]
            for j in range(i):
                if s[i] != s[j]:
                    continue
                if i - j <= 2 or memo[j + 1][i - 1]:
                    memo[j][i] = True
                    p = s[j : i + 1]
                    if len(p) > len(longest):
                        longest = p
        return longest
