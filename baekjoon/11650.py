"""
    11650 : 좌표 정렬하기
    URL : https://www.acmicpc.net/problem/11650
    Input :
        5
        3 4
        1 1
        1 -1
        2 2
        3 3
    Output :
        1 -1
        1 1
        2 2
        3 3
        3 4
"""

coordinates = []

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))

for x, y in sorted(coordinates):
    print("{} {}".format(x, y))
