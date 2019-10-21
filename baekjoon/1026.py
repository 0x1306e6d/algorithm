"""
    1026 : 보물
    URL : https://www.acmicpc.net/problem/1026
    Input :
        5
        1 1 1 6 0
        2 7 8 3 1
    Output :
        18
"""

n = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

s = 0
for a, b in zip(A, B):
    s += (a * b)
print(s)
