class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.ptr = None

    def visit(self, url: str) -> None:
        node = Node(url)
        if not self.ptr:
            self.head.next = self.ptr = node
            self.ptr.back = self.head
            return

        self.ptr.next = node
        node.back = self.ptr
        self.ptr = node

        p = self.head
        while p:
            print(p.data, end = ',')
            p = p.next
        print()
        

    def back(self, steps: int) -> str:

        for i in range(steps):
            if not self.head.next:
                return self.head.data
            if not self.ptr.back:
                return self.ptr.data
            self.ptr = self.ptr.back

        return self.ptr.data

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.head.next:
                return self.head.data
            if not self.ptr.next:
                return self.ptr.data
            self.ptr = self.ptr.next
        return self.ptr.data

class Node:
    def __init__(self, data = 0, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)