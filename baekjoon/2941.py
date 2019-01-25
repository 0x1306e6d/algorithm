"""
    2941 : 크로아티아 알파벳
    URL : https://www.acmicpc.net/problem/2941
    Input #1 :
        ljes=njak
    Output #1 :
        6
    Input #2 :
        ddz=z=
    Output #2 :
        3
    Input #3 :
        nljj
    Output #3 :
        3
    Input #4 :
        c=c=
    Output #4 :
        2
"""

count = 0

string = input()
a = None
b = None
for c in string:
    if (b == 'c' and c == '='):
        count += 1
    elif b == 'c' and c == '-':
        count += 1
    elif a == 'd' and b == 'z' and c == '=':
        count += 2
    elif b == 'd' and c == '-':
        count += 1
    elif b == 'l' and c == 'j':
        count += 1
    elif b == 'n' and c == 'j':
        count += 1
    elif b == 's' and c == '=':
        count += 1
    elif b == 'z' and c == '=':
        count += 1

    a = b
    b = c

print((len(string) - count))
