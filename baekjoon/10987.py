"""
    10987 : 모음의 개수
    URL : https://www.acmicpc.net/problem/10987
    Input :
        baekjoon
    Output :
        4
"""

count = 0
for c in input():
    if c in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(count)
