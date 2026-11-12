# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        x = set()
        while p:
            x.add(p.val)
            p = p.next

        p = head
        for i in sorted(x):
            q = p
            if not p:
                return head
            p.val = i
            p = p.next
        q.next = None

        return head