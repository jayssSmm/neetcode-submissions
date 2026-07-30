# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if k == 0:
            return head
        
        p = head
        count = 1
        while p.next:
            count+=1
            p = p.next
        p.next = head
        p = p.next

        rem = k % count
        for i in range(count-rem-1):
            p = p.next
        
        head = p.next
        p.next = None

        return head
          