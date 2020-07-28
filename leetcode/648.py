import unittest

from typing import List


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        tree = {}

        for root in dict:
            current = None
            for c in root:
                if current is None:
                    if c not in tree:
                        tree[c] = {}

                    current = tree[c]
                else:
                    if c not in current:
                        current[c] = {}

                    current = current[c]
            current[0] = True

        def replace(word: str):
            successor = ""
            current = None
            for c in word:
                if current is None:
                    if c in tree:
                        current = tree[c]
                        successor += c
                    else:
                        return word
                else:
                    if 0 in current:
                        return successor
                    elif c in current:
                        current = current[c]
                        successor += c
                    else:
                        return word
            return successor

        return " ".join(list(map(replace,  sentence.split())))


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        dict = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        # Output
        output = "the cat was rat by the bat"

        solution = Solution()
        self.assertEqual(solution.replaceWords(dict, sentence), output)


if __name__ == "__main__":
    unittest.main()
