"""
    File: 780.py
    Title: Reaching Points
    Difficulty: Hard
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty > sy:
                    tx = tx % ty
                else:
                    return (tx - sx) % ty == 0
            elif ty > tx:
                if tx > sx:
                    ty = ty % tx
                else:
                    return (ty - sy) % tx == 0
            else:
                break
        return sx == tx and sy == ty
