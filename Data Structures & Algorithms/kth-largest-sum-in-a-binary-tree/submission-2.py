# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)
        q.append(None)

        l = []
        l.append(root.val)
        
        count = 0
        while q:
            p = q.popleft()
            if not p:
                if not q:
                    break
                l.append(count)
                count = 0
                q.append(None)
                continue
            
            if p.left:
                count+=p.left.val
                q.append(p.left)
            if p.right:
                count+=p.right.val
                q.append(p.right)

        if k > len(l):
            return -1
        l.sort()
        return l[-k]