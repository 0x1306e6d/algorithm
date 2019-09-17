"""
    9613 : GCD 합
    URL : https://www.acmicpc.net/problem/9613
    Input :
        3
        4 10 20 30 40
        3 7 5 12
        3 125 15 25
    Output :
        70
        3
        35
"""


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    if (a % b) == 0:
        return b
    return gcd(b, a % b)


t = int(input())
for _ in range(t):
    test_case = list(map(int, input().split()))[1:]
    answer = 0
    for i in range(len(test_case)):
        for j in range(i + 1, len(test_case)):
            answer += gcd(test_case[i], test_case[j])
    print(answer)
