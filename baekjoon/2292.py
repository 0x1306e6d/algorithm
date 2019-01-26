"""
    2292 : 벌집
    URL : https://www.acmicpc.net/problem/2292
    Input :
        13
    Output :
        3
"""

N = int(input())

a = 1
i = 1
while a < N:
    a += (i * 6)
    i += 1

print(i)
