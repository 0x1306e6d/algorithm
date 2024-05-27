"""
    File: 32.py
    Title: Longest Valid Parentheses
    Difficulty: Hard
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        valid = [False] * n
        for i, c1 in enumerate(s):
            if c1 == ")":
                if not stack:
                    continue
                c2, j = stack.pop()
                if c2 == "(":
                    valid[i] = valid[j] = True
                else:
                    stack = []
            else:
                stack.append((c1, i))

        ans = current = 0
        for v in valid:
            if v:
                current += 1
            else:
                current = 0
            ans = max(ans, current)
        return ans
