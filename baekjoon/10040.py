"""
    10040 : 투표
    URL : https://www.acmicpc.net/problem/10040
    Input :
        4 3
        5
        3
        1
        4
        4
        3
        2
    Output :
        2
"""

A = {}
B = []

N, M = map(int, input().split())
for i in range(1, N + 1):
    a = int(input())
    A[i] = a
for j in range(M):
    b = int(input())
    B.append(b)
B = sorted(B, reverse=True)

max_i = 0
max_vote = 0
j = 0
for i, cost in A.items():
    vote = 0
    while (j < len(B)) and (B[j] >= cost):
        vote += 1
        j += 1
    if vote > max_vote:
        max_i = i
        max_vote = vote

print(max_i)
