"""
    11170 : 0의 개수
    URL : https://www.acmicpc.net/problem/11170
    Input :
        3
        0 10
        33 1005
        1 4
    Output :
        2
        199
        0
"""

T = int(input())
for _ in range(T):
    count = 0

    N, M = map(int, input().split(' '))
    for n in range(N, M + 1):
        strn = str(n)

        for c in strn:
            if c == '0':
                count += 1

    print(count)
