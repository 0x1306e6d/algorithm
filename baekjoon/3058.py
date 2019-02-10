"""
    3058 : 짝수를 찾아라
    URL : https://www.acmicpc.net/problem/3058
    Input :
        2
        1 2 3 4 5 6 7
        13 78 39 42 54 93 86
    Output :
        12 2
        260 42
"""

MAX_N = 101

T = int(input())
for _ in range(T):
    even_sum = 0
    even_min = MAX_N

    data = list(map(int, input().split(' ')))
    for n in data:
        if (n % 2) == 0:
            even_sum += n
            even_min = min(even_min, n)

    print('{} {}'.format(even_sum, even_min))
