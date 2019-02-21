"""
    9493 : 길면 기차, 기차는 빨라, 빠른 것은 비행기
    URL : https://www.acmicpc.net/problem/9493
    Input :
        21 70 80
        26 65 80
        0 0 0
    Output :
        0:02:15
        0:04:30
"""

import math

while True:
    M, A, B = map(int, input().split(' '))
    if (M is 0) and (A is 0) and (B is 0):
        break

    train = M / A
    airplane = M / B
    diff = train - airplane

    hour = int(diff)

    diff = (diff - hour) * 60
    minute = int(diff)

    diff = (diff - minute) * 60
    second = int(round(diff))

    print("{}:{}:{}".format(hour, str(minute).zfill(2), str(second).zfill(2)))
