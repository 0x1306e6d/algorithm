"""
    10810 : 공 넣기
    URL : https://www.acmicpc.net/problem/10810
    Input :
        5 4
        1 2 3
        3 4 4
        1 4 1
        2 2 2
    Output :
        1 2 1 1 0
"""

n, m = map(int, input().split())
baskets = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i - 1, j):
        baskets[l] = k
print(' '.join([str(i) for i in baskets]))
