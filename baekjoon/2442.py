"""
    2442 : 별 찍기 - 5
    URL : https://www.acmicpc.net/problem/2442
    Input :
        5
    Output :
            *
           ***
          *****
         *******
        *********
"""

from itertools import repeat

n = int(input())
m = (2 * n) - 1
for i in range(n - 1, 0 - 1, -1):
    space = i
    star = m - (2 * i)

    print("{}{}".format(''.join(repeat(' ', space)),
                        ''.join(repeat('*', star))))
