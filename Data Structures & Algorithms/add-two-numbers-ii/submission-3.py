# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1, x2 = [], []
        while l1:
            x1.append(str(l1.val))
            l1=l1.next
        while l2:
            x2.append(str(l2.val))
            l2=l2.next

        r = str(int("".join(x1)) + int("".join(x2)))

        p = ListNode()
        q = p
        for i in r:
            q.next = ListNode(val=int(i))
            q = q.next
        return p.next