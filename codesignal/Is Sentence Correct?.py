import re


def solution(sentence):
    pattern = "^[A-Z]{1}[^.?!]*[.?!]{1}$"
    return re.match(pattern, sentence) is not None
