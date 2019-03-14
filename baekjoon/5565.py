"""
    5565 : 영수증
    URL : https://www.acmicpc.net/problem/5565
    Input :
        9850
        1050
        800
        420
        380
        600
        820
        2400
        1800
        980
    Output :
        600
"""

total_price = int(input())
prices = []
for _ in range(9):
    prices.append(int(input()))

print(total_price - sum(prices))
