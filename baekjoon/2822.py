"""
    2822 : 점수 계산
    URL : https://www.acmicpc.net/problem/2822
    Input :
        20
        30
        50
        48
        33
        66
        0
        64
    Output :
        261
        3 4 5 6 8
"""

quiz = []

n = 8
for i in range(1, n + 1):
    quiz.append((int(input()), i))

quiz = list(reversed(sorted(quiz)))
quiz = quiz[:5]

scores = []
numbers = []

for q in quiz:
    scores.append(q[0])
    numbers.append(q[1])

print(sum(scores))
print(' '.join([str(i) for i in sorted(numbers)]))
