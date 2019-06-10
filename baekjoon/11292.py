"""
    11292 : 키 큰 사람
    URL : https://www.acmicpc.net/problem/11292
    Input :
        3
        John 1.75
        Mary 1.64
        Sam 1.81
        2
        Jose 1.62
        Miguel 1.58
        5
        John 1.75
        Mary 1.75
        Sam 1.74
        Jose 1.75
        Miguel 1.75
        0
    Output :
        Sam
        Jose
        John Mary Jose Miguel
"""

while True:
    n = int(input())
    if n == 0:
        break

    high_height = 0
    high_students = []
    for i in range(n):
        name, height = input().split()
        height = float(height)
        if height > high_height:
            high_height = height
            high_students = [name]
        elif height == high_height:
            high_students.append(name)

    print(' '.join(high_students))
