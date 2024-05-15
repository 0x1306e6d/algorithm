"""
    File: 433.py
    Title: Minimum Genetic Mutation
    Difficulty: Medium
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def mutate(a, b):
            count = 0
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    count += 1
                if count > 1:
                    return False
            return True

        adj = defaultdict(list)
        for i in range(len(bank)):
            if mutate(startGene, bank[i]):
                adj[startGene].append(bank[i])

            for j in range(i + 1, len(bank)):
                if mutate(bank[i], bank[j]):
                    adj[bank[i]].append(bank[j])
                    adj[bank[j]].append(bank[i])

        q = deque()
        q.append((startGene, 0))
        visited = set()
        visited.add(startGene)
        while q:
            g, c = q.pop()
            if g == endGene:
                return c
            for m in adj[g]:
                if m not in visited:
                    visited.add(m)
                    q.append((m, c + 1))
        return -1
