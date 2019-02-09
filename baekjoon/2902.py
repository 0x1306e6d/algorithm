"""
    2902 : KMP는 왜 KMP일까?
    URL : https://www.acmicpc.net/problem/2902
    Input :
        Knuth-Morris-Pratt
    Output :
        KMP
"""

shorter = ""

string = input()
for c in string:
    if 'A' <= c <= 'Z':
        shorter += c

print(shorter)
