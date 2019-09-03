"""
    5086: 배수와 약수
    URL: https://www.acmicpc.net/problem/5086
    Input #1:
        8 16
        32 4
        17 5
        0 0
    Output #1:
        factor
        multiple
        neither
"""

while True:
    a, b = map(int, input().split())
    if (a == 0) and (b == 0):
        break

    if (b % a) == 0:
        print("factor")
    elif (a % b) == 0:
        print("multiple")
    else:
        print("neither")
