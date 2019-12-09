"""
    2563 : 색종이
    URL : https://www.acmicpc.net/problem/2563
    Input:
        3
        3 7
        15 7
        5 2
    Output:
        260
"""

matrix = []
for i in range(100):
    matrix.append([False for j in range(100)])

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    for j in range(x, x + 10):
        for k in range(y, y + 10):
            matrix[j][k] = True

area = 0
for i in range(100):
    area += len(list(filter(lambda x: x, matrix[i])))
print(area)
