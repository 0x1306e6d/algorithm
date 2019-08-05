"""
    1330 : 두 수 비교하기
    URL : https://www.acmicpc.net/problem/1330
    Input #1 :
        1 2
    Output #1 :
        <
    Input #2 :
        10 2
    Output #2 :
        >
    Input #3 :
        5 5
    Output #3 :
        ==
"""

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
