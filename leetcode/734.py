"""
    File: 734.py
    Title: Sentence Similarity
    Difficulty: Easy
"""

from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilar(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]],
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similars = defaultdict(set)
        for s1, s2 in similarPairs:
            similars[s1].add(s2)
            similars[s2].add(s1)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if w1 in similars[w2] and w2 in similars[w1]:
                continue
            return False
        return True
