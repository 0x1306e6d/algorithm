"""
    16673 : 고려대학교에는 공식 와인이 있다
    URL : https://www.acmicpc.net/problem/16673
    Input #1 :
        3 1 1
    Output #1 :
        20
    Input #2 :
        5 28 27
    Output #2 :
        1905
"""

c, k, p = map(int, input().split())
a = 0
for i in range(c + 1):
    a += ((k * i) + (p * (i ** 2)))
print(a)
