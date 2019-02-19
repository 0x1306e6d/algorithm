"""
    2443 : 별 찍기 - 6
    URL : https://www.acmicpc.net/problem/2443
    Input :
        5
    Output :
        *********
         *******
          *****
           ***
            *
"""

N = int(input())

n = (2 * N) + 1
for i in range(N):
    n = n - 2
    print("{}{}".format(' ' * i, '*' * n))
