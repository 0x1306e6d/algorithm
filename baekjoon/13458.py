"""
    13458 : 시험 감독
    URL : https://www.acmicpc.net/problem/13458
    Input #1:
        1
        1
        1 1
    Output #1:
        1
    Input #2:
        3
        3 4 5
        2 2
    Output #2:
        7
    Input #3:
        5
        1000000 1000000 1000000 1000000 1000000
        5 7
    Output #3:
        714290
    Input #4:
        5
        10 9 10 9 10
        7 20
    Output #4:
        10
    Input #5:
        5
        10 9 10 9 10
        7 2
    Output #5:
        13
"""
N = int(input())
list = input().split()
BC = input().split()
B = int(BC[0])
C = int(BC[1])

count = 0

for i in list:
    num = int(i)
    num -= B
    count += 1

    if num > 0:
        if num % C == 0:
            count += (num // C)
        else:
            count += (num // C) + 1

print(count)
