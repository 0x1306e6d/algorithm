"""
    File: 224.py
    Title: Basic Calculator
    Difficulty: Hard
"""


def tokenize(s):
    tokens = []
    idx = 0
    while idx < len(s):
        c = s[idx]
        if c == "+" or c == "-" or c == "(" or c == ")":
            tokens.append(c)
        elif c == " ":
            pass
        else:
            num = c
            idx2 = idx + 1
            while idx2 < len(s) and "0" <= s[idx2] <= "9":
                num += s[idx2]
                idx += 1
                idx2 += 1
            tokens.append(int(num))
        idx += 1
    return tokens


def get_precedence(token):
    if token == "(":
        return 2
    if token == "+" or token == "-":
        return 1
    return 0


class Solution:
    def calculate(self, s: str) -> int:
        self.tokens = tokenize(s)
        self.idx = 0
        return self.eval(0)

    def eval(self, precedence):
        left = self.parse_prefix()

        while self.idx < len(self.tokens) and precedence < get_precedence(
            self.tokens[self.idx]
        ):
            token = self.tokens[self.idx]
            if token != "+" and token != "-":
                break
            self.idx += 1
            right = self.eval(get_precedence(token))
            if token == "+":
                left = left + right
            else:
                left = left - right

        return left

    def parse_prefix(self):
        token = self.tokens[self.idx]
        self.idx += 1

        if token == "(":
            expr = self.eval(0)
            self.idx += 1  # )
            return expr
        elif token == "-":
            right = self.eval(2)
            return -right
        else:
            # should be number
            return token
