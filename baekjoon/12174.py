"""
    12174 : #include <Google I/O.h>
    URL : https://www.acmicpc.net/problem/12174
    Input :
        2
        2
        OIOOIIIIOIOOIOII
        21
        OIOOIOOIOOIOOOOOOOIOOIIIOOIIIIOOOOIIOOIIOOIOOIIIOOIOOOOOOOIOOOIOOIOOOOIIOOIIOOOOOIIOOIOOOOIIOOIIOOIOOOOOOIOOIOIOOOIIOIOOOIIOIIOIOOIOOOIOOOIOOOOIOOIOOOOOOOIIIOIOOOIOIOOI
    Output :
        Case #1: OK
        Case #2: I '<3' "C0d3 J4m"! :)
"""


def google(s):
    for i in range(0, len(s), 8):
        a = 0
        t = 2 ** 7

        c = s[i:i + 8]
        for b in c:
            if b == 'I':
                a += t
            t //= 2

        yield chr(a)


T = int(input())
for t in range(T):
    b = int(input())
    s = input()

    print("Case #{}: {}".format(t + 1, ''.join(list(google(s)))))
