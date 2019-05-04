"""
    4949 : 균형잡힌 세상
    URL : https://www.acmicpc.net/problem/4949
    Input :
            So when I die (the [first] I will see in (heaven) is a score list).
            [ first in ] ( first out ).
            Half Moon tonight (At least it is better than no Moon at all].
            A rope may form )( a trail in a maze.
            Help( I[m being held prisoner in a fortune cookie factory)].
            ([ (([( [ ] ) ( ) (( ))] )) ]).
             .
            .
    Output :
        yes
        yes
        no
        no
        no
        yes
        yes
"""

while True:
    s = input()
    if s == '.':
        break

    balance = True
    stack = []
    for c in s:
        if (c == '(') or (c == '['):
            stack.append(c)
        if c == ')':
            if stack and (stack[-1] == '('):
                stack.pop()
            else:
                balance = False
                break
        if c == ']':
            if stack and (stack[-1] == '['):
                stack.pop()
            else:
                balance = False
                break

    if balance and (len(stack) == 0):
        print("yes")
    else:
        print("no")
