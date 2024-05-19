"""
    File: 1244.py
    Title: Design A Leaderboard
    Difficulty: Medium
"""


def find(arr, x):
    i, j = 0, len(arr)
    while i < j:
        mid = (i + j) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            i = mid + 1
        else:
            j = mid


def bisect_left(arr, x):
    i, j = 0, len(arr)
    while i < j:
        mid = (i + j) // 2
        if arr[mid] > x:
            i = mid + 1
        else:
            j = mid
    return i


class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.rank = []

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            previous_score = self.scores[playerId]
            score = previous_score + score

            i = find(self.rank, previous_score)
            self.rank.pop(i)
            i = bisect_left(self.rank, score)
            self.rank.insert(i, score)

            self.scores[playerId] = score
        else:
            i = bisect_left(self.rank, score)
            self.rank.insert(i, score)

            self.scores[playerId] = score

    def top(self, K: int) -> int:
        ans = 0
        for i in range(min(K, len(self.rank))):
            ans += self.rank[i]
        return ans

    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        del self.scores[playerId]

        i = find(self.rank, score)
        self.rank.pop(i)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
