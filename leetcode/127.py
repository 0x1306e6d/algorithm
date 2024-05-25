"""
    File: 127.py
    Title: Word Ladder
    Difficulty: Hard
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for i in range(len(wordList)):
            word1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                word2 = wordList[j]
                diff = 0
                for c1, c2 in zip(word1, word2):
                    if c1 != c2:
                        diff += 1
                        if diff >= 2:
                            break
                if diff == 1:
                    adj[word1].append(word2)
                    adj[word2].append(word1)

        q = deque()
        for word in wordList:
            diff = 0
            for c1, c2 in zip(beginWord, word):
                if c1 != c2:
                    diff += 1
                    if diff >= 2:
                        break
            if diff == 1:
                q.append((word, 1))
        visited = set()
        while q:
            word1, count = q.popleft()
            if word1 == endWord:
                return count + 1
            visited.add(word1)
            for word2 in adj[word1]:
                if word2 not in visited:
                    q.append((word2, count + 1))
        return 0
