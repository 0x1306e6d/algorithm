"""
    11123 : 양 한마리... 양 두마리...
    URL : https://www.acmicpc.net/problem/11123
    Input :
        2
        4 4
        #.#.
        .#.#
        #.##
        .#.#
        3 5
        ###.#
        ..#..
        #.###
    Output :
        6
        3
"""

from queue import deque

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]

t = int(input())
for tc in range(t):
    h, w = map(int, input().split())
    field = []
    for y in range(h):
        row = input()
        field.append(row)

    count = 0
    visited = [[False for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if visited[y][x]:
                continue
            if field[y][x] == '.':
                continue

            visited[y][x] = True

            q = deque()
            q.append((x, y))
            while q:
                p = q.pop()

                for dx, dy in zip(__dx__, __dy__):
                    nx = p[0] + dx
                    ny = p[1] + dy
                    if (nx >= 0) and (nx < w) and (ny >= 0) and (ny < h):
                        if field[ny][nx] == '#' and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((nx, ny))

            count += 1

    print(count)
