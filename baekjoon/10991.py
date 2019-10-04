"""
    10991 : 별 찍기 - 16
    URL : https://www.acmicpc.net/problem/10991
    Input #1 :
        1
    Output #1 :
        *
    Input #2 :
        2
    Output #2 :
         *
        * *                
    Input #3 :
        3
    Output #3 :
          *
         * *
        * * *
    Input #4 :
        4
    Output #4 :
           *
          * *
         * * *
        * * * *
"""

n = int(input())
for i in range(1, n + 1):
    print('{}{}'.format(' ' * (n - i), ' '.join(list('*' * i))))
