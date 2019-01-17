"""
    1157 : 단어 공부
    URL : https://www.acmicpc.net/problem/1157
    Input #1 :
        Mississipi
    Output #1 :
        ?
    Input #2 :
        zZa
    Output #2 :
        Z
    Input #3 :
        z
    Output #3 :
        Z
    Input #4 :
        baaa
    Output #4 :
        A
"""

cache = {}

word = input().upper()
for c in word:
    if c in cache:
        cache[c] += 1
    else:
        cache[c] = 1

max_c = None
max_counter = 0
duplicated = False
for c, counter in cache.items():
    if counter == max_counter:
        duplicated = True
    if counter > max_counter:
        max_c = c
        max_counter = counter
        duplicated = False

if duplicated:
    print("?")
else:
    print(max_c)
