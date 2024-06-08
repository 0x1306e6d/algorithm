"""
    File: 1857.py
    Title: Largest Color Value in a Directed Graph
    Difficulty: Hard
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        adj = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in edges:
            adj[a].append(b)
            indegree[b] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        graph = []
        while q:
            u = q.popleft()
            graph.append(u)

            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if len(graph) != n:
            return -1

        memo = {}

        def dfs(u):
            if u in memo:
                return memo[u]

            ans = defaultdict(int)
            for v in adj[u]:
                child = dfs(v)
                if child is None:
                    return None
                for color in child:
                    ans[color] = max(ans[color], child[color])
            ans[colors[u]] += 1
            memo[u] = ans
            return ans

        ans = 0
        for i in range(n):
            color = dfs(graph[i])
            ans = max(ans, max(color.values()))
        return ans
