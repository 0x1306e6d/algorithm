"""
    1085 : 직사각형에서 탈출
    URL : https://www.acmicpc.net/problem/1085
    Input :
        6 2 10 3
    Output :
        1
"""

x, y, w, h = map(int, input().split())
print(min([x, y, w - x, h - y]))
