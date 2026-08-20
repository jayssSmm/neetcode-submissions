# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        q = head.next
            
        while q:
            p = p.next
            q = q.next
            q = q.next if q else None
        return p