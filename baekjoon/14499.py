"""
    14499 : 주사위 굴리기
    URL : https://www.acmicpc.net/problem/14499
    Input #1 :
        4 2 0 0 8
        0 2
        3 4
        5 6
        7 8
        4 4 4 1 3 3 3 2
    Output #1 :
        0
        0
        3
        0
        0
        8
        6
        3
    Input #2 :
        3 3 1 1 9
        1 2 3
        4 0 5
        6 7 8
        1 3 2 2 4 4 1 1 3
    Output #2 :
        0
        0
        0
        3
        0
        1
        0
        6
        0
    Input #3 :
        2 2 0 0 16
        0 2
        3 4
        4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
    Output #3 :
        0
        0
        0
        0
    Input #4 :
        3 3 0 0 16
        0 1 2
        3 4 5
        6 7 8
        4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2
    Output #4 :
        0
        0
        0
        6
        0
        8
        0
        2
        0
        8
        0
        2
        0
        8
        0
        2
"""

EAST = 1
WEST = 2
NORTH = 3
SOUTH = 4

top = 0
back = 0
right = 0
left = 0
front = 0
bottom = 0

matrix = []

n, m, y, x, k = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
commands = list(map(int, input().split()))

for command in commands:
    if command == EAST:
        if (x + 1) > (m - 1):
            continue
        x = x + 1
        next_top = left
        next_back = back
        next_right = top
        next_left = bottom
        next_front = front
        next_bottom = right
    elif command == WEST:
        if (x - 1) < 0:
            continue
        x = x - 1
        next_top = right
        next_back = back
        next_right = bottom
        next_left = top
        next_front = front
        next_bottom = left
    elif command == NORTH:
        if (y - 1) < 0:
            continue
        y = y - 1
        next_top = front
        next_back = top
        next_right = right
        next_left = left
        next_front = bottom
        next_bottom = back
    elif command == SOUTH:
        if (y + 1) > (n - 1):
            continue
        y = y + 1
        next_top = back
        next_back = bottom
        next_right = right
        next_left = left
        next_front = top
        next_bottom = front

    if matrix[y][x] == 0:
        matrix[y][x] = next_bottom
    else:
        next_bottom = matrix[y][x]
        matrix[y][x] = 0

    top = next_top
    back = next_back
    right = next_right
    left = next_left
    front = next_front
    bottom = next_bottom

    print(top)
