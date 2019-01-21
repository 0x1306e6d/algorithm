"""
    8958 : OX퀴즈
    URL : https://www.acmicpc.net/problem/8958
    Input :
        5
        OOXXOXXOOO
        OOXXOOXXOO
        OXOXOXOXOXOXOX
        OOOOOOOOOO
        OOOOXOOOOXOOOOX
    Output :
        10
        9
        7
        55
        30
"""

N = int(input())
for _ in range(N):
    string = input()
    sequence = 0
    score = 0
    for c in string:
        if c is 'O':
            sequence += 1
            score += sequence
        elif c is 'X':
            sequence = 0
    print(score)
