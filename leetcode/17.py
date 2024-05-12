"""
    File: 17.py
    Title: Letter Combinations of a Phone Number
    Difficulty: Medium
"""

from typing import List


letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return letters[digits]
        ans = []
        combs = self.letterCombinations(digits[1:])
        for c in letters[digits[0]]:
            for comb in combs:
                ans.append(c + comb)
        return ans
