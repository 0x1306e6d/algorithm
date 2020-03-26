"""
    11943 : 파일 옮기기
    URL : https://www.acmicpc.net/problem/11943
    Input :
        1 2
        3 4
    Output :
        5
"""

a, b = map(int, input().split())
c, d = map(int, input().split())

print(min(a + d, b + c))
