"""
    File: 269.py
    Title: Alien Dictionary
    Difficulty: Hard
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        prev_word = None
        for word in words:
            if prev_word is None:
                for c in word:
                    graph[""].add(c)
            else:
                i = 0
                while i < len(prev_word):
                    c1 = prev_word[i]
                    if i < len(word):
                        c2 = word[i]
                    else:
                        c2 = ""
                    if c1 == c2:
                        i += 1
                    else:
                        graph[c1].add(c2)
                        break
                while i < len(word):
                    graph[""].add(word[i])
                    i += 1
            prev_word = word

        indegree = defaultdict(int)
        for u in graph:
            for v in graph[u]:
                indegree[v] += 1

        ans = []
        q = deque()
        for u in graph:
            if indegree[u] == 0:
                q.append(u)
        while q:
            u = q.popleft()
            ans.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        for u in indegree:
            if indegree[u] > 0:
                return ""
        return "".join(ans)
