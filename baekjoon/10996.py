"""
    10996 : 별 찍기 - 21
    URL : https://www.acmicpc.net/problem/10996
    Input #1 :
        1
    Output #1 :
        *
    Input #2 :
        2
    Output #2 :
        *
         *
        *
         *
    Input #3 :
        3
    Output #3 :
        * *
         *
        * *
         *
        * *
         *
    Input #4 :
        4
    Output #4 :
        * *
         * *
        * *
         * *
        * *
         * *
        * *
         * *
"""

n = int(input())

if n == 1:
    print('*')
elif (n % 2) == 0:
    stars = ' '.join(['*'] * (n // 2))
    for i in range(n):
        print(stars)
        print(' ' + stars)
else:
    stars_top = ' '.join(['*'] * ((n // 2) + 1))
    stars_bottom = ' '.join(['*'] * (n // 2))
    for i in range(n):
        print(stars_top)
        print(' ' + stars_bottom)
