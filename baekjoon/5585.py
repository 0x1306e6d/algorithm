"""
    5585 : 거스름돈
    URL : https://www.acmicpc.net/problem/5585
    Input :
        380
    Output :
        4
"""

n = 1000 - int(input())
c = 0
for i in [500, 100, 50, 10, 5, 1]:
    while (n - i) >= 0:
        n = (n - i)
        c = (c + 1)
print(c)
