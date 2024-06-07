"""
    File: 1061.py
    Title: Lexicographically Smallest Equivalent String
    Difficulty: Medium
"""


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(uf, c):
            if c not in uf:
                uf[c] = c
            elif uf[c] != c:
                uf[c] = find(uf, uf[c])
            return uf[c]

        uf = {}
        for c1, c2 in zip(s1, s2):
            r1, r2 = find(uf, c1), find(uf, c2)
            if r1 > r2:
                uf[r1] = r2
            else:
                uf[r2] = r1

        ans = ""
        for c in baseStr:
            ans += find(uf, c)
        return ans
