"""
    10156 : 과자
    URL : https://www.acmicpc.net/problem/10156
    Input :
        300 4 1000
    Output :
        200
"""

k, n, m = map(int, input().split())
print(max(0, (k * n) - m))
