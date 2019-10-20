"""
    5612 : 터널의 입구와 출구
    URL : https://www.acmicpc.net/problem/5612
    Input :
        3
        2
        2 3
        2 3
        4 1
    Output :
        3
"""

n = int(input())
m = int(input())

s = m
for j in range(n):
    i, o = map(int, input().split())
    m = (m + i - o)
    if m < 0:
        s = 0
        break
    else:
        s = max(s, m)


print(s)
