# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        p = None
        while (head):
            head = head.next
            last.next = p
            p = last
            last = head
            
        
        return p