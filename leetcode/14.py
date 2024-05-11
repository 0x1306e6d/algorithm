"""
    File: 14.py
    Title: Longest Common Prefix
    Difficulty: Easy
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        while True:
            idx = len(lcp)
            common = True
            prefix = ""
            for s in strs:
                if idx >= len(s):
                    return lcp
                if prefix == "":
                    prefix = s[idx]
                elif prefix != s[idx]:
                    common = False
                    break
            if common:
                lcp += prefix
            else:
                return lcp
