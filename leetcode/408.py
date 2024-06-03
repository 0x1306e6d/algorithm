"""
    File: 408.py
    Title: Valid Word Abbreviation
    Difficulty: Easy
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        tokens = []
        i = 0
        while i < len(abbr):
            c = abbr[i]
            if "a" <= c <= "z":
                tokens.append(c)
                i += 1
            elif c == "0":  # leading zero
                return False
            else:
                start = i
                while i < len(abbr) and "0" <= abbr[i] <= "9":
                    i += 1
                tokens.append(abbr[start:i])

        i = 0
        for token in tokens:
            if i >= len(word):
                return False
            if "a" <= token <= "z":
                if word[i] != token:
                    return False
                i += 1
            else:
                i += int(token)
        return True if i == len(word) else False
