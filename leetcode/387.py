"""
    File: 387.py
    Title: First Unique Character in a String
    Difficulty: Easy
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for i, c in enumerate(s):
            if c in counter:
                counter[c] = (counter[c][0] + 1, i)
            else:
                counter[c] = (1, i)
        ans = len(s)
        for c in counter:
            if counter[c][0] == 1:
                ans = min(ans, counter[c][1])
        return ans if ans != len(s) else -1
