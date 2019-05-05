"""
    10826 : 피보나치 수 4
    URL : https://www.acmicpc.net/problem/10826
    Input :
        10
    Output :
        55
"""

MAX_N = 10001

fibonacci = [0 for n in range(MAX_N)]
fibonacci[0] = 0
fibonacci[1] = 1
for i in range(2, MAX_N):
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

n = int(input())
print(fibonacci[n])
