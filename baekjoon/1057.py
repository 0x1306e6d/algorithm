"""
    1057 : 토너먼트
    URL : https://www.acmicpc.net/problem/1057
    Input :
        16 8 9
    Output :
        4
"""

import math

N, kim, lim = map(int, input().split(' '))

for r in range(1, int(math.ceil(math.log2(N))) + 1):
    left = min(kim, lim)
    right = max(kim, lim)
    if (right % 2) == 0 and right == (left + 1):
        break

    kim = (kim + 1) // 2
    lim = (lim + 1) // 2

print(r)
