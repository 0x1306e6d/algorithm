"""
    File: 1048.py
    Title: Longest String Chain
    Difficulty: Medium
"""

from collections import defaultdict
from functools import cache
from typing import List


def predecessor(s1, s2):
    if len(s1) + 1 != len(s2):
        return False
    i1 = i2 = 0
    inserted = False
    while i1 < len(s1):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            if inserted:
                return False
            inserted = True
            i2 += 1
    return True


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(list)
        for i in range(len(words)):
            word1 = words[i]
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if predecessor(word1, word2):
                    graph[word1].append(word2)
                elif predecessor(word2, word1):
                    graph[word2].append(word1)

        @cache
        def dp(word):
            if word not in graph:
                return 1
            ans = 0
            for w in graph[word]:
                ans = max(ans, 1 + dp(w))
            return ans

        ans = 0
        for word in words:
            ans = max(ans, dp(word))
        return ans
