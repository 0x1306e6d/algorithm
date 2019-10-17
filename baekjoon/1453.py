"""
    1453 : 피시방 알바
    URL : https://www.acmicpc.net/problem/1453
    Input :
        3
        1 2 3
    Output :
        0
"""

n = int(input())
empty = [True for i in range(101)]
persons = map(int, input().split())

rejected = 0
for person in persons:
    if not empty[person]:
        rejected += 1
    else:
        empty[person] = False

print(rejected)
