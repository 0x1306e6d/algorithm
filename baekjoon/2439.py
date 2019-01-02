"""
    2439 : 별 찍기 - 2
    URL : https://www.acmicpc.net/problem/2439
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
    print(''.join(list(repeat(' ', N - i)) + list(repeat('*', i))))