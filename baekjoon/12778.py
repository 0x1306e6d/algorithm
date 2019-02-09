"""
    12778 : CTP공국으로 이민 가자
    URL : https://www.acmicpc.net/problem/12778
    Input :
        3
        3 C
        C T P
        4 N
        9 14 8 1
        5 C
        H E L L O
    Output :
        3 20 16
        I N H A
        8 5 12 12 15
"""

T = int(input())
for _ in range(T):
    m, cmd = input().split(' ')
    question = input().split(' ')

    answer = []
    if cmd == 'C':
        for c in question:
            answer.append(ord(c) - ord('A') + 1)
    elif cmd == 'N':
        for n in question:
            answer.append(chr(ord('A') + int(n) - 1))

    print('{}'.format(' '.join(str(x) for x in answer)))
