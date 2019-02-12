"""
    2884 : 알람 시계
    URL : https://www.acmicpc.net/problem/2884
    Input :
        10 10
    Output :
        9 25
"""

H, M = map(int, input().split(' '))

hour = H
minute = M - 45
if minute < 0:
    hour -= 1
    minute += 60
if hour < 0:
    hour = 23

print("{} {}".format(hour, minute))
