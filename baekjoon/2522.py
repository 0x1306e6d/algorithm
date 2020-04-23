"""
    2522 : 별 찍기 - 12
    URL : https://www.acmicpc.net/problem/2522
    Input :
        3
    Output :
          *
         **
        ***
         **
         *
"""

n = int(input())

for i in range(1, n):
    print('{}{}'.format(' ' * (n - i), '*' * i))

for i in range(n, 0, -1):
    print('{}{}'.format(' ' * abs(i - n), '*' * i))
