"""
    2226: 이진수
    URL : https://www.acmicpc.net/problem/2226
    Input :
        3
    Output :
        1
"""

N = int(input())

binary = list([None, 0, 1, 1])

for n in range(4, N + 1):
    b = binary[n - 1]

    if (n % 2) == 0:
        binary.append((b * 2) + 1)
    else:
        binary.append((b * 2) - 1)

print(binary[N])
