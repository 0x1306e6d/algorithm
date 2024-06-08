"""
    File: 839.py
    Title: Similar String Groups
    Difficulty: Hard
"""

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(s1, s2):
            a1 = a2 = b1 = b2 = None
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    continue
                if a1 is None:
                    a1, b1 = c1, c2
                elif a2 is None:
                    a2, b2 = c1, c2
                else:
                    return False
            if a2 is None:
                return False
            return a1 == b2 and b1 == a2

        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for i in range(len(strs)):
            s1 = strs[i]
            for j in range(i + 1, len(strs)):
                s2 = strs[j]
                r1, r2 = find(s1), find(s2)
                if similar(s1, s2):
                    uf[r1] = r2

        roots = set()
        for s in strs:
            roots.add(find(s))
        return len(roots)
