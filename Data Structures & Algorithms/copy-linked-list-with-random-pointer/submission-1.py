"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        d = dict()

        p = head
        while p:
            q = Node(p.val)
            d[p] = q
            p = p.next

        for i in d:
            if i.next:
                d[i].next = d[i.next]
            else:
                d[i].next = None
            if i.random:
                d[i].random = d[i.random]
            else:
                d[i].random = None

        return d[head]