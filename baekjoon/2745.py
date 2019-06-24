"""
    2745 : 진법 변환
    URL : https://www.acmicpc.net/problem/2745
    Input :
        ZZZZZ 36
    Output :
        60466175
"""

n, b = input().split()
b = int(b)

i = 1
decimal = 0
for c in reversed(n):
    if '0' <= c <= '9':
        decimal += (int(c) * i)
    else:
        decimal += ((ord(c) - ord('A') + 10) * i)
    i = (i * b)
print(decimal)
