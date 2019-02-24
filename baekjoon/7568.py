"""
    7568 : 덩치
    URL : https://www.acmicpc.net/problem/7568
    Input :
        5
        55 185
        58 183
        88 186
        60 175
        46 155
    Output :
        2 2 1 2 5
"""

people = []

N = int(input())
for _ in range(N):
    x, y = map(int, input().split(' '))
    people.append((x, y))

ranks = []
for x, y in people:
    rank = 1
    for person in people:
        if (person[0] > x) and (person[1] > y):
            rank += 1
    ranks.append(rank)

print("{}".format(' '.join([str(rank) for rank in ranks])))
