"""
    File: 1041.py
    Title: Robot Bounded In Circle
    Difficulty: Medium
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        x, y = 0, 0
        for i in instructions:
            if i == "G":
                dx, dy = d[direction]
                x, y = x + dx, y + dy
            elif i == "L":
                direction = (direction - 1) % 4
            elif i == "R":
                direction = (direction + 1) % 4
        if x == 0 and y == 0:
            return True
        return direction != 0
