# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        d = dict()
        x = 0
        while p:
            d[x] = p.val
            x+=1
            p = p.next

        m = float('-inf')
        for i in range(x//2):
            if d[i] + d[x-i-1] > m:
                m = d[i] + d[x-i-1]

        return m