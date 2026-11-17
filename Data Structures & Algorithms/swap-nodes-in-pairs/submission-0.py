# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        p = head
        q = None
        while p.next:
            q = p
            p = p.next
            if p:
                q.val, p.val = p.val, q.val
                if p.next:
                    p = p.next

        return head