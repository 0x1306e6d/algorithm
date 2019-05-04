"""
    11022 : A+B - 8
    URL : https://www.acmicpc.net/problem/11022
    Input :
        5
        1 1
        2 3
        3 4
        9 8
        5 2
    Output :
        Case #1: 1 + 1 = 2
        Case #2: 2 + 3 = 5
        Case #3: 3 + 4 = 7
        Case #4: 9 + 8 = 17
        Case #5: 5 + 2 = 7
"""

T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split(' '))
    print("Case #{}: {} + {} = {}".format(t, a, b, a + b))
