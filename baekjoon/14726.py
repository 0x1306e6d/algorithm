"""
    14726 : 신용카드 판별
    URL : https://www.acmicpc.net/problem/14726
    Input :
        3
        2720992711828767
        3444063910462763
        6011733895106094
    Output :
        T
        F
        T
"""


def decrypt(encrypted):
    decrypted = []
    for i, c in enumerate(encrypted):
        if (i % 2) == 0:
            c = 2 * c
            if c >= 10:
                c = (c // 10) + (c % 10)
        decrypted.append(c)
    return decrypted


t = int(input())
for tc in range(t):
    card = decrypt(list(map(int, input())))
    s = sum(card)
    if (s % 10) == 0:
        print('T')
    else:
        print('F')
