# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p = head
        r = None
        s = None
        for i in range(1, left):
            r = s = p
            p = p.next
        y = r
        x = p
        for i in range(left, right+1):
            r = p
            p = p.next
            r.next = s
            s = r
        if y:
            y.next = r
        x.next = p
        if y:
            return head
        return r