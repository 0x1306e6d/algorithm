"""
    7562 : 나이트의 이동
    URL : https://www.acmicpc.net/problem/7562
    Input :
        3
        8
        0 0
        7 0
        100
        0 0
        30 50
        10
        1 1
        1 1
    Output :
        5
        28
        0
"""

from collections import deque

d = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

t = int(input())
for _ in range(t):
    l = int(input())
    x_from, y_from = map(int, input().split())
    x_to, y_to = map(int, input().split())

    v = [[False for _ in range(l)] for _ in range(l)]
    v[y_from][x_from] = True

    q = deque()
    q.append((x_from, y_from, 0))
    while q:
        x, y, count = q.popleft()

        if (x == x_to) and (y == y_to):
            print(count)
            break

        for dx, dy in d:
            xx = x + dx
            yy = y + dy

            if (xx >= 0) and (xx < l) and (yy >= 0) and (yy < l):
                if not v[yy][xx]:
                    v[yy][xx] = True
                    q.append((xx, yy, count + 1))
