# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        try:
            q = (p.next).next
        except AttributeError:
            return False

        while (p):
            if p==q:
                return True
            p=p.next
            try:
                q=(q.next).next
            except AttributeError:
                return False
        return False