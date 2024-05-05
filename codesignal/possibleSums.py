def solution(coins, quantity):
    ans = {0}
    for i, coin in enumerate(coins):
        sums = ans.copy()
        for k in sums:
            for q in range(quantity[i] + 1):
                ans.add(k + coin * q)
    return len(ans) - 1
