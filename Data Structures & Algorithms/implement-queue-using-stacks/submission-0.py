class MyQueue:

    def __init__(self):
        self.x = []

    def push(self, x: int) -> None:
        self.x.append(x)

    def pop(self) -> int:
        if not self.empty():
            y = self.x[0]
            self.x = self.x[1:]
            return y
        return -1

    def peek(self) -> int:
        if not self.empty():
            return self.x[0]
        return -1

    def empty(self) -> bool:
        return not len(self.x)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()