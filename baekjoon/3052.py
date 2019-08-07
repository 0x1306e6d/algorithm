"""
    3052 : 나머지
    URL : https://www.acmicpc.net/problem/3052
    Input :
        39
        40
        41
        42
        43
        44
        82
        83
        84
        85
    Output :
        6
"""

s = set()
for i in range(10):
    n = int(input())
    s.add(n % 42)
print(len(s))
