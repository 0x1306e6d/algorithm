"""
    10039 : 평균 점수
    URL : https://www.acmicpc.net/problem/10039
    Input :
        10
        65
        100
        30
        95
    Output :
        68
"""

sum = 0

for _ in range(5):
    score = max(int(input()), 40)
    sum += score

print((sum // 5))
