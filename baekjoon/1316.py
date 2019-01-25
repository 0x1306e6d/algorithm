"""
    1316 : 그룹 단어 체커
    URL : https://www.acmicpc.net/problem/1316
    Input #1 :
        3
        happy
        new
        year
    Output #1 :
        3
    Input #2 :
        4
        aba
        abab
        abcabc
        a
    Output #2 :
        1
"""

count = 0

N = int(input())
for _ in range(N):
    string = input()

    is_group = True
    group = {}

    for i, c in enumerate(string):
        if c in group:
            if i - group[c] == 1:
                group[c] = i
            else:
                is_group = False
        else:
            group[c] = i

    if is_group:
        count += 1

print(count)
