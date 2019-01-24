"""
    2309 : 일곱 난쟁이
    URL : https://www.acmicpc.net/problem/2309
    Input :
        20
        7
        23
        19
        10
        15
        25
        8
        13
    Output :
        7
        8
        10
        13
        19
        20
        23
"""

heights = [int(input()) for _ in range(9)]
heights = sorted(heights)
height_sum = sum(heights)

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if (height_sum - heights[i] - heights[j]) == 100:
            heights[i] = 0
            heights[j] = 0
            found = True
            break
    if found:
        break

heights = sorted(heights)[2:]
for height in heights:
    print(height)
