"""
    2446 : 별 찍기 - 9
    URL : https://www.acmicpc.net/problem/2446
    Input :
        5
    Output :
        *********
         *******
          *****
           ***
            *
           ***
          *****
         *******
        *********
"""

n = int(input())

lines = [''] * ((2 * n) - 1)
for i in range(n, 0, -1):
    line = (' ' * (n - i)) + ('*' * ((2 * i) - 1))
    lines[n - i] = line
    lines[-(n - i + 1)] = line

for line in lines:
    print(line)
