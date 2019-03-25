"""
    1024 : 수열의 합
    URL : https://www.acmicpc.net/problem/1024
    Input :
        18 2
    Output :
        5 6 7
"""

MAX_L = 101

N, L = map(int, input().split(' '))

sequence = []
for l in range(L, MAX_L):
    s = []
    a = int((((2 * N) / l) - l + 1) / 2)

    if a < 0:
        continue

    for i in range(a, a + l):
        s.append(i)

    if N == sum(s):
        sequence = s
        break

if sequence:
    print("{}".format(' '.join([str(x) for x in sequence])))
else:
    print("-1")
