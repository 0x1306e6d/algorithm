"""
    2164 : 카드2
    URL : https://www.acmicpc.net/problem/2164
    Input :
        6
    Output :
        4
"""

n = int(input())

m = 1
while m < n:
    m *= 2
m -= (2 * (m - n))

print(m)
