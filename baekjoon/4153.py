"""
    4153 : 직각삼각형
    URL : https://www.acmicpc.net/problem/4153
    Input :
        6 8 10
        25 52 60
        5 12 13
        0 0 0
    Output :
        right
        wrong
        right
"""

while True:
    a, b, c = map(int, input().split())
    if (a + b + c) == 0:
        break

    h = max([a, b, c])
    if (a**2 + b**2 + c**2) == (h**2 * 2):
        print("right")
    else:
        print("wrong")
