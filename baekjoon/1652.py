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

for x in room_x:
    a = False
    for b in x:
        if (a == True) and (b == True):
            x_count += 1
        a = b

for y in room_y:
    a = False
    for b in y:
        if (a == True) and (b == True):
            y_count += 1
        a = b

print("{} {}".format(x_count, y_count))
