"""
    File: 990.py
    Title: Satisfiability of Equality Equations
    Difficulty: Medium
"""

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(uf, i):
            if i not in uf:
                uf[i] = i
            elif uf[i] != i:
                uf[i] = find(uf, uf[i])
            return uf[i]

        uf = {}
        for equation in equations:
            if equation[1] == "=":
                a, b = equation[0], equation[3]
                ra, rb = find(uf, a), find(uf, b)
                uf[ra] = uf[rb]
        for equation in equations:
            if equation[1] == "!":
                a, b = equation[0], equation[3]
                if find(uf, a) == find(uf, b):
                    return False
        return True
