"""
    File: 58.py
    Title: Length of Last Word
    Difficulty: Easy
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count1 = count2 = 0
        for c in s:
            if c == " ":
                if count2 > 0:
                    count1, count2 = count2, 0
            else:
                count2 += 1
        if count2 == 0:
            return count1
        return count2
