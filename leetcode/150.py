"""
    File: 150.py
    Title: Evaluate Reverse Polish Notation
    Difficulty: Medium
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval(i):
            if i == 0:
                return int(tokens[i]), 0
            token = tokens[i]
            if token == "+" or token == "-" or token == "*" or token == "/":
                right, right_idx = eval(i - 1)
                left, left_idx = eval(right_idx - 1)
                ans = 0
                if token == "+":
                    ans = left + right
                elif token == "-":
                    ans = left - right
                elif token == "*":
                    ans = left * right
                else:
                    sign = (left * right) < 0
                    ans = abs(left) // abs(right)
                    if sign:
                        ans *= -1
                return ans, left_idx
            else:
                return int(tokens[i]), i

        ans = eval(len(tokens) - 1)
        return ans[0]
