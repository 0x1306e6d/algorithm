"""
    1005 : ACM Craft
    URL : https://www.acmicpc.net/problem/1005
    Input :
        2
        4 4
        10 1 100 10
        1 2
        1 3
        2 4
        3 4
        4
        8 8
        10 20 1 5 8 7 1 43
        1 2
        1 3
        2 4
        2 5
        3 6
        5 7
        6 7
        7 8
        7
    Output :
        120
        39
"""

import sys
import queue


def tsort(w, costs, graph, indegree):
    q = queue.Queue()
    dp = {}

    for i in graph:
        dp[i] = 0
        if indegree[i] == 0:
            q.put(i)
            dp[i] = costs[i]

    while not q.empty():
        i = q.get()
        if i == w:
            break

        for j in graph[i]:
            if indegree[j] > 0:
                dp[j] = max(dp[j], dp[i] + costs[j])

                indegree[j] -= 1
                if indegree[j] == 0:
                    q.put(j)

    return dp[w]


T = int(sys.stdin.readline())
for t in range(T):
    n, k = map(int, sys.stdin.readline().split())

    costs = list(map(int, sys.stdin.readline().split()))

    graph = {}
    indegree = {}
    for i in range(n):
        graph[i] = []
        indegree[i] = 0
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x - 1].append(y - 1)
        indegree[y - 1] += 1

    w = int(sys.stdin.readline()) - 1
    sys.stdout.write("{}\n".format(tsort(w, costs, graph, indegree)))
