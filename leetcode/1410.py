"""
    File: 1410.py
    Title: HTML Entity Parser
    Difficulty: Medium
    URL: https://leetcode.com/problems/html-entity-parser/
"""

import unittest


class Solution:
    def entityParser(self, text: str) -> str:
        parsed = ""

        special_character = None
        special_characters = [('&quot', '"'), ('&apos', '\''), ('&amp', '&'),
                              ('&gt', '>'), ('&lt', '<'), ('&frasl', '/')]
        for c in text:
            if special_character is None:
                if c == '&':
                    special_character = '&'
                else:
                    parsed += c
            else:
                if c == ';':
                    for entity, symbol in special_characters:
                        if entity == special_character:
                            parsed += symbol
                            special_character = None
                            break
                    if special_character is not None:
                        parsed += special_character
                        parsed += ';'
                        special_character = None
                else:
                    if len(special_character) > 6:
                        parsed += special_character
                        parsed += c
                        special_character = None
                    else:
                        special_character += c

        return parsed


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        text = "&amp; is an HTML entity but &ambassador; is not."
        # Output
        output = "& is an HTML entity but &ambassador; is not."

        solution = Solution()
        self.assertEqual(solution.entityParser(text), output)

    def test_example2(self):
        # Input
        text = "and I quote: &quot;...&quot;"
        # Output
        output = "and I quote: \"...\""

        solution = Solution()
        self.assertEqual(solution.entityParser(text), output)

    def test_example3(self):
        # Input
        text = "Stay home! Practice on Leetcode :)"
        # Output
        output = "Stay home! Practice on Leetcode :)"

        solution = Solution()
        self.assertEqual(solution.entityParser(text), output)

    def test_example4(self):
        # Input
        text = "x &gt; y &amp;&amp; x &lt; y is always false"
        # Output
        output = "x > y && x < y is always false"

        solution = Solution()
        self.assertEqual(solution.entityParser(text), output)

    def test_example5(self):
        # Input
        text = "leetcode.com&frasl;problemset&frasl;all"
        # Output
        output = "leetcode.com/problemset/all"

        solution = Solution()
        self.assertEqual(solution.entityParser(text), output)


if __name__ == "__main__":
    unittest.main()
