"""
    1100 : 하얀 칸
    URL : https://www.acmicpc.net/problem/1100
    Input :
        .F.F...F
        F...F.F.
        ...F.F.F
        F.F...F.
        .F...F..
        F...F.F.
        .F.F.F.F
        ..FF..F.
    Output :
        1
"""

chess = []
for i in range(8):
    chess.append(input())

count = 0
for i, row in enumerate(chess):
    for j, c in enumerate(row):
        if c == 'F':
            if ((i % 2) == 0) and ((j % 2) == 0):
                count += 1
            if ((i % 2) == 1) and ((j % 2) == 1):
                count += 1
print(count)
