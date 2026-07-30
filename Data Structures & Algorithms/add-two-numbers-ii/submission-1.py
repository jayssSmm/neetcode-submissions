# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1, x2 = 0, 0
        while l1:
            x1=x1*10+l1.val
            l1=l1.next
        while l2:
            x2=x2*10+l2.val
            l2=l2.next

        r = (str(x1 + x2))

        q = ListNode(val=int(r[0]))
        p = q
        r = r[1:]
        for i in r:
            q.next = ListNode(val=int(i))
            q = q.next
        return p