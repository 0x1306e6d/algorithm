"""
    3163 : 떨어지는 개미
    URL : https://www.acmicpc.net/problem/3163
    Input :
        2
        6 30 3
        5 4
        8 5
        19 -1
        22 -3
        24 -2
        25 6
        4 35 2
        5 -1
        12 3
        20 4
        30 2
    Output :
        -2
        2
"""

T = int(input())
for _ in range(T):
    ids = []
    ants = []

    N, L, K = map(int, input().split(' '))
    for i in range(N):
        pi, ai = map(int, input().split(' '))

        ids.append(ai)
        if ai > 0:
            ants.append((L - pi, ai))
        else:
            ants.append((pi, ai))

    index = 0
    new_ants = []
    for position, ant in ants:
        if ant < 0:
            new_ants.append((position, ids[index]))
            index += 1
    for position, ant in ants:
        if ant > 0:
            new_ants.append((position, ids[index]))
            index += 1
    ants = sorted(new_ants, key=lambda kv: kv[0])

    k = K - 1
    if (k > 0) and (ants[k][0] == ants[k - 1][0]):
        print(max(ants[k][1], ants[k - 1][1]))
    elif (k < (N - 1)) and (ants[k][0] == ants[k + 1][0]):
        print(min(ants[k][1], ants[k + 1][1]))
    else:
        print(ants[k][1])
