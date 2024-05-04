from collections import deque


def solution(n, tree):
    graph = [[] * n for _ in range(n)]
    for i, j in tree:
        graph[i].append(j)
        graph[j].append(i)

    def diameter(x):
        q = deque()
        q.append(x)
        visited = [False] * n
        visited[x] = True
        dis = [0] * n

        while q:
            y = q.pop()

            for edge in graph[y]:
                if visited[edge]:
                    continue
                visited[edge] = True
                dis[edge] = dis[y] + 1
                q.append(edge)

        idx = x
        longest = 0
        for i, d in enumerate(dis):
            if d > longest:
                idx, longest = i, d
        return idx, longest

    idx, _ = diameter(0)
    _, longest = diameter(idx)
    return longest
