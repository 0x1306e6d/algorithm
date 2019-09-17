"""
    4307 : 개미
    URL : https://www.acmicpc.net/problem/4307
    Input :
        2
        10 3
        2
        6
        7
        214 7
        11
        12
        7
        13
        176
        23
        191
    Output :
        4 8
        38 207
"""

T = int(input())
for _ in range(T):
    length, n = map(int, input().split())
    ants = []
    for i in range(n):
        ants.append(int(input()))

    min_time = 0
    max_time = 0
    for ant in ants:
        min_time = max(min_time, min(ant, length - ant))
        max_time = max(max_time, max(ant, length - ant))
    print('{} {}'.format(min_time, max_time))
