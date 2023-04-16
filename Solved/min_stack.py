class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def __str__(self):
        return str(self.arr)

    def push(self, val: int) -> None:
        if not self.min_stack or (self.min_stack and val <= self.min_stack[-1]):
            self.min_stack.append(val)
        self.arr.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self):
        return self.min_stack[-1]


# minStack = MinStack()
# minStack.push(2)
# print(minStack.min_stack)
# print(minStack)
# print()
# minStack.push(0)
# print(minStack.min_stack)
# print(minStack)
# print()
# minStack.push(3)
# print(minStack.min_stack)
# print(minStack)
# print()
# minStack.push(0)
# print(minStack.min_stack)
# print(minStack)
# print(minStack.getMin())
# minStack.pop()
# print()
# print(minStack.min_stack)
# print(minStack)
# print(minStack.getMin())
# print()
# print(minStack.min_stack)
# print(minStack)
# minStack.pop()
# print()
# print(minStack.min_stack)
# print(minStack)
# print(minStack.getMin())
# minStack.pop()
# print(minStack)
# print()
# print(minStack.min_stack)
# print(minStack)


# minStack = MinStack()
# minStack.push(-2)
# print(minStack.current_min)
# print(minStack.prev_min)
# print(minStack)
# print()
# minStack.push(0)
# print(minStack.current_min)
# print(minStack.prev_min)
# print(minStack)
# print()
# minStack.push(-3)
# print(minStack.current_min)
# print(minStack.prev_min)
# print(minStack)
# print(minStack.getMin())
# print(minStack)
# minStack.pop()
# print(minStack.current_min)
# print(minStack.prev_min)
# print(minStack)
# print(minStack.top())
# print(minStack.getMin())



# minStack = MinStack()
# minStack.push(0)
# print(minStack)
# minStack.push(1)
# print(minStack)
# minStack.push(0)
# print(minStack)
# print(minStack.getMin())
# print(minStack)
# minStack.pop()
# print(minStack)
# print(minStack.getMin())
