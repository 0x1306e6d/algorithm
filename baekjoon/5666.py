"""
    5666 : 핫도그
    URL : https://www.acmicpc.net/problem/5666
    Input :
        10 90
        840 11
        1 50
        33 1000
        34 1000
        36 1000
        37 1000
        1 1000
    Output :
        0.11
        76.36
        0.02
        0.03
        0.03
        0.04
        0.04
        0.00
"""

while True:
    try:
        h, p = map(int, input().split())
        print("%.2f" % (h / p))
    except ValueError:
        break
    except EOFError:
        break
