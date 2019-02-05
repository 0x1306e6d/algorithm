"""
    1427 : 소트인사이드
    URL : https://www.acmicpc.net/problem/1427
    Input :
        2143
    Output :
        4321
"""

array = []
N = input()
for n in N:
    n = int(n)

    i = 0
    found = False
    while not found and i < len(array):
        if array[i] > n:
            i += 1
        else:
            found = True
    array.insert(i, n)

print("{}".format("".join(map(str, array))))