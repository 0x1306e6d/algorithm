"""
    File: 735.py
    Title: Asteroid Collision
    Difficulty: Medium
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            if asteroid > 0:
                ans.append(asteroid)
            else:
                append = True
                while ans:
                    collision = ans[-1]
                    if collision < 0:
                        break
                    if collision < abs(asteroid):
                        ans.pop()
                    elif collision > abs(asteroid):
                        append = False
                        break
                    else:
                        append = False
                        ans.pop()
                        break
                if append:
                    ans.append(asteroid)
        return ans
