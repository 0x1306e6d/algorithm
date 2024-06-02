"""
    File: 28.py
    Title: Find the Index of the First Occurrence in a String
    Difficulty: Easy
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        pi = [0] * m
        for begin in range(1, m):
            for i in range(m - begin):
                if needle[begin + i] != needle[i]:
                    break
                pi[begin + i] = max(pi[begin + i], i + 1)

        begin = matched = 0
        while begin <= n - m:
            if matched < m and haystack[begin + matched] == needle[matched]:
                matched += 1
                if matched == m:
                    return begin
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - pi[matched - 1]
                    matched = pi[matched - 1]
        return -1
