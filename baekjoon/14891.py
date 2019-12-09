"""
    14891 : 톱니바퀴
    URL : https://www.acmicpc.net/problem/14891
    Input #1:
        10101111
        01111101
        11001110
        00000010
        2
        3 -1
        1 1
    Output #1:
        7
    Input #2:
        11111111
        11111111
        11111111
        11111111
        3
        1 1
        2 1
        3 1
    Output #2:
        15
    Input #3:
        10001011
        10000011
        01011011
        00111101
        5
        1 1
        2 1
        3 1
        4 1
        1 -1
    Output #3:
        6
    Input #4:
        10010011
        01010011
        11100011
        01010101
        8
        1 1
        2 1
        3 1
        4 1
        1 -1
        2 -1
        3 -1
        4 -1
    Output #4:
        5
"""

from copy import copy


def rotate(gear, clockwise):
    if clockwise:
        return [gear[-1]] + gear[:-1]
    else:
        return gear[1:] + [gear[0]]


gears = {}
for i in range(1, 4 + 1):
    gears[i] = list(map(lambda c: 'N' if c == '0' else 'S', input()))

k = int(input())
for i in range(k):
    n, d = map(int, input().split())

    next_gears = copy(gears)
    next_gears[n] = rotate(gears[n], d == 1)

    clockwise = (d == 1)
    for m in range(n - 1, 0, -1):
        if gears[m + 1][6] == gears[m][2]:
            break
        clockwise = not clockwise
        next_gears[m] = rotate(gears[m], clockwise)

    clockwise = (d == 1)
    for m in range(n + 1, 4 + 1, 1):
        if gears[m - 1][2] == gears[m][6]:
            break
        clockwise = not clockwise
        next_gears[m] = rotate(gears[m], clockwise)

    gears = next_gears

score = 0
for i in range(1, 4 + 1):
    if gears[i][0] == 'S':
        score += int(pow(2, i - 1))

print(score)
