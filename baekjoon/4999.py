"""
    4999 : 아!
    URL : https://www.acmicpc.net/problem/4999
    Input #1 :
        aaah
        aaaaah
    Output #1 :
        no
    Input #1 :
        aaah
        ah
    Output #1 :
        go
"""

a = input()
b = input()

if a.endswith(b):
    print('go')
else:
    print('no')
