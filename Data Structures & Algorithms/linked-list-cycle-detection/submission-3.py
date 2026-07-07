# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p, q = head, head
        while q and q.next:
            q = q.next.next
            p=p.next

            if p==q:
                return True

        return False