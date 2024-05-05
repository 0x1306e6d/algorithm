from collections import deque

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]


def solution(skyMap):
    rows = len(skyMap)
    if rows == 0:
        return 0
    cols = len(skyMap[0])
    if cols == 0:
        return 0

    clouds = 0
    visited = [[False] * cols for _ in range(rows)]
    for y in range(rows):
        for x in range(cols):
            if visited[y][x]:
                continue
            visited[y][x] = True

            if skyMap[y][x] == "0":
                continue
            clouds += 1

            q = deque()
            q.append((x, y))
            while q:
                xx, yy = q.pop()
                for dx, dy in zip(__dx__, __dy__):
                    xxx, yyy = xx + dx, yy + dy
                    if 0 <= xxx < cols and 0 <= yyy < rows:
                        if skyMap[yyy][xxx] == "1" and not visited[yyy][xxx]:
                            visited[yyy][xxx] = True
                            q.append((xxx, yyy))
    return clouds
