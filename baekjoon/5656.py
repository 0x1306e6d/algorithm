"""
    5656 : 비교 연산자
    URL : https://www.acmicpc.net/problem/5656
    Input :
        3 != 3
        4 < 4
        4 <= 5
        3 E 3
    Output :
        Case 1: false
        Case 2: false
        Case 3: true
"""

t = 1
while True:
    a, o, b = input().split()
    if o == 'E':
        break

    a = int(a)
    b = int(b)
    r = True
    if o == '>':
        r = (a > b)
    elif o == '>=':
        r = (a >= b)
    elif o == '<':
        r = (a < b)
    elif o == '<=':
        r = (a <= b)
    elif o == '==':
        r = (a == b)
    elif o == '!=':
        r = (a != b)

    print("Case {}: {}".format(t, "true" if r else "false"))

    t += 1
