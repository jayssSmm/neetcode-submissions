class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head=None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1

        if index==0:
            return self.head.val
        
        head=self.head
        for i in range(index):
            if head.next:
                head=head.next
            else:
                return -1

        return head.val

    def insertHead(self, val: int) -> None:
        p=ListNode(val=val, next=self.head)
        self.head=p

    def insertTail(self, val: int) -> None:

        if not self.head:
            self.head=ListNode(val=val, next=None)
            return

        head=self.head
        while head.next!=None:
            head=head.next
        head.next=ListNode(val=val, next=None)

    def remove(self, index: int) -> bool:
        head=self.head
        if not head:
            return False
        if index==0:
            self.head=self.head.next
            return True
        
        for i in range(index-1):
            if head:
                head=head.next
            else:
                return False
        
        if head and head.next:
            head.next=head.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        head=self.head
        l=[]
        while head:
            l.append(head.val)
            head=head.next

        return l
        