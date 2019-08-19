"""
    1541 : 잃어버린 괄호
    URL : https://www.acmicpc.net/problem/1541
    Input :
        55-50+40
    Output :
        -35
"""


def parse_equation(raw_equation):
    equation = []

    n = None
    for e in raw_equation:
        if (e == '+') or (e == '-'):
            equation.append(int(n))
            equation.append(e)

            n = None
        else:
            if n is None:
                n = e
            else:
                n = n + e
    equation.append(int(n))

    return equation


raw_equation = input()
equation = parse_equation(raw_equation)

result = 0
operator = None
for e in equation:
    if e == '-':
        operator = '-'
    elif e == '+':
        if operator != '-':
            operator = '+'
    else:
        if operator is None:
            result = e
        elif operator == '-':
            result -= e
        elif operator == '+':
            result += e

print(result)
