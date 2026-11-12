# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        x = []
        y = []
        while p:
            x.append(p)
            p = p.next
        
        p = headB
        while p:
            y.append(p)
            p = p.next

        flag = False
        while len(x) and len(y):
            a = x.pop()
            b = y.pop()
            print(len(x), len(y))

            if a == b:
                z = a
                flag = True
            else:
                if not flag:
                    return None

                return z

        if flag:
            return z
            
