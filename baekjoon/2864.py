"""
    2864 : 5와 6의 차이
    URL : https://www.acmicpc.net/problem/2864
    Input :
        1430 4862
    Output :
        6282 6292
"""

a, b = input().split()

a_min = int(a.replace('6', '5'))
a_max = int(a.replace('5', '6'))

b_min = int(b.replace('6', '5'))
b_max = int(b.replace('5', '6'))

print("{} {}".format((a_min + b_min), (a_max + b_max)))
