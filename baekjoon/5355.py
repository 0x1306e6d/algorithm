"""
    5355 : 화성 수학
    URL : https://www.acmicpc.net/problem/5355
    Input :
        3
        3 @ %
        10.4 # % @
        8 #
    Output :
        14.00
        25.20
        1.00
"""

T = int(input())
for t in range(T):
    equation = input().split()

    number = float(equation[0])
    operations = equation[1:]
    for operation in operations:
        if operation == '@':
            number *= 3
        elif operation == '%':
            number += 5
        elif operation == '#':
            number -= 7

    print(format(number, '.2f'))
