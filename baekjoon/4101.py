"""
    4101 : 크냐?
    URL : https://www.acmicpc.net/problem/4101
    Input :
        1 19
        4 4
        23 14
        0 0
    Output :
        No
        No
        Yes
"""

while True:
    a, b = map(int, input().split())

    if (a == 0) and (b == 0):
        break

    if a > b:
        print('Yes')
    else:
        print('No')
