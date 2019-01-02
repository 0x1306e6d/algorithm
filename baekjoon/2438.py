"""
    2438 : 별 찍기 - 1
    URL : https://www.acmicpc.net/problem/2438
    Input :
        5
    Output :
        *
        **
        ***
        ****
        *****
"""
from itertools import repeat

N = int(input())
for i in range(1, N + 1):
    print(''.join(repeat('*', i)))