"""
    File: 929.py
    Title: Unique Email Addresses
    Difficulty: Easy
    URL: https://leetcode.com/problems/unique-email-addresses/
"""

import unittest

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def resolve(email: str) -> str:
            at = email.index('@')
            local_name = email[:at]
            domain_name = email[at + 1:]

            plus = local_name.find('+')
            if plus >= 0:
                local_name = local_name[:plus]

            return local_name.replace('.', '') + '@' + domain_name

        unique_emails = set()
        for email in emails:
            unique_emails.add(resolve(email))
        return len(unique_emails)


class SolutionTestCase(unittest.TestCase):
    def test_example1(self):
        # Input
        emails = ["test.email+alex@leetcode.com",
                  "test.e.mail+bob.cathy@leetcode.com",
                  "testemail+david@lee.tcode.com"]
        # Output
        output = 2

        solution = Solution()
        self.assertEqual(solution.numUniqueEmails(emails), output)

    def test_example2(self):
        # Input
        emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
        # Output
        output = 3

        solution = Solution()
        self.assertEqual(solution.numUniqueEmails(emails), output)


if __name__ == "__main__":
    unittest.main()
