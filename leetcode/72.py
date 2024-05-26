"""
    File: 72.py
    Title: Edit Distance
    Difficulty: Medium
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        self.memo = {}
        return self.distance(word1, len(word1) - 1, word2, len(word2) - 1)

    def distance(self, word1, idx1, word2, idx2):
        if idx1 < 0:
            return idx2 + 1
        if idx2 < 0:
            return idx1 + 1
        if (idx1, idx2) in self.memo:
            return self.memo[(idx1, idx2)]
        if word1[idx1] == word2[idx2]:
            self.memo[(idx1, idx2)] = self.distance(word1, idx1 - 1, word2, idx2 - 1)
        else:
            insert = self.distance(word1, idx1, word2, idx2 - 1)
            delete = self.distance(word1, idx1 - 1, word2, idx2)
            replace = self.distance(word1, idx1 - 1, word2, idx2 - 1)
            self.memo[(idx1, idx2)] = min(insert, delete, replace) + 1
        return self.memo[(idx1, idx2)]
