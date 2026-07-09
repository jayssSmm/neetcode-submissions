# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None
        
        p=head
        q=ListNode(next=p)

        for i in range(0, n-1):
            p=p.next
        print(p.val)

        while p and p.next!=None:
            p=p.next
            q=q.next

        if q.next==head:
            head=q.next.next
        else:
            q.next=q.next.next

        return head