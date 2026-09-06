# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        l = []
        while p:
            l.append(p.val)
            p = p.next

        l.sort()
        i = 0

        p = head

        while p:
            p.val = l[i]
            i+=1
            p = p.next

        return head

