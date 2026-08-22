# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = head
        while p:
            if p.val != val:
                break
            p = p.next
            head = head.next
        if not p:
            return None
        else:
            p = ListNode(p.val)
            q = p
            head = head.next
        while head:
            if head.val != val:
                p.next = ListNode(head.val)
                p = p.next
            head = head.next

        return q