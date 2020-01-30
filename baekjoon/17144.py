"""
    17144 : 미세먼지 안녕!
    URL : https://www.acmicpc.net/problem/17144
    Input #1 :
        7 8 1
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #1 :
        188
    Input #2 :
        7 8 2
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #2 :
        188
    Input #3 :
        7 8 3
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #3 :
        186
    Input #4 :
        7 8 4
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #4 :
        178
    Input #5 :
        7 8 5
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #5 :
        172
    Input #6 :
        7 8 20
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #6 :
        71
    Input #7 :
        7 8 30
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #7 :
        52
    Input #8 :
        7 8 50
        0 0 0 0 0 0 0 9
        0 0 0 0 3 0 0 8
        -1 0 5 0 0 0 22 0
        -1 8 0 0 0 0 0 0
        0 0 0 0 0 10 43 0
        0 0 5 0 15 0 0 0
        0 0 40 0 0 0 20 0
    Output #8 :
        46
"""

__dx__ = [0, 0, -1, 1]
__dy__ = [-1, 1, 0, 0]

room = []

top_air_purifier = None
bottom_air_purifier = None

r, c, t = map(int, input().split())
for i in range(r):
    row = list(map(int, input().split()))
    room.append(row)

    if -1 in row:
        if top_air_purifier is None:
            top_air_purifier = i
        else:
            bottom_air_purifier = i

for _ in range(t):
    next_room = [[0] * c for i in range(r)]
    next_room[top_air_purifier][0] = -1
    next_room[bottom_air_purifier][0] = -1

    # spread dust
    for y in range(r):
        for x in range(c):
            if room[y][x] <= 0:
                continue

            spreaded = room[y][x] // 5
            spreaded_count = 0

            for dx, dy in zip(__dx__, __dy__):
                next_x = x + dx
                next_y = y + dy
                if (0 <= next_x < c) and (0 <= next_y < r):
                    if room[next_y][next_x] == -1:
                        continue

                    next_room[next_y][next_x] += spreaded
                    spreaded_count += 1

            next_room[y][x] += room[y][x] - (spreaded * spreaded_count)

    # run top air purifier
    for y in range(top_air_purifier - 1, 0, -1):
        next_room[y][0] = next_room[y - 1][0]
    for x in range(c - 1):
        next_room[0][x] = next_room[0][x + 1]
    for y in range(top_air_purifier):
        next_room[y][c - 1] = next_room[y + 1][c - 1]
    for x in range(c - 1, 1, -1):
        next_room[top_air_purifier][x] = next_room[top_air_purifier][x - 1]
    next_room[top_air_purifier][1] = 0

    # run bottom air purifier
    for y in range(bottom_air_purifier + 1, r - 1):
        next_room[y][0] = next_room[y + 1][0]
    for x in range(c - 1):
        next_room[r - 1][x] = next_room[r - 1][x + 1]
    for y in range(r - 1, bottom_air_purifier, -1):
        next_room[y][c - 1] = next_room[y - 1][c - 1]
    for x in range(c - 1, 1, -1):
        next_room[bottom_air_purifier][x] = next_room[bottom_air_purifier][x - 1]
    next_room[bottom_air_purifier][1] = 0

    room = next_room

dust = 2  # -1 * 2 for air purifier
for row in room:
    dust += sum(row)
print(dust)
