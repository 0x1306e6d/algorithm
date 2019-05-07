"""
    17173 : 배수들의 합
    URL : https://www.acmicpc.net/problem/17173
    Input #1 :
        10 2
        2 3
    Output #1 :
        42
    Input #2 :
        1000 3
        3 5 7
    Output #2 :
        272066
"""

n, m = map(int, input().split())
k = list(map(int, input().split()))

s = set()
for ki in k:
    for m in range(ki, n + 1, ki):
        s.add(m)

print(sum(s))
