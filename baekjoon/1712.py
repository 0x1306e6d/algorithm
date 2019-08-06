"""
    1712 : 손익분기점
    URL : https://www.acmicpc.net/problem/1712
    Input :
        1000 70 170
    Output :
        11
"""

import math

a, b, c = map(int, input().split())

profit = c - b
if profit <= 0:
    print(-1)
else:
    x = math.ceil(a / profit)
    income = c * x
    outcome = a + (b * x)

    if income == outcome:
        print(x + 1)
    else:
        print(x)
