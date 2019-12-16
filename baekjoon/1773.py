"""
    1773 : 폭죽쇼
    URL : https://www.acmicpc.net/problem/1773
    Input :
        2 20
        4
        6
    Output :
        7
"""

n, c = map(int, input().split())

periods = []
for i in range(n):
    period = int(input())
    periods.append(period)

count = 0
for i in range(1, c + 1):
    bomb = False

    for j in periods:
        if (i % j) == 0:
            bomb = True
            break

    if bomb:
        count += 1

print(count)
