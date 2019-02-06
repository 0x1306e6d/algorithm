"""
    2504 : 괄호의 값
    URL : https://www.acmicpc.net/problem/2504
    Input :
        (()[[]])([])
    Output :
        28
"""


class Stack:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def push(self, x):
        self._data += [x]

    def pop(self):
        if self.empty():
            return None
        else:
            last = self._data[-1]
            self._data = self._data[:-1]
            return last

    def size(self):
        return len(self._data)

    def empty(self):
        if self._data:
            return False
        else:
            return True

    def top(self):
        if self.empty():
            return None
        else:
            return self._data[-1]


def calculate_score(stack, current):
    score = 0

    top = stack.pop()
    if current == ')':
        if top == '(':
            score += 2
        else:
            score += 2 * calculate_score(stack, top)
            if stack.top() != '(':
                raise RuntimeError()
            else:
                stack.pop()
    elif current == ']':
        if top == '[':
            score += 3
        else:
            score += 3 * calculate_score(stack, top)
            if stack.top() != '[':
                raise RuntimeError()
            else:
                stack.pop()
    else:
        raise RuntimeError()

    if stack.top() == ')' or stack.top() == ']':
        score += calculate_score(stack, stack.pop())

    return score


stack = Stack()

string = input().strip()
for c in string:
    stack.push(c)

try:
    score = 0
    while not stack.empty():
        score += calculate_score(stack, stack.pop())
    print(score)
except:
    print(0)
