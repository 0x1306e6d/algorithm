"""
    File: 20.py
    Title: Valid Parentheses
    Difficulty: Easy
"""


class Solution:
    def isValid(self, s: str) -> bool:
        open = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c == ")" or c == "}" or c == "]":
                if stack and stack.pop(-1) == open[c]:
                    pass
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
