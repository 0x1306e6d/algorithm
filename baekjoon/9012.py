"""
    9012 : 괄호
    URL : https://www.acmicpc.net/problem/9012
    Input :
        6
        (())())
        (((()())()
        (()())((()))
        ((()()(()))(((())))()
        ()()()()(()()())()
        (()((())()(
    Output :
        NO
        NO
        YES
        NO
        YES
        NO
"""

N = int(input())
for _ in range(N):
    ps = input()
    if ps[-1] is '(':
        print("NO")
    else:
        count = 0
        for c in ps:
            if c is '(':
                count += 1
            elif c is ')':
                count -= 1
            if count < 0:
                break
        if count is 0:
            print("YES")
        else:
            print("NO")
