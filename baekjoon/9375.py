"""
    9375 : 패션왕 신해빈
    URL : https://www.acmicpc.net/problem/9375
    Input :
        2
        3
        hat headgear
        sunglasses eyewear
        turban headgear
        3
        mask face
        sunglasses face
        makeup face
    Output :
        5
        3
"""

T = int(input())
for _ in range(T):
    counts = {}

    n = int(input())
    for _ in range(n):
        name, kind = input().split(' ')

        if kind in counts:
            counts[kind] += 1
        else:
            counts[kind] = 1

    answer = 1
    for kind, count in counts.items():
        answer = answer * (count + 1)
    print(answer - 1)
