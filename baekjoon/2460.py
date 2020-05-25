"""
    2460 : 지능형 기차 2
    URL : https://www.acmicpc.net/problem/2460
    Input :
        0 32
        3 13
        28 25
        17 5
        21 20
        11 0
        12 12
        4 2
        0 8
        21 0
    Output :
        42
"""

n = 0
n_max = 0

for _ in range(10):
    n_out, n_in = map(int, input().split())

    n -= n_out
    n += n_in
    n_max = max(n_max, n)

print(n_max)
