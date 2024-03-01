#TC: O(1)
#SC: O(n)
class MinStack:
    
    def __init__(self):
        self.stack = deque()
        self.stack2 = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack2.append(min(val, self.stack2[-1] if self.stack2 else val))

    def pop(self) -> None:
        self.stack.pop()
        self.stack2.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]