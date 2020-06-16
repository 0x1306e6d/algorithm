"""
    14226 : 이모티콘
    URL : https://www.acmicpc.net/problem/14226
    Input #1 :
        2
    Output #1 :
        2
    Input #2 :
        4
    Output #2 :
        4
    Input #3 :
        6
    Output #3 :
        5
    Input #4 :
        18
    Output #4 :
        8
"""

import sys

dp = {}

s = int(input())


def operate(n, m, t):
    global dp

    if n == s:
        return t

    if n > s:
        return t + (n - s + 1)

    if t > s:
        return t

    if n in dp and m in dp[n]:
        return dp[n][m]

    if n not in dp:
        dp[n] = {}

    next_t = 987654321
    if n != m:
        next_t = min(next_t, operate(n, n, t + 1))
    if m > 0:
        next_t = min(next_t, operate(n + m, m, t + 1))
    if n > s:
        next_t = min(next_t, operate(n - 1, m, t + 1))
    dp[n][m] = next_t
    return dp[n][m]


sys.setrecursionlimit(987654321)
print(operate(1, 0, 0))
