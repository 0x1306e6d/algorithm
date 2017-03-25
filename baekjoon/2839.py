"""
    2839 : 설탕 배달
    URL : https://www.acmicpc.net/problem/2839
    Input :
        18
    Output :
        4
"""
N = int(input())

five = int(N // 5)
three = int((N % 5) // 3)

solve = False
while True:
    if (5 * five) + (3 * three) == N:
        print(five + three)
        solve = True
        break
    else:
        five = five - 1
        three = (N - (5 * five)) // 3

    if five < 0:
        break;

if not solve:
    print(-1)