"""
    11021 : A+B - 7
    URL : https://www.acmicpc.net/problem/11021
    Input :
        5
        1 1
        2 3
        3 4
        9 8
        5 2
    Output :
        Case #1: 2
        Case #2: 5
        Case #3: 7
        Case #4: 17
        Case #5: 7
"""

T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split(' '))
    print("Case #{}: {}".format(t, a + b))
