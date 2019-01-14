"""
    9095 : 1, 2, 3 더하기
    URL : https://www.acmicpc.net/problem/9095
    Input :
        3
        4
        7
        10
    Output :
        7
        44
        274
"""


def make(i, n):
    if i == n:
        return 1

    count = 0
    if (i + 1) <= n:
        count += make(i + 1, n)
    if (i + 2) <= n:
        count += make(i + 2, n)
    if (i + 3) <= n:
        count += make(i + 3, n)
    return count


T = int(input())
for _ in range(T):
    n = int(input())
    print((make(1, n) + make(2, n) + make(3, n)))
