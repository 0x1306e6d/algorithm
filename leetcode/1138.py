"""
    File: 1138.py
    Title: Alphabet Board Path
    Difficulty: Medium
    URL: https://leetcode.com/problems/alphabet-board-path/
"""

import unittest


class Solution:

    board = {
        'a': (0, 0), 'b': (1, 0), 'c': (2, 0), 'd': (3, 0), 'e': (4, 0),
        'f': (0, 1), 'g': (1, 1), 'h': (2, 1), 'i': (3, 1), 'j': (4, 1),
        'k': (0, 2), 'l': (1, 2), 'm': (2, 2), 'n': (3, 2), 'o': (4, 2),
        'p': (0, 3), 'q': (1, 3), 'r': (2, 3), 's': (3, 3), 't': (4, 3),
        'u': (0, 4), 'v': (1, 4), 'w': (2, 4), 'x': (3, 4), 'y': (4, 4),
        'z': (0, 5)
    }

    def alphabetBoardPath(self, target: str) -> str:
        path = ""

        here = None
        for there in target:
            if here == 'z' and there == 'z':
                pass
            elif here == 'z':
                path += 'U' + self.path_of('u', there)
            elif there == 'z':
                path += self.path_of(here, 'u') + 'D'
            else:
                path += self.path_of(here, there)
            path += '!'

            here = there

        return path

    def path_of(self, here: str, there: str) -> str:
        here_position = (0, 0) if here is None else self.board[here]
        there_position = self.board[there]

        path = self.vertical(here_position[1], there_position[1])
        path += self.horizontal(here_position[0], there_position[0])
        return path

    def horizontal(self, here: int, there: int) -> str:
        if here > there:
            return 'L' * (here - there)
        else:
            return 'R' * (there - here)

    def vertical(self, here: int, there: int) -> str:
        if here > there:
            return 'U' * (here - there)
        else:
            return 'D' * (there - here)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        target = "leet"
        # Output
        output = "DDR!UURRR!!DDD!"

        solution = Solution()
        self.assertEqual(solution.alphabetBoardPath(target), output)

    def test_example2(self):
        # Input
        target = "code"
        # Output
        output = "RR!DDRR!UUL!R!"

        solution = Solution()
        self.assertEqual(solution.alphabetBoardPath(target), output)


if __name__ == "__main__":
    unittest.main()
