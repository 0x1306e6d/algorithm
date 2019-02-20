"""
    11116 : 교통량
    URL : https://www.acmicpc.net/problem/11116
    Input :
        2
        4
        17 517 1432 1932
        432 932 1017 1517
        6
        235 451 735 951 2351 2851
        1235 1351 1451 1735 1851 1951
    Output :
        1
        2
"""

n = int(input())
for _ in range(n):
    m = int(input())
    left = list(map(int, input().split(' ')))
    right = list(map(int, input().split(' ')))

    left_first = []
    for t in left:
        if (t - 500) not in left_first and (t - 1000) not in right:
            left_first.append(t)

    print(len(left_first))
