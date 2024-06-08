"""
    File: 1489.py
    Title: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
    Difficulty: Hard
"""

from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]],
    ) -> List[List[int]]:
        sorted_edges = []
        for i in range(len(edges)):
            a, b, w = edges[i]
            sorted_edges.append([w, a, b, i])
        sorted_edges.sort()

        def find(uf, x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        mst = 0
        uf = {}
        for w, a, b, i in sorted_edges:
            ra, rb = find(uf, a), find(uf, b)
            if ra != rb:
                mst += w
                uf[ra] = rb

        critical = set()
        for i in range(len(sorted_edges)):
            st = 0
            uf = {}
            for w, a, b, j in sorted_edges:
                if i == j:
                    continue
                ra, rb = find(uf, a), find(uf, b)
                if ra != rb:
                    st += w
                    uf[ra] = rb
            if st != mst:
                critical.add(i)

        pseudo_critical = []
        for w, a, b, i in sorted_edges:
            if i in critical:
                continue
            st = w
            uf = {a: a, b: a}
            for w, a, b, j in sorted_edges:
                if i == j:
                    continue
                ra, rb = find(uf, a), find(uf, b)
                if ra != rb:
                    st += w
                    uf[ra] = rb
            if st == mst:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
