"""
    2511 : 카드놀이
    URL : https://www.acmicpc.net/problem/2511
    Input :
        4 5 6 7 0 1 2 3 9 8
        1 2 3 4 5 6 7 8 9 0
    Output :
        16 13
        A
"""

A = list(map(int, input().split()))
B = list(map(int, input().split()))

winners = []
for a, b in zip(A, B):
    if a > b:
        winners.append('A')
    elif a < b:
        winners.append('B')
    else:
        winners.append('D')

score_a = winners.count('A') * 3
score_b = winners.count('B') * 3
score_d = winners.count('D')

print('{} {}'.format(score_a + score_d, score_b + score_d))
if score_a > score_b:
    print('A')
elif score_a < score_b:
    print('B')
else:
    if score_a == score_b == 0:
        print('D')
    else:
        winner = None
        while winners:
            winner = winners.pop()
            if winner != 'D':
                break
        print(winner)
