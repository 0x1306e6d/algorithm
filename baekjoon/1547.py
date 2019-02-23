"""
    1547 : 공
    URL : https://www.acmicpc.net/problem/1547
    Input :
        4
        3 1
        2 3
        3 1
        3 2
    Output :
        3
"""

ball = 1

m = int(input())
for _ in range(m):
    x, y = map(int, input().split(' '))
    if x is ball:
        ball = y
    elif y is ball:
        ball = x

print(ball)
