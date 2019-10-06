"""
    14889 : 스타트와 링크
    URL : https://www.acmicpc.net/problem/14889
    Input #1 :
        4
        0 1 2 3
        4 0 5 6
        7 1 0 2
        3 4 5 0
    Output #1 :
        0
    Input #2 :
        6
        0 1 2 3 4 5
        1 0 2 3 4 5
        1 2 0 3 4 5
        1 2 3 0 4 5
        1 2 3 4 0 5
        1 2 3 4 5 0
    Output #2 :
        2
    Input #3 :
        8
        0 5 4 5 4 5 4 5
        4 0 5 1 2 3 4 5
        9 8 0 1 2 3 1 2
        9 9 9 0 9 9 9 9
        1 1 1 1 0 1 1 1
        8 7 6 5 4 0 3 2
        9 1 9 1 9 1 0 9
        6 5 4 3 2 1 9 0
    Output #3 :
        1
"""

from itertools import permutations

ability = []

n = int(input())
for _ in range(n):
    row = list(map(int, input().split()))
    ability.append(row)

m = n // 2
min_difference = 987654321
for team_a in permutations(range(n), m):
    team_a = set(team_a)
    team_b = set(range(n)) - team_a

    ability_a = 0
    for a_one in team_a:
        for a_two in team_a:
            ability_a += ability[a_one][a_two]
            ability_a += ability[a_two][a_one]

    ability_b = 0
    for b_one in team_b:
        for b_two in team_b:
            ability_b += ability[b_one][b_two]
            ability_b += ability[b_two][b_one]

    min_difference = min(min_difference, abs(ability_a - ability_b))

print(min_difference // 2)
