# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p = head
        l = []

        q = None
        count = 0
        while p.next:
            if not q:
                q = p
                p = p.next
                count+=1
                continue

            r = p.next
            if not r:
                break

            if p.val > q.val and p.val > r.val:
                l.append(count)
            elif p.val < q.val and p.val < r.val:
                l.append(count)
            count+=1
            q = p
            p = p.next



        if not l or len(l) == 1:
            return [-1, -1]

        mi = float("inf")
        for i in range(1, len(l)):
            x = l[i] - l[i-1]
            if x<mi:
                mi = x

        return [mi, l[-1] - l[0]]
