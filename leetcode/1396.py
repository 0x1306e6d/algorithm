"""
    File: 1396.py
    Title: Design Underground System
    Difficulty: Medium
"""


class UndergroundSystem:
    def __init__(self):
        self.checks = {}
        self.travels = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, check_in = self.checks[id]
        del self.checks[id]

        if startStation not in self.travels:
            self.travels[startStation] = {stationName: [t - check_in]}
        else:
            if stationName in self.travels[startStation]:
                self.travels[startStation][stationName].append(t - check_in)
            else:
                self.travels[startStation][stationName] = [t - check_in]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.travels[startStation][endStation]) / len(
            self.travels[startStation][endStation]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
