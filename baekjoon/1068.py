"""
    1068 : 트리
    URL : https://www.acmicpc.net/problem/1068
    Input :
        5
        -1 0 0 1 1
        2
    Output :
        2
"""

from collections import deque

n = int(input())
parents = list(map(int, input().split()))
m = int(input())

tree = {}

for i in range(n):
    tree[i] = []

for i, parent in enumerate(parents):
    if parent == -1:
        continue

    tree[parent].append(i)

if parents[m] != -1:
    tree[parents[m]].remove(m)

q = deque()
q.append(m)
while q:
    i = q.popleft()

    if i in tree:
        for j in tree[i]:
            q.append(j)
        del tree[i]

print(len(list(filter(lambda children: len(children) == 0, tree.values()))))
