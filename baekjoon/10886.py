"""
    10886 : 0 = not cute / 1 = cute
    URL : https://www.acmicpc.net/problem/10886
    Input :
        3
        1
        0
        0
    Output :
        Junhee is not cute!
"""

cute = 0
n = int(input())
for _ in range(n):
    if int(input()) == 1:
        cute += 1

if cute > (n // 2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
