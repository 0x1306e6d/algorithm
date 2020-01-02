"""
    1764 : 듣보잡
    URL : https://www.acmicpc.net/problem/1764
    Input :
        3 4
        ohhenrie
        charlie
        baesangwook
        obama
        baesangwook
        ohhenrie
        clinton
    Output :
        2
        baesangwook
        ohhenrie
"""

n, m = map(int, input().split())

d = set()
for i in range(n):
    d.add(input())

b = set()
for i in range(m):
    b.add(input())

dbj = d.intersection(b)
print(len(dbj))
for i in sorted(dbj):
    print(i)
