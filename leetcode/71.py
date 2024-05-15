"""
    File: 71.py
    Title: Simplify Path
    Difficulty: Medium
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for c in path.split("/"):
            if c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            elif c:
                stack.append(c)
        return "/" + "/".join(stack)
