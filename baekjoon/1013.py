"""
    1013 : Contact
    URL : https://www.acmicpc.net/problem/1013
    Input :
        3
        10010111
        011000100110001
        0110001011001
    Output :
        NO
        NO
        YES
"""


def test(s):
    if len(s) == 0:
        return True

    if s.startswith('10'):
        i = 2

        if i >= len(s):
            return False

        if s[i] != '0':
            return False

        while i < len(s) and s[i] == '0':
            i += 1

        if i >= len(s):
            return False

        if s[i] != '1':
            return False

        success = False
        while i < len(s) and s[i] == '1' and not success:
            i += 1
            success = test(s[i:])

        return test(s[i:])
    elif s.startswith('01'):
        return test(s[2:])

    return False


t = int(input())
for i in range(t):
    s = input()

    if test(s):
        print('YES')
    else:
        print('NO')
