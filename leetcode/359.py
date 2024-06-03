"""
    File: 359.py
    Title: Logger Rate Limiter
    Difficulty: Easy
"""


class Logger:

    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        if timestamp - self.messages[message] < 10:
            return False
        self.messages[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
