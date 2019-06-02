"""
    2217: 로프
    URL : https://www.acmicpc.net/problem/2217
    Input :
        2
        10
        15
    Output :
        20
"""

ropes = []

n = int(input())
for i in range(n):
    rope = int(input())
    ropes.append(rope)

ropes = sorted(ropes)
m = n
max_weight = 0
for rope in ropes:
    max_weight = max(max_weight, rope * m)
    m = m - 1
print(max_weight)
