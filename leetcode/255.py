"""
    File: 255.py
    Title: Verify Preorder Sequence in Binary Search Tree
    Difficulty: Medium
"""

from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minimum = -float("inf")
        stack = []
        for num in preorder:
            while stack and stack[-1] < num:
                minimum = stack.pop()
            if num < minimum:
                return False
            stack.append(num)
        return stack
