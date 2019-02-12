"""
    9325 : 얼마?
    URL : https://www.acmicpc.net/problem/9325
    Input :
        2
        10000
        2
        1 2000
        3 400
        50000
        0
    Output :
        13200
        50000
"""

T = int(input())
for _ in range(T):
    s = int(input())
    n = int(input())
    for _ in range(n):
        count, price = map(int, input().split(' '))
        s += (count * price)
    print(s)
