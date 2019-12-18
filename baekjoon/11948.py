"""
    11948 : 과목선택
    URL : https://www.acmicpc.net/problem/11948
    Input #1 :
        100
        34
        76
        42
        10
        0
    Output #1 :
        228
    Input #2 :
        15
        21
        15
        42
        15
        62
    Output #2 :
        140
"""

science = []
for i in range(4):
    science.append(int(input()))

society = []
for i in range(2):
    society.append(int(input()))

print(sum(science) - min(science) + max(society))
