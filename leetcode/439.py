"""
    File: 439.py
    Title: Ternary Expression Parser
    Difficulty: Medium
"""


class Solution:
    def parseTernary(self, expression: str) -> str:
        self.idx = 0

        def parse():
            operator = expression[self.idx]
            self.idx += 1
            if self.idx == len(expression) or expression[self.idx] == ":":
                return operator
            self.idx += 1  # ?
            first = parse()
            self.idx += 1  # :
            second = parse()
            return first if operator == "T" else second

        return parse()
