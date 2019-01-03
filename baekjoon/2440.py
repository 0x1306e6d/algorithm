"""
    2440 : 별 찍기 - 3
    URL : https://www.acmicpc.net/problem/2440
    Input :
        5
    Output :
        *****
        ****
        ***
        **
        *
"""
from itertools import repeat

N = int(input())
for i in range(N, 0, -1):
    print(''.join(list(repeat('*', i))))
