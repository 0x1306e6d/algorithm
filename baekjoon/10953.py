"""
    10953 : A+B - 6
    URL : https://www.acmicpc.net/problem/10953
    Input :
        5
        1,1
        2,3
        3,4
        9,8
        5,2
    Output :
        2
        5
        7
        17
        7
"""

T = int(input())
for _ in range(T):
    a, b = map(int, input().split(','))
    print((a + b))
