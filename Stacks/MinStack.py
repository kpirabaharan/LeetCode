# 155. Min Stack

class MinStack:

    def __init__(self):
        self.stack = []  # For O(1) to get min value need two stacks one for actual value and one to hold min value at each stack level
        # Can't have hold min in an int since min can change with pops
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)  # Ternary If Else
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
