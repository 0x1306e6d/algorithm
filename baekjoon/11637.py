"""
    11637 : 인기 투표
    URL : https://www.acmicpc.net/problem/11637
    Input :
        4
        3
        10
        21
        10
        3
        20
        10
        10
        3
        10
        10
        10
        4
        15
        15
        15
        45
    Output :
        majority winner 2
        minority winner 1
        no winner
        minority winner 4
"""

t = int(input())
for tc in range(t):
    n = int(input())

    max_score = 0
    max_score_id = 0
    max_score_duplicated = False

    sum_score = 0

    for i in range(1, n + 1):
        score = int(input())

        if score > max_score:
            max_score = score
            max_score_id = i
            max_score_duplicated = False
        elif score == max_score:
            max_score_duplicated = True

        sum_score += score

    if max_score_duplicated:
        print('no winner')
    else:
        if max_score > (sum_score // 2):
            print('majority winner {}'.format(max_score_id))
        else:
            print('minority winner {}'.format(max_score_id))
