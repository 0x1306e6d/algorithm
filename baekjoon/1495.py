"""
    1495 : 기타리스트
    URL : https://www.acmicpc.net/problem/1495
    Input :
        3 5 10
        5 3 7
    Output :
        10
"""

import sys
sys.setrecursionlimit(987654321)

MAX_N = 101
MAX_M = 1001

n, s, m = map(int, input().split())
diffs = list(map(int, input().split()))
cache = [[-1 for m in range(MAX_M)] for n in range(MAX_N)]


def play(i, current_volume):
    if i == n:
        return current_volume

    if cache[i][current_volume] != -1:
        return cache[i][current_volume]

    volume = None
    volume_diff = diffs[i]

    if (current_volume + volume_diff) <= m:
        next_volume = play(i + 1, current_volume + volume_diff)
        if next_volume is not None:
            volume = next_volume

    if (current_volume - volume_diff) >= 0:
        next_volume = play(i + 1, current_volume - volume_diff)
        if next_volume is not None:
            if volume is None:
                volume = next_volume
            else:
                volume = max(volume, next_volume)

    cache[i][current_volume] = volume
    return cache[i][current_volume]


last_volume = play(0, s)
if last_volume is None:
    print(-1)
else:
    print(last_volume)
