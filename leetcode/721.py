"""
    File: 721.py
    Title: Accounts Merge
    Difficulty: Medium
"""

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.uf = {}

        def find(email):
            if email not in self.uf:
                self.uf[email] = email
            if email != self.uf[email]:
                self.uf[email] = find(self.uf[email])
            return self.uf[email]

        names = {}

        for account in accounts:
            name = account[0]
            root_email = find(account[1])
            for i in range(2, len(account)):
                root = find(account[i])
                if root_email == root:
                    continue
                self.uf[root] = root_email
            names[root_email] = name

        groups = defaultdict(list)
        for email in self.uf:
            root = find(email)
            groups[root].append(email)

        ans = []
        for root_email in groups:
            user = [names[root_email]]
            user += list(sorted(groups[root_email]))
            ans.append(user)
        return ans
