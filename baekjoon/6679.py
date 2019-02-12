"""
    6679 : 싱기한 네자리 숫자
    URL : https://www.acmicpc.net/problem/6679
    Input :
    Output :
        2992
        2993
        2994
        2995
        2996
        2997
        2998
        2999
"""


def ndecimal(n, i):
    result = []
    while i > 0:
        result.append(i % n)
        i = i // n
    return result


for i in range(1000, 9999 + 1):
    decimal = ndecimal(10, i)
    duodecimal = ndecimal(12, i)
    hexadecimal = ndecimal(16, i)

    if sum(decimal) == sum(duodecimal) == sum(hexadecimal):
        print(i)
