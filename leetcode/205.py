"""
    File: 205.py
    Title: Isomorphic Strings
    Difficulty: Easy
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars = {}
        idx = 0
        s_idx = []
        for c in s:
            if c in chars:
                s_idx.append(chars[c])
            else:
                s_idx.append(idx)
                chars[c] = idx
                idx += 1

        chars = {}
        idx = 0
        t_idx = []
        for c in t:
            if c in chars:
                t_idx.append(chars[c])
            else:
                t_idx.append(idx)
                chars[c] = idx
                idx += 1

        return s_idx == t_idx
