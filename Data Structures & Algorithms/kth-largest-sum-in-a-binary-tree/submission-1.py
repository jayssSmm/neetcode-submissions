# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def s(q):
            x = 0
            for i in range(len(q)):
                x+=q[i].val
            return x

        q = deque()
        q.append(root)
        q.append(None)

        l = []
        l.append(root.val)
        
        while q:
            p = q.popleft()
            if not p:
                if not q:
                    break
                x = s(q)
                l.append(x)
                q.append(None)
                continue
            
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

        if k > len(l):
            return -1
        l.sort()
        return l[-k]