"""
    File: 1203.py
    Title: Sort Items by Groups Respecting Dependencies
    Difficulty: Hard
"""

from collections import defaultdict, deque
from typing import List


def tsort(graph, indegree):
    ans = []
    q = deque()
    for u in range(len(graph)):
        if indegree[u] == 0:
            q.append(u)
    while q:
        u = q.popleft()
        ans.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return ans


class Solution:
    def sortItems(
        self,
        n: int,
        m: int,
        group: List[int],
        beforeItems: List[List[int]],
    ) -> List[int]:
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id

        for u in range(n):
            for v in beforeItems[u]:
                item_graph[v].append(u)
                item_indegree[u] += 1

                if group[u] != group[v]:
                    group_graph[group[v]].append(group[u])
                    group_indegree[group[u]] += 1

        item_sorted = tsort(item_graph, item_indegree)
        if n != len(item_sorted):
            return []
        group_sorted = tsort(group_graph, group_indegree)
        if group_id != len(group_sorted):
            return []

        items = defaultdict(list)
        for item in item_sorted:
            items[group[item]].append(item)

        ans = []
        for g in group_sorted:
            ans += items[g]
        return ans
