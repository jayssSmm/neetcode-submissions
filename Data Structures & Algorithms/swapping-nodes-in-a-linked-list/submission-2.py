# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            n+=1
            p = p.next

        if k == n//2 + 1 and n%2 != 0:
            return head

        if k > n/2:
            g = k
            l = n-k+1
        else:
            g = n-k+1
            l = k

        p = head
        for i in range(1, g+1):
            if i == l:
                x = p
            if i == g:
                y = p
            p = p.next

        x.val, y.val = y.val, x.val
        return head
