class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        p = self.head
        for i in range(index):
            p = p.next
            if not p:
                return -1
        return p.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val=val)
            return
        p = Node(val=val)
        p.next = self.head
        self.head = p

    def addAtTail(self, val: int) -> None:
        p = self.head
        while p.next:
            p = p.next
        r = Node(val=val)
        p.next = r

    def addAtIndex(self, index: int, val: int) -> None:
        p = self.head
        for i in range(index-1):
            p = p.next
        r = Node(val=val)
        r.next = p.next
        p.next = r

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return

        p = self.head
        q = Node()
        q.next = self.head
        for i in range(index):
            q = p
            p = p.next
            if not p:
                return
        q.next = p.next
        

class Node:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)