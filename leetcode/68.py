"""
    File: 68.py
    Title: Text Justification
    Difficulty: Hard
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = []
        line_length = 0
        for word in words:
            if line_length + len(line) + len(word) > maxWidth:
                lines.append((line, line_length))
                line = []
                line_length = 0
            line.append(word)
            line_length += len(word)
        if line:
            lines.append((line, line_length))

        ans = []
        for i in range(len(lines)):
            line, line_length = lines[i]
            if i == len(lines) - 1 or len(line) == 1:
                line_str = " ".join(line)
                while len(line_str) < maxWidth:
                    line_str += " "
                ans.append(line_str)
            else:
                space = maxWidth - line_length
                space_per = space // (len(line) - 1)
                extra = space % (len(line) - 1)
                line_str = ""
                for j, word in enumerate(line):
                    line_str += word
                    if j < len(line) - 1:
                        line_str += " " * space_per
                        if extra > 0:
                            line_str += " "
                            extra -= 1
                ans.append(line_str)
        return ans
