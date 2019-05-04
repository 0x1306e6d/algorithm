"""
    15740 : A+B - 9
    URL : https://www.acmicpc.net/problem/15750
    Input #1 :
        1 2
    Output #1 :
        3
    Input #2 :
        -60 40
    Output #2 :
        -20
    Input #3 :
        -999999999 1000000000
    Output #3 :
        1
    Input #4 :
        1099511627776 1073741824
    Output #4 :
        1100585369600
    Input #5 :
        123456789123456789123456789 987654321987654321987654321
    Output #5 :
        1111111111111111111111111110
"""

a, b = map(int, input().split())
print(a + b)
