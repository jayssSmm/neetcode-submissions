# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        p = head
        q = head.next
        r = None

        while q:
            p.next = r
            r = p
            p = q
            q = q.next

        p.next = r
        return p
