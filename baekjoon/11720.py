"""
    11720 : 숫자의 합
    URL : https://www.acmicpc.net/problem/11720
    Input #1:
        1
        1
    Output #1:
        1
    Input #2:
        5
        54321
    Output #2:
        15
"""
input()
numbers = input()

sum = 0
for n in numbers:
    sum += int(n)
print(sum)