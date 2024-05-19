"""
    File: 1169.py
    Title: Invalid Transactions
    Difficulty: Medium
"""

from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions2 = []
        for t in transactions:
            name, time, amount, city = t.split(",")
            transactions2.append((name, int(time), int(amount), city))
        transactions = transactions2
        transactions.sort(key=lambda x: x[1])

        start = 0
        invalids = []
        for i in range(len(transactions)):
            t1 = transactions[i]
            invalid = t1[2] > 1000
            for j in range(start, len(transactions)):
                t2 = transactions[j]
                if t1[0] == t2[0] and t1[3] != t2[3] and abs(t1[1] - t2[1]) <= 60:
                    invalid = True
                if t1[1] - t2[1] > 60:
                    start = j
                if t2[1] - t1[1] > 60:
                    break
            if invalid:
                invalids.append(t1)
        return list(map(lambda x: ",".join(map(str, x)), invalids))
