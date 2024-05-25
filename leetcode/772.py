"""
    File: 772.py
    Title: Basic Calculator III
    Difficulty: Hard
"""


def tokenize(s):
    tokens = []
    idx = 0
    while idx < len(s):
        c = s[idx]
        if c == "+" or c == "-" or c == "*" or c == "/":
            tokens.append(c)
        elif c == "(" or c == ")":
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
        return 3
    if token == "*" or token == "/":
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

        while self.has_token() and precedence < get_precedence(self.tokens[self.idx]):
            token = self.tokens[self.idx]
            self.idx += 1
            right = self.eval(get_precedence(token))
            if token == "+":
                left = left + right
            elif token == "-":
                left = left - right
            elif token == "*":
                left = left * right
            elif token == "/":
                left = int(left / right)

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

    def has_token(self):
        return self.idx < len(self.tokens)
