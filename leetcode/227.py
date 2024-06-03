"""
    File: 227.py
    Title: Basic Calculator II
    Difficulty: Medium
"""


class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        ans = current = last = 0
        op = None
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
            elif "0" <= c <= "9":
                start = i
                while i < len(s) and "0" <= s[i] <= "9":
                    i += 1
                current = int(s[start:i])
            if c == "+" or c == "-" or c == "*" or c == "/" or i == len(s):
                if op is None:
                    last = current
                elif op == "+":
                    ans += last
                    last = current
                elif op == "-":
                    ans += last
                    last = -current
                elif op == "*":
                    last = last * current
                else:
                    last = int(last / current)
                op = c
                current = 0
                i += 1
        return ans + last
