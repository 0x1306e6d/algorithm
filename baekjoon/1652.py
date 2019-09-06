"""
    1652 : 누울 자리를 찾아라
    URL : https://www.acmicpc.net/problem/1652
    Input :
        5
        ....X
        ..XX.
        .....
        .XX..
        X....
    Output :
        5 4
"""

n = int(input())

room_x = [[True for _ in range(n)] for _ in range(n)]
room_y = [[True for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = input()
    for j in range(n):
        if row[j] == 'X':
            room_x[i][j] = False
            room_y[j][i] = False

x_count = 0
y_count = 0

for row in room_x:
    space = 0

    for x in row:
        if x == True:
            space += 1
        else:
            if space >= 2:
                x_count += 1
            space = 0

    if space >= 2:
        x_count += 1

for column in room_y:
    space = 0

    for y in column:
        if y == True:
            space += 1
        else:
            if space >= 2:
                y_count += 1
            space = 0

    if space >= 2:
        y_count += 1

print("{} {}".format(x_count, y_count))
