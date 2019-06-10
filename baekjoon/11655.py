"""
    11655 : ROT13
    URL : https://www.acmicpc.net/problem/11655
    Input #1 :
        Baekjoon Online Judge
    Output #1 :
        Onrxwbba Bayvar Whqtr
    Input #2 :
        One is 1
    Output #2 :
        Bar vf 1
"""

s = input()
e = []
for c in s:
    if 'A' <= c <= 'Z':
        e.append(chr((((ord(c) + 13) - ord('A')) % 26) + ord('A')))
    elif 'a' <= c <= 'z':
        e.append(chr((((ord(c) + 13) - ord('a')) % 26) + ord('a')))
    else:
        e.append(c)
print(''.join(e))
