"""
    10804 : 카드 역배치
    URL : https://www.acmicpc.net/problem/10804
    Input #1 :
        5 10
        9 13
        1 2
        3 4
        5 6
        1 2
        3 4
        5 6
        1 20
        1 20
    Output #1 :
        1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
    Input #2 :
        1 1
        2 2
        3 3
        4 4
        5 5
        6 6
        7 7
        8 8
        9 9
        10 10
    Output #2 :
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"""

cards = list(range(1, 20 + 1))

for i in range(10):
    a, b = map(lambda c: int(c) - 1, input().split())
    cards = cards[:a] + list(reversed(cards[a:(b + 1)])) + cards[(b + 1):]

print(' '.join([str(card) for card in cards]))
