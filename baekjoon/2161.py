"""
    2161 : 카드1
    URL : https://www.acmicpc.net/problem/2161
    Input :
        7
    Output :
        1 3 5 7 4 2 6
"""

N = int(input())

array = list(range(1, N + 1))
trash = []

while len(array) > 1:
    trash.append(array[0])
    array = array[2:] + [array[1]]
trash.append(array[0])

print('{}'.format(' '.join(str(x) for x in trash)))
