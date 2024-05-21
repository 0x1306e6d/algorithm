"""
    File: 1614.py
    Title: Maximum Nesting Depth of the Parentheses
    Difficulty: Easy
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for c in s:
            if c == "(":
                stack.append(c)
                ans = max(ans, len(stack))
            elif c == ")":
                stack.pop()
            else:
                continue
        return ans
