"""
    2753 : 윤년
    URL : https://www.acmicpc.net/problem/2753
    Input :
        2000
    Output :
        1
"""

year = int(input())

if (((year % 4) == 0) and (not ((year % 100) == 0))) or ((year % 400) == 0):
    print("1")
else:
    print("0")
