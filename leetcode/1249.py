"""
    File: 1249.py
    Title: Minimum Remove to Make Valid Parentheses
    Difficulty: Medium
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = [True] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    valid[i] = False

        for i in stack:
            valid[i] = False

        ans = ""
        for i, c in enumerate(s):
            if valid[i]:
                ans += c
        return ans
