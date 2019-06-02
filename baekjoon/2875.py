"""
    2875: 대회 or 인턴
    URL : https://www.acmicpc.net/problem/2875
    Input :
        6 3 2
    Output :
        2
"""

n, m, k = map(int, input().split())

while k > 0:
    while (n > (2 * m)) and (k > 0):
        n = n - 1
        k = k - 1

    while (m > (n // 2)) and (k > 0):
        m = m - 1
        k = k - 1

    if (n == (2 * m)) and (k > 0):
        n = n - 1
        k = k - 1

if n >= (2 * m):
    print(m)
else:
    print(n // 2)
