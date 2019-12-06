"""
    2523 : 별 찍기 - 13
    URL : https://www.acmicpc.net/problem/2523
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

for i in range(1, n + 1, 1):
    print(''.join(map(lambda x: '*', range(i))))
for i in range(n - 1, 0, -1):
    print(''.join(map(lambda x: '*', range(i))))
