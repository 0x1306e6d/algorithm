"""
    File: 30.py
    Title: Substring with Concatenation of All Words
    Difficulty: Hard
"""

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])

        concatenated = {}
        for word in words:
            if word in concatenated:
                concatenated[word] += 1
            else:
                concatenated[word] = 1

        matches = []
        words_set = set(words)
        for i in range(len(s) - n + 1):
            word = s[i : i + n]
            if word in words_set:
                matches.append(word)
            else:
                matches.append("")

        ans = []
        for i in range(n):
            fill = {}
            for j in range(i, len(matches), n):
                match = matches[j]

                if match in fill:
                    fill[match] += 1
                else:
                    fill[match] = 1

                if j - (len(words) * n) >= i:
                    first = j - (len(words) * n)
                    delete = matches[first]
                    if fill[delete] == 1:
                        del fill[delete]
                    else:
                        fill[delete] -= 1

                if fill == concatenated:
                    ans.append(j - ((len(words) - 1) * n))
        return ans
