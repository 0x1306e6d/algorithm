"""
    2441 : 별 찍기 - 4
    URL : https://www.acmicpc.net/problem/2441
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
    print(''.join(list(repeat(' ', N - i)) + list(repeat('*', i))))
