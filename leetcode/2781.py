"""
    File: 2781.py
    Title: Length of the Longest Valid Substring
    Difficulty: Hard
"""

from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        trie = {}
        for w in forbidden:
            node = trie
            for c in reversed(w):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[0] = w
        ans = 0
        i = 0
        while i < len(word):
            j = i
            invalid = ""
            while j < len(word):
                node = trie
                for k in range(j, i - 1, -1):
                    c = word[k]
                    if c not in node:
                        break
                    node = node[c]
                    if 0 in node:
                        invalid = node[0]
                        break
                if invalid:
                    break
                j += 1
            ans = max(ans, j - i)
            if invalid:
                i = j - len(invalid) + 2
            else:
                break
        return ans
