"""
    1780 : 종이의 개수
    URL : https://www.acmicpc.net/problem/1780
    Input :
        9
        0 0 0 1 1 1 -1 -1 -1
        0 0 0 1 1 1 -1 -1 -1
        0 0 0 1 1 1 -1 -1 -1
        1 1 1 0 0 0 0 0 0
        1 1 1 0 0 0 0 0 0
        1 1 1 0 0 0 0 0 0
        0 1 -1 0 1 -1 0 1 -1
        0 -1 1 0 1 -1 0 1 -1
        0 1 -1 1 0 -1 0 1 -1
    Output :
        10
        12
        11
"""

matrix = []

def count_paper(x, y, n):
    positive = True
    zero = True
    negative = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            k = matrix[i][j]
            if k == 1:
                zero = False
                negative = False
            if k == 0:
                positive = False
                negative = False
            if k == -1:
                positive = False
                zero = False
            
            if (not positive) and (not zero) and (not negative):
                break

        if (not positive) and (not zero) and (not negative):
            break
    
    if positive:
        return 1, 0, 0
    if zero:
        return 0, 1, 0
    if negative:
        return 0, 0, 1
    
    positive = 0
    zero = 0
    negative = 0
    m = (n // 3)
    for i in range(3):
        for j in range(3):
            p, z, n = count_paper(x + (m * i), y + (m * j), m)
            positive += p
            zero += z
            negative += n
    return positive, zero, negative


n = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

positive, zero, negative = count_paper(0, 0, n)
print(negative)
print(zero)
print(positive)
