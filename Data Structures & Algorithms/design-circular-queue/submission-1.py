class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.rear = None
        self.size = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if not self.head:
            self.head = Node(value)
            self.rear = self.head
            self.rear.next = self.head
            self.count+=1
            return True
        p = Node(value)
        self.rear.next = p
        p.next = self.head
        self.rear = p
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.count == 1:
            self.head = self.rear = None
            self.count = 0
            return True
            
        self.rear.next = self.head.next
        self.head = self.head.next
        self.count-=1
        return True

    def Front(self) -> int:
        if self.head:
            return self.head.val
        return -1

    def Rear(self) -> int:
        if self.rear:
            return self.rear.val
        return -1
        

    def isEmpty(self) -> bool:
        if self.rear and self.head:
            return False
        return True

    def isFull(self) -> bool:
        return self.count == self.size


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()