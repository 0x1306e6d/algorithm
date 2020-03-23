"""
    1789 : 수들의 합
    URL : https://www.acmicpc.net/problem/1789
    Input :
        200
    Output :
        19
"""

s = int(input())
s2 = s * 2

n = 1
while True:
    if n * (n + 1) > s2:
        print(n - 1)
        break

    n += 1
