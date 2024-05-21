"""
    File: 140.py
    Title: Word Break II
    Difficulty: Hard
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = {}

        for word in wordDict:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[0] = word

        def bt(i):
            ans = []
            node = trie
            for j in range(i, len(s)):
                c = s[j]
                if c not in node:
                    break
                node = node[c]
                if 0 in node:
                    w1 = node[0]
                    if j + 1 == len(s):
                        ans.append(w1)
                    else:
                        for w2 in bt(j + 1):
                            ans.append(f"{w1} {w2}")
            return ans

        return bt(0)
