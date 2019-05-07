"""
    17174 : 전체 계산 횟수
    URL : https://www.acmicpc.net/problem/17174
    Input #1 :
        13 10
    Output #1 :
        14
    Input #2 :
        100 8
    Output #2 :
        113
"""

n, m = map(int, input().split())
l = 0
while n > 0:
    l += n
    n = (n // m)
print(l)
