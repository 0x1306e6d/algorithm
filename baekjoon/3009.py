"""
    3009 : 네 번째 점
    URL : https://www.acmicpc.net/problem/3009
    Input :
        30 20
        10 10
        10 20
    Output :
        30 10
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x4 = x1
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2

y4 = y1
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2

print("{} {}".format(x4, y4))
