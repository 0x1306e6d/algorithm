"""
    1676 : 팩토리얼 0의 개수
    URL : https://www.acmicpc.net/problem/1676
    Input :
        10
    Output :
        2
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


count = 0

N = int(input())
N = str(factorial(N))
for n in reversed(N):
    if n == '0':
        count += 1
    else:
        break

print(count)
