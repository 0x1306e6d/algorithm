"""
    1015 : 수열 정렬
    URL : https://www.acmicpc.net/problem/1015
    Input :
        3
        2 3 1
    Output :
        1 2 0
"""

n = int(input())
a = list(map(int, input().split()))
b = list(sorted(a))
p = [0 for _ in range(n)]
for i, ai in enumerate(a):
    p[i] = b.index(ai)
    b[p[i]] = None
print(' '.join(str(i) for i in p))
